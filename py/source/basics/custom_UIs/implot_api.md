# ImPlot API Reference

All functions are in the `polyscope.implot` namespace. Please see the [ImPlot project](https://www.github.com/epezent/implot) for full documentation of ImPlot functions and features.

These Python bindings are a 1:1 mapping of the C++ ImPlot API, with concessions only for syntax that is not possible in Python. For example, C++ functions that take pointers and modify their arguments in-place instead return a Python tuple of `(is_changed, new_value)`.

See [here for an example UI]([[url.prefix]]/basics/interactive_UIs_and_animation/#sample-custom-ui).

## Functions

```python
BeginPlot(
    title_id: str,
    size: tuple[float, float] = (-1.0, 0.0),
    flags: int = 0,
    ) -> bool
EndPlot() -> None
BeginSubplots(
    title_id: str,
    rows: int,
    cols: int,
    size: tuple[float, float] = (-1.0, 0.0),
    flags: int = 0,
    row_ratios: Sequence[float] = [],
    col_ratios: Sequence[float] = [],
    ) -> bool
EndSubplots() -> None
SetupAxis(
    axis: int,
    label: str = '',
    flags: int = 0,
    ) -> None
SetupAxisLimits(
    axis: int,
    vmin: float,
    vmax: float,
    cond: int = 2,
    ) -> None
SetupAxisFormat(
    axis: int,
    fmt: str,
    ) -> None
SetupAxisTicks(
    axis: int,
    values: NDArray[numpy.float64],
    labels: Sequence[str] = [],
    keep_default: bool = False,
    ) -> None
SetupAxisTicks(
    axis: int,
    v_min: float,
    v_max: float,
    n_ticks: int,
    labels: Sequence[str] = [],
    keep_default: bool = False,
    ) -> None
SetupAxisScale(
    axis: int,
    scale: int,
    ) -> None
SetupAxisLimitsConstraints(
    axis: int,
    v_min: float,
    v_max: float,
    ) -> None
SetupAxisZoomConstraints(
    axis: int,
    z_min: float,
    z_max: float,
    ) -> None
SetupAxes(
    x_label: str,
    y_label: str,
    x_flags: int = 0,
    y_flags: int = 0,
    ) -> None
SetupAxesLimits(
    x_min: float,
    x_max: float,
    y_min: float,
    y_max: float,
    cond: int = 2,
    ) -> None
SetupLegend(
    location: int,
    flags: int = 0,
    ) -> None
SetupMouseText(
    location: int,
    flags: int = 0,
    ) -> None
SetupFinish() -> None
PlotLine(
    label_id: str,
    values: NDArray[numpy.float64],
    xscale: float = 1.0,
    xstart: float = 0.0,
    flags: int = 0,
    ) -> None
PlotLine(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotScatter(
    label_id: str,
    values: NDArray[numpy.float64],
    xscale: float = 1.0,
    xstart: float = 0.0,
    flags: int = 0,
    ) -> None
PlotScatter(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotStairs(
    label_id: str,
    values: NDArray[numpy.float64],
    xscale: float = 1.0,
    xstart: float = 0.0,
    flags: int = 0,
    ) -> None
PlotStairs(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotShaded(
    label_id: str,
    values: NDArray[numpy.float64],
    yref: float = 0.0,
    xscale: float = 1.0,
    xstart: float = 0.0,
    flags: int = 0,
    ) -> None
PlotShaded(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    yref: float = 0.0,
    flags: int = 0,
    ) -> None
PlotShaded(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys1: NDArray[numpy.float64],
    ys2: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotBars(
    label_id: str,
    values: NDArray[numpy.float64],
    bar_size: float = 0.67,
    shift: float = 0.0,
    flags: int = 0,
    ) -> None
PlotBars(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    bar_size: float,
    flags: int = 0,
    ) -> None
PlotBarGroups(
    label_ids: Sequence[str],
    values: NDArray[numpy.float64],
    group_size: float = 0.67,
    shift: float = 0.0,
    flags: int = 0,
    ) -> None
PlotErrorBars(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    err: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotErrorBars(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    neg: NDArray[numpy.float64],
    pos: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotStems(
    label_id: str,
    values: NDArray[numpy.float64],
    ref: float = 0.0,
    scale: float = 1.0,
    start: float = 0.0,
    flags: int = 0,
    ) -> None
PlotStems(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    ref: float = 0.0,
    flags: int = 0,
    ) -> None
PlotInfLines(
    label_id: str,
    values: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotPieChart(
    label_ids: Sequence[str],
    values: NDArray[numpy.float64],
    x: float,
    y: float,
    radius: float,
    label_fmt: str = '%.1f',
    angle0: float = 90,
    flags: int = 0,
    ) -> None
PlotHeatmap(
    label_id: str,
    values: NDArray[numpy.float64],
    scale_min: float = 0.0,
    scale_max: float = 0.0,
    label_fmt: str = '%.1f',
    bounds_min: tuple[float, float] = (0.0, 0.0),
    bounds_max: tuple[float, float] = (1.0, 1.0),
    flags: int = 0,
    ) -> None
PlotHistogram(
    label_id: str,
    values: NDArray[numpy.float64],
    bins: int = -2,
    bar_scale: float = 1.0,
    range: tuple[float, float] = (0.0, 0.0),
    flags: int = 0,
    ) -> None
PlotHistogram2D(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    x_bins: int = -2,
    y_bins: int = -2,
    range: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0),
    flags: int = 0,
    ) -> None
PlotDigital(
    label_id: str,
    xs: NDArray[numpy.float64],
    ys: NDArray[numpy.float64],
    flags: int = 0,
    ) -> None
PlotImage(
    label_id: str,
    tex_ref: int,
    bounds_min: tuple[float, float],
    bounds_max: tuple[float, float],
    uv0: tuple[float, float] = (0.0, 0.0),
    uv1: tuple[float, float] = (1.0, 1.0),
    tint_col: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
    flags: int = 0,
    ) -> None
PlotText(
    text: str,
    x: float,
    y: float,
    pix_offset: tuple[float, float] = (0.0, 0.0),
    flags: int = 0,
    ) -> None
PlotDummy(
    label_id: str,
    flags: int = 0,
    ) -> None
DragPoint(
    id: int,
    x: float,
    y: float,
    col: tuple[float, float, float, float],
    size: float = 4.0,
    flags: int = 0,
    ) -> tuple[bool, float, float]
DragLineX(
    id: int,
    x: float,
    col: tuple[float, float, float, float],
    thickness: float = 1.0,
    flags: int = 0,
    ) -> tuple[bool, float]
DragLineY(
    id: int,
    y: float,
    col: tuple[float, float, float, float],
    thickness: float = 1.0,
    flags: int = 0,
    ) -> tuple[bool, float]
DragRect(
    id: int,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    col: tuple[float, float, float, float],
    flags: int = 0,
    ) -> tuple[bool, float, float, float, float]
Annotation(
    x: float,
    y: float,
    col: tuple[float, float, float, float],
    pix_offset: tuple[float, float],
    clamp: bool,
    round: bool = False,
    ) -> None
Annotation(
    x: float,
    y: float,
    col: tuple[float, float, float, float],
    pix_offset: tuple[float, float],
    clamp: bool,
    text: str,
    ) -> None
TagX(
    x: float,
    col: tuple[float, float, float, float],
    round: bool = False,
    ) -> None
TagX(
    x: float,
    col: tuple[float, float, float, float],
    text: str,
    ) -> None
TagY(
    y: float,
    col: tuple[float, float, float, float],
    round: bool = False,
    ) -> None
TagY(
    y: float,
    col: tuple[float, float, float, float],
    text: str,
    ) -> None
SetAxis(axis: int) -> None
SetAxes(
    x_axis: int,
    y_axis: int,
    ) -> None
PixelsToPlot(
    pix: tuple[float, float],
    x_axis: int = -1,
    y_axis: int = -1,
    ) -> tuple[float, float]
PixelsToPlot(
    x: float,
    y: float,
    x_axis: int = -1,
    y_axis: int = -1,
    ) -> tuple[float, float]
PlotToPixels(
    plt: tuple[float, float],
    x_axis: int = -1,
    y_axis: int = -1,
    ) -> tuple[float, float]
PlotToPixels(
    x: float,
    y: float,
    x_axis: int = -1,
    y_axis: int = -1,
    ) -> tuple[float, float]
GetPlotPos() -> tuple[float, float]
GetPlotSize() -> tuple[float, float]
GetPlotMousePos(
    x_axis: int = -1,
    y_axis: int = -1,
    ) -> tuple[float, float]
GetPlotLimits(
    x_axis: int = -1,
    y_axis: int = -1,
    ) -> tuple[float, float, float, float]
IsPlotHovered() -> bool
IsAxisHovered(axis: int) -> bool
IsSubplotsHovered() -> bool
IsPlotSelected() -> bool
GetPlotSelection(
    x_axis: int = -1,
    y_axis: int = -1,
    ) -> tuple[float, float, float, float]
CancelPlotSelection() -> None
HideNextItem(
    hidden: bool = True,
    cond: int = 2,
    ) -> None
BeginAlignedPlots(
    group_id: str,
    vertical: bool = True,
    ) -> bool
EndAlignedPlots() -> None
BeginLegendPopup(
    label_id: str,
    mouse_button: int = 1,
    ) -> bool
EndLegendPopup() -> None
IsLegendEntryHovered(label_id: str) -> bool
BeginDragDropTargetPlot() -> bool
BeginDragDropTargetAxis(axis: int) -> bool
BeginDragDropTargetLegend() -> bool
EndDragDropTarget() -> None
BeginDragDropSourcePlot(flags: int = 0) -> bool
BeginDragDropSourceAxis(
    axis: int,
    flags: int = 0,
    ) -> bool
BeginDragDropSourceItem(
    label_id: str,
    flags: int = 0,
    ) -> bool
EndDragDropSource() -> None
GetStyle() -> ImPlotStyle
StyleColorsAuto(dst: ImPlotStyle | None = None) -> None
StyleColorsClassic(dst: ImPlotStyle | None = None) -> None
StyleColorsDark(dst: ImPlotStyle | None = None) -> None
StyleColorsLight(dst: ImPlotStyle | None = None) -> None
PushStyleColor(
    idx: int,
    col: int,
    ) -> None
PushStyleColor(
    idx: int,
    col: tuple[float, float, float, float],
    ) -> None
PopStyleColor(count: int = 1) -> None
PushStyleVar(
    idx: int,
    val: float,
    ) -> None
PushStyleVar(
    idx: int,
    val: int,
    ) -> None
PushStyleVar(
    idx: int,
    val: tuple[float, float],
    ) -> None
PopStyleVar(count: int = 1) -> None
SetNextLineStyle(
    col: tuple[float, float, float, float] = (0.0, 0.0, 0.0, -1.0),
    weight: float = -1.0,
    ) -> None
SetNextFillStyle(
    col: tuple[float, float, float, float] = (0.0, 0.0, 0.0, -1.0),
    alpha_mod: float = -1.0,
    ) -> None
SetNextMarkerStyle(
    marker: int = -1,
    size: float = -1.0,
    fill: tuple[float, float, float, float] = (0.0, 0.0, 0.0, -1.0),
    weight: float = -1.0,
    outline: tuple[float, float, float, float] = (0.0, 0.0, 0.0, -1.0),
    ) -> None
SetNextErrorBarStyle(
    col: tuple[float, float, float, float] = (0.0, 0.0, 0.0, -1.0),
    size: float = -1.0,
    weight: float = -1.0,
    ) -> None
GetLastItemColor() -> tuple[float, float, float, float]
GetStyleColorName(idx: int) -> str
GetMarkerName(idx: int) -> str
AddColormap(
    name: str,
    cols: Sequence[tuple[float, float, float, float]],
    qual: bool = True,
    ) -> int
GetColormapCount() -> int
GetColormapName(cmap: int) -> str
GetColormapIndex(name: str) -> int
PushColormap(cmap: int) -> None
PushColormap(name: str) -> None
PopColormap(count: int = 1) -> None
NextColormapColor() -> tuple[float, float, float, float]
GetColormapSize(cmap: int = -1) -> int
GetColormapColor(
    idx: int,
    cmap: int = -1,
    ) -> tuple[float, float, float, float]
SampleColormap(
    t: float,
    cmap: int = -1,
    ) -> tuple[float, float, float, float]
ColormapScale(
    label: str,
    scale_min: float,
    scale_max: float,
    size: tuple[float, float] = (0.0, 0.0),
    format: str = '%g',
    flags: int = 0,
    cmap: int = -1,
    ) -> None
ColormapSlider(
    label: str,
    t: float,
    format: str = '',
    cmap: int = -1,
    ) -> tuple[bool, float, tuple[float, float, float, float]]
ColormapButton(
    label: str,
    size: tuple[float, float] = (0.0, 0.0),
    cmap: int = -1,
    ) -> bool
BustColorCache(plot_title_id: str | None = None) -> None
GetInputMap() -> ImPlotInputMap
MapInputDefault(dst: ImPlotInputMap | None = None) -> None
MapInputReverse(dst: ImPlotInputMap | None = None) -> None
ItemIcon(col: tuple[float, float, float, float]) -> None
ItemIcon(col: int) -> None
ColormapIcon(cmap: int) -> None
GetPlotDrawList() -> polyscope_bindings.imgui.ImDrawList
PushPlotClipRect(expand: float = 0.0) -> None
PopPlotClipRect() -> None
ShowStyleSelector(label: str) -> bool
ShowColormapSelector(label: str) -> bool
ShowInputMapSelector(label: str) -> bool
ShowStyleEditor(ref: ImPlotStyle | None = None) -> None
ShowUserGuide() -> None
ShowMetricsWindow(p_open: bool = True) -> bool
```

## Classes

### ImPlotStyle

**Properties:**

```python
LineWeight: float
Marker: int
MarkerSize: float
MarkerWeight: float
FillAlpha: float
ErrorBarSize: float
ErrorBarWeight: float
DigitalBitHeight: float
DigitalBitGap: float
PlotBorderSize: float
MinorAlpha: float
MajorTickLen: tuple[float, float]
MinorTickLen: tuple[float, float]
MajorTickSize: tuple[float, float]
MinorTickSize: tuple[float, float]
MajorGridSize: tuple[float, float]
MinorGridSize: tuple[float, float]
PlotPadding: tuple[float, float]
LabelPadding: tuple[float, float]
LegendPadding: tuple[float, float]
LegendInnerPadding: tuple[float, float]
LegendSpacing: tuple[float, float]
MousePosPadding: tuple[float, float]
AnnotationPadding: tuple[float, float]
FitPadding: tuple[float, float]
PlotDefaultSize: tuple[float, float]
PlotMinSize: tuple[float, float]
Colormap: int
UseLocalTime: bool
UseISO8601: bool
Use24HourClock: bool
```

**Methods:**

```python
GetColor(idx: int) -> tuple[float, float, float, float]
SetColor(
    idx: int,
    color: tuple[float, float, float, float],
    ) -> None
GetColorCount() -> int
```

### ImPlotInputMap

**Properties:**

```python
Pan: int
PanMod: int
Fit: int
Select: int
SelectCancel: int
SelectMod: int
SelectHorzMod: int
SelectVertMod: int
Menu: int
OverrideMod: int
ZoomMod: int
ZoomRate: float
```

## Enums

### ImAxis

```python
ImAxis_X1 = 0
ImAxis_X2 = 1
ImAxis_X3 = 2
ImAxis_Y1 = 3
ImAxis_Y2 = 4
ImAxis_Y3 = 5
ImAxis_COUNT = 6
```

### ImPlotFlags

```python
ImPlotFlags_None = 0
ImPlotFlags_NoTitle = 1
ImPlotFlags_NoLegend = 2
ImPlotFlags_NoMouseText = 4
ImPlotFlags_NoInputs = 8
ImPlotFlags_NoMenus = 16
ImPlotFlags_NoBoxSelect = 32
ImPlotFlags_NoFrame = 64
ImPlotFlags_Equal = 128
ImPlotFlags_Crosshairs = 256
ImPlotFlags_CanvasOnly = 55
```

### ImPlotAxisFlags

```python
ImPlotAxisFlags_None = 0
ImPlotAxisFlags_NoLabel = 1
ImPlotAxisFlags_NoGridLines = 2
ImPlotAxisFlags_NoTickMarks = 4
ImPlotAxisFlags_NoTickLabels = 8
ImPlotAxisFlags_NoInitialFit = 16
ImPlotAxisFlags_NoMenus = 32
ImPlotAxisFlags_NoSideSwitch = 64
ImPlotAxisFlags_NoHighlight = 128
ImPlotAxisFlags_Opposite = 256
ImPlotAxisFlags_Foreground = 512
ImPlotAxisFlags_Invert = 1024
ImPlotAxisFlags_AutoFit = 2048
ImPlotAxisFlags_RangeFit = 4096
ImPlotAxisFlags_PanStretch = 8192
ImPlotAxisFlags_LockMin = 16384
ImPlotAxisFlags_LockMax = 32768
ImPlotAxisFlags_Lock = 49152
ImPlotAxisFlags_NoDecorations = 15
ImPlotAxisFlags_AuxDefault = 258
```

### ImPlotSubplotFlags

```python
ImPlotSubplotFlags_None = 0
ImPlotSubplotFlags_NoTitle = 1
ImPlotSubplotFlags_NoLegend = 2
ImPlotSubplotFlags_NoMenus = 4
ImPlotSubplotFlags_NoResize = 8
ImPlotSubplotFlags_NoAlign = 16
ImPlotSubplotFlags_ShareItems = 32
ImPlotSubplotFlags_LinkRows = 64
ImPlotSubplotFlags_LinkCols = 128
ImPlotSubplotFlags_LinkAllX = 256
ImPlotSubplotFlags_LinkAllY = 512
ImPlotSubplotFlags_ColMajor = 1024
```

### ImPlotLegendFlags

```python
ImPlotLegendFlags_None = 0
ImPlotLegendFlags_NoButtons = 1
ImPlotLegendFlags_NoHighlightItem = 2
ImPlotLegendFlags_NoHighlightAxis = 4
ImPlotLegendFlags_NoMenus = 8
ImPlotLegendFlags_Outside = 16
ImPlotLegendFlags_Horizontal = 32
ImPlotLegendFlags_Sort = 64
```

### ImPlotMouseTextFlags

```python
ImPlotMouseTextFlags_None = 0
ImPlotMouseTextFlags_NoAuxAxes = 1
ImPlotMouseTextFlags_NoFormat = 2
ImPlotMouseTextFlags_ShowAlways = 4
```

### ImPlotDragToolFlags

```python
ImPlotDragToolFlags_None = 0
ImPlotDragToolFlags_NoCursors = 1
ImPlotDragToolFlags_NoFit = 2
ImPlotDragToolFlags_NoInputs = 4
ImPlotDragToolFlags_Delayed = 8
```

### ImPlotColormapScaleFlags

```python
ImPlotColormapScaleFlags_None = 0
ImPlotColormapScaleFlags_NoLabel = 1
ImPlotColormapScaleFlags_Opposite = 2
ImPlotColormapScaleFlags_Invert = 4
```

### ImPlotItemFlags

```python
ImPlotItemFlags_None = 0
ImPlotItemFlags_NoLegend = 1
ImPlotItemFlags_NoFit = 2
```

### ImPlotLineFlags

```python
ImPlotLineFlags_None = 0
ImPlotLineFlags_Segments = 1024
ImPlotLineFlags_Loop = 2048
ImPlotLineFlags_SkipNaN = 4096
ImPlotLineFlags_NoClip = 8192
ImPlotLineFlags_Shaded = 16384
```

### ImPlotScatterFlags

```python
ImPlotScatterFlags_None = 0
ImPlotScatterFlags_NoClip = 1024
```

### ImPlotStairsFlags

```python
ImPlotStairsFlags_None = 0
ImPlotStairsFlags_PreStep = 1024
ImPlotStairsFlags_Shaded = 2048
```

### ImPlotShadedFlags

```python
ImPlotShadedFlags_None = 0
```

### ImPlotBarsFlags

```python
ImPlotBarsFlags_None = 0
ImPlotBarsFlags_Horizontal = 1024
```

### ImPlotBarGroupsFlags

```python
ImPlotBarGroupsFlags_None = 0
ImPlotBarGroupsFlags_Horizontal = 1024
ImPlotBarGroupsFlags_Stacked = 2048
```

### ImPlotErrorBarsFlags

```python
ImPlotErrorBarsFlags_None = 0
ImPlotErrorBarsFlags_Horizontal = 1024
```

### ImPlotStemsFlags

```python
ImPlotStemsFlags_None = 0
ImPlotStemsFlags_Horizontal = 1024
```

### ImPlotInfLinesFlags

```python
ImPlotInfLinesFlags_None = 0
ImPlotInfLinesFlags_Horizontal = 1024
```

### ImPlotPieChartFlags

```python
ImPlotPieChartFlags_None = 0
ImPlotPieChartFlags_Normalize = 1024
ImPlotPieChartFlags_IgnoreHidden = 2048
ImPlotPieChartFlags_Exploding = 4096
```

### ImPlotHeatmapFlags

```python
ImPlotHeatmapFlags_None = 0
ImPlotHeatmapFlags_ColMajor = 1024
```

### ImPlotHistogramFlags

```python
ImPlotHistogramFlags_None = 0
ImPlotHistogramFlags_Horizontal = 1024
ImPlotHistogramFlags_Cumulative = 2048
ImPlotHistogramFlags_Density = 4096
ImPlotHistogramFlags_NoOutliers = 8192
ImPlotHistogramFlags_ColMajor = 16384
```

### ImPlotDigitalFlags

```python
ImPlotDigitalFlags_None = 0
```

### ImPlotImageFlags

```python
ImPlotImageFlags_None = 0
```

### ImPlotTextFlags

```python
ImPlotTextFlags_None = 0
ImPlotTextFlags_Vertical = 1024
```

### ImPlotDummyFlags

```python
ImPlotDummyFlags_None = 0
```

### ImPlotCond

```python
ImPlotCond_None = 0
ImPlotCond_Always = 1
ImPlotCond_Once = 2
```

### ImPlotCol

```python
ImPlotCol_Line = 0
ImPlotCol_Fill = 1
ImPlotCol_MarkerOutline = 2
ImPlotCol_MarkerFill = 3
ImPlotCol_ErrorBar = 4
ImPlotCol_FrameBg = 5
ImPlotCol_PlotBg = 6
ImPlotCol_PlotBorder = 7
ImPlotCol_LegendBg = 8
ImPlotCol_LegendBorder = 9
ImPlotCol_LegendText = 10
ImPlotCol_TitleText = 11
ImPlotCol_InlayText = 12
ImPlotCol_AxisText = 13
ImPlotCol_AxisGrid = 14
ImPlotCol_AxisTick = 15
ImPlotCol_AxisBg = 16
ImPlotCol_AxisBgHovered = 17
ImPlotCol_AxisBgActive = 18
ImPlotCol_Selection = 19
ImPlotCol_Crosshairs = 20
ImPlotCol_COUNT = 21
```

### ImPlotStyleVar

```python
ImPlotStyleVar_LineWeight = 0
ImPlotStyleVar_Marker = 1
ImPlotStyleVar_MarkerSize = 2
ImPlotStyleVar_MarkerWeight = 3
ImPlotStyleVar_FillAlpha = 4
ImPlotStyleVar_ErrorBarSize = 5
ImPlotStyleVar_ErrorBarWeight = 6
ImPlotStyleVar_DigitalBitHeight = 7
ImPlotStyleVar_DigitalBitGap = 8
ImPlotStyleVar_PlotBorderSize = 9
ImPlotStyleVar_MinorAlpha = 10
ImPlotStyleVar_MajorTickLen = 11
ImPlotStyleVar_MinorTickLen = 12
ImPlotStyleVar_MajorTickSize = 13
ImPlotStyleVar_MinorTickSize = 14
ImPlotStyleVar_MajorGridSize = 15
ImPlotStyleVar_MinorGridSize = 16
ImPlotStyleVar_PlotPadding = 17
ImPlotStyleVar_LabelPadding = 18
ImPlotStyleVar_LegendPadding = 19
ImPlotStyleVar_LegendInnerPadding = 20
ImPlotStyleVar_LegendSpacing = 21
ImPlotStyleVar_MousePosPadding = 22
ImPlotStyleVar_AnnotationPadding = 23
ImPlotStyleVar_FitPadding = 24
ImPlotStyleVar_PlotDefaultSize = 25
ImPlotStyleVar_PlotMinSize = 26
ImPlotStyleVar_COUNT = 27
```

### ImPlotScale

```python
ImPlotScale_Linear = 0
ImPlotScale_Time = 1
ImPlotScale_Log10 = 2
ImPlotScale_SymLog = 3
```

### ImPlotMarker

```python
ImPlotMarker_None = -1
ImPlotMarker_Circle = 0
ImPlotMarker_Square = 1
ImPlotMarker_Diamond = 2
ImPlotMarker_Up = 3
ImPlotMarker_Down = 4
ImPlotMarker_Left = 5
ImPlotMarker_Right = 6
ImPlotMarker_Cross = 7
ImPlotMarker_Plus = 8
ImPlotMarker_Asterisk = 9
ImPlotMarker_COUNT = 10
```

### ImPlotColormap

```python
ImPlotColormap_Deep = 0
ImPlotColormap_Dark = 1
ImPlotColormap_Pastel = 2
ImPlotColormap_Paired = 3
ImPlotColormap_Viridis = 4
ImPlotColormap_Plasma = 5
ImPlotColormap_Hot = 6
ImPlotColormap_Cool = 7
ImPlotColormap_Pink = 8
ImPlotColormap_Jet = 9
ImPlotColormap_Twilight = 10
ImPlotColormap_RdBu = 11
ImPlotColormap_BrBG = 12
ImPlotColormap_PiYG = 13
ImPlotColormap_Spectral = 14
ImPlotColormap_Greys = 15
```

### ImPlotLocation

```python
ImPlotLocation_Center = 0
ImPlotLocation_North = 1
ImPlotLocation_South = 2
ImPlotLocation_West = 4
ImPlotLocation_East = 8
ImPlotLocation_NorthWest = 5
ImPlotLocation_NorthEast = 9
ImPlotLocation_SouthWest = 6
ImPlotLocation_SouthEast = 10
```

### ImPlotBin

```python
ImPlotBin_Sqrt = -1
ImPlotBin_Sturges = -2
ImPlotBin_Rice = -3
ImPlotBin_Scott = -4
```

## Constants

```python
ImAxis_X1: int = 0
ImAxis_X2: int = 1
ImAxis_X3: int = 2
ImAxis_Y1: int = 3
ImAxis_Y2: int = 4
ImAxis_Y3: int = 5
ImAxis_COUNT: int = 6
ImPlotFlags_None: int = 0
ImPlotFlags_NoTitle: int = 1
ImPlotFlags_NoLegend: int = 2
ImPlotFlags_NoMouseText: int = 4
ImPlotFlags_NoInputs: int = 8
ImPlotFlags_NoMenus: int = 16
ImPlotFlags_NoBoxSelect: int = 32
ImPlotFlags_NoFrame: int = 64
ImPlotFlags_Equal: int = 128
ImPlotFlags_Crosshairs: int = 256
ImPlotFlags_CanvasOnly: int = 55
ImPlotAxisFlags_None: int = 0
ImPlotAxisFlags_NoLabel: int = 1
ImPlotAxisFlags_NoGridLines: int = 2
ImPlotAxisFlags_NoTickMarks: int = 4
ImPlotAxisFlags_NoTickLabels: int = 8
ImPlotAxisFlags_NoInitialFit: int = 16
ImPlotAxisFlags_NoMenus: int = 32
ImPlotAxisFlags_NoSideSwitch: int = 64
ImPlotAxisFlags_NoHighlight: int = 128
ImPlotAxisFlags_Opposite: int = 256
ImPlotAxisFlags_Foreground: int = 512
ImPlotAxisFlags_Invert: int = 1024
ImPlotAxisFlags_AutoFit: int = 2048
ImPlotAxisFlags_RangeFit: int = 4096
ImPlotAxisFlags_PanStretch: int = 8192
ImPlotAxisFlags_LockMin: int = 16384
ImPlotAxisFlags_LockMax: int = 32768
ImPlotAxisFlags_Lock: int = 49152
ImPlotAxisFlags_NoDecorations: int = 15
ImPlotAxisFlags_AuxDefault: int = 258
ImPlotSubplotFlags_None: int = 0
ImPlotSubplotFlags_NoTitle: int = 1
ImPlotSubplotFlags_NoLegend: int = 2
ImPlotSubplotFlags_NoMenus: int = 4
ImPlotSubplotFlags_NoResize: int = 8
ImPlotSubplotFlags_NoAlign: int = 16
ImPlotSubplotFlags_ShareItems: int = 32
ImPlotSubplotFlags_LinkRows: int = 64
ImPlotSubplotFlags_LinkCols: int = 128
ImPlotSubplotFlags_LinkAllX: int = 256
ImPlotSubplotFlags_LinkAllY: int = 512
ImPlotSubplotFlags_ColMajor: int = 1024
ImPlotLegendFlags_None: int = 0
ImPlotLegendFlags_NoButtons: int = 1
ImPlotLegendFlags_NoHighlightItem: int = 2
ImPlotLegendFlags_NoHighlightAxis: int = 4
ImPlotLegendFlags_NoMenus: int = 8
ImPlotLegendFlags_Outside: int = 16
ImPlotLegendFlags_Horizontal: int = 32
ImPlotLegendFlags_Sort: int = 64
ImPlotMouseTextFlags_None: int = 0
ImPlotMouseTextFlags_NoAuxAxes: int = 1
ImPlotMouseTextFlags_NoFormat: int = 2
ImPlotMouseTextFlags_ShowAlways: int = 4
ImPlotDragToolFlags_None: int = 0
ImPlotDragToolFlags_NoCursors: int = 1
ImPlotDragToolFlags_NoFit: int = 2
ImPlotDragToolFlags_NoInputs: int = 4
ImPlotDragToolFlags_Delayed: int = 8
ImPlotColormapScaleFlags_None: int = 0
ImPlotColormapScaleFlags_NoLabel: int = 1
ImPlotColormapScaleFlags_Opposite: int = 2
ImPlotColormapScaleFlags_Invert: int = 4
ImPlotItemFlags_None: int = 0
ImPlotItemFlags_NoLegend: int = 1
ImPlotItemFlags_NoFit: int = 2
ImPlotLineFlags_None: int = 0
ImPlotLineFlags_Segments: int = 1024
ImPlotLineFlags_Loop: int = 2048
ImPlotLineFlags_SkipNaN: int = 4096
ImPlotLineFlags_NoClip: int = 8192
ImPlotLineFlags_Shaded: int = 16384
ImPlotScatterFlags_None: int = 0
ImPlotScatterFlags_NoClip: int = 1024
ImPlotStairsFlags_None: int = 0
ImPlotStairsFlags_PreStep: int = 1024
ImPlotStairsFlags_Shaded: int = 2048
ImPlotShadedFlags_None: int = 0
ImPlotBarsFlags_None: int = 0
ImPlotBarsFlags_Horizontal: int = 1024
ImPlotBarGroupsFlags_None: int = 0
ImPlotBarGroupsFlags_Horizontal: int = 1024
ImPlotBarGroupsFlags_Stacked: int = 2048
ImPlotErrorBarsFlags_None: int = 0
ImPlotErrorBarsFlags_Horizontal: int = 1024
ImPlotStemsFlags_None: int = 0
ImPlotStemsFlags_Horizontal: int = 1024
ImPlotInfLinesFlags_None: int = 0
ImPlotInfLinesFlags_Horizontal: int = 1024
ImPlotPieChartFlags_None: int = 0
ImPlotPieChartFlags_Normalize: int = 1024
ImPlotPieChartFlags_IgnoreHidden: int = 2048
ImPlotPieChartFlags_Exploding: int = 4096
ImPlotHeatmapFlags_None: int = 0
ImPlotHeatmapFlags_ColMajor: int = 1024
ImPlotHistogramFlags_None: int = 0
ImPlotHistogramFlags_Horizontal: int = 1024
ImPlotHistogramFlags_Cumulative: int = 2048
ImPlotHistogramFlags_Density: int = 4096
ImPlotHistogramFlags_NoOutliers: int = 8192
ImPlotHistogramFlags_ColMajor: int = 16384
ImPlotDigitalFlags_None: int = 0
ImPlotImageFlags_None: int = 0
ImPlotTextFlags_None: int = 0
ImPlotTextFlags_Vertical: int = 1024
ImPlotDummyFlags_None: int = 0
ImPlotCond_None: int = 0
ImPlotCond_Always: int = 1
ImPlotCond_Once: int = 2
ImPlotCol_Line: int = 0
ImPlotCol_Fill: int = 1
ImPlotCol_MarkerOutline: int = 2
ImPlotCol_MarkerFill: int = 3
ImPlotCol_ErrorBar: int = 4
ImPlotCol_FrameBg: int = 5
ImPlotCol_PlotBg: int = 6
ImPlotCol_PlotBorder: int = 7
ImPlotCol_LegendBg: int = 8
ImPlotCol_LegendBorder: int = 9
ImPlotCol_LegendText: int = 10
ImPlotCol_TitleText: int = 11
ImPlotCol_InlayText: int = 12
ImPlotCol_AxisText: int = 13
ImPlotCol_AxisGrid: int = 14
ImPlotCol_AxisTick: int = 15
ImPlotCol_AxisBg: int = 16
ImPlotCol_AxisBgHovered: int = 17
ImPlotCol_AxisBgActive: int = 18
ImPlotCol_Selection: int = 19
ImPlotCol_Crosshairs: int = 20
ImPlotCol_COUNT: int = 21
ImPlotStyleVar_LineWeight: int = 0
ImPlotStyleVar_Marker: int = 1
ImPlotStyleVar_MarkerSize: int = 2
ImPlotStyleVar_MarkerWeight: int = 3
ImPlotStyleVar_FillAlpha: int = 4
ImPlotStyleVar_ErrorBarSize: int = 5
ImPlotStyleVar_ErrorBarWeight: int = 6
ImPlotStyleVar_DigitalBitHeight: int = 7
ImPlotStyleVar_DigitalBitGap: int = 8
ImPlotStyleVar_PlotBorderSize: int = 9
ImPlotStyleVar_MinorAlpha: int = 10
ImPlotStyleVar_MajorTickLen: int = 11
ImPlotStyleVar_MinorTickLen: int = 12
ImPlotStyleVar_MajorTickSize: int = 13
ImPlotStyleVar_MinorTickSize: int = 14
ImPlotStyleVar_MajorGridSize: int = 15
ImPlotStyleVar_MinorGridSize: int = 16
ImPlotStyleVar_PlotPadding: int = 17
ImPlotStyleVar_LabelPadding: int = 18
ImPlotStyleVar_LegendPadding: int = 19
ImPlotStyleVar_LegendInnerPadding: int = 20
ImPlotStyleVar_LegendSpacing: int = 21
ImPlotStyleVar_MousePosPadding: int = 22
ImPlotStyleVar_AnnotationPadding: int = 23
ImPlotStyleVar_FitPadding: int = 24
ImPlotStyleVar_PlotDefaultSize: int = 25
ImPlotStyleVar_PlotMinSize: int = 26
ImPlotStyleVar_COUNT: int = 27
ImPlotScale_Linear: int = 0
ImPlotScale_Time: int = 1
ImPlotScale_Log10: int = 2
ImPlotScale_SymLog: int = 3
ImPlotMarker_None: int = -1
ImPlotMarker_Circle: int = 0
ImPlotMarker_Square: int = 1
ImPlotMarker_Diamond: int = 2
ImPlotMarker_Up: int = 3
ImPlotMarker_Down: int = 4
ImPlotMarker_Left: int = 5
ImPlotMarker_Right: int = 6
ImPlotMarker_Cross: int = 7
ImPlotMarker_Plus: int = 8
ImPlotMarker_Asterisk: int = 9
ImPlotMarker_COUNT: int = 10
ImPlotColormap_Deep: int = 0
ImPlotColormap_Dark: int = 1
ImPlotColormap_Pastel: int = 2
ImPlotColormap_Paired: int = 3
ImPlotColormap_Viridis: int = 4
ImPlotColormap_Plasma: int = 5
ImPlotColormap_Hot: int = 6
ImPlotColormap_Cool: int = 7
ImPlotColormap_Pink: int = 8
ImPlotColormap_Jet: int = 9
ImPlotColormap_Twilight: int = 10
ImPlotColormap_RdBu: int = 11
ImPlotColormap_BrBG: int = 12
ImPlotColormap_PiYG: int = 13
ImPlotColormap_Spectral: int = 14
ImPlotColormap_Greys: int = 15
ImPlotLocation_Center: int = 0
ImPlotLocation_North: int = 1
ImPlotLocation_South: int = 2
ImPlotLocation_West: int = 4
ImPlotLocation_East: int = 8
ImPlotLocation_NorthWest: int = 5
ImPlotLocation_NorthEast: int = 9
ImPlotLocation_SouthWest: int = 6
ImPlotLocation_SouthEast: int = 10
ImPlotBin_Sqrt: int = -1
ImPlotBin_Sturges: int = -2
ImPlotBin_Rice: int = -3
ImPlotBin_Scott: int = -4
```
