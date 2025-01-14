=========
Tutorials
=========

For more tests, check `pyabaqus/tests at main · Haiiliin/pyabaqus <https://github.com/Haiiliin/pyabaqus/tree/main/tests>`_.


Usually in Abaqus, we have several things to do:
    * Build the model
    * Submit and monitor the job
    * Get the output data and visualize it


Build an Abaqus model
---------------------

The most convenient way to build an Abaqus model is to do it in Abaqus CAE. When we use the 
Abaqus/CAE graphical user interface (GUI) to create a model and to visualize the results, 
commands are issued internally by Abaqus/CAE after every operation. These commands reflect the 
geometry you created along with the options and settings you selected from each dialog box.

Therefore, we can build our Abaqus model using Python script. We can totally use the Python 
script to build our Abaqus model, although it is not an efficient way. Usually, we do 
something in Abaqus/CAE, and check the Python script in the reply file (`.rpy`). And then copy 
it to our script file, this works, but not nicely.

However, if type hints are provided in Python scripting of Abaqus, things will getting much 
easier, and that is what `pyabaqus` does.


The example model described in the following is simple, there is a squre structure, the vertical displacement of the bottom face is fixed, and there is a vertical pressure in the top surface, the Abaqus model is showed as follows:


.. image:: images/model.png
    :width: 50%
    :align: center


Header of the script
~~~~~~~~~~~~~~~~~~~~

Usually, when we use Python script to build the model, we need to import the following modules:

.. code-block:: Python

    from abaqus import *
    from abaqusConstants import *
    from driverUtils import *

Module `abaqus` contains two most important variable `mdb` and `session` which control the model. Module `abaqusConstants` contains constant strings used in modelling, i.e., when we defines a part using the following code:

.. code-block:: Python

    mdb.models['Model-1'].Part(name='part', dimensionality=THREE_D, type=DEFORMABLE_BODY)

`THREE_D` indicates the part is a 3D part, `DEFORMABLE_BODY` indicates the part is deformable. 

Module `driverUtils` contains an important function `executeOnCaeStartup`, this function will be execute each time we open the Abaqus, so we need to call this function in our Python script. Now, the header of our Python script would be like:

.. code-block:: Python

    from abaqus import *
    from abaqusConstants import *
    from driverUtils import *

    executeOnCaeStartup()


Create parts
~~~~~~~~~~~~

First we need to create a sketch that will be used to create the part, we need to use :py:meth:`~abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch` to create a sketch:

.. code-block:: Python

    model = mdb.models['Model-1']
    sketch = model.ConstrainedSketch(name='sketch', sheetSize=1.0)
    sketch.rectangle((0, 0), (1, 1))

In this code, we draw a sketch with a squre. Now we can create a part using this sketch:

.. code-block:: Python

    part = model.Part(name='part', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    part.BaseSolidExtrude(sketch=sketch, depth=1)

The first line creates a 3D and deformable part. Then we use the :py:meth:`~abaqus.Part.Feature.Feature.BaseSolidExtrude` method to create a part using the sketch. 


Create some sets for boundary conditions and loads
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unlike building a model in Abaqus/CAE, we can just click the nodes/faces to create sets, when we use a Python script to build the model, we can use coordinates to find nodes/faces we need. 

We can use :py:meth:`~abaqus.Region.RegionPart.RegionPart.Set` and :py:meth:`~abaqus.Region.RegionPart.RegionPart.Surface` to create sets and surfaces:

.. code-block:: Python

    part.Set(name='set-all', cells=part.cells.findAt(coordinates=((0.5, 0.5, 0.5), )))
    part.Set(name='set-bottom', faces=part.faces.findAt(coordinates=((0.5, 0.5, 0.0), )))
    part.Set(name='set-top', faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))
    part.Surface(name='surface-top', 
                 side1Faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))

Merge parts to assembly
~~~~~~~~~~~~~~~~~~~~~~~

We can use :py:meth:`~abaqus.Assembly.AssemblyBase.AssemblyBase.Instance` to create instances：

.. code-block:: Python

    model.rootAssembly.DatumCsysByDefault(CARTESIAN)
    model.rootAssembly.Instance(name='instance', part=part, dependent=ON)

Create materials and sections, and assign materials to sections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First we create a Material object using :py:meth:`~abaqus.Material.MaterialModel.MaterialModel.Material`:

.. code-block:: Python

    material = model.Material(name='material')

Then we assign some properties to the Material object, i.e., :py:meth:`~abaqus.Material.Material.Material.Elastic` and :py:meth:`~abaqus.Material.Material.Material.Density`:

.. code-block:: Python

    material.Elastic(table=((1000, 0.2), ))
    material.Density(table=((2500, ), ))

Then we create a :py:meth:`~abaqus.Section.SectionModel.SectionModel.HomogeneousSolidSection` and assign the material to the section (:py:meth:`~abaqus.Property.PropertyPart.PropertyPart.SectionAssignment`):

.. code-block:: Python

    model.HomogeneousSolidSection(name='section', material='material', thickness=None)
    part.SectionAssignment(region=part.sets['set-all'], sectionName='section')


Create steps
~~~~~~~~~~~~

It is easy to create a :py:meth:`~abaqus.Step.StepModel.StepModel.StaticStep`:

.. code-block:: Python

    step = model.StaticStep(name='Step-1', previous='Initial', description='', 
                            timePeriod=1.0, timeIncrementationMethod=AUTOMATIC, 
                            maxNumInc=100, initialInc=0.01, minInc=0.001, maxInc=0.1)


Specify output requests
~~~~~~~~~~~~~~~~~~~~~~~

We can use the :py:meth:`~abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest` and :py:meth:`~abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest` to specify field output and history output information.

.. code-block:: Python

    field = model.FieldOutputRequest('F-Output-1', createStepName='Step-1', 
                                     variables=('S', 'E', 'U'))


Create boundary conditions
~~~~~~~~~~~~~~~~~~~~~~~~~~

We can use :py:meth:`~abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC` to create a displacement boundary condition:

.. code-block:: Python

    bottom_instance = model.rootAssembly.instances['instance'].sets['set-bottom']
    bc = model.DisplacementBC(name='BC-1', createStepName='Initial', 
                              region=bottom_instance, u3=SET)

It should be noted that region of the boundary condition should be a region of the instances instead of parts, since sets created in parts are copied to the instance, we can use the sets in the parts that we defined before. 

Create loads
~~~~~~~~~~~~

We can use :py:meth:`~abaqus.Load.LoadModel.LoadModel.Pressure` ro create a pressure:

.. code-block:: Python

    top_instance = model.rootAssembly.instances['instance'].surfaces['surface-top']
    pressure = model.Pressure('pressure', createStepName='Step-1', region=top_instance, 
                              magnitude=100)


Mesh
~~~~

To mesh the model, we have to set the :py:class:`~abaqus.Mesh.ElemType.ElemType`, which is defined in the `mesh` module, so we need to import `mesh` module:

.. code-block:: Python

    import mesh

    elem1 = mesh.ElemType(elemCode=C3D8R)
    elem2 = mesh.ElemType(elemCode=C3D6)
    elem3 = mesh.ElemType(elemCode=C3D4)
    part.setElementType(regions=(part.cells, ), elemTypes=(elem1, elem2, elem3))
    part.seedPart(size=0.1)
    part.generateMesh()


Create jobs
~~~~~~~~~~~

We can use :py:meth:`~abaqus.Job.JobMdb.JobMdb.Job` to create a job:

.. code-block:: Python

    job = mdb.Job(name='Job-1', model='Model-1')

Then we can write the model to an input file (`.inp`):

.. code-block:: Python

    job.writeInput()

Then we can submit the job:

.. code-block:: Python

    job.submit()
    job.waitForCompletion()


Save the Abaqus model to a `.cae` file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We can use :py:class:`~abaqus.Mdb.MdbBase.MdbBase.saveAs` to save the Abaqus model to a `.cae` file:

.. code-block:: Python

    mdb.saveAs('compression.cae')

It should be noted that we have to use this function to save the model when we use `pyabaqus` to build an Abaqus model. It is because that when we execute all the above codes, the Python script has not been sent to Abaqus kernel. All the functions mentioned above are included in `pyabaqus`, however, nothing has been done inside this functions, they are just provided for type hints. Therefore, if we want to send the Python script to the Abaqus kernel, we have to use the Abaqus command like this:

.. code-block:: sh

    abaqus cae -noGUI script.py

In order to make it simple, this has been done in the :py:meth:`~abaqus.Mdb.MdbBase.MdbBase.saveAs` function:

.. code-block:: Python

    def saveAs(self, pathName: str):
        abaqus = 'abaqus'
        if 'ABAQUS_BAT_PATH' in os.environ.keys():
            abaqus = os.environ['ABAQUS_BAT_PATH']
        os.system('{} cae -noGUI {}'.format(abaqus, os.path.abspath(sys.argv[0])))


The whole script
~~~~~~~~~~~~~~~~

The whole script of this example is showed as follows:

.. code-block:: Python
    :caption: compression.py

    from abaqus import *
    from abaqusConstants import *
    from caeModules import *
    from driverUtils import *

    executeOnCaeStartup()

    # Model
    model = mdb.models['Model-1']

    # Part
    sketch = model.ConstrainedSketch(name='sketch', sheetSize=1.0)
    sketch.rectangle((0, 0), (1, 1))
    part = model.Part(name='part', dimensionality=THREE_D, type=DEFORMABLE_BODY)
    part.BaseSolidExtrude(sketch=sketch, depth=1)

    # Create sets
    part.Set(name='set-all', cells=part.cells.findAt(coordinates=((0.5, 0.5, 0.5), )))
    part.Set(name='set-bottom', faces=part.faces.findAt(coordinates=((0.5, 0.5, 0.0), )))
    part.Set(name='set-top', faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))
    part.Surface(name='surface-top', 
                 side1Faces=part.faces.findAt(coordinates=((0.5, 0.5, 1.0), )))

    # Assembly
    model.rootAssembly.DatumCsysByDefault(CARTESIAN)
    model.rootAssembly.Instance(name='instance', part=part, dependent=ON)

    # Material
    material = model.Material(name='material')
    material.Elastic(table=((1000, 0.2), ))
    material.Density(table=((2500, ), ))

    # Section
    model.HomogeneousSolidSection(name='section', material='material', thickness=None)
    part.SectionAssignment(region=part.sets['set-all'], sectionName='section')

    # Step
    step = model.StaticStep(name='Step-1', previous='Initial', description='', 
                            timePeriod=1.0, timeIncrementationMethod=AUTOMATIC, 
                            maxNumInc=100, initialInc=0.01, minInc=0.001, maxInc=0.1)

    # Output request
    field = model.FieldOutputRequest('F-Output-1', createStepName='Step-1', 
                                     variables=('S', 'E', 'U'))

    # Boundary condition
    bottom_instance = model.rootAssembly.instances['instance'].sets['set-bottom']
    bc = model.DisplacementBC(name='BC-1', createStepName='Initial', 
                              region=bottom_instance, u3=SET)

    # Load
    top_instance = model.rootAssembly.instances['instance'].surfaces['surface-top']
    pressure = model.Pressure('pressure', createStepName='Step-1', region=top_instance, 
                              magnitude=100)

    # Mesh
    elem1 = mesh.ElemType(elemCode=C3D8R)
    elem2 = mesh.ElemType(elemCode=C3D6)
    elem3 = mesh.ElemType(elemCode=C3D4)
    part.setElementType(regions=(part.cells, ), elemTypes=(elem1, elem2, elem3))
    part.seedPart(size=0.1)
    part.generateMesh()

    # Job
    job = mdb.Job(name='Job-1', model='Model-1')
    job.writeInput()

    # Submit the job
    # job.submit()
    # job.waitForCompletion()

    # Save abaqus model
    mdb.saveAs('compression.cae')


Extract output data
-------------------

If we want to extract the output data, we have to write an outout script. 

Header of the output script
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similarly, we have to import some modules:

.. code-block:: Python

    from abaqus import *
    from abaqusConstants import *
    from driverUtils import *

    executeOnCaeStartup()


Open the output database
~~~~~~~~~~~~~~~~~~~~~~~~

We can use :py:meth:`~abaqus.Session.SessionBase.SessionBase.openOdb` to open the output database:

.. code-block:: Python

    odb = session.openOdb('Job-1.odb')


Extract the data
~~~~~~~~~~~~~~~~

We can use the :py:meth:`~abaqus.XY.XYSession.XYSession.xyDataListFromField` to extract the output data:

.. code-block:: Python

    dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL, 
                                           variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                           nodeSets=('INSTANCE.SET-TOP', ))

`dataList` is a list of `XYData` objects. `XYData` is a data type defined in Abaqus, the data is stored in tuples of tuples, so we can simply save it to a file, i.e., using the `numpy` (`numpy` is installed in Python interpreter of Abaqus already):

.. code-block:: Python

    import numpy as np
    
    data = np.array(dataList[0])
    np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')


Results of above example
~~~~~~~~~~~~~~~~~~~~~~~~

The distribution of `U3` of above model is showed as follows:

.. image:: images/output.png
    :width: 70%
    :align: center


The distribution of the vertical displacement of a point in the top surface is showed as follows:

.. image:: images/compression.png
    :width: 70%
    :align: center


The whole output script
~~~~~~~~~~~~~~~~~~~~~~~

The whole output script of this example is showed as follows:

.. code-block:: Python
    :caption: compression-output.py

    from abaqus import *
    from abaqusConstants import *
    from driverUtils import *
    import numpy as np

    executeOnCaeStartup()

    # Open output database
    odb = session.openOdb('Job-1.odb')

    # Extract output data
    dataList = session.xyDataListFromField(odb=odb, outputPosition=NODAL, 
                                           variable=(('U', NODAL, ((COMPONENT, 'U3'),)),),
                                           nodeSets=('INSTANCE.SET-TOP', ))
    data = np.array(dataList[0])
    np.savetxt('data.csv', data, header='time,U3', delimiter=',', comments='')



Some simply used functions
--------------------------

There are several simply used provided in `pyabaqus`, we cannot call it in Python script to build the model or extract the output data, but we can use it to interact our Python script to Python interpreter of Abaqus.


Execute Python script in Abaqus
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`abaqus.runPythonScript` is provided to execute our Python script in Abaqus, the signature of `abaqus.runPythonScript` is:

.. autofunction:: abaqus.runPythonScript

We can use it to execute our Python script in Abaqus:

.. code-block:: Python

    import abaqus

    abaqus.runPythonScript('compression.py')


Submit a job by an input file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`abaqus.submitJobByInputFile` is provided to submit the job by an input file (`.inp`), the signature of `abaqus.submitJobByInputFile` is:

.. autofunction:: abaqus.submitJobByInputFile

We can use it to submit the job by an input file:

.. code-block:: Python

    import abaqus

    abaqus.submitJobByInputFile('Job-1.inp')


If argument `showStatus` of `abaqus.submitJobByInputFile` is set to True (by default, it is set to True), a job monitor will be create to monitor the job, showed in the following figure:

.. image:: images/job_monitor.png
    :width: 100%
    :align: center


Execute output script
~~~~~~~~~~~~~~~~~~~~~

`abaqus.extractOutputData` is provided is execute the output script, the signature of `abaqus.extractOutputData` is:

.. autofunction:: abaqus.extractOutputData

We can use it to execute the output script:

.. code-block:: Python

    import abaqus

    abaqus.extractOutputData('Job-1.odb', 'compression-output.py')
