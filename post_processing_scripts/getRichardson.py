#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
dambreak_pxmf = FindSource('dambreak_p.xmf')

# create a new 'Calculator'
calculator1 = Calculator(Input=dambreak_pxmf)
calculator1.Function = ''

# Properties modified on calculator1
calculator1.ResultArrayName = 'Speed'
calculator1.Function = 'sqrt(velocity_X^2+velocity_Y^2+velocity_Z^2)'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1214, 781]

# get color transfer function/color map for 'Speed'
speedLUT = GetColorTransferFunction('Speed')
speedLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.878906683738906e-39, 0.865003, 0.865003, 0.865003, 1.1757813367477812e-38, 0.705882, 0.0156863, 0.14902]
speedLUT.ScalarRangeInitialized = 1.0

# show data in view
calculator1Display = Show(calculator1, renderView1)
# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.ColorArrayName = ['POINTS', 'Speed']
calculator1Display.LookupTable = speedLUT
calculator1Display.OSPRayScaleArray = 'Speed'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.SelectOrientationVectors = 'velocity'
calculator1Display.ScaleFactor = 0.1
calculator1Display.SelectScaleArray = 'Speed'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityUnitDistance = 0.020550784211436433
calculator1Display.GaussianRadius = 0.05
calculator1Display.SetScaleArray = ['POINTS', 'Speed']
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityArray = ['POINTS', 'Speed']
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(dambreak_pxmf, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=calculator1)
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'Speed']

# show data in view
gradientOfUnstructuredDataSet1Display = Show(gradientOfUnstructuredDataSet1, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet1Display.Representation = 'Surface'
gradientOfUnstructuredDataSet1Display.ColorArrayName = ['POINTS', 'Speed']
gradientOfUnstructuredDataSet1Display.LookupTable = speedLUT
gradientOfUnstructuredDataSet1Display.OSPRayScaleArray = 'Speed'
gradientOfUnstructuredDataSet1Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet1Display.SelectOrientationVectors = 'velocity'
gradientOfUnstructuredDataSet1Display.ScaleFactor = 0.1
gradientOfUnstructuredDataSet1Display.SelectScaleArray = 'Speed'
gradientOfUnstructuredDataSet1Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet1Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet1Display.ScalarOpacityUnitDistance = 0.020550784211436433
gradientOfUnstructuredDataSet1Display.GaussianRadius = 0.05
gradientOfUnstructuredDataSet1Display.SetScaleArray = ['POINTS', 'Speed']
gradientOfUnstructuredDataSet1Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet1Display.OpacityArray = ['POINTS', 'Speed']
gradientOfUnstructuredDataSet1Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator2 = Calculator(Input=gradientOfUnstructuredDataSet1)
calculator2.Function = ''

# Properties modified on calculator2
calculator2.ResultArrayName = 'density'
calculator2.Function = '1045*(1-vof)+1025*vof'

# get color transfer function/color map for 'density'
densityLUT = GetColorTransferFunction('density')
densityLUT.RGBPoints = [1025.0, 0.231373, 0.298039, 0.752941, 1035.0, 0.865003, 0.865003, 0.865003, 1045.0, 0.705882, 0.0156863, 0.14902]
densityLUT.ScalarRangeInitialized = 1.0

# show data in view
calculator2Display = Show(calculator2, renderView1)
# trace defaults for the display properties.
calculator2Display.Representation = 'Surface'
calculator2Display.ColorArrayName = ['POINTS', 'density']
calculator2Display.LookupTable = densityLUT
calculator2Display.OSPRayScaleArray = 'density'
calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator2Display.SelectOrientationVectors = 'velocity'
calculator2Display.ScaleFactor = 0.1
calculator2Display.SelectScaleArray = 'density'
calculator2Display.GlyphType = 'Arrow'
calculator2Display.PolarAxes = 'PolarAxesRepresentation'
calculator2Display.ScalarOpacityUnitDistance = 0.020550784211436433
calculator2Display.GaussianRadius = 0.05
calculator2Display.SetScaleArray = ['POINTS', 'density']
calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator2Display.OpacityArray = ['POINTS', 'density']
calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(gradientOfUnstructuredDataSet1, renderView1)

# show color bar/color legend
calculator2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet2 = GradientOfUnstructuredDataSet(Input=calculator2)
gradientOfUnstructuredDataSet2.ScalarArray = ['POINTS', 'density']

# Properties modified on gradientOfUnstructuredDataSet2
gradientOfUnstructuredDataSet2.ResultArrayName = 'density_grad'

# show data in view
gradientOfUnstructuredDataSet2Display = Show(gradientOfUnstructuredDataSet2, renderView1)
# trace defaults for the display properties.
gradientOfUnstructuredDataSet2Display.Representation = 'Surface'
gradientOfUnstructuredDataSet2Display.ColorArrayName = ['POINTS', 'density']
gradientOfUnstructuredDataSet2Display.LookupTable = densityLUT
gradientOfUnstructuredDataSet2Display.OSPRayScaleArray = 'density'
gradientOfUnstructuredDataSet2Display.OSPRayScaleFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet2Display.SelectOrientationVectors = 'velocity'
gradientOfUnstructuredDataSet2Display.ScaleFactor = 0.1
gradientOfUnstructuredDataSet2Display.SelectScaleArray = 'density'
gradientOfUnstructuredDataSet2Display.GlyphType = 'Arrow'
gradientOfUnstructuredDataSet2Display.PolarAxes = 'PolarAxesRepresentation'
gradientOfUnstructuredDataSet2Display.ScalarOpacityUnitDistance = 0.020550784211436433
gradientOfUnstructuredDataSet2Display.GaussianRadius = 0.05
gradientOfUnstructuredDataSet2Display.SetScaleArray = ['POINTS', 'density']
gradientOfUnstructuredDataSet2Display.ScaleTransferFunction = 'PiecewiseFunction'
gradientOfUnstructuredDataSet2Display.OpacityArray = ['POINTS', 'density']
gradientOfUnstructuredDataSet2Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(calculator2, renderView1)

# show color bar/color legend
gradientOfUnstructuredDataSet2Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Calculator'
calculator3 = Calculator(Input=gradientOfUnstructuredDataSet2)
calculator3.Function = ''

# Properties modified on calculator3
calculator3.ResultArrayName = 'richardson'
calculator3.Function = '9.81/density*density_grad_Y/Gradients_Y/Gradients_Y'

# get color transfer function/color map for 'richardson'
richardsonLUT = GetColorTransferFunction('richardson')
richardsonLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 5.878906683738906e-39, 0.865003, 0.865003, 0.865003, 1.1757813367477812e-38, 0.705882, 0.0156863, 0.14902]
richardsonLUT.ScalarRangeInitialized = 1.0

# show data in view
calculator3Display = Show(calculator3, renderView1)
# trace defaults for the display properties.
calculator3Display.Representation = 'Surface'
calculator3Display.ColorArrayName = ['POINTS', 'richardson']
calculator3Display.LookupTable = richardsonLUT
calculator3Display.OSPRayScaleArray = 'richardson'
calculator3Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator3Display.SelectOrientationVectors = 'velocity'
calculator3Display.ScaleFactor = 0.1
calculator3Display.SelectScaleArray = 'richardson'
calculator3Display.GlyphType = 'Arrow'
calculator3Display.PolarAxes = 'PolarAxesRepresentation'
calculator3Display.ScalarOpacityUnitDistance = 0.020550784211436433
calculator3Display.GaussianRadius = 0.05
calculator3Display.SetScaleArray = ['POINTS', 'richardson']
calculator3Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator3Display.OpacityArray = ['POINTS', 'richardson']
calculator3Display.OpacityTransferFunction = 'PiecewiseFunction'

# hide data in view
Hide(gradientOfUnstructuredDataSet2, renderView1)

# show color bar/color legend
calculator3Display.SetScalarBarVisibility(renderView1, True)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.5, 0.25, 10000.0]
renderView1.CameraFocalPoint = [0.5, 0.25, 0.0]
renderView1.CameraParallelScale = 0.5590169943749475

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).