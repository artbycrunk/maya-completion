
def aaf2fcp(*args, **kwargs):
    """
    This command is used to convert an aff file to a Final Cut Pro (fcp) xml file The conversion process can take several seconds to complete and the command is meant to be run asynchronously.

    Returns: `string` Command result

    """
    pass


def about(*args, **kwargs):
    """
    This command displays version information about the application if it is executed without flags.

    Returns: `string` The application's version information.

    """
    pass


def addAttr(*args, **kwargs):
    """
    This command is used to add a dynamic attribute to a node or nodes.

    Returns: None
    """
    pass


def addDynamic(*args, **kwargs):
    """
    Makes the "object" specified as second argument the source of an existing field or emitter specified as the first argument.

    Returns: `string` The name of the source object and the field or emitter which was attached to it.

    """
    pass


def addExtension(*args, **kwargs):
    """
    This command is used to add an extension attribute to a node type.

    Returns: None
    """
    pass


def addMetadata(*args, **kwargs):
    """
    Defines the attachment of a metadata structure to one or more selected objects.

    Returns: `string[]` List of nodes to which a new Stream was successfully added (create mode)

    `string[]` List of channel types containing metadata on an object when querying the channelName flag

    `string[]` List of stream names on an object when querying the streamName flag

    `string[]` List of structures used by an object's metadata Streams when querying the structure flag

    `string[]` List of index types used by an object when querying the indexType flag

    """
    pass


def addPP(*args, **kwargs):
    """
    Adds per-point (per-cv, per-vertex, or per-particle) attribute capability for an attribute of an emitter or field.

    Returns: `string[]` Returns names of emitters/fields for which the per-point capability was added for the specified attribute.

    """
    pass


def affectedNet(*args, **kwargs):
    """
    This command gets the list of attributes on a node or node type and creates nodes of type TdnAffect, one for each attribute, that are connected iff the source node's attribute affects the destination node's attribute.

    Returns: None
    """
    pass


def affects(*args, **kwargs):
    """
    This command returns the list of attributes on a node or node type which affect the named attribute.

    Returns: `string` List of affected/affecting attributes

    """
    pass


def aimConstraint(*args, **kwargs):
    """
    Constrain an object's orientation to point at a target object or at the average position of a number of targets.

    Returns: `string[]` name of the created constraint node

    """
    pass


def air(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def aliasAttr(*args, **kwargs):
    """
    Allows aliases (alternate names) to be defined for any attribute of a specified node.

    Returns: `string[]` in query mode.

    """
    pass


def align(*args, **kwargs):
    """
    Align or spread objects along X Y and Z axis.

    Returns: `boolean` true/false

    """
    pass


def alignCtx(*args, **kwargs):
    """
    The alignCtx command creates a tool for aligning and distributing objects.

    Returns: `string` (name of the new context)

    """
    pass


def alignCurve(*args, **kwargs):
    """
    The curve align command is used to align curves in maya.

    Returns: `string[]` Object name and node name

    """
    pass


def alignSurface(*args, **kwargs):
    """
    The surface align command is used to align surfaces in maya.

    Returns: `string[]` Object name and node name

    """
    pass


def allNodeTypes(*args, **kwargs):
    """
    This command returns a list containing the type names of every kind of creatable node registered with the system.

    Returns: `string[]` List of node types

    """
    pass


def ambientLight(*args, **kwargs):
    """
    TlightCmd is the base class for other light commands.

    Returns: `double[]` when querying the rgb or shadowColor flags double when querying the intensity flag boolean when querying the useRayTraceShadows or exclusive flags linear[] when querying the position flag angle[] when querying the rotation flag string when querying the name flag

    `string` Light shape name

    """
    pass


def angleBetween(*args, **kwargs):
    """
    Returns the axis and angle required to rotate one vector onto another.

    Returns: `float[]` 3 Euler angles or axis and angle

    `string` When constructionHistory flag is used.

    """
    pass


def animCurveEditor(*args, **kwargs):
    """
    Edit a characteristic of a graph editor.

    Returns: `string` Editor name

    """
    pass


def animDisplay(*args, **kwargs):
    """
    This command changes certain display options used by animation windows.

    Returns: None
    """
    pass


def animLayer(*args, **kwargs):
    """
    This command creates and edits animation layers.

    Returns: `string` Return values currently not documented.

    """
    pass


def animView(*args, **kwargs):
    """
    This command allows you to specify the current view range within an animation editor.

    Returns: None
    """
    pass


def annotate(*args, **kwargs):
    """
    This command is used to create an annotation to be attached to the specified objects at the specified point.

    Returns: `string` Annotation added

    """
    pass


def applyAttrPattern(*args, **kwargs):
    """
    Take the attribute structure described by a pre-defined pattern and apply it either to a node (as dynamic attributes) or a node type (as extension attributes).

    Returns: `int` Number of nodes or node types to which the attribute were added

    """
    pass


def applyMetadata(*args, **kwargs):
    """
    Define the values of a particular set of metadata on selected objects.

    Returns: `Boolean` True if the application succeeded

    """
    pass


def applyTake(*args, **kwargs):
    """
    This command takes data in a device (refered to as a take) and converts it into a form that may be played back and reviewed.

    Returns: None
    """
    pass


def arcLenDimContext(*args, **kwargs):
    """
    Command used to register the arcLenDimCtx tool.

    Returns: `string` : name of the context created

    """
    pass


def arcLengthDimension(*args, **kwargs):
    """
    This command is used to create an arcLength dimension to display the arcLength of a curve/surface at a specified point on the curve/surface.

    Returns: `string` Name of the arcLengthDimension node created

    """
    pass


def arclen(*args, **kwargs):
    """
    This command returns the arclength of a curve if the history flag is not set (the default).

    Returns: `float` Length in non history mode.

    `string` Node name, in history mode.

    """
    pass


def arrayMapper(*args, **kwargs):
    """
    Create an arrayMapper node and connect it to a target object.

    Returns: `string[]` Names of created arrayMapper nodes.

    """
    pass


def art3dPaintCtx(*args, **kwargs):
    """
    This is a tool context command for 3d Paint tool.

    Returns: None
    """
    pass


def artAttrCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations.

    Returns: `string` The name of the context created.

    """
    pass


def artAttrPaintVertexCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations.

    Returns: None
    """
    pass


def artAttrSkinPaintCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations.

    Returns: None
    """
    pass


def artAttrTool(*args, **kwargs):
    """
    The artAttrTool command manages the list of tool types which are         used for attribute painting.

    Returns: None
    """
    pass


def artBuildPaintMenu(*args, **kwargs):
    """
    ??.

    Returns: None
    """
    pass


def artFluidAttrCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations.

    Returns: None
    """
    pass


def artPuttyCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations.

    Returns: None
    """
    pass


def artSelectCtx(*args, **kwargs):
    """
    This command is used to select/deselect/toggle components on selected surfaces using a brush interface (Maya Artisan).

    Returns: None
    """
    pass


def artSetPaintCtx(*args, **kwargs):
    """
    This tool allows the user to modify the set membership (add, transfer, remove cvs) on nurbs surfaces using Maya Artisan's interface.

    Returns: None
    """
    pass


def artUserPaintCtx(*args, **kwargs):
    """
    This is a context command to set the flags on the artAttrContext, which is the base context for attribute painting operations.

    Returns: `string` The name of the context created.

    """
    pass


def arubaNurbsToPoly(*args, **kwargs):
    """
    This command tesselates a NURBS surface and produces a polygonal surface.

    Returns: `string[]` The polygon and optionally the dependency node name

    """
    pass


def assembly(*args, **kwargs):
    """
    Command to register assemblies for the scene assembly framework, to create them, and to edit and query them.

    Returns: None
    """
    pass


def assignCommand(*args, **kwargs):
    """
    This command allows the user to assign hotkeys and manipulate the internal array of named command objects.

    Returns: None
    """
    pass


def assignInputDevice(*args, **kwargs):
    """
    This command associates a command string (i.

    Returns: `string` Command result

    """
    pass


def assignViewportFactories(*args, **kwargs):
    """
    Sets viewport factories for displays as materials or textures.

    Returns: None
    """
    pass


def attachCurve(*args, **kwargs):
    """
    This attach command is used to attach curves.

    Returns: `string[]` Object name and node name

    """
    pass


def attachDeviceAttr(*args, **kwargs):
    """
    This command associates a device/axis pair with a node/attribute pair.

    Returns: None
    """
    pass


def attachSurface(*args, **kwargs):
    """
    This attach command is used to attach surfaces.

    Returns: `string[]` Object name and node name

    """
    pass


def attrColorSliderGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` (the name of the created group)

    """
    pass


def attrCompatibility(*args, **kwargs):
    """
    This command is used by Maya to handle compatibility issues between file format versions by providing a mechanism to describe differences between two versions.

    Returns: None
    """
    pass


def attrControlGrp(*args, **kwargs):
    """
    This command creates a control of the type most appropriate for the specified attribute, and associates the control with the attribute.

    Returns: `string` The control name.

    """
    pass


def attrEnumOptionMenu(*args, **kwargs):
    """
    This command creates an enumerated attribute control.

    Returns: `string` The full name of the control.

    """
    pass


def attrEnumOptionMenuGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` The full name of the control on creation.

    """
    pass


def attrFieldGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` The full name of the control.

    """
    pass


def attrFieldSliderGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def attrNavigationControlGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def attributeInfo(*args, **kwargs):
    """
    This command lists all of the attributes that are marked with certain flags.

    Returns: `string[]` List of attributes matching criteria

    """
    pass


def attributeMenu(*args, **kwargs):
    """
    Action to generate popup connection menus for Hypershade.

    Returns: `string` Command result

    """
    pass


def attributeName(*args, **kwargs):
    """
    This command takes one "node.

    Returns: `string` Command result

    """
    pass


def attributeQuery(*args, **kwargs):
    """
    attributeQuery returns information about the configuration of an attribute.

    Returns: `float[]` when querying ranges or default values

    `boolean` when querying attribute flags

    """
    pass


def audioTrack(*args, **kwargs):
    """
    This command is used for inserting and removing tracks related to the audio clips displayed in the sequencer.

    Returns: None
    """
    pass


def autoKeyframe(*args, **kwargs):
    """
    With no flags, this command will set keyframes on all attributes that have been modified since an "autoKeyframe -state on" command was issued.

    Returns: `int` Number of keyframes set.

    """
    pass


def autoPlace(*args, **kwargs):
    """
    This command takes a point in the centre of the current modeling pane and projects it onto the live surface.

    Returns: `float[]` Placement location in 3D space

    """
    pass


def autoSave(*args, **kwargs):
    """
    Provides an interface to the auto-save mechanism.

    Returns: None
    """
    pass


def bakeClip(*args, **kwargs):
    """
    This command is used to bake clips and blends into a single clip.

    Returns: `string` clip name

    """
    pass


def bakeDeformer(*args, **kwargs):
    """
    Given a rigged character, whose mesh shape is determined by a set of deformers, bakeDeformer calculates linear blend skin weights most closely approximating observed deformations.

    Returns: `string` BakeDeformer name

    """
    pass


def bakePartialHistory(*args, **kwargs):
    """
    This command is used to bake sections of the construction history of a shape node when possible.

    Returns: `string` name of shapes that were baked

    """
    pass


def bakeResults(*args, **kwargs):
    """
    This command allows the user to replace a chain of dependency nodes which define the value for an attribute with a single animation curve.

    Returns: `int` - The number of channels baked

    """
    pass


def bakeSimulation(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: None
    """
    pass


def baseTemplate(*args, **kwargs):
    """
    This is the class for the commands that edit and/or query templates.

    Returns: None
    """
    pass


def baseView(*args, **kwargs):
    """
    A view defines the layout information for the attributes of a particular node type or container.

    Returns: None
    """
    pass


def batchRender(*args, **kwargs):
    """
    The batchRender command is used to spawn off a separate rendering session of the current maya file.

    Returns: None
    """
    pass


def bevel(*args, **kwargs):
    """
    The bevel command creates a new bevel surface for the specified curve.

    Returns: `string[]` Object name and node name

    """
    pass


def bevelPlus(*args, **kwargs):
    """
    The bevelPlus command creates a new bevel surface for the specified curves using a given style curve.

    Returns: `string[]` Object name(s) and node name

    """
    pass


def bezierAnchorPreset(*args, **kwargs):
    """
    This command provides a queryable interface for Bezier curve shapes.

    Returns: `int` (number of modified anchors)

    """
    pass


def bezierAnchorState(*args, **kwargs):
    """
    The bezierAnchorState command provides an easy interface to modify anchor states:.

    Returns: `int` (number of modified anchors)

    """
    pass


def bezierCurveToNurbs(*args, **kwargs):
    """
    The bezierCurveToNurbs command attempts to convert an existing NURBS curve to a Bezier curve.

    Returns: `string[]` (object name and node name)

    """
    pass


def bezierInfo(*args, **kwargs):
    """
    This command provides a queryable interface for Bezier curve shapes.

    Returns: `int` Queried value

    """
    pass


def binMembership(*args, **kwargs):
    """
    Command to assign nodes to bins.

    Returns: `boolean` Command result

    """
    pass


def bindSkin(*args, **kwargs):
    """
    This command binds the currently selected objects to the currently selected skeletons.

    Returns: `string` Command result

    """
    pass


def blend2(*args, **kwargs):
    """
    This command creates a surface by blending between given curves.

    Returns: `string[]` Object name and node name

    """
    pass


def blendShape(*args, **kwargs):
    """
    This command creates a blendShape deformer, which blends in specified amounts of each target shape to the initial base shape.

    Returns: `string[]` (the blendShape node name)

    """
    pass


def blendShapeEditor(*args, **kwargs):
    """
    This command creates an editor that derives from the base editor class that has controls for blendShape, control nodes.

    Returns: `string` The name of the editor

    """
    pass


def blendShapePanel(*args, **kwargs):
    """
    This command creates a panel that derives from the base panel class that houses a blendShapeEditor.

    Returns: `string` The name of the panel

    """
    pass


def blendTwoAttr(*args, **kwargs):
    """
    A blendTwoAttr nodes takes two inputs, and blends the values of the inputs from one to the other, into an output value.

    Returns: `string[]` The names of the blendTwoAttr dependency nodes that were created.

    """
    pass


def blindDataType(*args, **kwargs):
    """
    This command creates a blind data type, which is represented by a blindDataTemplate node in the DG.

    Returns: `string` Name of nodes created

    """
    pass


def boneLattice(*args, **kwargs):
    """
    This command creates/edits/queries a boneLattice deformer.

    Returns: `string` Name of bone lattice algorithm node created/edited.

    """
    pass


def boundary(*args, **kwargs):
    """
    This command produces a boundary surface given 3 or 4 curves.

    Returns: `string[]` Object name and node name

    """
    pass


def boxDollyCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a dolly context.

    Returns: `string` The name of the context

    """
    pass


def boxZoomCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a box zoom context.

    Returns: `string` The name of the context

    """
    pass


def bufferCurve(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` Number of buffer curves

    """
    pass


def buildBookmarkMenu(*args, **kwargs):
    """
    This command handles building the "dynamic" Bookmark menu, to show all bookmarks ("sets") of a specified type ("sets -text").

    Returns: None
    """
    pass


def buildKeyframeMenu(*args, **kwargs):
    """
    This command handles building the "dynamic" Keyframe menu, to show attributes of currently selected objects, filtered by the current manipulator.

    Returns: None
    """
    pass


def button(*args, **kwargs):
    """
    Create a button control capable of displaying a textual label and executing a command when selected by the user.

    Returns: `string` Full path name to the control.

    """
    pass


def buttonManip(*args, **kwargs):
    """
    This creates a button manipulator.

    Returns: None
    """
    pass


def cacheFile(*args, **kwargs):
    """
    Creates one or more cache files on disk to store attribute data for a span of frames.

    Returns: `string` name of created cache description file(s)

    """
    pass


def cacheFileCombine(*args, **kwargs):
    """
    Creates a cacheBlend node that can be used to combine, layer or blend multiple cacheFiles for a given object.

    Returns: `string` Name of created cache layer node(s)

    """
    pass


def cacheFileMerge(*args, **kwargs):
    """
    If selected/specified caches can be successfully merged, will return the start/end frames of the new cache followed by the start/end frames of any gaps in the merged cache for which no data should be written to file.

    Returns: `float[]` The start and end times of merged cache followed by start/end of any gaps

    `string[]` Names of geometry associated with specified cache in query mode.

    """
    pass


def cacheFileTrack(*args, **kwargs):
    """
    This command is used for inserting and removing tracks related to the caches displayed in the trax editor.

    Returns: None
    """
    pass


def callbacks(*args, **kwargs):
    """
    This command allows you to add callbacks at key times during UI creation so that the Maya UI can be extended.

    Returns: `string[]` Command result

    """
    pass


def camera(*args, **kwargs):
    """
    Create, edit, or query a camera with the specified properties.

    Returns: `string[]` (transform name and shape name)

    """
    pass


def cameraSet(*args, **kwargs):
    """
    This command manages camera set nodes.

    Returns: `string` The new cameraSet node (when in create mode)

    """
    pass


def cameraView(*args, **kwargs):
    """
    This command creates a preset view for a camera which is then independent of the camera.

    Returns: `string` (name of the camera view)

    """
    pass


def canCreateCaddyManip(*args, **kwargs):
    """
    This command returns true if there can be a manipulator made for the specified selection, false otherwise.

    Returns: `boolean` The queried value

    """
    pass


def canCreateManip(*args, **kwargs):
    """
    This command returns true if there can be a manipulator made for the specified selection, false otherwise.

    Returns: `boolean` Command result

    """
    pass


def canvas(*args, **kwargs):
    """
    Creates a control capable of displaying a color swatch.

    Returns: `string` The full name of the canvas.

    """
    pass


def changeSubdivComponentDisplayLevel(*args, **kwargs):
    """
    Explicitly forces the subdivision surface to display components at a particular level of refinement.

    Returns: `int` Command result

    """
    pass


def changeSubdivRegion(*args, **kwargs):
    """
    Changes a subdivision surface region based on the command parameters.

    Returns: `boolean` Command result

    """
    pass


def channelBox(*args, **kwargs):
    """
    This command creates a channel box, which is sensitive to the active list.

    Returns: `string` (the name of the new channel box)

    """
    pass


def character(*args, **kwargs):
    """
    This command is used to manage the membership of a character.

    Returns: `string` For creation operations (name of the character that was created or edited)

    `string[]` For query operation (names of items in the character)

    `boolean` For isMember operation

    """
    pass


def characterMap(*args, **kwargs):
    """
    This command is used to create a correlation between the attributes of 2 or more characters.

    Returns: `string` characterMap name

    """
    pass


def characterize(*args, **kwargs):
    """
    This command is used to scan a joint hierarchy for predefined joint names or labels.

    Returns: `string` Names of full body IK effectors that were created.

    """
    pass


def checkBox(*args, **kwargs):
    """
    This command creates a check box.

    Returns: `string` Full path name to the control.

    """
    pass


def checkBoxGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def checkDefaultRenderGlobals(*args, **kwargs):
    """
    To query whether or not the defaultRenderGlobals node has been modified since the last file save, use `ls -modified`.

    Returns: None
    """
    pass


def choice(*args, **kwargs):
    """
    The choice command provides a mechanism for changing the inputs to an attribute based on some (usually time-based) criteria.

    Returns: `string[]` The newly created and/or modified choice nodes, with the attribute for which a selector keyframe was created. For example: choice1.input[3] choice2.input[3]

    """
    pass


def circle(*args, **kwargs):
    """
    The circle command creates a circle or partial circle (arc).

    Returns: `string[]` Object name and node name

    """
    pass


def circularFillet(*args, **kwargs):
    """
    The cmd is used to compute the rolling ball surface fillet ( circular fillet ) between two given NURBS surfaces.

    Returns: `string[]` Object name, node name.

    """
    pass


def clearCache(*args, **kwargs):
    """
    Even though dependency graph values are computed or dirty they may still occupy space temporarily within the nodes.

    Returns: `int` Number of items removed from caches

    """
    pass


def clip(*args, **kwargs):
    """
    This command is used to create, edit and query character clips.

    Returns: `string[]` clip names

    """
    pass


def clipEditor(*args, **kwargs):
    """
    Create a clip editor with the given name.

    Returns: `string` Editor name

    """
    pass


def clipEditorCurrentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the track area of a clip editor.

    Returns: `string` Context name

    """
    pass


def clipMatching(*args, **kwargs):
    """
    This command is used to compute an offset to apply on a source clip in order to automatically align it to a destination clip at a specified match element.

    Returns: None
    """
    pass


def clipSchedule(*args, **kwargs):
    """
    This command is used to create, edit and query clips and blends in the Trax editor.

    Returns: `string` Clip name

    """
    pass


def clipSchedulerOutliner(*args, **kwargs):
    """
    This command creates/edits/queries a clip scheduler outliner control.

    Returns: `string` The name of the outliner control.

    """
    pass


def closeCurve(*args, **kwargs):
    """
    The closeCurve command closes a curve, making it periodic.

    Returns: `string[]` Object name and node name

    """
    pass


def closeSurface(*args, **kwargs):
    """
    The closeSurface command closes a surface in the U, V, or both directions, making it periodic.

    Returns: `string[]` Object name and node name

    """
    pass


def cluster(*args, **kwargs):
    """
    The cluster command creates a cluster or edits the membership of an existing cluster.

    Returns: `string[]` (the cluster node name and the cluster handle name)

    """
    pass


def cmdFileOutput(*args, **kwargs):
    """
    This command will open a text file to receive all of the commands and results that normally get printed to the Script Editor window or console.

    Returns: `int` : On open, returns a value (descriptor) that can be used to query the status or close the file. Otherwise, a status code indicating status of file

    """
    pass


def cmdScrollFieldExecuter(*args, **kwargs):
    """
    A script editor executer control used to issue script commands to Maya.

    Returns: `string` The name of the executer control

    """
    pass


def cmdScrollFieldReporter(*args, **kwargs):
    """
    A script editor reporter control used to receive and display the history of processed commmands.

    Returns: `string` The name of the reporter control

    """
    pass


def cmdShell(*args, **kwargs):
    """
    This command creates a scrolling field that behaves similar to a unix shell for entering user input.

    Returns: `string` Full path name to the control.

    """
    pass


def coarsenSubdivSelectionList(*args, **kwargs):
    """
    Coarsens a subdivision surface set of components based on the selection list.

    Returns: `boolean` Command result

    """
    pass


def collision(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string[]` Geometry names that were setup for particle collision.

    """
    pass


def color(*args, **kwargs):
    """
    This command sets the dormant wireframe color of the specified objects to be their class color or if the -ud/userDefined flag is specified, one of the user defined colors.

    Returns: None
    """
    pass


def colorAtPoint(*args, **kwargs):
    """
    The  command is used to query textures or ocean           shaders at passed in uv coordinates.

    Returns: None
    """
    pass


def colorEditor(*args, **kwargs):
    """
    The  command displays a modal dialog that may be used to specify colors in RGB or HSV.

    Returns: `string` The string format is "float float float boolean". The first three float values correspond to the color components.  The final argument is 1 if the dialog's "OK" button was pressed, and 0 if the "Cancel" button was pressed.

    """
    pass


def colorIndex(*args, **kwargs):
    """
    The index specifies a color index in the color palette.

    Returns: `int` Returns 1 on success.

    """
    pass


def colorIndexSliderGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def colorInputWidgetGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` (the name of the created group)

    """
    pass


def colorManagementCatalog(*args, **kwargs):
    """
    This non-undoable action performs additions and removals of custom color transforms from the Autodesk native color transform catalog.

    Returns: None
    """
    pass


def colorManagementConvert(*args, **kwargs):
    """
    This command can be used to convert rendering (a.

    Returns: None
    """
    pass


def colorManagementFileRules(*args, **kwargs):
    """
    This non-undoable action manages the list of rules that Maya uses to assign an initial input color space to dependency graph nodes that read in color information from a file.

    Returns: None
    """
    pass


def colorManagementPrefs(*args, **kwargs):
    """
    This command allows querying and editing the color management global data in a scene.

    Returns: None
    """
    pass


def colorSliderButtonGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def colorSliderGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def columnLayout(*args, **kwargs):
    """
    This command creates a layout that arranges its children in a single column.

    Returns: `string` Full path name to the control.

    """
    pass


def combinationShape(*args, **kwargs):
    """
    Command to create or edit drive relationship of blend shape targets.

    Returns: `Int` In edit mode, return the newly created combination shape node name.

    """
    pass


def commandEcho(*args, **kwargs):
    """
    This command controls what is echoed to the command window.

    Returns: None
    """
    pass


def commandLine(*args, **kwargs):
    """
    This command creates a single line for command input/output.

    Returns: `string` : Full path name to the control.

    """
    pass


def commandLogging(*args, **kwargs):
    """
    This command controls logging of Maya commands, in memory and on disk.

    Returns: None
    """
    pass


def commandPort(*args, **kwargs):
    """
    Opens or closes the Maya command port.

    Returns: `boolean` - in query mode

    """
    pass


def componentBox(*args, **kwargs):
    """
    This command creates a component box, which is sensitive to the active list.

    Returns: `string` (the name of the new component box)

    """
    pass


def componentEditor(*args, **kwargs):
    """
    This command creates a new component editor in the current layout.

    Returns: `string` The panel name

    """
    pass


def condition(*args, **kwargs):
    """
    This command creates a new named condition object whose true/false value is calculated by running a mel script.

    Returns: None
    """
    pass


def cone(*args, **kwargs):
    """
    The cone command creates a new cone and/or a dependency node that creates one, and returns their names.

    Returns: `string[]` Object name and node name

    """
    pass


def confirmDialog(*args, **kwargs):
    """
    The confirmDialog command creates a modal dialog with a message to the user and a variable number of buttons to dismiss the dialog.

    Returns: `string` `Indicates how the dialog was dismissed. If a button is
pressed then the label of the button is returned. If the dialog is
closed then the value for the flag dismissString is
returned.`
    """
    pass


def connectAttr(*args, **kwargs):
    """
    Connect the attributes of two dependency nodes and return the names of the two connected attributes.

    Returns: `string` A phrase containing the names of the connected attributes.

    """
    pass


def connectControl(*args, **kwargs):
    """
    This command attaches a UI widget, specified as the first argument, to one or more dependency node attributes.

    Returns: None
    """
    pass


def connectDynamic(*args, **kwargs):
    """
    Dynamic connection specifies that the force fields, emitters, or collisions of an object affect another dynamic object.

    Returns: `string` Command result

    """
    pass


def connectJoint(*args, **kwargs):
    """
    This command will connect two skeletons based on the two selected joints.

    Returns: None
    """
    pass


def connectionInfo(*args, **kwargs):
    """
    The  command is used to get information about connection sources and destinations.

    Returns: `boolean` When asking for a property, depending on the flags used.

    `string` When asking for a plug name.

    `string[]` When asking for a list of plugs.

    """
    pass


def constrain(*args, **kwargs):
    """
    This command constrains rigid bodies to the world or other rigid bodies.

    Returns: None
    """
    pass


def constructionHistory(*args, **kwargs):
    """
    This command turns construction history on or off.

    Returns: None
    """
    pass


def container(*args, **kwargs):
    """
    
    Returns: `string` Name of the node created.

    """
    pass


def containerBind(*args, **kwargs):
    """
    This is an accessory command to the container command which is used for some automated binding operations on the container.

    Returns: None
    """
    pass


def containerProxy(*args, **kwargs):
    """
    Creates a new container with the same published interface, dynamic attributes and attribute values as the specified container but with fewer container members.

    Returns: None
    """
    pass


def containerPublish(*args, **kwargs):
    """
    This is an accessory command to the container command which is used for some advanced publishing operations on the container.

    Returns: None
    """
    pass


def containerTemplate(*args, **kwargs):
    """
    A container template is a description of a container's published interface.

    Returns: None
    """
    pass


def containerView(*args, **kwargs):
    """
    A container view defines the layout information for the published attributes of a particular container.

    Returns: None
    """
    pass


def contentBrowser(*args, **kwargs):
    """
    This command is used to edit and query a Content Browser.

    Returns: `string` The name of the panel

    """
    pass


def contextInfo(*args, **kwargs):
    """
    This command allows you to get information on named contexts.

    Returns: `string` Info requested

    """
    pass


def control(*args, **kwargs):
    """
    This command allows you to edit or query the properties of any control.

    Returns: None
    """
    pass


def controller(*args, **kwargs):
    """
    Commands for managing animation sources.

    Returns: `string` Command result

    """
    pass


def convertIffToPsd(*args, **kwargs):
    """
    Converts iff file to PSD file of given size.

    Returns: None
    """
    pass


def convertSolidTx(*args, **kwargs):
    """
    Command to convert a texture on a surface to a file texture.

    Returns: `string[]` File texture nodes

    """
    pass


def convertTessellation(*args, **kwargs):
    """
    Command to translate the basic tessellation attributes to advanced.

    Returns: `boolean` Success or Failure.

    """
    pass


def convertUnit(*args, **kwargs):
    """
    This command converts values between different units of measure.

    Returns: `float` or string

    """
    pass


def copyAttr(*args, **kwargs):
    """
    Given two nodes, transfer the connections and/or the values from the first node to the second for all attributes whose names and data types match.

    Returns: None
    """
    pass


def copyDeformerWeights(*args, **kwargs):
    """
    Command to copy or mirror the deformer weights accross one  of the three major axes.

    Returns: None
    """
    pass


def copyFlexor(*args, **kwargs):
    """
    This command copies an existing bone or joint flexor from one bone (joint) to another.

    Returns: `string` The name of the new flexor node

    """
    pass


def copyKey(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` Number of animation curves copied.

    """
    pass


def copySkinWeights(*args, **kwargs):
    """
    Command to copy or mirror the skinCluster weights accross one  of the three major axes.

    Returns: None
    """
    pass


def crashInfo(*args, **kwargs):
    """
    Provides an interface to the crash file information.

    Returns: None
    """
    pass


def createAttrPatterns(*args, **kwargs):
    """
    Create a new instance of an attribute pattern given a pattern type (e.

    Returns: `string` Name of created pattern

    """
    pass


def createDisplayLayer(*args, **kwargs):
    """
    Create a new display layer.

    Returns: `string` Name of display layer node that was created

    """
    pass


def createEditor(*args, **kwargs):
    """
    This command creates a property sheet for any dependency node.

    Returns: None
    """
    pass


def createLayeredPsdFile(*args, **kwargs):
    """
    Creates a  layered PSD file with image names as input to individual layers.

    Returns: None
    """
    pass


def createNode(*args, **kwargs):
    """
    This command creates a new node in the dependency graph of the specified type.

    Returns: `string` The name of the new node.

    """
    pass


def createRenderLayer(*args, **kwargs):
    """
    Create a new render layer.

    Returns: `string` Name of render layer node that was created

    """
    pass


def createSubdivRegion(*args, **kwargs):
    """
    Creates a subdivision surface region based on the selection list.

    Returns: `boolean` Command result

    """
    pass


def ctxAbort(*args, **kwargs):
    """
    This command tells the current context to reset itself, losing what has been done so far.

    Returns: None
    """
    pass


def ctxCompletion(*args, **kwargs):
    """
    This command tells the current context to finish what it is doing and create any objects that is is working on.

    Returns: None
    """
    pass


def ctxEditMode(*args, **kwargs):
    """
    This command tells the current context to switch edit modes.

    Returns: None
    """
    pass


def ctxTraverse(*args, **kwargs):
    """
    This command tells the current context to do a traversal.

    Returns: None
    """
    pass


def currentCtx(*args, **kwargs):
    """
    This command returns the currently selected tool context.

    Returns: `string` : The name of the currently selected tool context.

    """
    pass


def currentTime(*args, **kwargs):
    """
    When given a time argument (with or without the -edit flag) this command sets the current global time.

    Returns: `time` Command result

    """
    pass


def currentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the graph editor.

    Returns: `string` Context name

    """
    pass


def currentUnit(*args, **kwargs):
    """
    This command allows you to change the units in which you will work in Maya.

    Returns: `string` The new current unit that has been set

    """
    pass


def curve(*args, **kwargs):
    """
    The curve command creates a new curve from a list of control vertices (CVs).

    Returns: `string` The path to the new curve or the replaced curve

    """
    pass


def curveAddPtCtx(*args, **kwargs):
    """
    The curveAddPtCtx command creates a new curve add points context, which adds either control vertices (CVs) or edit points to an existing curve.

    Returns: `string` (name of the new context)

    """
    pass


def curveCVCtx(*args, **kwargs):
    """
    The curveCVCtx command creates a new context for creating curves by placing control vertices (CVs).

    Returns: `string` (name of the new context)

    """
    pass


def curveEPCtx(*args, **kwargs):
    """
    The curveEPCtx command creates a new context for creating curves by placing edit points.

    Returns: `string` (name of the new context)

    """
    pass


def curveEditorCtx(*args, **kwargs):
    """
    The curveEditorCtx command creates a new NURBS editor context, which is used to edit a NURBS curve or surface.

    Returns: `string` (name of the new context)

    """
    pass


def curveIntersect(*args, **kwargs):
    """
    You must specify two curves to intersect.

    Returns: `string` the parameter values at which two curves intersect.

    """
    pass


def curveMoveEPCtx(*args, **kwargs):
    """
    The curveMoveEPCtx command creates a new context for moving curve edit points using a manipulator.

    Returns: `string` (name of the new context)

    """
    pass


def curveOnSurface(*args, **kwargs):
    """
    The curve command creates a new curve from a list of control vertices (CVs).

    Returns: `string` - name of new curve-on-surface

    `string` The path to the new curve or the replaced curve

    """
    pass


def curveRGBColor(*args, **kwargs):
    """
    This command creates, changes or removes custom curve colors, which are used to draw the curves in the Graph Editor.

    Returns: `float[]` HSV values from querying the hsv flag

    """
    pass


def curveSketchCtx(*args, **kwargs):
    """
    The curveSketchCtx command creates a new curve sketch context, also known as the "pencil context".

    Returns: `string` (name of the new curve sketch context)

    """
    pass


def cutKey(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` Number of animation curves cut.

    """
    pass


def cycleCheck(*args, **kwargs):
    """
    This command searches for plug cycles in the dependency graph.

    Returns: `boolean` in the general case.

    `string[]` When the list flag is used.

    """
    pass


def cylinder(*args, **kwargs):
    """
    The cylinder command creates a new cylinder and/or a dependency node that creates one, and returns their names.

    Returns: `string[]` Object name and node name

    """
    pass


def dagObjectCompare(*args, **kwargs):
    """
    
    Returns: None
    """
    pass


def dagPose(*args, **kwargs):
    """
    This command is used to save and restore the matrix information for a dag hierarchy.

    Returns: `string` Name of pose

    """
    pass


def dataStructure(*args, **kwargs):
    """
    Takes in a description of the structure and creates it, adding it to the list of available data structures.

    Returns: `string` Name of the resulting structure, should match the name defined in the structure description

    `string[]` Name(s) of the removed structures.

    """
    pass


def date(*args, **kwargs):
    """
    Returns information about current time and date.

    Returns: `string` Command result

    """
    pass


def dbcount(*args, **kwargs):
    """
    The  command is used to print and manage a list of statistics collected for counting operations.

    Returns: None
    """
    pass


def dbfootprint(*args, **kwargs):
    """
    This command lets you explore the memory usage of specific parts of the scene.

    Returns: `string` JSON data representing the memory usage of the requested objects

    `string[]` List of types for which footprint measurements can be made (Query with no flags)

    `string` Description of what a particular type will measure (Query with a 'type' flag)

    """
    pass


def dbmessage(*args, **kwargs):
    """
    The  command is used to install monitors for certain message types, dumping debug information as they are sent so that the flow of messages can be examined.

    Returns: None
    """
    pass


def dbpeek(*args, **kwargs):
    """
    The  command is used to analyze the Maya data for information of interest.

    Returns: `string[]` Query of operation yields a string array with available operations

    `string[]` Query of argument yields a string array with available argument definitions on the specified operation

    `string` Query of specific operation without an output file returns a string with help information for that operation

    `int` Query of specific operation with an output file dumps the help information for that operation to that file and returns the number of errors encountered

    """
    pass


def dbtrace(*args, **kwargs):
    """
    The  command is used to manipulate trace objects.

    Returns: None
    """
    pass


def defaultLightListCheckBox(*args, **kwargs):
    """
    This command creates a checkBox that controls whether a shadingGroup is connected/disconnected from the defaultLightList.

    Returns: `string` Full name to the control

    """
    pass


def defaultNavigation(*args, **kwargs):
    """
    The defaultNavigation command defines default behaviours when creating or manipulating connections between nodes and when navigating between nodes via those connections.

    Returns: `string` or array of strings

    """
    pass


def defineDataServer(*args, **kwargs):
    """
    Connects to the specified data servername, creating a named device which then can be attached to device handlers.

    Returns: None
    """
    pass


def defineVirtualDevice(*args, **kwargs):
    """
    This command defines a virtual device.

    Returns: None
    """
    pass


def deformer(*args, **kwargs):
    """
    This command creates a deformer of the specified type.

    Returns: `string[]` Name of the algorithm node created/edited.

    """
    pass


def deformerEvaluator(*args, **kwargs):
    """
    Print debug information about deformer evaluator status.

    Returns: `string[]` the debug information when query mode is used.

    """
    pass


def deformerWeights(*args, **kwargs):
    """
    Command to import and export deformer weights to and from a simple XML  file.

    Returns: `STRING` path to the file imported/exported, if successful

    """
    pass


def delete(*args, **kwargs):
    """
    This command is used to delete selected objects, or all objects, or objects specified along with the command.

    Returns: None
    """
    pass


def deleteAttr(*args, **kwargs):
    """
    This command is used to delete a dynamic attribute from a node or nodes.

    Returns: None
    """
    pass


def deleteAttrPattern(*args, **kwargs):
    """
    After a while the list of attribute patterns could become cluttered.

    Returns: `string` Name(s) of deleted pattern(s)

    """
    pass


def deleteExtension(*args, **kwargs):
    """
    This command is used to delete an extension attribute from a node type.

    Returns: `int` Number of nodes with altered data after the delete

    """
    pass


def deleteUI(*args, **kwargs):
    """
    This command deletes UI objects such as windows and controls.

    Returns: None
    """
    pass


def deltaMush(*args, **kwargs):
    """
    This command is used to create, edit and query deltaMush nodes.

    Returns: `string` Delta mush deformer node name

    """
    pass


def detachCurve(*args, **kwargs):
    """
    The detachCurve command detaches a curve into pieces, given a list of parameter values.

    Returns: `string[]` Object name and node name

    """
    pass


def detachDeviceAttr(*args, **kwargs):
    """
    This command detaches connections between device axes and node attributes.

    Returns: None
    """
    pass


def detachSurface(*args, **kwargs):
    """
    The detachSurface command detaches a surface into pieces, given a list of parameter values and a direction.

    Returns: `string[]` Object name and node name

    """
    pass


def deviceEditor(*args, **kwargs):
    """
    This creates an editor for creating/modifying attachments to input devices.

    Returns: `string` name of the editor

    """
    pass


def deviceManager(*args, **kwargs):
    """
    This command queriers the internal device manager for information on attached devices.

    Returns: None
    """
    pass


def devicePanel(*args, **kwargs):
    """
    This command is now obsolete.

    Returns: `string` name of panel

    """
    pass


def dgInfo(*args, **kwargs):
    """
    This command prints information about the DG in plain text.

    Returns: None
    """
    pass


def dgdirty(*args, **kwargs):
    """
    The  command is used to force a dependency graph dirty message on a node or plug.

    Returns: `string[]` List of dirty/clean plugs in list plug mode.

    `string[]` List of plugs with dirty/clean data in list data mode.

    `string[]` Pairs of dirty/clean connected plugs in list connection mode.

    `int` Number of dirty/clean messages sent out in normal mode.

    """
    pass


def dgeval(*args, **kwargs):
    """
    The  command is used to force a dependency graph evaluate of a node or plug.

    Returns: None
    """
    pass


def dgfilter(*args, **kwargs):
    """
    The  command is used to define Dependency Graph filters that select DG objects based on certain criteria.

    Returns: `string` if creating filter or getting filter info

    `string[]` if listing filters

    `boolean` if applying filter

    """
    pass


def dgmodified(*args, **kwargs):
    """
    The  command is used to find out which nodes in the           dependency graph have been modified.

    Returns: `string[]` list of all nodes that have been modified

    """
    pass


def dgtimer(*args, **kwargs):
    """
    This command measures dependency graph node performance by managing timers on a per-node basis.

    Returns: `float` By default, the total of self-compute time for all nodes. Can be modified via the -returnType, -sortMetric and -sortType flags.

    """
    pass


def dimWhen(*args, **kwargs):
    """
    This method attaches the named UI object (first argument) to the named condition (second argument) so that the object will be dimmed when the condition is in a particular state.

    Returns: None
    """
    pass


def directKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to directly manipulate keyframes within the graph editor.

    Returns: `string` Context name

    """
    pass


def directionalLight(*args, **kwargs):
    """
    TlightCmd is the base class for other light commands.

    Returns: `double[]` when querying the rgb or shadowColor flags double when querying the intensity flag boolean when querying the useRayTraceShadows or exclusive flags linear[] when querying the position flag angle[] when querying the rotation flag string when querying the name flag

    `int` rate of light decay, when querying the decayRate flag

    `int` Number of shadow samples, when querying the shadowSamples flag boolean True if soft shadows are enabled, when querying the softShadow flag float Shadow dithering value, when querying the shadowDither flag float Disc radius value, when querying the discRadius flag

    `string` Light shape name

    """
    pass


def dirmap(*args, **kwargs):
    """
    Use this command to map a directory to another directory.

    Returns: `string` when convertDirectory is used

    """
    pass


def disable(*args, **kwargs):
    """
    This command enables or disables the control passed as argument.

    Returns: None
    """
    pass


def disableIncorrectNameWarning(*args, **kwargs):
    """
    Disable the warning dialog which complains about incorrect node names when opening Maya files.

    Returns: None
    """
    pass


def disconnectAttr(*args, **kwargs):
    """
    Disconnects two connected attributes.

    Returns: `string` A phrase containing the names of the disconnected attributes.

    """
    pass


def disconnectJoint(*args, **kwargs):
    """
    This command will break a skeleton at the selected joint and delete any associated handles.

    Returns: `string` After the joint is disconnected, a new joint will be created. The return value is the name of the newly created joint and its ancestor.

    """
    pass


def diskCache(*args, **kwargs):
    """
    Command to create, clear, or close disk cache(s).

    Returns: None
    """
    pass


def displacementToPoly(*args, **kwargs):
    """
    Command bakes geometry with displacement mapping into a polygonal object.

    Returns: `boolean` Success or Failure.

    """
    pass


def displayAffected(*args, **kwargs):
    """
    Turns on/off the special coloring of objects that are affected by the objects that are currently in the selection list.

    Returns: `int` Affected display count

    """
    pass


def displayColor(*args, **kwargs):
    """
    This command changes or queries the display color for anything in the application that allows the user to set its color.

    Returns: None
    """
    pass


def displayCull(*args, **kwargs):
    """
    This command is responsible for setting the display culling property of back faces of surfaces.

    Returns: None
    """
    pass


def displayLevelOfDetail(*args, **kwargs):
    """
    This command is responsible for setting the display level-of-detail for edit refreshes.

    Returns: None
    """
    pass


def displayPref(*args, **kwargs):
    """
    This command sets/queries the state of global display parameters.

    Returns: None
    """
    pass


def displayRGBColor(*args, **kwargs):
    """
    This command changes or queries the display color for anything in the application that allows the user to set its color.

    Returns: `string` when the list flag is used, none otherwise

    """
    pass


def displaySmoothness(*args, **kwargs):
    """
    This command is responsible for setting the display smoothness of NURBS curves and surfaces to either predefined or custom values.

    Returns: None
    """
    pass


def displayString(*args, **kwargs):
    """
    Assign a string value to a string identifier.

    Returns: None
    """
    pass


def displaySurface(*args, **kwargs):
    """
    This command toggles display options on the specified or active surfaces.

    Returns: `boolean` when in the query mode.

    """
    pass


def distanceDimContext(*args, **kwargs):
    """
    Command used to register the distanceDimCtx tool.

    Returns: `string` - name of the context created

    """
    pass


def distanceDimension(*args, **kwargs):
    """
    This command is used to create a distance dimension to display the distance between two specified points.

    Returns: `string` - the shape name of the DAG node created.

    """
    pass


def doBlur(*args, **kwargs):
    """
    The doBlur command  will invoke the blur2d, which is a Maya stand-alone application to do 2.

    Returns: `string` Command result

    """
    pass


def dockControl(*args, **kwargs):
    """
    Create a dockable control, also known as tool palette or utility window.

    Returns: `string` Full path name to the control.

    """
    pass


def dolly(*args, **kwargs):
    """
    The dolly command moves a camera along the viewing direction in the world space.

    Returns: None
    """
    pass


def dollyCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a dolly context.

    Returns: `string` The name of the context

    """
    pass


def dopeSheetEditor(*args, **kwargs):
    """
    Edit a characteristic of a dope sheet editor.

    Returns: `string` Editor name

    """
    pass


def doubleProfileBirailSurface(*args, **kwargs):
    """
    The arguments are 4 cuves called "profile1" "profile2" "rail1" "rail2".

    Returns: `string[]` Object name and node name

    """
    pass


def drag(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def dragAttrContext(*args, **kwargs):
    """
    The dragAttrContext allows a user to manipulate the attributes of an object by using a virtual slider within the viewport.

    Returns: `string` The name of the context created

    """
    pass


def draggerContext(*args, **kwargs):
    """
    The draggerContext allows the user to program the behavior of the mouse or an equivalent dragging device in MEL.

    Returns: `string` The name of the context.

    """
    pass


def dropoffLocator(*args, **kwargs):
    """
    This command adds one or more dropoff locators to a wire curve, one for each selected curve point.

    Returns: `string[]` Locator name(s)

    """
    pass


def duplicate(*args, **kwargs):
    """
    This command duplicates the given objects.

    Returns: `string[]` : names of the objects created

    """
    pass


def duplicateCurve(*args, **kwargs):
    """
    The duplicateCurve command takes a curve on a surface and and returns the 3D curve.

    Returns: `string[]` Object name and node name

    """
    pass


def duplicateSurface(*args, **kwargs):
    """
    The duplicateSurface command takes a surface patch (face) and and returns the 3D surface.

    Returns: `string[]` Object name and node name

    """
    pass


def dynCache(*args, **kwargs):
    """
    Cache the current state of all particle shapes at the current time.

    Returns: None
    """
    pass


def dynExport(*args, **kwargs):
    """
    Export particle data to disk files.

    Returns: `string` Path to the exported files

    """
    pass


def dynExpression(*args, **kwargs):
    """
    This command describes an expression that belongs to the specified particle shape.

    Returns: `string` The particle shape which this expression belongs to

    """
    pass


def dynGlobals(*args, **kwargs):
    """
    This node edits and queries the attributes of the active dynGlobals node in the scene.

    Returns: `string` For edit commands

    `int` or string For query commands, depending on the flag queried.

    """
    pass


def dynPaintEditor(*args, **kwargs):
    """
    Create a editor window that can be painted into.

    Returns: `string` Editor name

    """
    pass


def dynParticleCtx(*args, **kwargs):
    """
    The particle context command creates a particle context.

    Returns: None
    """
    pass


def dynPref(*args, **kwargs):
    """
    This action modifies and queries the current state of "autoCreate rigid bodies", "run up to current time", and  "run up from" (previous time or start time).

    Returns: None
    """
    pass


def dynamicLoad(*args, **kwargs):
    """
    Dynamically load the DLL passed as argument.

    Returns: None
    """
    pass


def editDisplayLayerGlobals(*args, **kwargs):
    """
    Edit the parameter values common to all display layers.

    Returns: `boolean` Command success

    `string` Current display layer name, when querying

    `int` Merge type, when querying

    `int` Base ID, when querying

    """
    pass


def editDisplayLayerMembers(*args, **kwargs):
    """
    This command is used to query and edit membership of display layers.

    Returns: `int` Number of objects added to the layer

    `string[]` Query: List of objects in layer

    """
    pass


def editMetadata(*args, **kwargs):
    """
    This command is used to set metadata elements onto or remove metadata elements from an object.

    Returns: `string` Name of the node where the new edits reside, empty string if edits failed. It will be an editMetadata node if construction history was present.

    """
    pass


def editRenderLayerAdjustment(*args, **kwargs):
    """
    This command is used to create, edit, and query adjustments to render layers.

    Returns: `int` Number of adjustments applied

    `string[]` Query: List of plugs adjustments to layer

    """
    pass


def editRenderLayerGlobals(*args, **kwargs):
    """
    Edit the parameter values common to all render layers.

    Returns: `boolean` Command success

    `string` Current render layer name, when querying

    `int` Merge type, when querying

    `int` Base ID, when querying

    """
    pass


def editRenderLayerMembers(*args, **kwargs):
    """
    This command is used to query and edit memberships to render layers.

    Returns: `int` Number of objects added to the layer

    `string[]` Query: List of objects in layer

    """
    pass


def editor(*args, **kwargs):
    """
    Edit the characteristic of an editor.

    Returns: `string` Name of the editor

    """
    pass


def editorTemplate(*args, **kwargs):
    """
    The editorTemplate command allows the user to specify the conceptual layout of an attribute editor and leave the details of exactly which UI elements are used in the final result to the automatic dialog generation mechanism.

    Returns: `string` For queryControl, the appropriate attribute type will be returned. string array For listExtraAttributes, extra attributes will be returned.

    """
    pass


def effector(*args, **kwargs):
    """
    The effector command is used to set the name or hidden flag for the effector.

    Returns: `string` Command result

    """
    pass


def emit(*args, **kwargs):
    """
    The  action allows users to add particles to an existing particle object without the use of an emitter.

    Returns: `int[]` `Integer array containing the list of the particleId attribute values
for the created particles in the same order that the position flags
were passed.`
    """
    pass


def emitter(*args, **kwargs):
    """
    Creates, edits or queries an auxiliary dynamics object (for example, a field or emitter).

    Returns: `string` Command result

    """
    pass


def enableDevice(*args, **kwargs):
    """
    Sets (or queries) the device enable state for actions involving the device.

    Returns: None
    """
    pass


def encodeString(*args, **kwargs):
    """
    This action will take a string and encode any character that would need to be escaped before being sent to some other command.

    Returns: `string` Command result

    """
    pass


def error(*args, **kwargs):
    """
    The error command is provided so that the user can issue error messages from his/her scripts and control execution in the event of runtime errors.

    Returns: None
    """
    pass


def eval(*args, **kwargs):
    """
    This function takes a string which contains MEL code and evaluates it using the MEL interpreter.

    Returns: `Any` depending on input.

    """
    pass


def evalDeferred(*args, **kwargs):
    """
    This command takes the string it is given and evaluates it during the next available idle time.

    Returns: `string[]` Command result

    """
    pass


def evaluationManager(*args, **kwargs):
    """
    Handles turning on and off the evaluation manager method of evaluating the DG.

    Returns: `string[]` The names of all evaluation manager modes (querying without flags)

    `string[]` The names of all nodes involved in a cycle cluster with the selected one.

    `boolean` The success of activating of deactivating manipulation (with the 'manipulation' flag)

    `boolean` The manipulation active or inactive state (querying the 'manipulation' flag)

    `boolean` The success of setting the evaluation manager mode (with the 'mode' flag)

    `boolean` The success of setting the evaluation manager idle refresh build mode (with the 'idleBuild' flag)

    `boolean` Is the idle refresh build mode active? (querying with the 'idleBuild' flag)

    `boolean` Is the evaluation graph currently valid? (querying with the 'invalidate' flag)

    `boolean` The success of setting the node type parallel scheduling mode (with the 'nodeTypeParallel' flag)

    `boolean[]` The parallel scheduling states of specified node types (querying the 'nodeTypeParallel' flag with object(s))

    `string[]` The names of all node types in parallel scheduling mode (querying the 'nodeTypeParallel' flag alone)

    `boolean` The success of setting the node type serialized mode (with the 'nodeTypeSerialize' flag)

    `boolean[]` The serialized states of specified node types (querying the 'nodeTypeSerialize' flag with object(s))

    `string[]` The names of all node types in serial scheduling mode (querying the 'nodeTypeSerialize' flag alone)

    `boolean` The success of setting the node type globally serialized mode (with the 'nodeTypeGloballySerialize' flag)

    `boolean[]` The globally serialized states of specified node types (querying the 'nodeTypeGloballySerialize' flag with object(s))

    `string[]` The names of all node types in globally serialized scheduling mode (querying the 'nodeTypeGloballySerialize' flag alone)

    `boolean` The success of setting the node type untrusted mode (with the 'nodeTypeUntrusted' flag)

    `boolean[]` The untrusted of specified node types (querying the 'nodeTypeUntrusted' flag with object(s))

    `string[]` The names of all node types in untrusted scheduling mode (querying the 'nodeTypeUntrusted' flag alone)

    `string` The evaluation manager mode (querying with the 'mode' flag)

    `string[]` The names of all nodes immediately downstream/upstream of the named one(s) (with the 'upstreamFrom' or 'downstreamFrom' flags)

    """
    pass


def evaluator(*args, **kwargs):
    """
    Handles turning on and off custom evaluation overrides used by the evaluation manager.

    Returns: `string[]` the list of available evaluators (querying with no evaluator flag or invalid evaluator name)

    `boolean` the previous active state of the named evaluator (with 'name' and 'enable' flags)

    `boolean` the active state of the named evaluator (query with 'name' and 'enable' flags)

    `string[]` the list of evaluators in the requested active state (query 'enable' flag alone)

    `string[]` the list of nodes for which the evaluator was activated or deactivated (with 'nodeType' or 'nodeTypeChildren' flags)

    `string` the queried value for the evaluator (with 'name' and 'valueName' flags)

    `boolean` true if the configuration request was accepted by the evaluator (with 'name' flag and 'configuration' flag)

    `string[]` the list of configuration parameters accepted by the evaluator (query mode with 'name' flag and 'configuration' flag)

    `string[]` the list of clusters currently assigned to the evaluator with intervening sublist sizes (query mode with 'name' flag and 'clusters' flag)

    `string` the help information supplied by the evaluator (query mode with 'name' flag and 'info' flag)

    `int` the priority value of the evaluator (query mode with 'name' flag and 'priority' flag)

    """
    pass


def event(*args, **kwargs):
    """
    The event command assigns collision events to a particle object.

    Returns: `string` for creation; string array for list.

    """
    pass


def exactWorldBoundingBox(*args, **kwargs):
    """
    This command figures out an exact-fit bounding box for the specified objects (or selected objects if none are specified) This bounding box is always in world space.

    Returns: `float[]` xmin, ymin, zmin, xmax, ymax, zmax.

    """
    pass


def exclusiveLightCheckBox(*args, **kwargs):
    """
    This command creates a checkBox that controls a light's exclusive non-exclusive status.

    Returns: `string` Full name to the control

    """
    pass


def expandedSelection(*args, **kwargs):
    """
    Examines the current selection list and returns that list, expanded to meet certain criteria.

    Returns: `string` List of objects in the requested selection list expansion

    `string[]` List of nodes visited in the DG expansion

    `string[]` (Python only) List of single nodes and tuples visited in the EG or SG expansion, where tuples represent the DG nodes in a cluster

    """
    pass


def exportEdits(*args, **kwargs):
    """
    Use this command to export edits made in the scene to a file.

    Returns: `string[]` For query execution.

    """
    pass


def expression(*args, **kwargs):
    """
    This command describes an expression that belongs to the current scene.

    Returns: `string` The name of the expression

    """
    pass


def expressionEditorListen(*args, **kwargs):
    """
    Listens for messages for the Expression Editor, at its request, and communicates them to it.

    Returns: None
    """
    pass


def extendCurve(*args, **kwargs):
    """
    This command extends a curve or creates a new curve as an extension.

    Returns: `string[]` Object name and node name

    """
    pass


def extendSurface(*args, **kwargs):
    """
    This command extends a surface or creates a new surface as an extension.

    Returns: `string[]` Object name and node name

    """
    pass


def extrude(*args, **kwargs):
    """
    This command computes a surface given a profile curve and possibly a path curve.

    Returns: `string[]` Object name and node name

    """
    pass


def falloffCurve(*args, **kwargs):
    """
    This command creates a control for editing a 2D control curve.

    Returns: `string` The name of the port created or modified

    """
    pass


def falloffCurveAttr(*args, **kwargs):
    """
    
    Returns: `string` The name of the port created or modified

    """
    pass


def fcheck(*args, **kwargs):
    """
    Invokes the fcheck program to display images in a separate window.

    Returns: None
    """
    pass


def file(*args, **kwargs):
    """
    
    Returns: `string` The name of the specified file for most actions. When the returnNewNodes flag is used, an array of strings will be returned indicating the names of the nodes that were read.

    """
    pass


def fileBrowserDialog(*args, **kwargs):
    """
    The fileBrowserDialog and fileDialog commands have now been deprecated.

    Returns: `string` Dialog name

    """
    pass


def fileDialog(*args, **kwargs):
    """
    The fileBrowserDialog and fileDialog commands have now been deprecated.

    Returns: `string` Name of dialog

    """
    pass


def fileDialog2(*args, **kwargs):
    """
    This command provides a dialog that allows users to select files or directories.

    Returns: `string` array

    """
    pass


def fileInfo(*args, **kwargs):
    """
    fileInfo provides a mechanism for keeping information related to a Maya scene file.

    Returns: `string[]` Command result

    """
    pass


def filePathEditor(*args, **kwargs):
    """
    Maya can reference and use external files, such as textures or other Maya scenes.

    Returns: None
    """
    pass


def filletCurve(*args, **kwargs):
    """
    The curve fillet command creates a fillet curve between two curves.

    Returns: `string[]` Object name and node name

    """
    pass


def filter(*args, **kwargs):
    """
    Creates or modifies a filter node.

    Returns: `string` filter name

    """
    pass


def filterCurve(*args, **kwargs):
    """
    The filterCurve command takes a list of anim curve and filters         them.

    Returns: `int` The number of filtered curves

    """
    pass


def filterExpand(*args, **kwargs):
    """
    Based on selected components (or components specified on the command line), the command filters and/or expands the list given the options.

    Returns: `string[]` Command result

    """
    pass


def filterStudioImport(*args, **kwargs):
    """
    Directly sets the filter options on the studioImport plugin from     anywhere in MEL without having to use the UI.

    Returns: None
    """
    pass


def findDeformers(*args, **kwargs):
    """
    This command finds all deformers for the specified shape(s).

    Returns: None
    """
    pass


def findKeyframe(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `time` Command result

    """
    pass


def findType(*args, **kwargs):
    """
    The  command is used to search through a dependency subgraph on a certain node to find all nodes of the given type.

    Returns: `string[]` The list of node(s) of the requested type connected to the given node(s)

    """
    pass


def fitBspline(*args, **kwargs):
    """
    The fitBspline command fits the CVs from an input curve and and returns a 3D curve.

    Returns: `string[]` Object name and node name

    """
    pass


def flexor(*args, **kwargs):
    """
    This command creates a flexor.

    Returns: `string[]` (the names of the new flexor nodes)

    """
    pass


def floatField(*args, **kwargs):
    """
    Create a field control that accepts only float values and is bound by a minimum and maximum value.

    Returns: `string` Full path name to the control.

    """
    pass


def floatFieldGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def floatScrollBar(*args, **kwargs):
    """
    Create a scroll bar control that accepts only float values and is bound by a minimum and maximum value.

    Returns: `string` Full path name to the control.

    """
    pass


def floatSlider(*args, **kwargs):
    """
    Create a slider control that accepts only float values and is bound by a minimum and maximum value.

    Returns: `string` Full path name to the control.

    """
    pass


def floatSlider2(*args, **kwargs):
    """
    This command creates a float slider containing two handles.

    Returns: `string` The name of the port created or modified

    """
    pass


def floatSliderButtonGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def floatSliderGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name of the control.

    """
    pass


def flow(*args, **kwargs):
    """
    The flow command creates a deformation lattice to `bend' the object that is animated along a curve of a motion path animation.

    Returns: `string[]` The names of the created flow node and associated lattice nodes.

    """
    pass


def flowLayout(*args, **kwargs):
    """
    This command creates a layout that arranges its children along a single line (either horizontal or vertical).

    Returns: `string` Full path name to the control.

    """
    pass


def fluidCacheInfo(*args, **kwargs):
    """
    A command to get information about the fluids cache.

    Returns: None
    """
    pass


def fluidEmitter(*args, **kwargs):
    """
    Creates, edits or queries an auxiliary dynamics object (for example, a field or emitter).

    Returns: `string` Command result

    """
    pass


def fluidVoxelInfo(*args, **kwargs):
    """
    Provides basic information about the mapping of a fluid voxel grid into world- or object space of the fluid.

    Returns: None
    """
    pass


def flushUndo(*args, **kwargs):
    """
    Removes everything from the undo queue, freeing up memory.

    Returns: None
    """
    pass


def fontDialog(*args, **kwargs):
    """
    Displays a dialog of available fonts for the user to select from.

    Returns: `string` Dialog name

    """
    pass


def formLayout(*args, **kwargs):
    """
    This command creates a form layout control.

    Returns: `string` The full name of the control.

    """
    pass


def format(*args, **kwargs):
    """
    This command takes a format string, where the format string contains format specifiers.

    Returns: `string` Command result

    """
    pass


def frameBufferName(*args, **kwargs):
    """
    Returns the frame buffer name for a given renderPass renderLayer and camera combination.

    Returns: `string` Command result

    """
    pass


def frameLayout(*args, **kwargs):
    """
    This command creates frame layout control.

    Returns: `string` Full path name to the control.

    """
    pass


def freeFormFillet(*args, **kwargs):
    """
    This command creates a free form surface fillet across two surface trim edges or isoparms or curve on surface.

    Returns: `string[]` Object name and node name

    """
    pass


def freeze(*args, **kwargs):
    """
    When a node is frozen none of its inputs will be requested when they change, the node will use the inputs that existed at the time of freezing until the node is unfrozen.

    Returns: `string[]` In query mode the list of currently frozen or unfrozen nodes. The list is in three parts separated by an empty string; nodes with frozen state (un)set, nodes with frozenAffected state (un)set, and the rest of the selected nodes

    `string[]` the list of nodes whose frozen state was set by the command. The list is in two parts separated by an empty string; nodes with frozen state set, and nodes with frozenAffected state set

    """
    pass


def freezeOptions(*args, **kwargs):
    """
    This command provides access to the options used by the evaluation manager to handle propagation and recognition of when a node is in a frozen state.

    Returns: `string` Current value of the option if querying the downstream or upstream flags

    `boolean` Current value of the option if querying the displayLayers, invisible, referencedNodes, explicitPropagation, or runtimePropagaton flags

    `boolean` In creation mode returns true if all options were successfully set

    """
    pass


def geomBind(*args, **kwargs):
    """
    This command is used to compute weights using geodesic voxel binding algorithm.

    Returns: None
    """
    pass


def geomToBBox(*args, **kwargs):
    """
    Create polygonal mesh bounding boxes for geometry.

    Returns: None
    """
    pass


def geometryConstraint(*args, **kwargs):
    """
    Constrain an object's position based on the shape of the target surface(s) at the closest point(s) to the object.

    Returns: `string[]` Name of the created constraint node

    """
    pass


def getAttr(*args, **kwargs):
    """
    This command returns the value of the named object's attribute.

    Returns: `Any` Value or state of the attribute. The number and type of values returned is dependent on the attribute type.

    """
    pass


def getClassification(*args, **kwargs):
    """
    Returns the classification string for a given node type.

    Returns: `string[]` Returns the classification strings for the given node type, or an empty array if the node type is not classified.

    """
    pass


def getDefaultBrush(*args, **kwargs):
    """
    The command returns the name of the default Paint Effects brush.

    Returns: `string` Name of the default brush node

    """
    pass


def getFileList(*args, **kwargs):
    """
    Returns a list of files matching an optional wildcard pattern.

    Returns: `string[]` an array of file names

    """
    pass


def getFluidAttr(*args, **kwargs):
    """
    Returns values of built-in fluid attributes such as density, velocity, etc.

    Returns: None
    """
    pass


def getInputDeviceRange(*args, **kwargs):
    """
    This command lists the minimum and maximum values the device axis can return.

    Returns: `float[]` Command result

    """
    pass


def getMetadata(*args, **kwargs):
    """
    This command is used to retrieve the values of metadata elements from a node or scene.

    Returns: `int[]` List of integer values from the metadata member

    `float[]` List of real values from the metadata member

    `string[]` List of string values from the metadata member

    """
    pass


def getModifiers(*args, **kwargs):
    """
    This command returns the current state of the modifier keys.

    Returns: `int` indicating which modifier keys are pressed.

    """
    pass


def getModulePath(*args, **kwargs):
    """
    Returns the module path for a given module name.

    Returns: `string` Command result

    """
    pass


def getPanel(*args, **kwargs):
    """
    This command returns panel and panel configuration information.

    Returns: `string[]` An array of panel names

    """
    pass


def getParticleAttr(*args, **kwargs):
    """
    This action will return either an array of values, or the average value and maximum offset, for a specied per-particle attribute of a particle object or component.

    Returns: `float[]` Command result

    """
    pass


def getRenderDependencies(*args, **kwargs):
    """
    Command to return dependencies of an image source.

    Returns: `string` Dependencies for argument image source

    """
    pass


def getRenderTasks(*args, **kwargs):
    """
    Command to return render tasks to render an image source.

    Returns: `string[]` Render tasks (one per string) for argument render target.

    """
    pass


def glRender(*args, **kwargs):
    """
    This command provides access to the Hardware Render Manager (HRM).

    Returns: None
    """
    pass


def glRenderEditor(*args, **kwargs):
    """
    Create a glRender view.

    Returns: None
    """
    pass


def globalStitch(*args, **kwargs):
    """
    This command computes a globalStitch of NURBS surfaces.

    Returns: `string[]` Object name and node name

    """
    pass


def goal(*args, **kwargs):
    """
    Specifies the given objects as being goals for the given particle object.

    Returns: `string` Command result

    """
    pass


def grabColor(*args, **kwargs):
    """
    This command changes the cursor and enters a modal state which will be exited by pressing a mouse button.

    Returns: `float` []  Three float values representing the color components of the pixel below the cursor.  If no flags are specified then the default is to return the red, green and blue color components.

    """
    pass


def gradientControl(*args, **kwargs):
    """
    
    Returns: `string` The name of the port created or modified

    """
    pass


def gradientControlNoAttr(*args, **kwargs):
    """
    This command creates a control for editing a ramp (2D control curve).

    Returns: `string` The name of the port created or modified

    """
    pass


def graphDollyCtx(*args, **kwargs):
    """
    This command can be used to create a dolly context for the graph editor.

    Returns: `string` Context name

    """
    pass


def graphSelectContext(*args, **kwargs):
    """
    This command can be used to create a selection context for the hypergraph editor.

    Returns: `string` Command result

    """
    pass


def graphTrackCtx(*args, **kwargs):
    """
    This command can be used to create a track context for the graph editor.

    Returns: `string` Context name

    """
    pass


def gravity(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def greasePencilCtx(*args, **kwargs):
    """
    This is a tool context command for the grease pencil tool.

    Returns: None
    """
    pass


def grid(*args, **kwargs):
    """
    This command changes the size and spacing of lines on the ground plane displayed in the perspective and orthographic views.

    Returns: None
    """
    pass


def gridLayout(*args, **kwargs):
    """
    This layout arranges children in a grid fashion where every cell in the grid is the same size.

    Returns: `string` Full path name to the control.

    """
    pass


def group(*args, **kwargs):
    """
    This command groups the specified objects under a new group and returns the name of the new group.

    Returns: `string` - name of the group node

    """
    pass


def hardenPointCurve(*args, **kwargs):
    """
    The hardenPointCurve command changes the knots of a curve given a list of control point indices so that the knot corresponding to that control point gets the specified multiplicity.

    Returns: `string[]` Object name and node name

    """
    pass


def hardware(*args, **kwargs):
    """
    Return description of the hardware available in the machine.

    Returns: `string` Command result

    """
    pass


def hardwareRenderPanel(*args, **kwargs):
    """
    This command creates, edit and queries hardware render panels which contain only a hardware render editor.

    Returns: `string` Panel name

    """
    pass


def hasMetadata(*args, **kwargs):
    """
    This command is used to query for the presence of metadata elements on a node, components, or scene.

    Returns: `string[]` List of indexes in the filtered list which contain metadata

    `boolean[]` List of answers to whether the specified item(s) have metadata

    """
    pass


def headsUpDisplay(*args, **kwargs):
    """
    This command creates a Heads-up Display (HUD) object which is placed in a 2D inactive overlay plane on the 3D viewport.

    Returns: `int` ID number of the Heads-Up Display (HUD), for regular command execution.

    `string|int|int[2]` HUD name, HUD ID or Section and block value, for respective remove commands.

    """
    pass


def headsUpMessage(*args, **kwargs):
    """
    This command draws a message in the 3d view.

    Returns: None
    """
    pass


def help(*args, **kwargs):
    """
    With no arguments, help tells how to use help.

    Returns: None
    """
    pass


def helpLine(*args, **kwargs):
    """
    This command creates a help line where tool help/hints are shown.

    Returns: `string` Full path name of control.

    """
    pass


def hide(*args, **kwargs):
    """
    The  command is used to make objects invisible.

    Returns: None
    """
    pass


def hikGlobals(*args, **kwargs):
    """
    Sets global HumanIK flags for the application.

    Returns: `boolean` Giving the state of the option

    """
    pass


def hilite(*args, **kwargs):
    """
    Hilites/Unhilites the specified object(s).

    Returns: None
    """
    pass


def hitTest(*args, **kwargs):
    """
    The  command hit-tests a point in the named control and returns a list of items underneath the point.

    Returns: `string[]` items underneath the hit-point

    """
    pass


def hotBox(*args, **kwargs):
    """
    This command controls parameters related to the hotBox menubar palette.

    Returns: None
    """
    pass


def hotkey(*args, **kwargs):
    """
    This command sets the single-key hotkeys for the entire application.

    Returns: None
    """
    pass


def hotkeyCheck(*args, **kwargs):
    """
    This command checks if the given hotkey is mapped to a nameCommand object.

    Returns: `string` Contains all clients name, each followed by the annotation of the corresponding nameCommand object, or an empty string.

    """
    pass


def hotkeyCtx(*args, **kwargs):
    """
    This command sets the hotkey context for the entire application.

    Returns: None
    """
    pass


def hotkeyEditorPanel(*args, **kwargs):
    """
    A hotkeyEditor creates a new hotkey editor in the current layout.

    Returns: `string` Full path name to the editor.

    """
    pass


def hotkeySet(*args, **kwargs):
    """
    Manages hotkey sets in Maya.

    Returns: `string` The name of the hotkey set.

    """
    pass


def hudButton(*args, **kwargs):
    """
    This command creates a Heads-up Display (HUD) button control which is placed in a 2D inactive overlay plane on the 3D viewport.

    Returns: `int` ID number of the Heads-Up Display (HUD).

    `string|int|int[2]` HUD name, HUD ID or Section and block value, for respective remove commands.

    """
    pass


def hudSlider(*args, **kwargs):
    """
    This command creates a Heads-up Display (HUD) slider control which is placed in a 2D inactive overlay plane on the 3D viewport.

    Returns: `int` ID number of the Heads-Up Display (HUD).

    `string|int|int[2]` HUD name, HUD ID or Section and block value, for respective remove commands.

    """
    pass


def hudSliderButton(*args, **kwargs):
    """
    This command creates a Heads-up Display (HUD) slider button control which is placed in a 2D inactive overlay plane on the 3D viewport.

    Returns: `int` ID number of the Heads-Up Display (HUD).

    `string|int|int[2]` HUD name, HUD ID or Section and block value, for respective remove commands.

    """
    pass


def hwReflectionMap(*args, **kwargs):
    """
    This command creates a hwReflectionMap node for having reflection on textured surfaces that currently have their boolean attribute displayHWEnvironment set to true.

    Returns: `string` (name of the created hwReflectionMap node)

    """
    pass


def hwRender(*args, **kwargs):
    """
    Renders an image or a sequence using the hardware rendering engine.

    Returns: `boolean` Command result

    """
    pass


def hwRenderLoad(*args, **kwargs):
    """
    Empty command used to force the dynamic load of HR render.

    Returns: None
    """
    pass


def hyperGraph(*args, **kwargs):
    """
    The following is an overview of the basic features of the hypergraph.

    Returns: `string` the name of the panel

    """
    pass


def hyperPanel(*args, **kwargs):
    """
    This command creates, edit and queries hypergraph panels which contain only a hypergraph editor.

    Returns: `string` The name of the panel

    """
    pass


def hyperShade(*args, **kwargs):
    """
    Commands for shader editing in the hypergraph.

    Returns: `string` Command result

    """
    pass


def iconTextButton(*args, **kwargs):
    """
    This control supports up to 3 icon images and 4 different display styles.

    Returns: `string` The name of the iconTextButton.

    """
    pass


def iconTextCheckBox(*args, **kwargs):
    """
    This control supports up to 3 icon images and 4 different display styles.

    Returns: `string` Full path name to the control.

    """
    pass


def iconTextRadioButton(*args, **kwargs):
    """
    This control supports up to 3 icon images and 4 different display styles.

    Returns: `string` The name of the iconTextRadioButton created.

    """
    pass


def iconTextRadioCollection(*args, **kwargs):
    """
    This command creates a cluster for iconTextRadioButtons.

    Returns: `string` The name of the iconTextRadioCollection created.

    """
    pass


def iconTextScrollList(*args, **kwargs):
    """
    This command creates/edits/queries a text scrolling list.

    Returns: `string` Full path name to the control.

    """
    pass


def iconTextStaticLabel(*args, **kwargs):
    """
    This control supports up to 3 icon images and 4 different display styles.

    Returns: `string` The name of the iconTextStaticLabel created.

    """
    pass


def ikHandle(*args, **kwargs):
    """
    The handle command is used to create, edit, and query a handle within Maya.

    Returns: `string` Command result

    """
    pass


def ikHandleCtx(*args, **kwargs):
    """
    The ikHandle context command (ikHandleCtx) updates parameters of ikHandle tool.

    Returns: `string` Context name

    """
    pass


def ikHandleDisplayScale(*args, **kwargs):
    """
    This action modifies and queries the current display size of ikHandle.

    Returns: None
    """
    pass


def ikSolver(*args, **kwargs):
    """
    The ikSolver command is used to set the attributes for an IK Solver or create a new one.

    Returns: `string` Command result

    """
    pass


def ikSplineHandleCtx(*args, **kwargs):
    """
    The ikSplineHandle context command (ikSplineHandleCtx) updates parameters of ikSplineHandle tool.

    Returns: `string` The name of the context.

    """
    pass


def ikSystem(*args, **kwargs):
    """
    The ikSystem command is used to set the global snapping flag for handles and set the global solve flag for solvers.

    Returns: `string` Command result

    """
    pass


def ikSystemInfo(*args, **kwargs):
    """
    This action modifies and queries the current ikSystem controls.

    Returns: None
    """
    pass


def ikfkDisplayMethod(*args, **kwargs):
    """
    The  command is used to specify how ik/fk       blending should be shown.

    Returns: None
    """
    pass


def illustratorCurves(*args, **kwargs):
    """
    The illustratorCurves command creates NURBS curves from an input Adobe(R) Illustrator(R) file.

    Returns: `string[]` Object name and node name

    """
    pass


def image(*args, **kwargs):
    """
    This command creates a static image for non-xpm files.

    Returns: `string` The name of the image created.

    """
    pass


def imagePlane(*args, **kwargs):
    """
    The imagePlane command allows querying of various properties of         an image plane and any movie in use by the image plane.

    Returns: `boolean` Command result

    """
    pass


def imfPlugins(*args, **kwargs):
    """
    This command queries all the available imf plugins for its name, keyword or image file extension.

    Returns: `string[]` Command result

    """
    pass


def inViewEditor(*args, **kwargs):
    """
    Mel access to the In-View Editor.

    Returns: None
    """
    pass


def inViewMessage(*args, **kwargs):
    """
    Used for displaying in-view messages.

    Returns: None
    """
    pass


def inheritTransform(*args, **kwargs):
    """
    This command toggles the inherit state of an object.

    Returns: None
    """
    pass


def insertJoint(*args, **kwargs):
    """
    This command will insert a new joint under the given or selected joint.

    Returns: `string` The name of the new inserted joint

    """
    pass


def insertJointCtx(*args, **kwargs):
    """
    The command will create an insert joint context.

    Returns: `string` The name of the context.

    """
    pass


def insertKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to insert keys within the graph editor.

    Returns: `string` Context name

    """
    pass


def insertKnotCurve(*args, **kwargs):
    """
    The insertKnotCurve command inserts knots into a curve given a list of parameter values.

    Returns: `string[]` Object name and node name

    """
    pass


def insertKnotSurface(*args, **kwargs):
    """
    The insertKnotSurface command inserts knots (aka isoparms) into a surface given a list of parameter values.

    Returns: `string[]` Object name and node name

    """
    pass


def instance(*args, **kwargs):
    """
    Instancing is a way of making the same object appear twice in the scene.

    Returns: `string` - the name of the new transform node is returned.

    """
    pass


def instanceable(*args, **kwargs):
    """
    Flags one or more DAG nodes so that they can (or cannot) be instanced.

    Returns: `boolean[]` For query execution.

    """
    pass


def instancer(*args, **kwargs):
    """
    This command is used to create a instancer node and set the proper attributes in the node.

    Returns: `string` Command result

    """
    pass


def intField(*args, **kwargs):
    """
    Create a field control that accepts only integer values and is bound by a minimum and maximum value.

    Returns: `string` Full path name to the control.

    """
    pass


def intFieldGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def intScrollBar(*args, **kwargs):
    """
    Create a scroll bar control that accepts only integer values and is bound by a minimum and maximum value.

    Returns: `string` Full path name to the control.

    """
    pass


def intSlider(*args, **kwargs):
    """
    Create a slider control that accepts only integer values and is bound by a minimum and maximum value.

    Returns: `string` Full path name to the control.

    """
    pass


def intSliderGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name of the control on creation.

    """
    pass


def internalVar(*args, **kwargs):
    """
    This command returns the values of internal variables.

    Returns: `string` The value of the variable specified by the flag use.

    """
    pass


def intersect(*args, **kwargs):
    """
    The intersect command creates a curve on surface where all surfaces intersect with each other.

    Returns: `string[]` Object name and node name

    """
    pass


def iprEngine(*args, **kwargs):
    """
    Command to create or edit an iprEngine.

    Returns: `string` - the name of the ipr engine created or modified

    """
    pass


def isConnected(*args, **kwargs):
    """
    The  command is used to check if two plugs are connected in the dependency graph.

    Returns: `boolean` Are the two plugs connected?

    """
    pass


def isDirty(*args, **kwargs):
    """
    The  command is used to check if a plug is dirty.

    Returns: `boolean` Is the plug dirty? If more than one plug is given then it returns the logical "and" of all dirty states.

    """
    pass


def isTrue(*args, **kwargs):
    """
    This commmand returns the state of the named condition.

    Returns: None
    """
    pass


def isolateSelect(*args, **kwargs):
    """
    This command turns on/off isolate select mode in a specified modeling view, specified as the argument.

    Returns: `boolean` When used with query

    """
    pass


def itemFilter(*args, **kwargs):
    """
    This command creates a named itemFilter object.

    Returns: `string` Single command result

    `string[]` Multiple command result

    """
    pass


def itemFilterAttr(*args, **kwargs):
    """
    This command creates a named itemFilterAttr object.

    Returns: `string` Single command result

    `string[]` Multiple command result

    """
    pass


def itemFilterType(*args, **kwargs):
    """
    This command queries a named itemFilter object.

    Returns: `string` Single command result

    `string[]` Multiple command result

    """
    pass


def joint(*args, **kwargs):
    """
    The joint command is used to create, edit, and query, joints within Maya.

    Returns: `string` Command result

    """
    pass


def jointCluster(*args, **kwargs):
    """
    
    Returns: `string` Name of the new jointCluster node

    """
    pass


def jointCtx(*args, **kwargs):
    """
    The joint context command (jointCtx) updates the parameters of the joint tool.

    Returns: `string` The name of the context.

    """
    pass


def jointDisplayScale(*args, **kwargs):
    """
    This action modifies and queries the current display size of skelton joints.

    Returns: None
    """
    pass


def jointLattice(*args, **kwargs):
    """
    This command creates/edits/queries a jointLattice deformer.

    Returns: `string` Name of joint lattice algorithm node created/edited.

    """
    pass


def keyTangent(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` Number of curves on which tangents were modified.

    """
    pass


def keyframe(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` (except where noted below) Number of curves on which keys were modified. In -query mode, the command can return a variety of things, as described with each queryable flag below.

    """
    pass


def keyframeOutliner(*args, **kwargs):
    """
    This command creates/edits/queries a keyframe outliner control.

    Returns: `string` The name of the outliner control.

    """
    pass


def keyframeRegionCurrentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the keyframe region of the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionDirectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to directly manipulate keyframes within the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionDollyCtx(*args, **kwargs):
    """
    This command can be used to create a dolly context for the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionInsertKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to insert keys within the keyframe region of the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionMoveKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to move keyframes within the keyframe region of the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionScaleKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the keyframe region of the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionSelectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionSetKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to set keys within the keyframe region of the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeRegionTrackCtx(*args, **kwargs):
    """
    This command can be used to create a track context for the dope sheet editor.

    Returns: `string` Context name

    """
    pass


def keyframeStats(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` The name of the stats control.

    """
    pass


def keyingGroup(*args, **kwargs):
    """
    This command is used to manage the membership of a keying group.

    Returns: `string` For creation operations (name of the keying group that was created or edited)

    `string[]` For query operation (names of items in the keying group)

    `boolean` For isMember operation

    """
    pass


def lassoContext(*args, **kwargs):
    """
    Creates a context to perform selection via a "lasso".

    Returns: `string` Name of the context created

    """
    pass


def lattice(*args, **kwargs):
    """
    This command creates a lattice deformer that will deform the selected objects.

    Returns: `string[]` Ffd node name, lattice name, base lattice name.

    """
    pass


def latticeDeformKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to deform key frames with lattice manipulator.

    Returns: `string` Context name

    """
    pass


def launch(*args, **kwargs):
    """
    Launch the appropriate application to open the document, web page or directory specified.

    Returns: None
    """
    pass


def launchImageEditor(*args, **kwargs):
    """
    Launch the appropriate application to edit/view the image files specified.

    Returns: None
    """
    pass


def layerButton(*args, **kwargs):
    """
    Creates a layer bar button widget.

    Returns: `string` Full path name to the control.

    """
    pass


def layeredShaderPort(*args, **kwargs):
    """
    This command creates a 3dPort that displays an image representing the layered shader node specified.

    Returns: `string` Full path name to the control.

    """
    pass


def layeredTexturePort(*args, **kwargs):
    """
    This command creates a 3dPort that displays an image representing the layered texture node specified.

    Returns: `string` Full path name to the control.

    """
    pass


def layout(*args, **kwargs):
    """
    This command allows you to edit or query the properties of any layout.

    Returns: None
    """
    pass


def layoutDialog(*args, **kwargs):
    """
    The layoutDialog command creates a modal dialog containing a formLayout with 100 divisions.

    Returns: `string` The string specified by the -dismiss flag, or "dismiss" if the dialog was closed.

    """
    pass


def license(*args, **kwargs):
    """
    This command displays version information about the application if it is executed without flags.

    Returns: `string` The application's license information.

    """
    pass


def lightList(*args, **kwargs):
    """
    Add/Remove a relationship between an object and the current light.

    Returns: None
    """
    pass


def lightlink(*args, **kwargs):
    """
    This command is used to make, break and query light linking relationships between lights/sets of lights and objects/sets of objects.

    Returns: `string` Single element command result

    `string[]` Multi element command result

    """
    pass


def linearPrecision(*args, **kwargs):
    """
    This command controls the display of linear strings in the interface.

    Returns: None
    """
    pass


def listAnimatable(*args, **kwargs):
    """
    This command list the animatable attributes of a node.

    Returns: `string[]` All animatable attributes found

    """
    pass


def listAttr(*args, **kwargs):
    """
    This command lists the attributes of a node.

    Returns: `string[]` : List of attributes matching criteria

    """
    pass


def listAttrPatterns(*args, **kwargs):
    """
    Attribute patterns are plain text descriptions of an entire Maya attribute forest.

    Returns: `string[]` List of patterns or pattern instances available

    """
    pass


def listCameras(*args, **kwargs):
    """
    Command to list all cameras.

    Returns: `string[]` Command result

    """
    pass


def listConnections(*args, **kwargs):
    """
    This command returns a list of all attributes/objects of a specified type that are connected to the given object(s).

    Returns: `string[]` List of connection plugs/nodes

    """
    pass


def listDeviceAttachments(*args, **kwargs):
    """
    This command lists the current set of device attachments.

    Returns: `string` Command result

    """
    pass


def listHistory(*args, **kwargs):
    """
    This command traverses backwards or forwards in the graph from the specified node and returns all of the nodes whose construction history it passes through.

    Returns: `string[]` List of history nodes

    """
    pass


def listInputDeviceAxes(*args, **kwargs):
    """
    This command lists all of the axes of the specified input device.

    Returns: `string[]` Command result

    """
    pass


def listInputDeviceButtons(*args, **kwargs):
    """
    This command lists all of the buttons of the specified input device specified as an argument.

    Returns: `string[]` Command result

    """
    pass


def listInputDevices(*args, **kwargs):
    """
    This command lists all input devices that maya knows about.

    Returns: `string[]` Command result

    """
    pass


def listNodeTypes(*args, **kwargs):
    """
    Lists dependency node types satisfying a specified classification string.

    Returns: `string[]` The type names of all node types in the system that satisfy the given classification string.

    """
    pass


def listNodesWithIncorrectNames(*args, **kwargs):
    """
    List all nodes with incorrect names in the Script Editor.

    Returns: None
    """
    pass


def listRelatives(*args, **kwargs):
    """
    This command lists parents and children of DAG objects.

    Returns: `string[]` Command result

    """
    pass


def listSets(*args, **kwargs):
    """
    The listSets command is used to get a list of all the sets an object belongs to.

    Returns: `string[]` (string array of all sets the object belongs to)

    """
    pass


def loadFluid(*args, **kwargs):
    """
    A command to set builtin fluid attributes such as Density, Velocity, etc for all cells in the grid from the initial state cache.

    Returns: None
    """
    pass


def loadModule(*args, **kwargs):
    """
    Maya plug-ins may be installed individually within one of Maya's standard plug-in directories, or they may be packaged up with other resources in a "module".

    Returns: `string[]` Command result

    """
    pass


def loadPlugin(*args, **kwargs):
    """
    Load plug-ins into Maya.

    Returns: `string[]` the internal names of the successfully loaded plug-ins

    """
    pass


def loadPrefObjects(*args, **kwargs):
    """
    This command loads preference dependency nodes from "userPrefObjects.

    Returns: `boolean` True if successful.

    """
    pass


def loadUI(*args, **kwargs):
    """
    loadUI command allows loading of a user interface created in Trolltech .

    Returns: `string` Full path name to the root control.

    """
    pass


def lockNode(*args, **kwargs):
    """
    Locks or unlocks one or more dependency nodes.

    Returns: `boolean[]` For query execution.

    """
    pass


def loft(*args, **kwargs):
    """
    This command computes a skinned (lofted) surface passing through a number of NURBS curves.

    Returns: `string[]` Object name and node name

    """
    pass


def lookThru(*args, **kwargs):
    """
    This command sets a particular camera to look through in a view.

    Returns: None
    """
    pass


def ls(*args, **kwargs):
    """
    The  command returns the names (and optionally the type names) of objects in the scene.

    Returns: `string[]` Command result

    """
    pass


def lsThroughFilter(*args, **kwargs):
    """
    List all objects in the world that pass a given filter.

    Returns: `string[]` List of nodes passing the filter

    """
    pass


def lsUI(*args, **kwargs):
    """
    This command returns the names of UI objects.

    Returns: `string[]` The names of the object arguments.

    """
    pass


def makeIdentity(*args, **kwargs):
    """
    
    Returns: None
    """
    pass


def makeLive(*args, **kwargs):
    """
    This commmand makes an object live.

    Returns: None
    """
    pass


def makePaintable(*args, **kwargs):
    """
    Make attributes of nodes paintable to Attribute Paint Tool.

    Returns: None
    """
    pass


def makeSingleSurface(*args, **kwargs):
    """
    This command performs a stitch and tessellate operation.

    Returns: `string[]` Object name and node name.

    """
    pass


def makebot(*args, **kwargs):
    """
    The makebot command takes an image file and produces a block ordered texture (BOT) file, to be used for texture caching.

    Returns: None
    """
    pass


def manipMoveContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a move manip context.

    Returns: `string` The name of the new context

    """
    pass


def manipMoveLimitsCtx(*args, **kwargs):
    """
    Create a context for the translate limits manipulator.

    Returns: `string` Name of newly created context

    """
    pass


def manipOptions(*args, **kwargs):
    """
    Changes the global manipulator parameters.

    Returns: None
    """
    pass


def manipPivot(*args, **kwargs):
    """
    Changes transform component pivot used by the move/rotate/scale manipulators.

    Returns: None
    """
    pass


def manipRotateContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a rotate manip context.

    Returns: `string` (name of the new context)

    """
    pass


def manipRotateLimitsCtx(*args, **kwargs):
    """
    Create a context for the rotate limits manipulator.

    Returns: `string` Name of newly created context

    """
    pass


def manipScaleContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a scale manip context.

    Returns: `string` (name of the new context)

    """
    pass


def manipScaleLimitsCtx(*args, **kwargs):
    """
    Create a context for the scale limits manipulator.

    Returns: `string` Name of newly created context.

    """
    pass


def marker(*args, **kwargs):
    """
    The marker command creates one or two markers, on a motion path curve, at the specified time and location.

    Returns: `string[]` (name of the created markers)

    """
    pass


def matchTransform(*args, **kwargs):
    """
    This command modifies the source object's transform to match the target object's transform.

    Returns: None
    """
    pass


def mayaDpiSetting(*args, **kwargs):
    """
    Provide Maya interface scaling based on system DPI or custom scale setting or no scaling.

    Returns: `int` Scale mode or system DPI value, as queried

    `float` Defined scale or real scale, as queried

    """
    pass


def mayaHasRenderSetup(*args, **kwargs):
    """
    This command controls and queries render setup states.

    Returns: None
    """
    pass


def melInfo(*args, **kwargs):
    """
    This command returns the names of all global MEL procedures that are currently defined as a string array.

    Returns: `string[]` procedure names

    """
    pass


def melOptions(*args, **kwargs):
    """
    Set and query options that affect the behavior of Maya's Embedded Language (MEL).

    Returns: None
    """
    pass


def memory(*args, **kwargs):
    """
    Used to query essential statistics on memory availability and usage.

    Returns: None
    """
    pass


def menu(*args, **kwargs):
    """
    This command creates a new menu and adds it to the default window's menubar if no parent is specified.

    Returns: `string` Full path name to the menu.

    """
    pass


def menuBarLayout(*args, **kwargs):
    """
    Create a layout containing a menu bar.

    Returns: `string` Full path name to the control.

    """
    pass


def menuEditor(*args, **kwargs):
    """
    A menuEditor displays the contents of a popup menu and allows the menu's items to be edited.

    Returns: `string` Full path name to the editor.

    """
    pass


def menuItem(*args, **kwargs):
    """
    This command creates/edits/queries menu items.

    Returns: `string` Full path name to the menu item.

    """
    pass


def menuSet(*args, **kwargs):
    """
    Create a menu set which is used to logically order menus for display in the main menu bar.

    Returns: `string` Name of resulting menu set.  (If there are no menu sets left, an empty string is returned)

    """
    pass


def menuSetPref(*args, **kwargs):
    """
    Provides the functionality to save and load menuSets between sessions of Maya.

    Returns: None
    """
    pass


def messageLine(*args, **kwargs):
    """
    This command creates a message line where tool feedback is shown.

    Returns: `string` : Full path name to the control.

    """
    pass


def minimizeApp(*args, **kwargs):
    """
    This command minimizes (iconifies) all of the application's windows into a single desktop icon.

    Returns: None
    """
    pass


def mirrorJoint(*args, **kwargs):
    """
    This command will duplicate a branch of the skeleton from the selected joint symmetrically about a plane in world space.

    Returns: `string[]` Names of the mirrored joints

    """
    pass


def modelCurrentTimeCtx(*args, **kwargs):
    """
    This command creates a context which may be used to change current time within the model views.

    Returns: `string` Context name

    """
    pass


def modelEditor(*args, **kwargs):
    """
    Create, edit or query a model editor.

    Returns: `string` the name of the editor.

    """
    pass


def modelPanel(*args, **kwargs):
    """
    This command creates a panel consisting of a model editor.

    Returns: `string` The name of the panel.

    """
    pass


def moduleInfo(*args, **kwargs):
    """
    Returns information on modules found by Maya.

    Returns: `string[]` Command result

    """
    pass


def mouse(*args, **kwargs):
    """
    This command allows to configure mouse.

    Returns: `int` When -scrollWheelStatus flag is used, will return 1 if scroll wheel support enabled, otherwise 0. When -mouseButtonTrackingStatus flag is used, will return the number of mouse buttons being tracked.

    """
    pass


def movIn(*args, **kwargs):
    """
    Imports a .

    Returns: None
    """
    pass


def movOut(*args, **kwargs):
    """
    Exports a .

    Returns: None
    """
    pass


def move(*args, **kwargs):
    """
    The move command is used to change the positions of geometric objects.

    Returns: None
    """
    pass


def moveKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to move keyframes within the graph editor.

    Returns: `string` Context name

    """
    pass


def moveVertexAlongDirection(*args, **kwargs):
    """
    The command moves the selected vertex ( control vertex ) in the specified unit direction by the given magnitude.

    Returns: None
    """
    pass


def movieInfo(*args, **kwargs):
    """
    movieInfo provides a mechanism for querying information about movie files.

    Returns: None
    """
    pass


def multiProfileBirailSurface(*args, **kwargs):
    """
    The cmd creates a railed surface by sweeping the profiles using two rail curves.

    Returns: `string[]` Object name and node name

    """
    pass


def multiTouch(*args, **kwargs):
    """
    Used to interact with the Gestura (multi-touch) library.

    Returns: None
    """
    pass


def mute(*args, **kwargs):
    """
    The mute command is used to disable and enable playback on a channel.

    Returns: `string[]` Name(s) of the mute node(s)

    """
    pass


def nBase(*args, **kwargs):
    """
    Edits one or more nBase objects.

    Returns: `boolean` Command result

    """
    pass


def nParticle(*args, **kwargs):
    """
    The nParticle command creates a new nParticle object from a list of world space points.

    Returns: `string` The name of the nParticle object created

    """
    pass


def nSoft(*args, **kwargs):
    """
    Makes a nSoft body from the object(s) passed on the command line or in the selection list.

    Returns: `string` array

    """
    pass


def nameCommand(*args, **kwargs):
    """
    This command creates a nameCommand object.

    Returns: `string` The name of the nameCommand object created

    """
    pass


def nameField(*args, **kwargs):
    """
    This command creates an editable field that can be linked to the name of a Maya object.

    Returns: `string` Full path name to the control.

    """
    pass


def namespace(*args, **kwargs):
    """
    This command allows a namespace to be created, set or removed.

    Returns: `string` Command result

    """
    pass


def namespaceInfo(*args, **kwargs):
    """
    This command displays information about a namespace.

    Returns: `string` Command result

    """
    pass


def newton(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def nodeCast(*args, **kwargs):
    """
    Given two nodes, a source node of type A and a target node of type B, where type A is either type B or a sub-type of B, this command will replace the target node with the source node.

    Returns: `int` 0 for success, 1 for failure.

    """
    pass


def nodeEditor(*args, **kwargs):
    """
    This command creates/edits/queries a nodeEditor editor.

    Returns: `string` The name of the created control.

    """
    pass


def nodeIconButton(*args, **kwargs):
    """
    This control supports up to 3 icon images and 4 different display styles.

    Returns: `string` The name of the button

    """
    pass


def nodeOutliner(*args, **kwargs):
    """
    The nodeOutliner command creates, edits and queries an outline control that shows dependency nodes and their attributes.

    Returns: None
    """
    pass


def nodePreset(*args, **kwargs):
    """
    Command to save and load preset settings for a node.

    Returns: `boolean` if isValidName or exists is used.

    """
    pass


def nodeTreeLister(*args, **kwargs):
    """
    This command creates/edits/queries the node tree lister control.

    Returns: `string` The name of the created control.

    """
    pass


def nodeType(*args, **kwargs):
    """
    This command returns a string which identifies the given node's type.

    Returns: `string` Single command result

    `string[]` Multiple command result

    """
    pass


def nonLinear(*args, **kwargs):
    """
    This command creates a functional deformer of the specified type that will deform the selected objects.

    Returns: `string[]` Deformer driver name, deformer handle transform name.

    """
    pass


def normalConstraint(*args, **kwargs):
    """
    Constrain an object's orientation based on the normal of the target surface(s) at the closest point(s) to the object.

    Returns: `string[]` Name of the created constraint node

    """
    pass


def nurbsBoolean(*args, **kwargs):
    """
    This command performs a boolean operation.

    Returns: `string[]` Object name and node name

    """
    pass


def nurbsCopyUVSet(*args, **kwargs):
    """
    This is only a sample command for debugging purposes, which makes a copy of the implicit st parameterization on a nurbs surface to be the 1st explicit uvset.

    Returns: `boolean` Success or Failure.

    """
    pass


def nurbsCube(*args, **kwargs):
    """
    The nurbsCube command creates a new NURBS Cube made up of six planes.

    Returns: `string[]` Object name and node name

    """
    pass


def nurbsCurveToBezier(*args, **kwargs):
    """
    The nurbsCurveToBezier command attempts to convert an existing NURBS curve to a Bezier curve.

    Returns: `string[]` (object name and node name)

    """
    pass


def nurbsEditUV(*args, **kwargs):
    """
    Command Edits UVs on NURBS objects.

    Returns: `boolean` Success or Failure.

    """
    pass


def nurbsPlane(*args, **kwargs):
    """
    The nurbsPlane command creates a new NURBS Plane and return the name of the new surface.

    Returns: `string[]` Object name and node name

    """
    pass


def nurbsSelect(*args, **kwargs):
    """
    Performs selection operations on NURBS objects.

    Returns: None
    """
    pass


def nurbsSquare(*args, **kwargs):
    """
    The nurbsSquare command creates a square.

    Returns: `string[]` Object name and node name

    """
    pass


def nurbsToPoly(*args, **kwargs):
    """
    This command tesselates a NURBS surface and produces a polygonal surface.

    Returns: `string[]` The polygon and optionally the dependency node name.

    """
    pass


def nurbsToPolygonsPref(*args, **kwargs):
    """
    This command sets the values used by the nurbs-to-polygons (or "tesselate") preference.

    Returns: None
    """
    pass


def nurbsToSubdiv(*args, **kwargs):
    """
    This command converts a NURBS surface and produces a subd surface.

    Returns: `string[]` The subd surface and optionally the dependency node name

    """
    pass


def nurbsToSubdivPref(*args, **kwargs):
    """
    This command sets the values used by the nurbs-to-subdivision surface preference.

    Returns: None
    """
    pass


def nurbsUVSet(*args, **kwargs):
    """
    Allows user to toggle between implicit and explicit UVs on a NURBS object.

    Returns: `boolean` Success or Failure.

    """
    pass


def objExists(*args, **kwargs):
    """
    This command simply returns true or false depending on whether an object with the given name exists.

    Returns: `boolean` Command result

    """
    pass


def objectCenter(*args, **kwargs):
    """
    This command returns the coordinates of the center of the bounding box of the specified object.

    Returns: `float[]` When the asking for the center (default).

    `float` When asking for one coordinate only.

    """
    pass


def objectType(*args, **kwargs):
    """
    This command returns the type of elements.

    Returns: `string` The type of the specified object

    `boolean` For "isType": was the object of the specified type?

    """
    pass


def objectTypeUI(*args, **kwargs):
    """
    This command returns the type of UI element such as button, sliders, etc.

    Returns: `string` The type of the specified object.

    """
    pass


def offsetCurve(*args, **kwargs):
    """
    The offset command creates new offset curves from the selected curves.

    Returns: `string[]` Object name and node name

    """
    pass


def offsetCurveOnSurface(*args, **kwargs):
    """
    The offsetCurveOnSurface command offsets a curve on surface resulting in another curve on surface.

    Returns: `string[]` Object name and node name

    """
    pass


def offsetSurface(*args, **kwargs):
    """
    The offset command creates new offset surfaces from the selected surfaces.

    Returns: `string[]` Object name and node name

    """
    pass


def ogs(*args, **kwargs):
    """
    OGS is one of the viewport renderers.

    Returns: `string` Result of the operation

    """
    pass


def ogsRender(*args, **kwargs):
    """
    Renders an image or a sequence using the OGS rendering engine.

    Returns: `boolean` Query result

    """
    pass


def openGLExtension(*args, **kwargs):
    """
    Command returns the extension name depending on whether a given OpenGL extension is supported or not.

    Returns: `string` The supported string(s)

    """
    pass


def openMayaPref(*args, **kwargs):
    """
    Set or query API preferences.

    Returns: `int` indicates success or failure

    """
    pass


def optionMenu(*args, **kwargs):
    """
    This command creates a popup menu control.

    Returns: `string` Full path name to the control.

    """
    pass


def optionMenuGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` The full name of the control on creation.

    """
    pass


def optionVar(*args, **kwargs):
    """
    This command allows you to set and query variables which are persistent between different invocations of Maya.

    Returns: `int` `0 or 1 for the exists option`
    `string[]` `When the list option is used`
    """
    pass


def orbit(*args, **kwargs):
    """
    The orbit command revolves the camera(s) horizontally and/or vertically in the perspective window.

    Returns: None
    """
    pass


def orbitCtx(*args, **kwargs):
    """
    Create, edit, or query an orbit context.

    Returns: `string` The name of the context

    """
    pass


def orientConstraint(*args, **kwargs):
    """
    Constrain an object's orientation to match the orientation of the target or the average of a number of targets.

    Returns: `string` [] ( name of the created constraint node)

    """
    pass


def outlinerEditor(*args, **kwargs):
    """
    This command creates an outliner editor which can be used to display a list of objects.

    Returns: `string` (the name of the editor)

    """
    pass


def outlinerPanel(*args, **kwargs):
    """
    This command creates, edit and queries outliner panels which contain only an outliner editor.

    Returns: `string` (the name of the panel)

    """
    pass


def overrideModifier(*args, **kwargs):
    """
    This command allows you to assign modifier key behaviour to other parts of the system.

    Returns: None
    """
    pass


def paintEffectsDisplay(*args, **kwargs):
    """
    Command to set the global display methods for paint effects items.

    Returns: None
    """
    pass


def pairBlend(*args, **kwargs):
    """
    The pairBlend node allows a weighted combinations of 2 inputs to be blended together.

    Returns: `string` name of pairBlend node

    """
    pass


def palettePort(*args, **kwargs):
    """
    This command creates an array of color cells.

    Returns: `string` The name of the palettePort created

    """
    pass


def panZoom(*args, **kwargs):
    """
    The panZoom command pans/zooms the 2D film.

    Returns: None
    """
    pass


def panZoomCtx(*args, **kwargs):
    """
    This command can be used to create camera 2D pan/zoom context.

    Returns: `string` The name of the context

    """
    pass


def paneLayout(*args, **kwargs):
    """
    This command creates a pane layout.

    Returns: `string` Full path name to the control.

    """
    pass


def panel(*args, **kwargs):
    """
    This command allows editing or querying properties of any panels.

    Returns: None
    """
    pass


def panelConfiguration(*args, **kwargs):
    """
    This command creates a panel configuration object.

    Returns: `string` The name of the panelConfiguration created.

    """
    pass


def panelHistory(*args, **kwargs):
    """
    This command creates a panel history object.

    Returns: `string` The name of the panelHistory object created.

    """
    pass


def paramDimContext(*args, **kwargs):
    """
    Command used to register the paramDimCtx tool.

    Returns: `string` - name of the context created

    """
    pass


def paramDimension(*args, **kwargs):
    """
    This command is used to create a param dimension to display the parameter value of a curve/surface at a specified point on the curve/surface.

    Returns: `string` Name of the paramDimension shape node created

    """
    pass


def paramLocator(*args, **kwargs):
    """
    The command creates a locator in the underworld of a NURBS curve or NURBS surface at the specified parameter value.

    Returns: `string` Name for the new locator in the underworld of NURBS shape.

    """
    pass


def parent(*args, **kwargs):
    """
    This command parents (moves) objects under a new group, removes objects from an existing group, or adds/removes parents.

    Returns: `string[]` Names of the objects parented (possibly renamed)

    """
    pass


def parentConstraint(*args, **kwargs):
    """
    Constrain an object's position and rotation so that it behaves as if it were a child of the target object(s).

    Returns: `string[]` Name of the created constraint node

    """
    pass


def particle(*args, **kwargs):
    """
    The particle command creates a new particle object from a list of world space points.

    Returns: `string` The name of the particle object created

    """
    pass


def particleExists(*args, **kwargs):
    """
    This command is used to query if a particle or soft object with the given name exists.

    Returns: `boolean` True if there is a particle object or soft object by the given name, false otherwise.

    """
    pass


def particleFill(*args, **kwargs):
    """
    This command generates an nParticle system that fills the selected object with a grid of particles.

    Returns: None
    """
    pass


def particleInstancer(*args, **kwargs):
    """
    This command is used to create a particle instancer node and set the proper attributes in the particle shape and in the instancer node.

    Returns: `string` Command result

    """
    pass


def particleRenderInfo(*args, **kwargs):
    """
    This action provides information access to the particle render subclasses.

    Returns: None
    """
    pass


def partition(*args, **kwargs):
    """
    This command is used to create, query or add/remove sets to a partition.

    Returns: `string` Name of the partition that was created or edited

    """
    pass


def pasteKey(*args, **kwargs):
    """
    The pasteKey command pastes curve segment hierarchies from the clipboard onto other objects or curves.

    Returns: `int` The number of curves pasted

    """
    pass


def pathAnimation(*args, **kwargs):
    """
    The pathAnimation command constructs the necessary graph nodes and their interconnections for a motion path animation.

    Returns: `string` (name of the created motionPath node)

    """
    pass


def pause(*args, **kwargs):
    """
    Pause for a specified number of seconds for canned demos or for test scripts to allow user to view results.

    Returns: None
    """
    pass


def perCameraVisibility(*args, **kwargs):
    """
    The perCameraVisibility command creates, queries and removes visibility relationships between DAG objects and cameras.

    Returns: `string[]` Command result

    """
    pass


def percent(*args, **kwargs):
    """
    This command sets percent values on members of a weighted node such as a cluster or a jointCluster.

    Returns: None
    """
    pass


def performanceOptions(*args, **kwargs):
    """
    Sets the global performance options for the application.

    Returns: `string` One of "on", "off", or "interactive" giving the state of the option

    `float` Global resolution value

    """
    pass


def pfxstrokes(*args, **kwargs):
    """
    This command will loop through all the Paint Effects strokes, including pfxHair nodes, and write the current state of all the tubes to a file.

    Returns: None
    """
    pass


def pickWalk(*args, **kwargs):
    """
    The pickWalk command allows you to quickly change the selection list relative to the nodes that are currently selected.

    Returns: `string[]` A list of the newly selected items

    """
    pass


def picture(*args, **kwargs):
    """
    This command creates a static image.

    Returns: `string` The name of the picture control created.

    """
    pass


def pixelMove(*args, **kwargs):
    """
    The pixelMove command moves objects by what appears as pixel units based on the current view.

    Returns: None
    """
    pass


def planarSrf(*args, **kwargs):
    """
    This command computes a planar trimmed surface given planar boundary curves that form a closed region.

    Returns: `string[]` Object name and node name

    """
    pass


def plane(*args, **kwargs):
    """
    The command creates a sketch plane (also known as a "construction plane") in space.

    Returns: `string` (name of the new plane)

    """
    pass


def play(*args, **kwargs):
    """
    This command starts and stops playback.

    Returns: None
    """
    pass


def playbackOptions(*args, **kwargs):
    """
    This command sets/queries certain values associated with playback: looping style, start/end times, etc.

    Returns: `string` or float Query of edited option.

    """
    pass


def playblast(*args, **kwargs):
    """
    This command playblasts the current playback range.

    Returns: `string` Name of moviefile created.

    """
    pass


def pluginDisplayFilter(*args, **kwargs):
    """
    Register, deregister or query a plugin display filter.

    Returns: `string` string[]

    """
    pass


def pluginInfo(*args, **kwargs):
    """
    This command provides access to the plug-in registry of the application.

    Returns: `Any` Dependent upon the action requested.

    """
    pass


def pointConstraint(*args, **kwargs):
    """
    Constrain an object's position to the position of the target object or to the average position of a number of targets.

    Returns: `string[]` Name of the created constraint node

    """
    pass


def pointCurveConstraint(*args, **kwargs):
    """
    The command enables direct manipulation of a NURBS curve.

    Returns: `string[]` Object Name(s), node name.

    """
    pass


def pointLight(*args, **kwargs):
    """
    The pointLight command is used to edit the parameters of existing pointLights, or to create new ones.

    Returns: `string` Light shape name

    """
    pass


def pointOnCurve(*args, **kwargs):
    """
    This command returns information for a point on a NURBS curve.

    Returns: `float[3]` Vector query result

    `float` Single float query result

    `string` String query result

    """
    pass


def pointOnPolyConstraint(*args, **kwargs):
    """
    Constrain an object's position to the position of the target object or to the average position of a number of targets.

    Returns: `string[]` Name of the created constraint node

    """
    pass


def pointOnSurface(*args, **kwargs):
    """
    This command returns information for a point on a surface.

    Returns: `float[3]` Vector query result

    `string` String query result

    """
    pass


def pointPosition(*args, **kwargs):
    """
    This command returns the world or local space position for any type of point object.

    Returns: `float[]` Command result

    """
    pass


def poleVectorConstraint(*args, **kwargs):
    """
    Constrains the poleVector of an ikRPsolve handle to point at a target object or at the average position of a number of targets.

    Returns: `string[]` name of the created constraint node

    """
    pass


def polyAppend(*args, **kwargs):
    """
    Appends a new face to the selected polygonal object.

    Returns: `string` The node name.

    """
    pass


def polyAppendFacetCtx(*args, **kwargs):
    """
    Create a new context to append facets on polygonal objects.

    Returns: None
    """
    pass


def polyAppendVertex(*args, **kwargs):
    """
    Appends a new face to the selected polygonal object.

    Returns: `string` The node name.

    """
    pass


def polyAutoProjection(*args, **kwargs):
    """
    Projects a map onto an object, using several orthogonal projections simultaneously.

    Returns: `string` The node name.

    """
    pass


def polyAverageNormal(*args, **kwargs):
    """
    Set normals of vertices or vertex-faces to an average value when the vertices within a given threshold.

    Returns: `string` of the node name.

    """
    pass


def polyAverageVertex(*args, **kwargs):
    """
    Moves the selected vertices of a polygonal object to round its shape.

    Returns: `string` The node name.

    """
    pass


def polyBevel(*args, **kwargs):
    """
    Bevel edges.

    Returns: `string` The node name.

    """
    pass


def polyBevel3(*args, **kwargs):
    """
    Bevel edges.

    Returns: `string` The node name.

    """
    pass


def polyBlendColor(*args, **kwargs):
    """
    Takes two color sets and blends them together into a third specified color set.

    Returns: `string` The node name.

    """
    pass


def polyBlindData(*args, **kwargs):
    """
    Command creates blindData types (basically creates an instance of TdnPolyBlindData).

    Returns: `string` Name of nodes created

    """
    pass


def polyBoolOp(*args, **kwargs):
    """
    This command creates a new poly as the result of a boolean operation on input polys : union, intersection, difference.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyBridgeEdge(*args, **kwargs):
    """
    Bridges two sets of edges.

    Returns: `string` The node name.

    """
    pass


def polyCBoolOp(*args, **kwargs):
    """
    This command creates a new poly as the result of a boolean operation on input polys : union, intersection, difference.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyCacheMonitor(*args, **kwargs):
    """
    When the cacheInput attribute has a positive value the midModifier node caches the output mesh improving performance in computations of downstream nodes.

    Returns: None
    """
    pass


def polyCanBridgeEdge(*args, **kwargs):
    """
    Returns true if the specified poly edges can be bridged using polyBridgeEdge.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyCheck(*args, **kwargs):
    """
    Dumps a description of internal memory representation of poly objects.

    Returns: `int` The number of errors.

    """
    pass


def polyChipOff(*args, **kwargs):
    """
    Extract facets.

    Returns: `string` The node name.

    """
    pass


def polyCircularize(*args, **kwargs):
    """
    Mirror all the faces of the selected object.

    Returns: `string` The node name.

    """
    pass


def polyCircularizeEdge(*args, **kwargs):
    """
    Mirror all the faces of the selected object.

    Returns: `string` The node name.

    """
    pass


def polyCircularizeFace(*args, **kwargs):
    """
    Mirror all the faces of the selected object.

    Returns: `string` The node name.

    """
    pass


def polyClean(*args, **kwargs):
    """
    polyClean will attempt to remove components that are invalid in the description of a poly mesh.

    Returns: `string` The node name.

    """
    pass


def polyClipboard(*args, **kwargs):
    """
    The command allows the user to copy and paste certain polygonal attributes to a clipboard.

    Returns: `boolean` Success or Failure

    """
    pass


def polyCloseBorder(*args, **kwargs):
    """
    Closes open borders of objects.

    Returns: `string` The node name.

    """
    pass


def polyCollapseEdge(*args, **kwargs):
    """
    Turns each selected edge into a point.

    Returns: `string` The node name.

    """
    pass


def polyCollapseFacet(*args, **kwargs):
    """
    Turns each selected facet into a point.

    Returns: `string` The node name.

    """
    pass


def polyCollapseTweaks(*args, **kwargs):
    """
    A command that updates a mesh's vertex tweaks by applying its tweak data (stored on the mesh node) onto its respective vertex data.

    Returns: None
    """
    pass


def polyColorBlindData(*args, **kwargs):
    """
    This command applies false color to the selected polygonal components and objects, depending on whether or not blind data exists for the selected components (or, in the case of poly objects, dynamic attributes), and, depending on the color mode indicated, what the values are.

    Returns: `string[]` Command result

    """
    pass


def polyColorDel(*args, **kwargs):
    """
    Deletes color from selected components.

    Returns: `string` The node name.

    """
    pass


def polyColorMod(*args, **kwargs):
    """
    Modifies the attributes of a poly color set.

    Returns: `string` The node name.

    """
    pass


def polyColorPerVertex(*args, **kwargs):
    """
    Command associates color(rgb and alpha) with vertices on polygonal objects.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyColorSet(*args, **kwargs):
    """
    Command to do the following to color sets:         - delete an existing color set.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyCompare(*args, **kwargs):
    """
    Compares two Polygonal Geometry objects with a fine control on what to compare.

    Returns: `int` 0 if successful, non-zero if poly1 and poly2 are not determined to be equal based on requested flags. The non-zero value depends on which attributes are different:  Vertices = 1           Edges = 2              Face Descriptions = 4  UV Sets = 8            UV Indices = 16        Color Sets = 32        Color Indices = 64     User Normals = 128      So a return value of 3, for example, indicates both vertices and edges are different.

    """
    pass


def polyCone(*args, **kwargs):
    """
    The cone command creates a new polygonal cone.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyConnectComponents(*args, **kwargs):
    """
    Splits polygon edges according to the selected components.

    Returns: `string` The node name.

    """
    pass


def polyContourProjection(*args, **kwargs):
    """
    Performs a contour stretch UV projection onto an object.

    Returns: `string` The node name.

    """
    pass


def polyCopyUV(*args, **kwargs):
    """
    Copy some UVs from a UV set into another.

    Returns: `string` The node name.

    """
    pass


def polyCrease(*args, **kwargs):
    """
    Command to set the crease values on the edges or vertices of a poly.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyCreaseCtx(*args, **kwargs):
    """
    Create a new context to crease components on polygonal objects.

    Returns: None
    """
    pass


def polyCreateFacet(*args, **kwargs):
    """
    Create a new polygonal object with the specified face, which will be closed.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyCreateFacetCtx(*args, **kwargs):
    """
    Create a new context to create polygonal objects.

    Returns: None
    """
    pass


def polyCube(*args, **kwargs):
    """
    The cube command creates a new polygonal cube.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyCut(*args, **kwargs):
    """
    This command splits a mesh, or a set of poly faces, along a plane.

    Returns: `string` The node name.

    """
    pass


def polyCutCtx(*args, **kwargs):
    """
    Create a new context to cut facets on polygonal objects.

    Returns: None
    """
    pass


def polyCutUVCtx(*args, **kwargs):
    """
    Create a new context to cut UVs on polygonal objects.

    Returns: `boolean` Whether steady stroke is on or not, when querying the steadyStroke flag.

    `float` The distance for a steady stroke, when querying the steadyStrokeDistance flag.

    """
    pass


def polyCylinder(*args, **kwargs):
    """
    The cylinder command creates a new polygonal cylinder.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyCylindricalProjection(*args, **kwargs):
    """
    TpolyProjCmdBase is a base class for the command to create a mapping on the selected polygonal faces.

    Returns: `string` The node name.

    """
    pass


def polyDelEdge(*args, **kwargs):
    """
    Deletes selected edges, and merges neighboring faces.

    Returns: `string` The node name.

    """
    pass


def polyDelFacet(*args, **kwargs):
    """
    Deletes faces.

    Returns: `string` The node name.

    """
    pass


def polyDelVertex(*args, **kwargs):
    """
    Deletes vertices.

    Returns: `string` The node name.

    """
    pass


def polyDuplicateAndConnect(*args, **kwargs):
    """
    This command duplicates the input polygonal object, connects up the outMesh attribute of the original polygonal shape to the inMesh attribute of the newly created duplicate shape and copies over the shader assignments from the original shape to the new duplicated shape.

    Returns: None
    """
    pass


def polyDuplicateEdge(*args, **kwargs):
    """
    Duplicates a series of connected edges (edgeLoop).

    Returns: `string` The node name.

    """
    pass


def polyEditEdgeFlow(*args, **kwargs):
    """
    Edit edges of a polygonal object to respect surface curvature.

    Returns: `string` The node name.

    """
    pass


def polyEditUV(*args, **kwargs):
    """
    Command edits uvs on polygonal objects.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyEditUVShell(*args, **kwargs):
    """
    Command edits uv shells on polygonal objects.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyEvaluate(*args, **kwargs):
    """
    Returns the required counts on the specified objects.

    Returns: `Any` a MEL array of values, a Python dictionary, or a string, depending on the format requested and the language called from.

    """
    pass


def polyExtrudeEdge(*args, **kwargs):
    """
    Extrude edges separately or together.

    Returns: `string` The node name.

    """
    pass


def polyExtrudeFacet(*args, **kwargs):
    """
    Extrude faces.

    Returns: `string` The node name.

    """
    pass


def polyExtrudeVertex(*args, **kwargs):
    """
    Command that extrudes selected vertices outwards.

    Returns: `string` The node name.

    """
    pass


def polyFlipEdge(*args, **kwargs):
    """
    Command to flip the edges shared by 2 adjacent triangles.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyFlipUV(*args, **kwargs):
    """
    Flip (mirror) the UVs (in texture space) of input polyFaces, about either the U or V axis.

    Returns: `string` The node name.

    """
    pass


def polyForceUV(*args, **kwargs):
    """
    A set of functionalities can be called through this command.

    Returns: `boolean` true/false

    """
    pass


def polyGeoSampler(*args, **kwargs):
    """
    
    Returns: `boolean` Success or Failure

    """
    pass


def polyHelix(*args, **kwargs):
    """
    The polyHelix command creates a new polygonal helix.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyHole(*args, **kwargs):
    """
    Command to set and clear holes on given faces.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyInfo(*args, **kwargs):
    """
    Command queries topological information on polygonal objects and components.

    Returns: `string` Components

    """
    pass


def polyInstallAction(*args, **kwargs):
    """
    
    Returns: `string[]` When installing constraint, returns as an array of strings the items on which the installed command will act on. otherwise, returns nothing

    """
    pass


def polyLayoutUV(*args, **kwargs):
    """
    Move UVs in the texture plane to avoid overlaps.

    Returns: `string` The node name.

    """
    pass


def polyListComponentConversion(*args, **kwargs):
    """
    This command converts poly components from one or more types to another one or more types, and returns the list of the conversion.

    Returns: `selectionItem[]` List of poly components

    """
    pass


def polyMapCut(*args, **kwargs):
    """
    Cut along edges of the texture mapping.

    Returns: `string` The node name.

    """
    pass


def polyMapDel(*args, **kwargs):
    """
    Deletes texture coordinates (UVs) from selected faces.

    Returns: `string` The node name.

    """
    pass


def polyMapSew(*args, **kwargs):
    """
    Sew border edges in texture space.

    Returns: `string` The node name.

    """
    pass


def polyMapSewMove(*args, **kwargs):
    """
    This command can be used to Move and Sew together separate UV pieces along geometric edges.

    Returns: `string` The node name.

    """
    pass


def polyMergeEdge(*args, **kwargs):
    """
    Sews two border edges together.

    Returns: `string` The node name.

    """
    pass


def polyMergeEdgeCtx(*args, **kwargs):
    """
    Sews two border edges together.

    Returns: `string` The node name.

    """
    pass


def polyMergeFacet(*args, **kwargs):
    """
    The second face becomes a hole in the first face.

    Returns: `string` The node name.

    """
    pass


def polyMergeFacetCtx(*args, **kwargs):
    """
    The second face becomes a hole in the first face.

    Returns: `string` The node name.

    """
    pass


def polyMergeUV(*args, **kwargs):
    """
    Merge UVs of an object based on their distance.

    Returns: `string` The node name.

    """
    pass


def polyMergeVertex(*args, **kwargs):
    """
    Merge vertices within a given threshold.

    Returns: `string` The node name.

    """
    pass


def polyMirrorFace(*args, **kwargs):
    """
    Mirror all the faces of the selected object.

    Returns: `string` The node name.

    """
    pass


def polyMoveEdge(*args, **kwargs):
    """
    Modifies edges of a polygonal object.

    Returns: `string` The node name.

    """
    pass


def polyMoveFacet(*args, **kwargs):
    """
    Modifies facet of a polygonal object.

    Returns: `string` The node name.

    """
    pass


def polyMoveFacetUV(*args, **kwargs):
    """
    Modifies the map by moving all UV values associated with the selected face(s).

    Returns: `string` The node name.

    """
    pass


def polyMoveUV(*args, **kwargs):
    """
    Moves selected UV coordinates in 2D space.

    Returns: `string` The node name.

    """
    pass


def polyMoveVertex(*args, **kwargs):
    """
    Modifies vertices of a polygonal object.

    Returns: `string` The node name.

    """
    pass


def polyMultiLayoutUV(*args, **kwargs):
    """
    place the UVs of the selected polygonal objects so that they do not overlap.

    Returns: None
    """
    pass


def polyNormal(*args, **kwargs):
    """
    Control the normals of an object.

    Returns: `string` The node name.

    """
    pass


def polyNormalPerVertex(*args, **kwargs):
    """
    Command associates normal(x, y, z) with vertices on polygonal objects.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyNormalizeUV(*args, **kwargs):
    """
    Normalizes the UVs of input polyFaces.

    Returns: `string` The node name.

    """
    pass


def polyOptUvs(*args, **kwargs):
    """
    Optimizes selected UVs.

    Returns: `string` The node name.

    """
    pass


def polyOptions(*args, **kwargs):
    """
    Changes the global display polygonal attributes.

    Returns: None
    """
    pass


def polyOutput(*args, **kwargs):
    """
    Dumps a description of internal memory representation of poly objects.

    Returns: None
    """
    pass


def polyPinUV(*args, **kwargs):
    """
    This command is used to pin and unpin UVs.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyPipe(*args, **kwargs):
    """
    The polyPipe command creates a new polygonal pipe.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyPlanarProjection(*args, **kwargs):
    """
    TpolyProjCmdBase is a base class for the command to create a mapping on the selected polygonal faces.

    Returns: `string` The node name.

    """
    pass


def polyPlane(*args, **kwargs):
    """
    Create a new polygonal plane.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyPlatonicSolid(*args, **kwargs):
    """
    The polyPlatonicSolid command creates a new polygonal platonic solid.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyPoke(*args, **kwargs):
    """
    Introduces a new vertex in the middle of the selected face, and connects it to the rest of the vertices of the face.

    Returns: `string` The node name

    """
    pass


def polyPrimitive(*args, **kwargs):
    """
    Create a polygon primative.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyPrism(*args, **kwargs):
    """
    The prism command creates a new polygonal prism.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyProjectCurve(*args, **kwargs):
    """
    The polyProjectCurve command creates curves by projecting a selected curve onto a selected poly mesh.

    Returns: `string[]` Object name and node name

    """
    pass


def polyProjection(*args, **kwargs):
    """
    Creates a mapping on the selected polygonal faces.

    Returns: `string` Name of node created

    """
    pass


def polyPyramid(*args, **kwargs):
    """
    The pyramid command creates a new polygonal pyramid.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyQuad(*args, **kwargs):
    """
    Merges selected triangles of a polygonal object into four-sided faces.

    Returns: `string` The node name.

    """
    pass


def polyQueryBlindData(*args, **kwargs):
    """
    Command query's blindData associated with particular polygonal components.

    Returns: `string` Blind data

    """
    pass


def polyReduce(*args, **kwargs):
    """
    Simplify a polygonal object by reducing geometry while preserving the overall shape of the mesh.

    Returns: `string` The node name.

    """
    pass


def polyRemesh(*args, **kwargs):
    """
    Triangulates, then remeshes the given mesh through edge splitting and collapsing.

    Returns: `string` The node name.

    """
    pass


def polyRetopo(*args, **kwargs):
    """
    Retopologize a polygonial surface.

    Returns: `string` The node name.

    """
    pass


def polyRetopoCtx(*args, **kwargs):
    """
    Create a new context to manipulate reform nodes.

    Returns: None
    """
    pass


def polySelect(*args, **kwargs):
    """
    This command makes different types of poly component selections.

    Returns: `int[]` List of selected components.

    """
    pass


def polySelectConstraint(*args, **kwargs):
    """
    Changes the global polygonal selection constraints.

    Returns: None
    """
    pass


def polySelectConstraintMonitor(*args, **kwargs):
    """
    Manage the window to display/edit the polygonal selection constraint parameters.

    Returns: None
    """
    pass


def polySelectCtx(*args, **kwargs):
    """
    Create a new context to select polygon components.

    Returns: None
    """
    pass


def polySelectEditCtx(*args, **kwargs):
    """
    Create a new context to select and edit polygonal objects.

    Returns: `string` The context name

    """
    pass


def polySeparate(*args, **kwargs):
    """
    This command creates new objects from the given poly.

    Returns: `string[]` Object name(s) and node name.

    """
    pass


def polySetToFaceNormal(*args, **kwargs):
    """
    This command takes selected polygonal vertices or vertex-faces and changes their normals.

    Returns: `string` of the node name

    """
    pass


def polySewEdge(*args, **kwargs):
    """
    Merge border edges within a given threshold.

    Returns: `string` The node name.

    """
    pass


def polyShortestPathCtx(*args, **kwargs):
    """
    Creates a new context to select shortest edge path between two vertices or UVs in the 3d viewport.

    Returns: None
    """
    pass


def polySlideEdge(*args, **kwargs):
    """
    Moves an edge loop selection along the edges connected to the sides of its vertices.

    Returns: `boolean` Success value

    """
    pass


def polySmooth(*args, **kwargs):
    """
    Smooth a polygonal object.

    Returns: `string` The node name.

    """
    pass


def polySoftEdge(*args, **kwargs):
    """
    Selectively makes edges soft or hard.

    Returns: `string` The name of the polySoftEdge node.

    """
    pass


def polySphere(*args, **kwargs):
    """
    The sphere command creates a new polygonal sphere.

    Returns: `string[]` Object name and node name.

    """
    pass


def polySphericalProjection(*args, **kwargs):
    """
    TpolyProjCmdBase is a base class for the command to create a mapping on the selected polygonal faces.

    Returns: `string` The node name.

    """
    pass


def polySplit(*args, **kwargs):
    """
    Split facets/edges of a polygonal object.

    Returns: `string` The node name.

    """
    pass


def polySplitCtx(*args, **kwargs):
    """
    Create a new context to split facets on polygonal objects.

    Returns: None
    """
    pass


def polySplitCtx2(*args, **kwargs):
    """
    Create a new context to split facets on polygonal objects.

    Returns: None
    """
    pass


def polySplitEdge(*args, **kwargs):
    """
    Split Edges.

    Returns: `string` The node name.

    """
    pass


def polySplitRing(*args, **kwargs):
    """
    Splits a series of ring edges of connected quads and inserts connecting edges between them.

    Returns: `string` The node name.

    """
    pass


def polySplitVertex(*args, **kwargs):
    """
    Use this command to split one or more vertices.

    Returns: `string` The polySplitVert node name.

    """
    pass


def polyStraightenUVBorder(*args, **kwargs):
    """
    Move border UVs along a simple curve.

    Returns: `string` The node name

    """
    pass


def polySubdivideEdge(*args, **kwargs):
    """
    Subdivides an edge into two or more subedges.

    Returns: `string` The node name.

    """
    pass


def polySubdivideFacet(*args, **kwargs):
    """
    Subdivides a face into quads or triangles.

    Returns: `string` The node name.

    """
    pass


def polyToSubdiv(*args, **kwargs):
    """
    This command converts a polygon and produces a subd surface.

    Returns: `string` - the subdivision and optionally the dependency node name

    """
    pass


def polyTorus(*args, **kwargs):
    """
    The torus command creates a new polygonal torus.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyTransfer(*args, **kwargs):
    """
    Transfer information from one polygonal object to another one.

    Returns: `string` representing the node name.

    """
    pass


def polyTriangulate(*args, **kwargs):
    """
    Triangulation breaks polygons down into triangles, ensuring that all faces are planar and non-holed.

    Returns: `string` The node name.

    """
    pass


def polyUVCoverage(*args, **kwargs):
    """
    Return the UV space coverage of the specified components.

    Returns: `float[]` UV space coverage percentage

    """
    pass


def polyUVOverlap(*args, **kwargs):
    """
    Return the required result on the specified components.

    Returns: `selectionItem[]` List of poly components

    """
    pass


def polyUVRectangle(*args, **kwargs):
    """
    Given two vertices, does one of the following: 1) If the vertices define opposite corners of a rectangular area of quads, assigns a grid of UVs spanning the 0-1 area to that rectangle.

    Returns: `string` The node name.

    """
    pass


def polyUVSet(*args, **kwargs):
    """
    Command to do the following to uv sets:         - delete an existing uv set.

    Returns: `boolean` Success or Failure.

    """
    pass


def polyUVStackSimilarShells(*args, **kwargs):
    """
    Stack Similar UV Shells.

    Returns: `string[]` UVs of stacked UV Shells or target UV shells.

    """
    pass


def polyUnite(*args, **kwargs):
    """
    This command creates a new poly as an union of a list of polys If no objects are specified in the command line, then the objects from the active list are used.

    Returns: `string[]` Object name and node name.

    """
    pass


def polyUniteSkinned(*args, **kwargs):
    """
    Command to combine poly mesh objects (as polyUnite) while retaining the smooth skinning setup on the combined object.

    Returns: None
    """
    pass


def polyWedgeFace(*args, **kwargs):
    """
    Extrude faces about an axis.

    Returns: `string` The node name.

    """
    pass


def popupMenu(*args, **kwargs):
    """
    This command creates a popup menu and attaches it to the current control if no parent is specified.

    Returns: `string` Full path name to the menu.

    """
    pass


def pose(*args, **kwargs):
    """
    This command is used to create character poses.

    Returns: `string` Pose name

    """
    pass


def poseEditor(*args, **kwargs):
    """
    This command creates an editor that derives from the base editor class that has controls for deformer and control nodes.

    Returns: `string` The name of the editor

    """
    pass


def posePanel(*args, **kwargs):
    """
    This command creates a panel that derives from the base panel class that houses a poseEditor.

    Returns: `string` The name of the panel

    """
    pass


def preferredRenderer(*args, **kwargs):
    """
    Command to set the preferred renderer.

    Returns: None
    """
    pass


def preloadRefEd(*args, **kwargs):
    """
    This creates an editor for managing which references will be read in (loaded) and which deferred (unloaded) upon opening a file.

    Returns: `string` Name of editor

    """
    pass


def prepareRender(*args, **kwargs):
    """
    This command is used to register, manage and invoke render traversals.

    Returns: None
    """
    pass


def profiler(*args, **kwargs):
    """
    The profiler is used to record timing information from key events within Maya, as an aid in tuning the performance of scenes, scripts and plug-ins.

    Returns: None
    """
    pass


def profilerTool(*args, **kwargs):
    """
    This script is intended to be used by the profilerPanel to interact with the profiler tool's view (draw region).

    Returns: None
    """
    pass


def progressBar(*args, **kwargs):
    """
    Creates a progress bar control that graphically fills in as its progress value increases.

    Returns: `string` Full path name to the control.

    """
    pass


def progressWindow(*args, **kwargs):
    """
    The progressWindow command creates a window containing a status message, a graphical progress gauge, and optionally a "Hit ESC to Cancel" label for interruptable operations.

    Returns: `boolean` Returns true if the window was successfully created, and false if the window could not be created (possibly because one is already showing).

    """
    pass


def projectCurve(*args, **kwargs):
    """
    The projectCurve command creates curves on surface where all selected curves project onto the selected surfaces.

    Returns: `string[]` Object name and node name

    """
    pass


def projectTangent(*args, **kwargs):
    """
    The project tangent command is used to align (for tangents) a curve to two other curves or a surface.

    Returns: `string[]` Object name and node name

    """
    pass


def projectionContext(*args, **kwargs):
    """
    Set the context for projection manips.

    Returns: `string` Context name.

    """
    pass


def projectionManip(*args, **kwargs):
    """
    Various commands to set the manipulator to interesting positions.

    Returns: None
    """
    pass


def promptDialog(*args, **kwargs):
    """
    The promptDialog command creates a modal dialog with a message to the user, a text field in which the user may enter a response, and a variable number of buttons to dismiss the dialog.

    Returns: `string` `Indicates how the dialog was dismissed. If a button is
pressed then the label of the button is returned. If the dialog is
closed then the value for the flag ds/dismissString is
returned.`
    """
    pass


def propModCtx(*args, **kwargs):
    """
    Controls the proportional move context.

    Returns: `string` Name of the new context created

    """
    pass


def propMove(*args, **kwargs):
    """
    Performs a proportional translate, scale or rotate operation on any number of objects.

    Returns: None
    """
    pass


def psdChannelOutliner(*args, **kwargs):
    """
    Create a psdChannelOutliner control which is capable of displaying a tree structure upto one level.

    Returns: `string` The full name of the psdChannelOutliner control

    """
    pass


def psdEditTextureFile(*args, **kwargs):
    """
    Edits the existing PSD file.

    Returns: None
    """
    pass


def psdExport(*args, **kwargs):
    """
    Writes the Photoshop file layer set into different formats.

    Returns: None
    """
    pass


def psdTextureFile(*args, **kwargs):
    """
    Creates a Photoshop file with UVSnap shot image and the layer set names as the input.

    Returns: None
    """
    pass


def querySubdiv(*args, **kwargs):
    """
    Queries a subdivision surface based on a set of query parameters and updates the selection list with the results.

    Returns: `boolean` Command result

    """
    pass


def quit(*args, **kwargs):
    """
    This command is used to exit the application.

    Returns: None
    """
    pass


def radial(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def radioButton(*args, **kwargs):
    """
    This command creates a radio button that is added to the most recently created radio collection if the  flag is not used.

    Returns: `string` Full path name to the control.

    """
    pass


def radioButtonGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def radioCollection(*args, **kwargs):
    """
    This command creates a radio button collection.

    Returns: `string` Full path name to the collection.

    """
    pass


def radioMenuItemCollection(*args, **kwargs):
    """
    This command creates a radioMenuItemCollection.

    Returns: `string` Full path name to the collection.

    """
    pass


def rampColorPort(*args, **kwargs):
    """
    This command creates a control that displays an image representing the ramp node specified, and supports editing of that node.

    Returns: `string` The name of the port created or modified

    """
    pass


def rangeControl(*args, **kwargs):
    """
    This command creates a control used for displaying and modifying the current playback range.

    Returns: `string` Name of newly created rangeControl.

    """
    pass


def readTake(*args, **kwargs):
    """
    This action reads a take (.

    Returns: None
    """
    pass


def rebuildCurve(*args, **kwargs):
    """
    This command rebuilds a curve by modifying its parameterization.

    Returns: `string[]` Object name and node name

    """
    pass


def rebuildSurface(*args, **kwargs):
    """
    This command rebuilds a surface by modifying its parameterization.

    Returns: `string[]` Object name and node name

    """
    pass


def recordAttr(*args, **kwargs):
    """
    This command sets up an attribute to be recorded.

    Returns: None
    """
    pass


def recordDevice(*args, **kwargs):
    """
    Starts and stops server side device recording.

    Returns: None
    """
    pass


def redo(*args, **kwargs):
    """
    Takes the most recently undone command from the undo list and redoes it.

    Returns: None
    """
    pass


def referenceEdit(*args, **kwargs):
    """
    Use this command to remove and change the modifications which have been applied to references.

    Returns: None
    """
    pass


def referenceQuery(*args, **kwargs):
    """
    Use this command to find out information about references and referenced nodes.

    Returns: `string[]` For query execution.

    """
    pass


def refineSubdivSelectionList(*args, **kwargs):
    """
    Refines a subdivision surface set of components based on the selection list.

    Returns: `boolean` Command result

    """
    pass


def refresh(*args, **kwargs):
    """
    This command is used to force a redraw during script execution.

    Returns: None
    """
    pass


def refreshEditorTemplates(*args, **kwargs):
    """
    This command refreshes all cached attribute editor templates, including those copied from the standard AE.

    Returns: None
    """
    pass


def regionSelectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the graph editor using the region select tool.

    Returns: `float` Manip values, when queried

    """
    pass


def relationship(*args, **kwargs):
    """
    This is primarily for use with file IO.

    Returns: None
    """
    pass


def reloadImage(*args, **kwargs):
    """
    This command reloads an xpm image from disk.

    Returns: `boolean` True if image is successfully loaded, false otherwise.

    """
    pass


def removeJoint(*args, **kwargs):
    """
    This command will remove the selected joint or the joint given at the command line from the skeleton.

    Returns: None
    """
    pass


def removeMultiInstance(*args, **kwargs):
    """
    Removes a particular instance of a multiElement.

    Returns: `boolean` (true if the instance was removed, false if something went wrong, like the attribute is connected but -b true was not specified)

    """
    pass


def rename(*args, **kwargs):
    """
    Renames the given object to have the new name.

    Returns: `string` The new name. When undone returns original name.

    """
    pass


def renameAttr(*args, **kwargs):
    """
    Renames the given user-defined attribute to the name given in the string argument.

    Returns: `string` The new name. When undone returns the original name.

    """
    pass


def renameUI(*args, **kwargs):
    """
    This command renames the UI object passed as first arument to the new name specified as second argument.

    Returns: `string` The new name, or the old name if re-naming fails.

    """
    pass


def render(*args, **kwargs):
    """
    The render command is used to start off a MayaSoftware rendering session of the currently active camera.

    Returns: `string` The name of the rendered image.

    """
    pass


def renderGlobalsNode(*args, **kwargs):
    """
    This command creates a new node in the dependency graph of the specified type.

    Returns: `string` The name of the new node.

    `string` The name of the render globals node

    """
    pass


def renderInfo(*args, **kwargs):
    """
    The renderInfo commands sets geometric properties of surfaces of the selected object.

    Returns: None
    """
    pass


def renderLayerPostProcess(*args, **kwargs):
    """
    Post process the results when rendering is done with.

    Returns: None
    """
    pass


def renderManip(*args, **kwargs):
    """
    This command creates manipulators for cameras or lights.

    Returns: None
    """
    pass


def renderPartition(*args, **kwargs):
    """
    Set or query the model's current partition.

    Returns: `string` The render partition

    """
    pass


def renderPassRegistry(*args, **kwargs):
    """
    query information related with render passes.

    Returns: `string[]` Command result

    """
    pass


def renderQualityNode(*args, **kwargs):
    """
    This command creates a new node in the dependency graph of the specified type.

    Returns: `string` The name of the new node.

    `string` The Name of the render quality node

    """
    pass


def renderSettings(*args, **kwargs):
    """
    Query interface to the common tab of the render settings.

    Returns: `string[]` Command result

    """
    pass


def renderThumbnailUpdate(*args, **kwargs):
    """
    Toggle the updating of object thumbnails.

    Returns: None
    """
    pass


def renderWindowEditor(*args, **kwargs):
    """
    Create a editor window that can receive the result of the rendering process.

    Returns: `string` The name of the editor

    """
    pass


def renderWindowSelectContext(*args, **kwargs):
    """
    Set the selection context for the render view panel.

    Returns: `string` Context name

    """
    pass


def renderer(*args, **kwargs):
    """
    Command to register renders.

    Returns: None
    """
    pass


def reorder(*args, **kwargs):
    """
    This command reorders (moves) objects relative to their siblings.

    Returns: None
    """
    pass


def reorderContainer(*args, **kwargs):
    """
    This command reorders (moves) objects relative to their siblings in a container.

    Returns: None
    """
    pass


def reorderDeformers(*args, **kwargs):
    """
    This command changes the order in which 2 deformation nodes affect the output geometry.

    Returns: None
    """
    pass


def requires(*args, **kwargs):
    """
    This command is used during file I/O to specify the requirements needed to load the given file.

    Returns: None
    """
    pass


def reroot(*args, **kwargs):
    """
    This command will reroot a skeleton.

    Returns: None
    """
    pass


def resampleFluid(*args, **kwargs):
    """
    A command to extend the fluid grid, keeping the voxels the same size, and keeping the existing contents of the fluid in the same place.

    Returns: None
    """
    pass


def resetTool(*args, **kwargs):
    """
    This command resets a tool back to its "factory settings".

    Returns: None
    """
    pass


def resolutionNode(*args, **kwargs):
    """
    This command creates a new node in the dependency graph of the specified type.

    Returns: `string` The name of the new node.

    `string` The name of the render resolution node

    """
    pass


def resourceManager(*args, **kwargs):
    """
    List resources matching certain properties.

    Returns: None
    """
    pass


def retimeKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the graph editor using the retime tool.

    Returns: `boolean` Query value from the snapOnFame setting.

    """
    pass


def reverseCurve(*args, **kwargs):
    """
    The reverseCurve command reverses the direction of a curve or curve-on-surface.

    Returns: `string[]` (object name and node name)

    """
    pass


def reverseSurface(*args, **kwargs):
    """
    The reverseSurface command reverses one or both directions of a surface or can be used to "swap" the U and V directions (this creates the effect of reversing the surface normal).

    Returns: `string[]` Object name and node name

    """
    pass


def revolve(*args, **kwargs):
    """
    This command creates a revolved surface by revolving the given profile curve about an axis.

    Returns: `string[]` Object name and node name

    """
    pass


def rigidBody(*args, **kwargs):
    """
    This command creates a rigid body from a polygonal or nurbs surface.

    Returns: `string` New rigid body name.

    """
    pass


def rigidSolver(*args, **kwargs):
    """
    This command sets the attributes for the rigid solver.

    Returns: None
    """
    pass


def roll(*args, **kwargs):
    """
    The roll command rotates a camera about its viewing direction, a positive angle produces clockwise camera rotation, while a negative angle produces counter-clockwise camera rotation.

    Returns: None
    """
    pass


def rollCtx(*args, **kwargs):
    """
    Create, edit, or query a roll context.

    Returns: `string` The name of the context

    """
    pass


def rotate(*args, **kwargs):
    """
    The rotate command is used to change the rotation of geometric objects.

    Returns: None
    """
    pass


def rotationInterpolation(*args, **kwargs):
    """
    The rotationInterpolation command converts the rotation curves to the         desired rotation interpolation representation.

    Returns: None
    """
    pass


def roundConstantRadius(*args, **kwargs):
    """
    This command generates constant radius NURBS fillets and NURBS corner surfaces for matching edge pairs on NURBS surfaces.

    Returns: `string[]` (resulting NURBS surfaces' names and node name)

    """
    pass


def rowColumnLayout(*args, **kwargs):
    """
    This command creates a rowColumn layout.

    Returns: `string` Full path name to the control.

    """
    pass


def rowLayout(*args, **kwargs):
    """
    This command creates a layout capable of positioning children into a single horizontal row.

    Returns: `string` Full path name to the control.

    """
    pass


def runup(*args, **kwargs):
    """
    runup plays the scene through a frame of frames, forcing dynamic objects to evaluate as it does so.

    Returns: `string` Command result

    """
    pass


def sampleImage(*args, **kwargs):
    """
    The sampleImage command is used to control parameters of sample images, such as swatches in the multilister.

    Returns: None
    """
    pass


def saveAllShelves(*args, **kwargs):
    """
    This command writes all shelves that are immediate children of the specified control layout to the prefs directory.

    Returns: `boolean` True if successful, otherwise issues an error message and returns false.

    """
    pass


def saveFluid(*args, **kwargs):
    """
    A command to save the current state of the fluid to the initial state cache.

    Returns: None
    """
    pass


def saveImage(*args, **kwargs):
    """
    This command creates a static image for non-xpm files.

    Returns: `string` The name of the image created.

    `string` The name of the saveImage control created.

    """
    pass


def saveInitialState(*args, **kwargs):
    """
    saveInitialState saves the current state of dynamics objects as the initial state.

    Returns: `string` Command result

    """
    pass


def saveMenu(*args, **kwargs):
    """
    This command is used for saving the contents of a menu, so that another instance of the menu may be recreated later.

    Returns: `string` The name of the saved file.

    """
    pass


def savePrefObjects(*args, **kwargs):
    """
    This command saves preference dependency nodes to "userPrefObjects.

    Returns: `boolean` True if successful.

    """
    pass


def savePrefs(*args, **kwargs):
    """
    This command saves preferences to disk.

    Returns: None
    """
    pass


def saveShelf(*args, **kwargs):
    """
    This command saves the specified shelf (first argument) to the specified file (second argument).

    Returns: `boolean` True if successful.

    """
    pass


def saveToolSettings(*args, **kwargs):
    """
    This command causes all the tools not on the shelf to save their settings as optionVars.

    Returns: None
    """
    pass


def saveViewportSettings(*args, **kwargs):
    """
    This command causes all the 3d views to save their settings as optionVar's.

    Returns: None
    """
    pass


def scale(*args, **kwargs):
    """
    The scale command is used to change the sizes of geometric objects.

    Returns: None
    """
    pass


def scaleComponents(*args, **kwargs):
    """
    This is a limited version of the scale command.

    Returns: None
    """
    pass


def scaleConstraint(*args, **kwargs):
    """
    Constrain an object's scale to the scale of the target object or to the average scale of a number of targets.

    Returns: `string[]` Name of the created constraint node

    """
    pass


def scaleKey(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` Number of curves on which scale was performed

    """
    pass


def scaleKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to scale keyframes within the graph editor.

    Returns: `string` Scale type, if the type flag was queried

    `boolean` Whether specified keys should be scaled, if the scaleSpecifiedKeys flag was queried

    """
    pass


def sceneEditor(*args, **kwargs):
    """
    This creates an editor for managing the files in a scene.

    Returns: `string` Name of editor.

    """
    pass


def sceneUIReplacement(*args, **kwargs):
    """
    This command returns existing scene based UI that can be utilized by the scene that is being loaded.

    Returns: `string` When used with getNextScriptedPanel, getNextPanel, or getNextFilter

    """
    pass


def scmh(*args, **kwargs):
    """
    Set the current manipulator handle value(s).

    Returns: None
    """
    pass


def scriptCtx(*args, **kwargs):
    """
    This command allows a user to create their own tools based on the selection tool.

    Returns: `string` Context name

    """
    pass


def scriptEditorInfo(*args, **kwargs):
    """
    Use this command to directly manipulate and query the contents of the Command Window window.

    Returns: `string` The name of the Command Window window is returned.

    """
    pass


def scriptJob(*args, **kwargs):
    """
    This command creates a "script job", which is a MEL command or script.

    Returns: `int` `The job number, which can be used to kill the job. The job
number will be a value greater than or equal to zero`
    `string[]` `A string list when the list flag is used`
    `boolean` `For the exists flag.`
    """
    pass


def scriptNode(*args, **kwargs):
    """
    scriptNodes contain scripts that are executed when a file is loaded or when the script node is deleted.

    Returns: None
    """
    pass


def scriptTable(*args, **kwargs):
    """
    This command creates/edits/queries the script table control.

    Returns: `string` The full path name to the created script table control.

    """
    pass


def scriptedPanel(*args, **kwargs):
    """
    This command will create an instance of the specified scriptedPanelType.

    Returns: `string` The name of the scripted panel.

    """
    pass


def scriptedPanelType(*args, **kwargs):
    """
    This command defines the callbacks for a type of scripted panel.

    Returns: `string` The name of the scripted panel type.

    """
    pass


def scrollField(*args, **kwargs):
    """
    This command creates a scrolling field that handles multiple lines of text.

    Returns: `string` Full path name to the control.

    """
    pass


def scrollLayout(*args, **kwargs):
    """
    This command creates a scroll layout.

    Returns: `string` Full path name to the control.

    """
    pass


def sculpt(*args, **kwargs):
    """
    This command creates/edits/queries a sculpt object deformer.

    Returns: `string[]` Sculpt algorithm node name, sculpt sphere name, and sculpt stretch origin name

    """
    pass


def sculptMeshCacheChangeCloneSource(*args, **kwargs):
    """
    This command changes the source blend shape and target for the clone target tool.

    Returns: None
    """
    pass


def sculptMeshCacheCtx(*args, **kwargs):
    """
    This is a tool context command for mesh cache sculpting tool.

    Returns: None
    """
    pass


def sculptTarget(*args, **kwargs):
    """
    This command is used to specify the blend shape target to be modified by the sculpting tools and transform manipulators.

    Returns: None
    """
    pass


def selLoadSettings(*args, **kwargs):
    """
    
    Returns: `string` For query execution.

    """
    pass


def select(*args, **kwargs):
    """
    This command is used to put objects onto or off of the active list.

    Returns: None
    """
    pass


def selectContext(*args, **kwargs):
    """
    Creates a context to perform selection.

    Returns: `string` Name of the context created

    """
    pass


def selectKey(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` The number of curves on which keys were selected (or deselcted).

    """
    pass


def selectKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to select keyframes within the graph editor.

    Returns: None
    """
    pass


def selectKeyframeRegionCtx(*args, **kwargs):
    """
    This command creates a context which may be used to select keyframes within the keyframe region of the dope sheet editor.

    Returns: None
    """
    pass


def selectMode(*args, **kwargs):
    """
    The  command is used to change the selection mode.

    Returns: `boolean` if a query operation

    """
    pass


def selectPref(*args, **kwargs):
    """
    This command controls state variables used to selection UI behavior.

    Returns: `boolean` in the query mode.

    """
    pass


def selectPriority(*args, **kwargs):
    """
    The  command is used to change the selection priority of particular types of objects that can be selected when using the select tool.

    Returns: `int` if a query operation

    """
    pass


def selectType(*args, **kwargs):
    """
    The  command is used to change the set of allowable types of objects that can be selected when using the select tool.

    Returns: `boolean` if a query operation

    """
    pass


def selectionConnection(*args, **kwargs):
    """
    This command creates a named selectionConnection object.

    Returns: `string` Value of the queried flag

    """
    pass


def separator(*args, **kwargs):
    """
    This command creates a separator widget in a variety of drawing styles.

    Returns: `string` Full path name to the control.

    """
    pass


def sequenceManager(*args, **kwargs):
    """
    The sequenceManager command manages sequences, shots, and their related scenes.

    Returns: None
    """
    pass


def setAttr(*args, **kwargs):
    """
    Sets the value of a dependency node attribute.

    Returns: None
    """
    pass


def setAttrMapping(*args, **kwargs):
    """
    This command applies an offset and scale to a specified device attachment.

    Returns: None
    """
    pass


def setDefaultShadingGroup(*args, **kwargs):
    """
    The setDefaultShadingGroup command is used to change which shading group is considered the current default shading group.

    Returns: None
    """
    pass


def setDrivenKeyframe(*args, **kwargs):
    """
    This command sets a driven keyframe.

    Returns: `int` Number of keyframes set.

    """
    pass


def setDynamic(*args, **kwargs):
    """
    setDynamic sets the isDynamic attribute of particle objects on or off.

    Returns: `string` array

    """
    pass


def setEditCtx(*args, **kwargs):
    """
    This command creates a tool that can be used to modify set membership.

    Returns: `string` The name of the context

    """
    pass


def setFluidAttr(*args, **kwargs):
    """
    Sets values of built-in fluid attributes such as density, velocity, etc.

    Returns: None
    """
    pass


def setFocus(*args, **kwargs):
    """
    Give keyboard focus to a specific control or panel, passed as an argument.

    Returns: None
    """
    pass


def setInfinity(*args, **kwargs):
    """
    Set the infinity type before (after) a paramCurve's first (last) keyframe.

    Returns: None
    """
    pass


def setInputDeviceMapping(*args, **kwargs):
    """
    The command sets a scale and offset for all attachments made to a specified device axis.

    Returns: None
    """
    pass


def setKeyCtx(*args, **kwargs):
    """
    This command creates a context which may be used to set keys within the graph editor.

    Returns: `boolean` Value of the breakdown flag, when queried

    """
    pass


def setKeyPath(*args, **kwargs):
    """
    The setKeyPath command either creates or edits the path (a nurbs curve) based on the current position of the selected object at the current time.

    Returns: `string[]` (Names of the created curve node and motionPath node)

    """
    pass


def setKeyframe(*args, **kwargs):
    """
    This command creates keyframes for the specified objects, or the active objects if none are specified on the command line.

    Returns: `int` Number of keyframes set by this command.

    """
    pass


def setKeyframeBlendshapeTargetWts(*args, **kwargs):
    """
    This command can be used to keyframe per-point blendshape target weights.

    Returns: `int` number of vertices for which the targets weights are keyed

    """
    pass


def setMenuMode(*args, **kwargs):
    """
    Optionally sets a new Menu Mode for the menu bar in the main Maya window.

    Returns: `string` The current Menu Mode for the menu bar in the main Maya window.

    """
    pass


def setNodeTypeFlag(*args, **kwargs):
    """
    This command sets static data on the specified node type.

    Returns: `boolean` Did the command succeed?

    """
    pass


def setParent(*args, **kwargs):
    """
    This command changes the default parent to be the specified parent.

    Returns: `string` Name of the parent if the parent changes. Empty string if the parent doesn't change.

    """
    pass


def setParticleAttr(*args, **kwargs):
    """
    This action will set the value of the chosen attribute for every particle or selected component in the selected or passed particle object.

    Returns: None
    """
    pass


def setRenderPassType(*args, **kwargs):
    """
    This command will set the passID of a renderPass node and create the custom attributes specified by the corresponding render pass definition.

    Returns: `boolean` true/false

    """
    pass


def setStartupMessage(*args, **kwargs):
    """
    Update the startup window message.

    Returns: None
    """
    pass


def setToolTo(*args, **kwargs):
    """
    This command switches control to the named context.

    Returns: None
    """
    pass


def setUITemplate(*args, **kwargs):
    """
    This command sets the current(default) command template for the ELF commands.

    Returns: `string` The name of the currently selected command template.

    """
    pass


def setXformManip(*args, **kwargs):
    """
    This command changes some of the settings of the xform manip, to control its appearance.

    Returns: None
    """
    pass


def sets(*args, **kwargs):
    """
    This command is used to create a set, query some state of a set, or perform operations to update the membership of a set.

    Returns: `string` For creation operations (name of the set that was created or edited)

    `string[]` For query operation (names of items in the set)

    `boolean` For isIntersecting and isMember operations

    """
    pass


def shadingConnection(*args, **kwargs):
    """
    Sets the connection state of a connection between nodes that are used in shading.

    Returns: None
    """
    pass


def shadingGeometryRelCtx(*args, **kwargs):
    """
    This command creates a context that can be used for associating geometry to shading groups.

    Returns: `string` Name of the context created.

    """
    pass


def shadingLightRelCtx(*args, **kwargs):
    """
    This command creates a context that can be used for associating lights to shading groups.

    Returns: `string` Name of the context created.

    """
    pass


def shadingNetworkCompare(*args, **kwargs):
    """
    This command allows you to compare two shading networks.

    Returns: `string[]|string|int` Command result

    """
    pass


def shadingNode(*args, **kwargs):
    """
    This command creates a new node in the dependency graph of the specified type.

    Returns: `string` The name of the new node.

    `string` (the name of the new node)

    """
    pass


def shapeCompare(*args, **kwargs):
    """
    Compares two shapes.

    Returns: `int` 0 if successful, 1 if both shapes are not determined to be equal based on requested flags.

    """
    pass


def shapeEditor(*args, **kwargs):
    """
    This command creates an editor that derives from the base editor class that has controls for deformer, control nodes.

    Returns: `string` The name of the editor

    """
    pass


def shapePanel(*args, **kwargs):
    """
    This command creates a panel that derives from the base panel class that houses a shapeEditor.

    Returns: `string` The name of the panel

    """
    pass


def shelfButton(*args, **kwargs):
    """
    This control supports up to 3 icon images and 4 different display styles.

    Returns: `string` The full name of the button.

    """
    pass


def shelfLayout(*args, **kwargs):
    """
    This command creates a new empty shelf layout.

    Returns: `string` The name of the layout.

    """
    pass


def shelfTabLayout(*args, **kwargs):
    """
    This command creates/edits/queries a shelf tab group which is essentially a normal tabLayout with some drop behaviour in the tab bar.

    Returns: `string` The name of the shelfTabLayout.

    """
    pass


def shot(*args, **kwargs):
    """
    Use this command to create a shot node or manipulate that node.

    Returns: `string` Shot name

    """
    pass


def shotRipple(*args, **kwargs):
    """
    When Ripple Edit Mode is enabled, neighboring shots to the shot that gets manipulated are moved in sequence time to either make way or close up gaps corresponding to that node's editing.

    Returns: None
    """
    pass


def shotTrack(*args, **kwargs):
    """
    This command is used for inserting and removing tracks related to the shots displayed in the Sequencer.

    Returns: None
    """
    pass


def showHelp(*args, **kwargs):
    """
    Invokes a web browser to open the on-line documentation and help files.

    Returns: None
    """
    pass


def showHidden(*args, **kwargs):
    """
    The  command is used to make invisible objects visible.

    Returns: None
    """
    pass


def showManipCtx(*args, **kwargs):
    """
    This command can be used to create a show manip context.

    Returns: `string` The name of the newly created context.

    """
    pass


def showMetadata(*args, **kwargs):
    """
    This command is used to show metadata values which is in the specified channels "vertex", "edge", "face", and "vertexFace" in the viewport.

    Returns: `string` result of the operation or the queried status

    """
    pass


def showSelectionInTitle(*args, **kwargs):
    """
    This command causes the title of the window specified as an argument to be linked to the current file and selection.

    Returns: None
    """
    pass


def showShadingGroupAttrEditor(*args, **kwargs):
    """
    The showShadingGroupAttrEditor command opens up the attribute editor for the current object's shading-group information.

    Returns: `boolean` true if a shading group is displayed, otherwise false.

    """
    pass


def showWindow(*args, **kwargs):
    """
    Make a window visible.

    Returns: None
    """
    pass


def simplify(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` Number of animation curves simplified

    """
    pass


def singleProfileBirailSurface(*args, **kwargs):
    """
    This cmd creates a railed surface by sweeping the profile curve along the two rail curves.

    Returns: `string[]` Object name and node name

    """
    pass


def skeletonEmbed(*args, **kwargs):
    """
    This command is used to embed a skeleton inside meshes.

    Returns: None
    """
    pass


def skinBindCtx(*args, **kwargs):
    """
    This command creates a tool that can be used to edit volumes from an interactive bind.

    Returns: `string` The name of the context created

    """
    pass


def skinCluster(*args, **kwargs):
    """
    The skinCluster command is used for smooth skinning in maya.

    Returns: `string` (the skinCluster node name)

    """
    pass


def skinPercent(*args, **kwargs):
    """
    This command edits and queries the weight values on members of a skinCluster node, given as the first argument.

    Returns: None
    """
    pass


def smoothCurve(*args, **kwargs):
    """
    The smooth command smooths the curve at the given control points.

    Returns: `string[]` Object name and node name

    """
    pass


def smoothTangentSurface(*args, **kwargs):
    """
    The smoothTangentSurface command smooths the surface along an isoparm at each parameter value.

    Returns: `string[]` Object name and node name

    """
    pass


def snapKey(*args, **kwargs):
    """
    This command operates on a keyset.

    Returns: `int` Number of animation curves with keys that were not snapped because of time-snapping conflicts.

    """
    pass


def snapMode(*args, **kwargs):
    """
    The snapMode command is used to control snapping.

    Returns: `boolean` if command is a query

    """
    pass


def snapTogetherCtx(*args, **kwargs):
    """
    The snapTogetherCtx command creates a tool for snapping surfaces together.

    Returns: `string` (name of the new context)

    """
    pass


def snapshot(*args, **kwargs):
    """
    This command can be used to create either a series of surfaces evaluated at the times specified by the command flags, or a motion trail displaying the trajectory of the object's pivot point at the times specified.

    Returns: `string[]` names of nodes created or edited: transform-name [snapshot-node-name]

    """
    pass


def snapshotBeadCtx(*args, **kwargs):
    """
    Creates a context for manipulating in and/or out tangent beads on the motion trail.

    Returns: `string` (name of the new context)

    """
    pass


def snapshotModifyKeyCtx(*args, **kwargs):
    """
    Creates a context for inserting/delete keys on an editable motion trail.

    Returns: `string` (name of the new context)

    """
    pass


def soft(*args, **kwargs):
    """
    Makes a soft body from the object(s) passed on the command line or in the selection list.

    Returns: `string` array

    """
    pass


def softMod(*args, **kwargs):
    """
    The softMod command creates a softMod or edits the membership of an existing softMod.

    Returns: `string` [] (the softMod node name and the softMod handle name)

    """
    pass


def softModCtx(*args, **kwargs):
    """
    Controls the softMod context.

    Returns: `string` - name of the new context created

    """
    pass


def softSelect(*args, **kwargs):
    """
    This command allows you to change the soft modelling options.

    Returns: None
    """
    pass


def soloMaterial(*args, **kwargs):
    """
    Shows a preview of a specified material node output attribute.

    Returns: `boolean` Success or Failure

    """
    pass


def sortCaseInsensitive(*args, **kwargs):
    """
    This command sorts all the strings of an array in a case insensitive way.

    Returns: `string[]` string to sort

    """
    pass


def sound(*args, **kwargs):
    """
    Creates an audio node which can be used with UI commands such as soundControl or timeControl which support sound scrubbing and sound during playback.

    Returns: `string` Name of resulting audio node

    """
    pass


def soundControl(*args, **kwargs):
    """
    This command creates a control used for changing current time and scratching/scrubbing through sound files.

    Returns: `string` Name of created or edited control.

    """
    pass


def spaceLocator(*args, **kwargs):
    """
    The command creates a locator at the specified position in space.

    Returns: `string[]` The name for the new locator in space.

    """
    pass


def sphere(*args, **kwargs):
    """
    The sphere command creates a new sphere.

    Returns: `string[]` Object name and node name

    """
    pass


def spotLight(*args, **kwargs):
    """
    TlightCmd is the base class for other light commands.

    Returns: `string` Light shape name boolean Barn door enabled state angle Left barn door angle angle Right barn door angle angle Top barn door angle angle Bottom barn door angle angle Cone angle angle Penumbra angle float Dropoff value

    `double[]` when querying the rgb or shadowColor flags double when querying the intensity flag boolean when querying the useRayTraceShadows or exclusive flags linear[] when querying the position flag angle[] when querying the rotation flag string when querying the name flag

    `int` rate of light decay, when querying the decayRate flag

    `int` Number of shadow samples, when querying the shadowSamples flag boolean True if soft shadows are enabled, when querying the softShadow flag float Shadow dithering value, when querying the shadowDither flag float Disc radius value, when querying the discRadius flag

    """
    pass


def spotLightPreviewPort(*args, **kwargs):
    """
    This command creates a 3dPort that displays an image representing the illumination provided by the spotLight.

    Returns: `string` - the name of the port created or modified

    """
    pass


def spreadSheetEditor(*args, **kwargs):
    """
    This command creates a new spread sheet editor in the current layout.

    Returns: `string` The name of the editor

    """
    pass


def spring(*args, **kwargs):
    """
    The spring command can do any of the following: * create a new spring object (shape plus transform).

    Returns: `string` Command result

    """
    pass


def squareSurface(*args, **kwargs):
    """
    This command produces a square surface given 3 or 4 curves.

    Returns: `string[]` Object name and node name

    """
    pass


def srtContext(*args, **kwargs):
    """
    This command can be used to create a combined transform (translate/scale/rotate) context.

    Returns: `string` - name of the newly created context

    """
    pass


def stereoCameraView(*args, **kwargs):
    """
    Create, edit or query a model editor.

    Returns: `string` the name of the editor.

    """
    pass


def stereoRigManager(*args, **kwargs):
    """
    This command manages the set of stereo rig tools.

    Returns: None
    """
    pass


def stitchSurface(*args, **kwargs):
    """
    The stitchSurface command aligns two surfaces together to be G(0) and/or G(1) continuous by ajusting only the Control Vertices of the surfaces.

    Returns: `string[]` Object name and node name

    """
    pass


def stitchSurfacePoints(*args, **kwargs):
    """
    The stitchSurfacePoints command aligns two or more surface points along the boundaries together to a single point.

    Returns: `string[]` Object name and node name

    """
    pass


def stringArrayIntersector(*args, **kwargs):
    """
    The stringArrayIntersector command creates and edits an object which is able to efficiently intersect large string arrays.

    Returns: `string` The name of the intersector.

    """
    pass


def stroke(*args, **kwargs):
    """
    The stroke command creates a new Paint Effects stroke node.

    Returns: `string` (The path to the new stroke or the replaced stroke)

    """
    pass


def subdAutoProjection(*args, **kwargs):
    """
    Projects a texture map onto an object, using several orthogonal projections simultaneously.

    Returns: `string` The node name.

    """
    pass


def subdCleanTopology(*args, **kwargs):
    """
    Command cleans topology of subdiv surfaces - at all levels.

    Returns: `boolean` Success or Failure.

    """
    pass


def subdCollapse(*args, **kwargs):
    """
    This command converts a takes a subdivision surface, passed as the argument, and produces a subdivision surface with a number of hierarchy levels "removed".

    Returns: `string[]` The subd surface and optionally the dependency node name

    """
    pass


def subdDuplicateAndConnect(*args, **kwargs):
    """
    This command duplicates the input subdivision surface object, connects up the outSubdiv attribute of the original subd shape to the create attribute of the newly created duplicate shape and copies over the shader assignments from the original shape to the new duplicated shape.

    Returns: None
    """
    pass


def subdEditUV(*args, **kwargs):
    """
    Command edits uvs on subdivision surfaces.

    Returns: `boolean` Success or Failure.

    """
    pass


def subdLayoutUV(*args, **kwargs):
    """
    Move UVs in the texture plane to avoid overlaps.

    Returns: `string` The node name.

    """
    pass


def subdListComponentConversion(*args, **kwargs):
    """
    This command converts subdivision surface components from one or more types to another one or more types, and returns the list of the conversion.

    Returns: `string[]` List of subdivision surface components

    """
    pass


def subdMapCut(*args, **kwargs):
    """
    Cut along edges of the texture mapping.

    Returns: `string` The node name.

    """
    pass


def subdMapSewMove(*args, **kwargs):
    """
    This command can be used to Move and Sew together separate UV pieces along geometric edges.

    Returns: `string` The node name.

    """
    pass


def subdMatchTopology(*args, **kwargs):
    """
    Command matches topology across multiple subdiv surfaces - at all levels.

    Returns: `boolean` Success or Failure.

    """
    pass


def subdMirror(*args, **kwargs):
    """
    This command takes a subdivision surface, passed as the argument, and produces a subdivision surface that is a mirror.

    Returns: `string[]` The subdivision surface and optionally the dependency node name

    """
    pass


def subdPlanarProjection(*args, **kwargs):
    """
    TsubProjCmdBase is a base class for the command to create a mapping on the selected subdivision faces.

    Returns: `string` The node name.

    """
    pass


def subdToBlind(*args, **kwargs):
    """
    The subdivision surface hierarchical edits will get copied into blind data on the given polygon.

    Returns: `boolean` Command result

    """
    pass


def subdToPoly(*args, **kwargs):
    """
    This command tessellates a subdivision surface and produces polygon.

    Returns: `string[]` The polygon and optionally the dependency node name

    """
    pass


def subdTransferUVsToCache(*args, **kwargs):
    """
    The subdivision surface finer level uvs will get copied to the polygonToSubd node sent in as argument.

    Returns: `boolean` Command result

    """
    pass


def subdiv(*args, **kwargs):
    """
    Provides useful information about the selected subdiv or components, such as the deepest subdivided level, the children or parents of the currently selected components, etc.

    Returns: None
    """
    pass


def subdivCrease(*args, **kwargs):
    """
    Set the creasing on subdivision mesh edges or mesh points that are on the selection list.

    Returns: `boolean` Command result

    """
    pass


def subdivDisplaySmoothness(*args, **kwargs):
    """
    Sets or querys the display smoothness of subdivision surfaces on the selection list or of all subdivision surfaces if the -all option is set.

    Returns: `boolean` Command result

    """
    pass


def substituteGeometry(*args, **kwargs):
    """
    This command can be used to replace the geometry which is already connected to deformers with a new geometry.

    Returns: `string` Name of shapes that were replaced

    """
    pass


def suitePrefs(*args, **kwargs):
    """
    This command sets the mouse and keyboard interaction mode for Maya and other Suites applications (if Maya is part of a Suites install).

    Returns: None
    """
    pass


def surface(*args, **kwargs):
    """
    The cmd creates a NURBS spline surface (rational or non rational).

    Returns: `string` The path to the new surface

    """
    pass


def surfaceSampler(*args, **kwargs):
    """
    Maps surface detail from a source surface to a new texture map on a target surface.

    Returns: None
    """
    pass


def surfaceShaderList(*args, **kwargs):
    """
    Add/Remove a relationship between an object and the current shading group.

    Returns: None
    """
    pass


def swatchDisplayPort(*args, **kwargs):
    """
    This command creates a 3dPort that displays a swatch representing the shading node.

    Returns: `string` - the name of the port created or modified

    """
    pass


def swatchRefresh(*args, **kwargs):
    """
    The  command causes image source node swatches to be refreshed on screen.

    Returns: `boolean` true if all arguments are valid image source nodes and the operation succeded.

    """
    pass


def switchTable(*args, **kwargs):
    """
    This command creates/edits/queries the switch table control.

    Returns: `string` The name of the switch table control.

    """
    pass


def symbolButton(*args, **kwargs):
    """
    This command creates a symbol button.

    Returns: `string` Full path name to the control.

    """
    pass


def symbolCheckBox(*args, **kwargs):
    """
    This command creates a symbol check box.

    Returns: `string` Full path name to the control.

    """
    pass


def symmetricModelling(*args, **kwargs):
    """
    This command allows you to change the symmetric modelling options.

    Returns: None
    """
    pass


def sysFile(*args, **kwargs):
    """
    This command provides a system independent way to create a directory or to rename or delete a file.

    Returns: `boolean` True if successful, false otherwise.

    """
    pass


def tabLayout(*args, **kwargs):
    """
    This command creates a tab group.

    Returns: `string` Full path name to the control.

    """
    pass


def tangentConstraint(*args, **kwargs):
    """
    Constrain an object's orientation based on the tangent of the target curve[s] at the closest point[s] to the object.

    Returns: `string[]` Name of the created constraint node

    """
    pass


def targetWeldCtx(*args, **kwargs):
    """
    Create a new context to weld vertices together on a poly object.

    Returns: None
    """
    pass


def tension(*args, **kwargs):
    """
    This command is used to create, edit and query tension nodes.

    Returns: `string` Tension deformer node name

    """
    pass


def texCutContext(*args, **kwargs):
    """
    This command creates a context for cut uv tool.

    Returns: `float` Size of the brush rung, when querying brushSize

    `float` The value of the edge selection sensitivity, when querying the edgeSelectSensitive flag.

    `boolean` Whether steady stroke is on or not, when querying the steadyStroke flag.

    `float` The distance for a steady stroke, when querying the steadyStrokeDistance flag.

    `float` The cut open ratio relative to edge length, when querying the moveRatio flag.

    `string` The type of effect the brush will perform, when querying the mode flag.

    `boolean` Whether shell borders are displayed, when querying the displayShellBorders flag.

    `boolean` Current touch-to-sew mode, when querying the touchToSew flag.

    """
    pass


def texLatticeDeformContext(*args, **kwargs):
    """
    This command creates a context which may be used to deform UV maps with lattice manipulator.

    Returns: `int` Number of column divisions, when querying the latticeColumns flag.

    `int` Number of row divisions, when querying the latticeRows flag.

    `float` Value of the deform envelope, when querying the envelope flag.

    `boolean` Whether snapping to pixels is on, when querying the snapPixelMode flag.

    `boolean` Whether the bounding rectangle is to be used for deforemation, when querying the useBoundingRect flag.

    """
    pass


def texManipContext(*args, **kwargs):
    """
    Command used to register the texSelectCtx tool.

    Returns: `string` : name of the context created

    `string` : name of the context created

    """
    pass


def texMoveContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a texture editor move manip context.

    Returns: `string` (the name of the new context)

    """
    pass


def texMoveUVShellContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a texture editor move manip context.

    Returns: `string` (the name of the new context)

    """
    pass


def texRotateContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a rotate context for the UV Editor.

    Returns: `string` : name of the context created

    """
    pass


def texScaleContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a scale context for the UV Editor.

    Returns: `string` : name of the context created

    """
    pass


def texSculptCacheContext(*args, **kwargs):
    """
    This is a tool context command for uv cache sculpting tool.

    Returns: None
    """
    pass


def texSelectContext(*args, **kwargs):
    """
    Command used to register the texSelectCtx tool.

    Returns: `string` : name of the context created

    """
    pass


def texSelectShortestPathCtx(*args, **kwargs):
    """
    Creates a new context to select shortest edge path between two vertices or UVs in the texture editor window.

    Returns: None
    """
    pass


def texSmudgeUVContext(*args, **kwargs):
    """
    This command creates a context for smudge UV tool.

    Returns: `string` Name of the effect type created.

    """
    pass


def texTweakUVContext(*args, **kwargs):
    """
    This command can be used to create, edit, or query a texture editor move manip context.

    Returns: `string` (the name of the new context)

    """
    pass


def texWinToolCtx(*args, **kwargs):
    """
    This class creates a context for the View Tools "track", "dolly", and "box zoom" in the texture window.

    Returns: `string` Context name

    """
    pass


def text(*args, **kwargs):
    """
    Create a simple text label control.

    Returns: `string` Full path name to the control.

    """
    pass


def textCurves(*args, **kwargs):
    """
    The textCurves command creates NURBS curves from a text string using the specified font.

    Returns: `string[]` Object name and node name

    """
    pass


def textField(*args, **kwargs):
    """
    Create a text field control.

    Returns: `string` Full path name to the control.

    """
    pass


def textFieldButtonGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def textFieldGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def textManip(*args, **kwargs):
    """
    Shows/hides the text manip.

    Returns: None
    """
    pass


def textScrollList(*args, **kwargs):
    """
    This command creates/edits/queries a text scrolling list.

    Returns: `string` Full path name to the control.

    """
    pass


def textureDeformer(*args, **kwargs):
    """
    This command creates a texture deformer for the object.

    Returns: `string` Texture deformer node name

    """
    pass


def texturePlacementContext(*args, **kwargs):
    """
    Create a command for creating new texture placement contexts.

    Returns: `string` The name of the context created

    """
    pass


def textureWindow(*args, **kwargs):
    """
    This command is used to create a UV Editor and to query or edit the texture editor settings.

    Returns: `string` The name of the texture window

    """
    pass


def threadCount(*args, **kwargs):
    """
    This command sets the number of threads to be used by Maya in regions of code that are multithreaded.

    Returns: None
    """
    pass


def threePointArcCtx(*args, **kwargs):
    """
    The threePointArcCtx command creates a new context for creating 3 point arcs.

    Returns: `string` (name of the new context)

    """
    pass


def thumbnailCaptureComponent(*args, **kwargs):
    """
    This command is used to generate a thumbnail/playblast sequence from the scene.

    Returns: None
    """
    pass


def timeCode(*args, **kwargs):
    """
    Use this command to query and set the time code information in the file.

    Returns: `time` values

    """
    pass


def timeControl(*args, **kwargs):
    """
    This command creates a control that can be used for changing current time, displaying/editing keys, and displaying/scrubbing sound.

    Returns: `string` Name of created or edited control

    """
    pass


def timeEditor(*args, **kwargs):
    """
    General Time Editor commands.

    Returns: `string` Command result

    """
    pass


def timeEditorAnimSource(*args, **kwargs):
    """
    Commands for managing animation sources.

    Returns: `string` Command result

    """
    pass


def timeEditorBakeClips(*args, **kwargs):
    """
    This command is used to bake Time Editor clips and to blend them into a single clip.

    Returns: `int` Command result

    """
    pass


def timeEditorClip(*args, **kwargs):
    """
    This command edits/queries Time Editor clips.

    Returns: `string` Return created clip's name.

    """
    pass


def timeEditorClipLayer(*args, **kwargs):
    """
    Time Editor clip layers commands.

    Returns: `string` Command result

    """
    pass


def timeEditorClipOffset(*args, **kwargs):
    """
    This command is used to compute an offset to apply on a source clip in order to automatically align it to a destination clip at a specified match element.

    Returns: None
    """
    pass


def timeEditorComposition(*args, **kwargs):
    """
    Commands related to composition management inside Time Editor.

    Returns: `string` Return values currently not documented.

    """
    pass


def timeEditorPanel(*args, **kwargs):
    """
    Time Editor - non-linear animation editor.

    Returns: `string` Command result

    """
    pass


def timeEditorTracks(*args, **kwargs):
    """
    Time Editor tracks commands.

    Returns: `Int` In edit mode, return the newly created Track index.

    """
    pass


def timeField(*args, **kwargs):
    """
    Create a field control that accepts only time values.

    Returns: `string` Full path name to the control.

    """
    pass


def timeFieldGrp(*args, **kwargs):
    """
    All of the group commands position their individual controls in columns starting at column 1.

    Returns: `string` Full path name to the control.

    """
    pass


def timePort(*args, **kwargs):
    """
    This command creates a simple time control widget.

    Returns: `string` Widget name

    """
    pass


def timeWarp(*args, **kwargs):
    """
    This command is used to create a time warp input to a set of animation curves.

    Returns: `string` timeWarp name

    """
    pass


def timer(*args, **kwargs):
    """
    Allow simple timing of scripts and commands.

    Returns: None
    """
    pass


def timerX(*args, **kwargs):
    """
    Used to calculate elapsed time.

    Returns: `float` This command returns a different value depending on the flag used. If no flag is used, then the start time is returned. If the "-st" flag is used, then it returns the elapsed time since the start time.

    """
    pass


def toggle(*args, **kwargs):
    """
    The toggle command is used to toggle the display of various object features for objects which have these components.

    Returns: `boolean` when in the query mode. none otherwise.

    """
    pass


def toggleAxis(*args, **kwargs):
    """
    Toggles the state of the display axis.

    Returns: `boolean` if in the query mode, otherwise none.

    """
    pass


def toggleDisplacement(*args, **kwargs):
    """
    This command toggles the displacement preview of the polygon.

    Returns: None
    """
    pass


def toggleWindowVisibility(*args, **kwargs):
    """
    Toggle the visibility of a window.

    Returns: None
    """
    pass


def tolerance(*args, **kwargs):
    """
    This command sets tolerances used by modelling operations that require a tolerance, such as surface fillet.

    Returns: None
    """
    pass


def toolBar(*args, **kwargs):
    """
    Create a toolbar.

    Returns: `string` Full path name to the control.

    """
    pass


def toolButton(*args, **kwargs):
    """
    This command creates a toolButton that is added to the most recently created tool button collection unless the  flag is used.

    Returns: `string` The name of the toolButton created.

    """
    pass


def toolCollection(*args, **kwargs):
    """
    This command creates a tool button collection.

    Returns: `string` The name of the toolCollection created.

    """
    pass


def toolDropped(*args, **kwargs):
    """
    This command builds and executes the commands necessary to recreate the specified tool button.

    Returns: None
    """
    pass


def toolHasOptions(*args, **kwargs):
    """
    This command queries a tool to see if it has options.

    Returns: `boolean` True if the queried tool has options, otherwise false.

    """
    pass


def toolPropertyWindow(*args, **kwargs):
    """
    End users should only call this command as 1.

    Returns: None
    """
    pass


def torus(*args, **kwargs):
    """
    The torus command creates a new torus and/or a dependency node that creates one, and returns their names.

    Returns: `string[]` Object name and node name

    """
    pass


def track(*args, **kwargs):
    """
    The track command translates a camera horizontally or vertically in the world space.

    Returns: None
    """
    pass


def trackCtx(*args, **kwargs):
    """
    This command can be used to create a track context.

    Returns: `string` The name of the context

    """
    pass


def transferAttributes(*args, **kwargs):
    """
    Samples the attributes of a source surface (first argument) and transfers them onto a target surface (second argument).

    Returns: `string` The node name.

    """
    pass


def transferShadingSets(*args, **kwargs):
    """
    Command to transfer shading set assignments between meshes.

    Returns: None
    """
    pass


def transformCompare(*args, **kwargs):
    """
    Compares two transforms passed as arguments.

    Returns: `int` 0 if successful, 1 if transform1 and transform2 are not determined to be equal.

    """
    pass


def transformLimits(*args, **kwargs):
    """
    The transformLimits command allows us to set, edit, or query the limits of the transformation that can be applied to objects.

    Returns: None
    """
    pass


def translator(*args, **kwargs):
    """
    Set or query parameters associated with the file translators specified in as the argument.

    Returns: `boolean` or string array depending upon which flags are specified.

    """
    pass


def treeLister(*args, **kwargs):
    """
    This command creates/edits/queries the tree lister control.

    Returns: `string` The name of the created control.

    """
    pass


def treeView(*args, **kwargs):
    """
    This command creates a custom control.

    Returns: `string` The full name of the control.

    """
    pass


def trim(*args, **kwargs):
    """
    This command trims a surface to its curves on surface by first splitting the surface and then selecting which regions to keep or discard.

    Returns: `string[]` Object name and node name.

    """
    pass


def truncateFluidCache(*args, **kwargs):
    """
    This command sets the end time of a fluid cache to the current time.

    Returns: None
    """
    pass


def truncateHairCache(*args, **kwargs):
    """
    This command sets the end time of a hair cache to the current time.

    Returns: None
    """
    pass


def tumble(*args, **kwargs):
    """
    The tumble command revolves the camera(s) by varying the azimuth and elevation angles in the perspective window.

    Returns: None
    """
    pass


def tumbleCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a tumble context.

    Returns: `string` The name of the context

    """
    pass


def turbulence(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def twoPointArcCtx(*args, **kwargs):
    """
    The twoPointArcCtx command creates a new context for creating two point circular arcs.

    Returns: `string` Name of the new context

    """
    pass


def ubercam(*args, **kwargs):
    """
    Use this command to create a "ubercam" with equivalent behavior to all cameras used by shots in the sequencer.

    Returns: `string` Ubercam name

    """
    pass


def uiTemplate(*args, **kwargs):
    """
    This command creates a new command template object.

    Returns: `string` The name of the uiTemplate created.

    """
    pass


def unassignInputDevice(*args, **kwargs):
    """
    This command deletes all command strings associated with this device.

    Returns: None
    """
    pass


def undo(*args, **kwargs):
    """
    Takes the most recent command from the undo list and undoes it.

    Returns: None
    """
    pass


def undoInfo(*args, **kwargs):
    """
    This command controls the undo/redo parameters.

    Returns: `string` If querying undoName or redoName

    `int` If querying state, infinity, or length

    """
    pass


def unfold(*args, **kwargs):
    """
    None.

    Returns: `int` the number of relaxation iterations carried out

    """
    pass


def ungroup(*args, **kwargs):
    """
    This command ungroups the specified objects.

    Returns: None
    """
    pass


def uniform(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def unknownNode(*args, **kwargs):
    """
    Allows querying of the data stored for unknown nodes (nodes that are defined by a plug-in that Maya could not load when loading a scene file).

    Returns: `string[]` in query mode

    """
    pass


def unknownPlugin(*args, **kwargs):
    """
    Allows querying of the unknown plug-ins used by the scene, and provides a means to remove them.

    Returns: `string[]` in query mode

    """
    pass


def unloadPlugin(*args, **kwargs):
    """
    Unload plug-ins from Maya.

    Returns: `string[]` the internal names of the successfully unloaded plug-ins

    """
    pass


def untangleUV(*args, **kwargs):
    """
    This command will aid in the creation of non-overlapping regions (i.

    Returns: `int` the number of relaxation iterations carried out

    """
    pass


def untrim(*args, **kwargs):
    """
    Untrim the surface.

    Returns: `string[]` Object name and node name

    """
    pass


def upAxis(*args, **kwargs):
    """
    The upAxis command changes the world up direction.

    Returns: None
    """
    pass


def uvLink(*args, **kwargs):
    """
    This command is used to make, break and query UV linking relationships between UV sets on objects and textures that use those UV sets.

    Returns: `string` or array of strings for query boolean for isValid

    """
    pass


def uvSnapshot(*args, **kwargs):
    """
    Builds an image containg the UVs of the selected objects.

    Returns: None
    """
    pass


def vectorize(*args, **kwargs):
    """
    This command renders Maya scenes to various vector and raster formats using the Maya Vector renderer.

    Returns: None
    """
    pass


def view2dToolCtx(*args, **kwargs):
    """
    This class creates a context for the View Tools "track", "dolly", and "box zoom" in the Hypergraph.

    Returns: `string` The context name

    """
    pass


def viewCamera(*args, **kwargs):
    """
    The viewCamera command is used to position a camera to look directly at the side or top of another camera.

    Returns: None
    """
    pass


def viewClipPlane(*args, **kwargs):
    """
    The viewClipPlane command can be used to query or set a camera's clip planes.

    Returns: None
    """
    pass


def viewFit(*args, **kwargs):
    """
    The viewFit command positions the specified camera so its point-of-view contains all selected objects other than itself.

    Returns: None
    """
    pass


def viewHeadOn(*args, **kwargs):
    """
    The viewHeadOn command positions the specified camera so it is looking "down" the normal of the live object, and fitted to the live object.

    Returns: None
    """
    pass


def viewLookAt(*args, **kwargs):
    """
    The viewLookAt command positions the specified camera so it is looking at the centroid of all selected objects.

    Returns: None
    """
    pass


def viewManip(*args, **kwargs):
    """
    Mel access to the view cube manipulator.

    Returns: None
    """
    pass


def viewPlace(*args, **kwargs):
    """
    This command positions the camera as specified.

    Returns: None
    """
    pass


def viewSet(*args, **kwargs):
    """
    This command positions the camera to one of the pre-defined positions.

    Returns: None
    """
    pass


def visor(*args, **kwargs):
    """
    Command for the creation and manipulation of a Visor UI element.

    Returns: `string` Command result

    """
    pass


def volumeAxis(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def volumeBind(*args, **kwargs):
    """
    Command for creating and editing volume binding nodes.

    Returns: `string[]` List of queried influences

    """
    pass


def vortex(*args, **kwargs):
    """
    For each listed object, the command creates a new field.

    Returns: `string` Command result

    """
    pass


def waitCursor(*args, **kwargs):
    """
    This command sets/resets a wait cursor for the entire Maya application.

    Returns: `boolean` True if the wait cursor is on.

    """
    pass


def walkCtx(*args, **kwargs):
    """
    This command can be used to create, edit, or query a walk context.

    Returns: `string` The name of the context

    """
    pass


def warning(*args, **kwargs):
    """
    The warning command is provided so that the user can issue warning messages from his/her scripts.

    Returns: None
    """
    pass


def webBrowser(*args, **kwargs):
    """
    This command is obsolete and will be removed in next version of Maya.

    Returns: `string` Full path name to the control

    """
    pass


def webView(*args, **kwargs):
    """
    This command allows the user to bring up a web page view.

    Returns: None
    """
    pass


def whatsNewHighlight(*args, **kwargs):
    """
    This command is used to toggle the What's New highlighting feature, and the display of the settings dialog for the feature that appears on startup.

    Returns: None
    """
    pass


def window(*args, **kwargs):
    """
    This command creates a new window but leaves it invisible.

    Returns: `string` Name to the window.

    """
    pass


def windowPref(*args, **kwargs):
    """
    Create or modify preferred window attributes.

    Returns: None
    """
    pass


def wire(*args, **kwargs):
    """
    This command creates a wire deformer.

    Returns: `string[]` The wire node name and the wire curve name

    """
    pass


def wireContext(*args, **kwargs):
    """
    This command creates a tool that can be used to create a wire deformer.

    Returns: `string` The name of the context created

    """
    pass


def workspace(*args, **kwargs):
    """
    Create, open, or edit a workspace associated with a given workspace file.

    Returns: `string` Project short name when querying the 'shortName' flag.

    `string` Project full name when querying the 'fullName' flag.

    `string` Current workspace name when querying the 'openWorkspace' flag and there is a current one.

    `string` Working space directory when querying the 'directory' flag.

    `string` File rule on the current workspace when querying one of the 'renderTypeEntry', 'fileRuleEntry', or 'objectTypeEntry' flags.

    `string` File rule on the current workspace when querying the 'variableEntry' flag.

    `string` Resolved full name of the given file name, or the current root directory if no name given when querying the 'expandName' flag.

    `string` Path to the current project workspace when querying the 'projectPath' flag.

    `string` Current workspace's base workspace name when querying the 'baseWorkspace' flag.

    `string` Current workspace's root directory when querying the 'rootDirectory' flag.

    `string[]` List of file rules when querying the 'fileRule' flag.

    `string[]` List of variables when querying the 'variableList' flag.

    `string[]` List of all workspaces when querying the 'listWorkspaces' flag.

    `string[]` List of full names of all workspaces when querying the 'listFullWorkspaces' flag.

    `string[]` List of path names for all workspace in the directory named when querying the 'list' flag or the current workspace if no directory is named.

    `string[]` List of alternating (file rule, rule location) strings corresponding to the current workspace's file rules.

    `string[]` List of alternating (variable, value) strings corresponding to the current workspace's variables.

    """
    pass


def workspaceControl(*args, **kwargs):
    """
    Creates and manages the widget used to host windows in a layout that enables docking and stacking windows together.

    Returns: `string` Full path name to the control.

    """
    pass


def workspaceControlState(*args, **kwargs):
    """
    Create or modify preferred window attributes for workspace controls.

    Returns: None
    """
    pass


def workspaceLayoutManager(*args, **kwargs):
    """
    The Workspace Layout Manager loads and saves the layout of the various toolbars and windows in the user interface.

    Returns: `string[]` depending on arguments

    """
    pass


def workspacePanel(*args, **kwargs):
    """
    Workspace panel.

    Returns: `string` Full path name to the workspace panel.

    """
    pass


def wrinkle(*args, **kwargs):
    """
    The wrinkle command is used to create a network of wrinkles on a surface.

    Returns: `string[]` List of clusters created followed by list of wire deformers created.

    """
    pass


def wrinkleContext(*args, **kwargs):
    """
    This command creates a context that creates wrinkles.

    Returns: `string` The name of the context created

    """
    pass


def writeTake(*args, **kwargs):
    """
    This action writes a take from a device with recorded data to a take (.

    Returns: None
    """
    pass


def xform(*args, **kwargs):
    """
    This command can be used query/set any element in a transformation node.

    Returns: None
    """
    pass


def xformConstraint(*args, **kwargs):
    """
    This command allows you to change the transform constraint used by the transform tools during component transforms.

    Returns: None
    """
    pass


def xpmPicker(*args, **kwargs):
    """
    Open a dialog and ask you to choose a xpm file.

    Returns: `string` The full name of the xpm file

    """
    pass

