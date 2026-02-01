# ImGui API Reference

All functions are in the `polyscope.imgui` namespace. Please see the [ImGui project](https://www.github.com/ocornut/imgui) for full documentation of ImGui functions and features.

These Python bindings are a 1:1 mapping of the C++ ImGui API, with concessions only for syntax that is not possible in Python. For example, C++ functions that take pointers and modify their arguments in-place instead return a Python tuple of `(is_changed, new_value)`.

See [here for an example UI]([[url.prefix]]/basics/interactive_UIs_and_animation/#sample-custom-ui).

## Functions

```python
IM_COL32() -> int
GetIO() -> ImGuiIO
GetStyle() -> ImGuiStyle
NewFrame() -> None
EndFrame() -> None
Render() -> None
GetDrawData() -> ImDrawData
CreateContext(shared_font_atlas: ImFontAtlas | None = None) -> typing_extensions.CapsuleType
DestroyContext(ctx: typing_extensions.CapsuleType | None = None) -> None
GetCurrentContext() -> typing_extensions.CapsuleType
SetCurrentContext(ctx: typing_extensions.CapsuleType) -> None
ShowDemoWindow(open: bool = True) -> bool
ShowMetricsWindow(open: bool = True) -> bool
ShowDebugLogWindow(open: bool = True) -> bool
ShowIDStackToolWindow(open: bool = True) -> bool
ShowAboutWindow(open: bool = True) -> bool
ShowStyleEditor(open: bool = True) -> bool
ShowStyleSelector(label: str) -> bool
ShowFontSelector(label: str) -> None
ShowUserGuide() -> None
GetVersion() -> str
StyleColorsDark(dst: ImGuiStyle | None = None) -> None
StyleColorsLight(dst: ImGuiStyle | None = None) -> None
StyleColorsClassic(dst: ImGuiStyle | None = None) -> None
Begin(
    name: str,
    open: bool,
    flags: int = 0,
    ) -> tuple[bool, bool]
Begin(
    name: str,
    flags: int = 0,
    ) -> bool
End() -> None
BeginChild(
    str_id: str,
    size: tuple[float, float] = (0.0, 0.0),
    child_flags: int = 0,
    window_flags: int = 0,
    ) -> bool
BeginChild(
    id: int,
    size: tuple[float, float] = (0.0, 0.0),
    child_flags: int = 0,
    window_flags: int = 0,
    ) -> bool
EndChild() -> None
IsWindowAppearing() -> bool
IsWindowCollapsed() -> bool
IsWindowFocused(flags: int = 0) -> bool
IsWindowHovered(flags: int = 0) -> bool
GetWindowDrawList() -> ImDrawList
GetWindowPos() -> tuple[float, float]
GetWindowSize() -> tuple[float, float]
GetWindowWidth() -> float
GetWindowHeight() -> float
SetNextWindowPos(
    pos: tuple[float, float],
    cond: int = 0,
    pivot: tuple[float, float] = (0.0, 0.0),
    ) -> None
SetNextWindowSize(
    size: tuple[float, float],
    cond: int = 0,
    ) -> None
SetNextWindowSizeConstraints(
    size_min: tuple[float, float],
    size_max: tuple[float, float],
    ) -> None
SetNextWindowContentSize(size: tuple[float, float]) -> None
SetNextWindowCollapsed(
    collapsed: bool,
    cond: int = 0,
    ) -> None
SetNextWindowFocus() -> None
SetNextWindowScroll(scroll: tuple[float, float]) -> None
SetNextWindowBgAlpha(alpha: float) -> None
SetWindowPos(
    pos: tuple[float, float],
    cond: int = 0,
    ) -> None
SetWindowPos(
    name: str,
    pos: tuple[float, float],
    cond: int = 0,
    ) -> None
SetWindowSize(
    size: tuple[float, float],
    cond: int = 0,
    ) -> None
SetWindowSize(
    name: str,
    size: tuple[float, float],
    cond: int = 0,
    ) -> None
SetWindowCollapsed(
    collapsed: bool,
    cond: int = 0,
    ) -> None
SetWindowCollapsed(
    name: str,
    collapsed: bool,
    cond: int = 0,
    ) -> None
SetWindowFocus() -> None
SetWindowFocus(name: str) -> None
GetScrollX() -> float
GetScrollY() -> float
SetScrollX(scroll_x: float) -> None
SetScrollY(scroll_y: float) -> None
GetScrollMaxX() -> float
GetScrollMaxY() -> float
SetScrollHereX(center_x_ratio: float = 0.5) -> None
SetScrollHereY(center_y_ratio: float = 0.5) -> None
SetScrollFromPosX(
    local_x: float,
    center_x_ratio: float = 0.5,
    ) -> None
SetScrollFromPosY(
    local_y: float,
    center_y_ratio: float = 0.5,
    ) -> None
PushFont(
    font: ImFont | None = None,
    font_size_base_unscaled: float = 0.0,
    ) -> None
PopFont() -> None
GetFont() -> ImFont
GetFontSize() -> float
GetFontBaked() -> ImFontBaked
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
    val: tuple[float, float],
    ) -> None
PushStyleVarX(
    idx: int,
    val_x: float,
    ) -> None
PushStyleVarY(
    idx: int,
    val_y: float,
    ) -> None
PopStyleVar(count: int = 1) -> None
PushItemFlag(
    option: int,
    enabled: bool,
    ) -> None
PopItemFlag() -> None
PushItemWidth(item_width: float) -> None
PopItemWidth() -> None
SetNextItemWidth(item_width: float) -> None
CalcItemWidth() -> float
PushTextWrapPos(wrap_local_pos_x: float = 0.0) -> None
PopTextWrapPos() -> None
GetFontTexUvWhitePixel() -> tuple[float, float]
GetColorU32(
    idx: int,
    alpha_mul: float = 1.0,
    ) -> int
GetColorU32(col: tuple[float, float, float, float]) -> int
GetColorU32(
    col: int,
    alpha_mul: float = 1.0,
    ) -> int
GetStyleColorVec4(idx: int) -> tuple[float, float, float, float]
GetCursorScreenPos() -> tuple[float, float]
SetCursorScreenPos(pos: tuple[float, float]) -> None
GetContentRegionAvail() -> tuple[float, float]
GetCursorPos() -> tuple[float, float]
GetCursorPosX() -> float
GetCursorPosY() -> float
SetCursorPos(local_pos: tuple[float, float]) -> None
SetCursorPosX(local_x: float) -> None
SetCursorPosY(local_y: float) -> None
GetCursorStartPos() -> tuple[float, float]
Separator() -> None
SameLine(
    offset_from_start_x: float = 0.0,
    spacing: float = -1.0,
    ) -> None
NewLine() -> None
Spacing() -> None
Dummy(size: tuple[float, float]) -> None
Indent(indent_w: float = 0.0) -> None
Unindent(indent_w: float = 0.0) -> None
BeginGroup() -> None
EndGroup() -> None
AlignTextToFramePadding() -> None
GetTextLineHeight() -> float
GetTextLineHeightWithSpacing() -> float
GetFrameHeight() -> float
GetFrameHeightWithSpacing() -> float
PushID(str_id: str) -> None
PushID(int_id: int) -> None
PopID() -> None
GetID(str_id: str) -> int
GetID(int_id: int) -> int
TextUnformatted(text: str) -> None
Text(text: str) -> None
TextColored(
    col: tuple[float, float, float, float],
    text: str,
    ) -> None
TextDisabled(text: str) -> None
TextWrapped(text: str) -> None
LabelText(
    label: str,
    text: str,
    ) -> None
BulletText(text: str) -> None
SeparatorText(label: str) -> None
Button(
    label: str,
    size: tuple[float, float] = (0.0, 0.0),
    ) -> bool
SmallButton(label: str) -> bool
InvisibleButton(
    str_id: str,
    size: tuple[float, float],
    flags: int = 0,
    ) -> bool
ArrowButton(
    str_id: str,
    dir: ImGuiDir,
    ) -> bool
Checkbox(
    label: str,
    v: bool,
    ) -> tuple[bool, bool]
CheckboxFlags(
    label: str,
    flags: int,
    flags_value: int,
    ) -> tuple[bool, int]
CheckboxFlags(
    label: str,
    flags: int,
    flags_value: int,
    ) -> tuple[bool, int]
RadioButton(
    label: str,
    active: bool,
    ) -> bool
RadioButton(
    label: str,
    v: int,
    v_button: int,
    ) -> tuple[bool, int]
ProgressBar(
    fraction: float,
    size_arg: tuple[float, float] = (-1.1754943508222875e-38, 0.0),
    overlay: str | None = None,
    ) -> None
Bullet() -> None
TextLink(label: str) -> bool
TextLinkOpenURL(
    label: str,
    url: str | None = None,
    ) -> bool
Image(
    user_texture_ref: ImTextureRef,
    image_size: tuple[float, float],
    uv0: tuple[float, float] = (0.0, 0.0),
    uv1: tuple[float, float] = (1.0, 1.0),
    ) -> None
ImageWithBg(
    user_texture_ref: ImTextureRef,
    image_size: tuple[float, float],
    uv0: tuple[float, float] = (0.0, 0.0),
    uv1: tuple[float, float] = (1.0, 1.0),
    bg_col: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0),
    tint_col: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
    ) -> None
ImageButton(
    str_id: str,
    user_texture_ref: ImTextureRef,
    image_size: tuple[float, float],
    uv0: tuple[float, float] = (0.0, 0.0),
    uv1: tuple[float, float] = (1.0, 1.0),
    bg_col: tuple[float, float, float, float] = (0.0, 0.0, 0.0, 0.0),
    tint_col: tuple[float, float, float, float] = (1.0, 1.0, 1.0, 1.0),
    ) -> bool
BeginCombo(
    label: str,
    preview_value: str,
    flags: int = 0,
    ) -> bool
EndCombo() -> None
Combo(
    label: str,
    current_item: int,
    items: Sequence[str],
    popup_max_height_in_items: int = -1,
    ) -> tuple[bool, int]
Combo(
    label: str,
    current_item: int,
    items_separated_by_zeros: str,
    popup_max_height_in_items: int = -1,
    ) -> tuple[bool, int]
DragFloat(
    label: str,
    v: float,
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, float]
DragFloat2(
    label: str,
    v: Sequence[float],
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float]]
DragFloat3(
    label: str,
    v: Sequence[float],
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float]]
DragFloat4(
    label: str,
    v: Sequence[float],
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float, float]]
DragFloatRange2(
    label: str,
    v_current_min: float,
    v_current_max: float,
    v_speed: float = 1.0,
    v_min: float = 0.0,
    v_max: float = 0.0,
    format: str = '%.3f',
    format_max: str | None = None,
    flags: int = 0,
    ) -> tuple[bool, float, float]
DragInt(
    label: str,
    v: int,
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, int]
DragInt2(
    label: str,
    v: Sequence[int],
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int]]
DragInt3(
    label: str,
    v: Sequence[int],
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int, int]]
DragInt4(
    label: str,
    v: Sequence[int],
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int, int, int]]
DragIntRange2(
    label: str,
    v_current_min: int,
    v_current_max: int,
    v_speed: float = 1.0,
    v_min: int = 0,
    v_max: int = 0,
    format: str = '%d',
    format_max: str | None = None,
    flags: int = 0,
    ) -> tuple[bool, int, int]
SliderFloat(
    label: str,
    v: float,
    v_min: float,
    v_max: float,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, float]
SliderFloat2(
    label: str,
    v: Sequence[float],
    v_min: float,
    v_max: float,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float]]
SliderFloat3(
    label: str,
    v: Sequence[float],
    v_min: float,
    v_max: float,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float]]
SliderFloat4(
    label: str,
    v: Sequence[float],
    v_min: float,
    v_max: float,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float, float]]
SliderAngle(
    label: str,
    v_rad: float,
    v_degrees_min: float = -360.0,
    v_degrees_max: float = 360.0,
    format: str = '%.0f deg',
    flags: int = 0,
    ) -> tuple[bool, float]
SliderInt(
    label: str,
    v: int,
    v_min: int,
    v_max: int,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, int]
SliderInt2(
    label: str,
    v: Sequence[int],
    v_min: int,
    v_max: int,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int]]
SliderInt3(
    label: str,
    v: Sequence[int],
    v_min: int,
    v_max: int,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int, int]]
SliderInt4(
    label: str,
    v: Sequence[int],
    v_min: int,
    v_max: int,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int, int, int]]
VSliderFloat(
    label: str,
    size: tuple[float, float],
    v: float,
    v_min: float,
    v_max: float,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, float]
VSliderInt(
    label: str,
    size: tuple[float, float],
    v: int,
    v_min: int,
    v_max: int,
    format: str = '%d',
    flags: int = 0,
    ) -> tuple[bool, int]
InputText(
    label: str,
    buf: str,
    flags: int = 0,
    max_str_len: int = 1024,
    ) -> tuple[bool, str]
InputTextMultiline(
    label: str,
    buf: str,
    size: tuple[float, float] = (0.0, 0.0),
    flags: int = 0,
    max_str_len: int = 4096,
    ) -> tuple[bool, str]
InputTextWithHint(
    label: str,
    hint: str,
    buf: str,
    flags: int = 0,
    max_str_len: int = 1024,
    ) -> tuple[bool, str]
InputFloat(
    label: str,
    v: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, float]
InputFloat2(
    label: str,
    v: Sequence[float],
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float]]
InputFloat3(
    label: str,
    v: Sequence[float],
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float]]
InputFloat4(
    label: str,
    v: Sequence[float],
    format: str = '%.3f',
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float, float]]
InputInt(
    label: str,
    v: int,
    step: int = 1,
    step_fast: int = 100,
    flags: int = 0,
    ) -> tuple[bool, int]
InputInt2(
    label: str,
    v: Sequence[int],
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int]]
InputInt3(
    label: str,
    v: Sequence[int],
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int, int]]
InputInt4(
    label: str,
    v: Sequence[int],
    flags: int = 0,
    ) -> tuple[bool, tuple[int, int, int, int]]
InputDouble(
    label: str,
    v: float,
    step: float = 0.0,
    step_fast: float = 0.0,
    format: str = '%.6f',
    flags: int = 0,
    ) -> tuple[bool, float]
ColorEdit3(
    label: str,
    col: Sequence[float],
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float]]
ColorEdit4(
    label: str,
    col: Sequence[float],
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float, float]]
ColorPicker3(
    label: str,
    col: Sequence[float],
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float]]
ColorPicker4(
    label: str,
    col: Sequence[float],
    flags: int = 0,
    ) -> tuple[bool, tuple[float, float, float, float]]
ColorButton(
    desc_id: str,
    col: tuple[float, float, float, float],
    flags: int = 0,
    size: tuple[float, float] = (0.0, 0.0),
    ) -> bool
SetColorEditOptions(flags: int) -> None
TreeNode(label: str) -> bool
TreeNode(
    str_id: str,
    text: str,
    ) -> bool
TreeNodeEx(
    label: str,
    flags: int = 0,
    ) -> bool
TreeNodeEx(
    str_id: str,
    flags: int,
    text: str,
    ) -> bool
TreePush(str_id: str) -> None
TreePop() -> None
GetTreeNodeToLabelSpacing() -> float
CollapsingHeader(
    label: str,
    flags: int = 0,
    ) -> bool
CollapsingHeader(
    label: str,
    p_visible: bool,
    flags: int = 0,
    ) -> tuple[bool, bool]
SetNextItemOpen(
    is_open: bool,
    cond: int = 0,
    ) -> None
SetNextItemStorageID(storage_id: int) -> None
Selectable(
    label: str,
    selected: bool = False,
    flags: int = 0,
    size: tuple[float, float] = (0.0, 0.0),
    ) -> bool
Selectable(
    label: str,
    p_selected: bool,
    flags: int = 0,
    size: tuple[float, float] = (0.0, 0.0),
    ) -> tuple[bool, bool]
BeginMultiSelect(
    flags: int,
    selection_size: int = -1,
    items_count: int = -1,
    ) -> 'ImGuiMultiSelectIO'
EndMultiSelect() -> 'ImGuiMultiSelectIO'
SetNextItemSelectionUserData(selection_user_data: int) -> None
IsItemToggledSelection() -> bool
BeginListBox(
    label: str,
    size: tuple[float, float] = (0.0, 0.0),
    ) -> bool
EndListBox() -> None
ListBox(
    label: str,
    current_item: int,
    items: Sequence[str],
    height_in_items: int = -1,
    ) -> tuple[bool, int]
PlotLines(
    label: str,
    values: NDArray[numpy.float32],
    values_offset: int = 0,
    overlay_text: str | None = None,
    scale_min: float = 3.4028234663852886e+38,
    scale_max: float = 3.4028234663852886e+38,
    graph_size: tuple[float, float] = (0.0, 0.0),
    ) -> None
PlotHistogram(
    label: str,
    values: NDArray[numpy.float32],
    values_offset: int = 0,
    overlay_text: str | None = None,
    scale_min: float = 3.4028234663852886e+38,
    scale_max: float = 3.4028234663852886e+38,
    graph_size: tuple[float, float] = (0.0, 0.0),
    ) -> None
Value(
    prefix: str,
    b: bool,
    ) -> None
Value(
    prefix: str,
    v: int,
    ) -> None
Value(
    prefix: str,
    v: int,
    ) -> None
Value(
    prefix: str,
    v: float,
    float_format: str | None = None,
    ) -> None
BeginMenuBar() -> bool
EndMenuBar() -> None
BeginMainMenuBar() -> bool
EndMainMenuBar() -> None
BeginMenu(
    label: str,
    enabled: bool = True,
    ) -> bool
EndMenu() -> None
MenuItem(
    label: str,
    shortcut: str | None = None,
    selected: bool = False,
    enabled: bool = True,
    ) -> bool
MenuItem(
    label: str,
    shortcut: str,
    p_selected: bool,
    enabled: bool = True,
    ) -> tuple[bool, bool]
BeginTooltip() -> bool
EndTooltip() -> None
SetTooltip(text: str) -> None
BeginItemTooltip() -> bool
SetItemTooltip(text: str) -> None
BeginPopup(
    str_id: str,
    flags: int = 0,
    ) -> bool
BeginPopupModal(
    name: str,
    p_open: bool,
    flags: int = 0,
    ) -> tuple[bool, bool]
BeginPopupModal(
    name: str,
    flags: int = 0,
    ) -> bool
EndPopup() -> None
OpenPopup(
    str_id: str,
    popup_flags: int = 0,
    ) -> None
OpenPopup(
    id: int,
    popup_flags: int = 0,
    ) -> None
OpenPopupOnItemClick(
    str_id: str | None = None,
    popup_flags: int = 1,
    ) -> None
CloseCurrentPopup() -> None
BeginPopupContextItem(
    str_id: str | None = None,
    popup_flags: int = 1,
    ) -> bool
BeginPopupContextWindow(
    str_id: str | None = None,
    popup_flags: int = 1,
    ) -> bool
BeginPopupContextVoid(
    str_id: str | None = None,
    popup_flags: int = 1,
    ) -> bool
IsPopupOpen(
    str_id: str,
    flags: int = 0,
    ) -> bool
BeginTable(
    str_id: str,
    columns: int,
    flags: int = 0,
    outer_size: tuple[float, float] = (0.0, 0.0),
    inner_width: float = 0.0,
    ) -> bool
EndTable() -> None
TableNextRow(
    row_flags: int = 0,
    min_row_height: float = 0.0,
    ) -> None
TableNextColumn() -> bool
TableSetColumnIndex(column_n: int) -> bool
TableSetupColumn(
    label: str,
    flags: int = 0,
    init_width_or_weight: float = 0.0,
    user_id: int = 0,
    ) -> None
TableSetupScrollFreeze(
    cols: int,
    rows: int,
    ) -> None
TableHeader(label: str) -> None
TableHeadersRow() -> None
TableAngledHeadersRow() -> None
TableGetSortSpecs() -> ImGuiTableSortSpecs
TableGetColumnCount() -> int
TableGetColumnIndex() -> int
TableGetRowIndex() -> int
TableGetColumnName(column_n: int = -1) -> str
TableGetColumnFlags(column_n: int = -1) -> int
TableSetColumnEnabled(
    column_n: int,
    v: bool,
    ) -> None
TableGetHoveredColumn() -> int
TableSetBgColor(
    target: int,
    color: int,
    column_n: int = -1,
    ) -> None
Columns(
    count: int = 1,
    id: str | None = None,
    borders: bool = True,
    ) -> None
NextColumn() -> None
GetColumnIndex() -> int
GetColumnWidth(column_index: int = -1) -> float
SetColumnWidth(
    column_index: int,
    width: float,
    ) -> None
GetColumnOffset(column_index: int = -1) -> float
SetColumnOffset(
    column_index: int,
    offset_x: float,
    ) -> None
GetColumnsCount() -> int
BeginTabBar(
    str_id: str,
    flags: int = 0,
    ) -> bool
EndTabBar() -> None
BeginTabItem(
    label: str,
    p_open: bool,
    flags: int = 0,
    ) -> tuple[bool, bool]
EndTabItem() -> None
TabItemButton(
    label: str,
    flags: int = 0,
    ) -> bool
SetTabItemClosed(tab_or_docked_window_label: str) -> None
LogToTTY(auto_open_depth: int = -1) -> None
LogToFile(
    auto_open_depth: int = -1,
    filename: str | None = None,
    ) -> None
LogToClipboard(auto_open_depth: int = -1) -> None
LogFinish() -> None
LogButtons() -> None
LogText(text: str) -> None
BeginDragDropSource(flags: int = 0) -> bool
SetDragDropPayload(
    type: str,
    data: str,
    cond: int = 0,
    ) -> bool
EndDragDropSource() -> None
BeginDragDropTarget() -> bool
AcceptDragDropPayload(
    type: str,
    flags: int = 0,
    ) -> ImGuiPayload
EndDragDropTarget() -> None
GetDragDropPayload() -> ImGuiPayload
BeginDisabled(disabled: bool = True) -> None
EndDisabled() -> None
PushClipRect(
    clip_rect_min: tuple[float, float],
    clip_rect_max: tuple[float, float],
    intersect_with_current_clip_rect: bool,
    ) -> None
PopClipRect() -> None
SetItemDefaultFocus() -> None
SetKeyboardFocusHere(offset: int = 0) -> None
SetNavCursorVisible(visible: bool) -> None
SetNextItemAllowOverlap() -> None
IsItemHovered(flags: int = 0) -> bool
IsItemActive() -> bool
IsItemFocused() -> bool
IsItemClicked(mouse_button: int = 0) -> bool
IsItemVisible() -> bool
IsItemEdited() -> bool
IsItemActivated() -> bool
IsItemDeactivated() -> bool
IsItemDeactivatedAfterEdit() -> bool
IsItemToggledOpen() -> bool
IsAnyItemHovered() -> bool
IsAnyItemActive() -> bool
IsAnyItemFocused() -> bool
GetItemID() -> int
GetItemRectMin() -> tuple[float, float]
GetItemRectMax() -> tuple[float, float]
GetItemRectSize() -> tuple[float, float]
GetMainViewport() -> ImGuiViewport
GetBackgroundDrawList() -> ImDrawList
GetForegroundDrawList() -> ImDrawList
IsRectVisible(size: tuple[float, float]) -> bool
IsRectVisible(
    rect_min: tuple[float, float],
    rect_max: tuple[float, float],
    ) -> bool
GetTime() -> float
GetFrameCount() -> int
GetStyleColorName(idx: int) -> str
SetStateStorage(storage: 'ImGuiStorage') -> None
GetStateStorage() -> 'ImGuiStorage'
CalcTextSize(
    text: str,
    hide_text_after_double_hash: bool = False,
    wrap_width: float = -1.0,
    ) -> tuple[float, float]
ColorConvertU32ToFloat4(in_val: int) -> tuple[float, float, float, float]
ColorConvertFloat4ToU32(in_val: tuple[float, float, float, float]) -> int
ColorConvertRGBtoHSV(
    r: float,
    g: float,
    b: float,
    ) -> tuple[float, float, float]
ColorConvertHSVtoRGB(
    h: float,
    s: float,
    v: float,
    ) -> tuple[float, float, float]
IsKeyDown(key: ImGuiKey) -> bool
IsKeyPressed(
    key: ImGuiKey,
    repeat: bool = True,
    ) -> bool
IsKeyReleased(key: ImGuiKey) -> bool
IsKeyChordPressed(key_chord: int) -> bool
GetKeyPressedAmount(
    key: ImGuiKey,
    repeat_delay: float,
    rate: float,
    ) -> int
GetKeyName(key: ImGuiKey) -> str
SetNextFrameWantCaptureKeyboard(want_capture_keyboard: bool) -> None
IsMouseDown(button: int) -> bool
IsMouseClicked(
    button: int,
    repeat: bool = False,
    ) -> bool
IsMouseReleased(button: int) -> bool
IsMouseDoubleClicked(button: int) -> bool
IsMouseReleasedWithDelay(
    button: int,
    delay: float,
    ) -> bool
GetMouseClickedCount(button: int) -> int
IsMouseHoveringRect(
    r_min: 'ImVec2',
    r_max: 'ImVec2',
    clip: bool = True,
    ) -> bool
IsMousePosValid(mouse_pos: 'ImVec2' | None = None) -> bool
IsAnyMouseDown() -> bool
GetMousePos() -> tuple[float, float]
GetMousePosOnOpeningCurrentPopup() -> tuple[float, float]
IsMouseDragging(
    button: int,
    lock_threshold: float = -1.0,
    ) -> bool
GetMouseDragDelta(
    button: int = 0,
    lock_threshold: float = -1.0,
    ) -> tuple[float, float]
ResetMouseDragDelta(button: int = 0) -> None
GetMouseCursor() -> int
SetMouseCursor(cursor_type: int) -> None
SetNextFrameWantCaptureMouse(want_capture_mouse: bool) -> None
GetClipboardText() -> str
SetClipboardText(text: str) -> None
LoadIniSettingsFromDisk(ini_filename: str) -> None
LoadIniSettingsFromMemory(
    ini_data: str,
    ini_size: int = 0,
    ) -> None
SaveIniSettingsToDisk(ini_filename: str) -> None
SaveIniSettingsToMemory() -> str
DebugTextEncoding(text: str) -> None
DebugFlashStyleColor(idx: int) -> None
DebugStartItemPicker() -> None
DebugCheckVersionAndDataLayout(
    version_str: str,
    sz_io: int,
    sz_style: int,
    sz_vec2: int,
    sz_vec4: int,
    sz_drawvert: int,
    sz_drawidx: int,
    ) -> bool
MemAlloc(size: int) -> typing_extensions.CapsuleType
MemFree(ptr: typing_extensions.CapsuleType) -> None
```

## Classes

### ImTextureRef

**Methods:**

```python
__init__() -> None
__init__(tex_id: int) -> None
__init__(tex_ptr: typing_extensions.CapsuleType) -> None
GetTexID() -> int
```

### ImGuiTableSortSpecs

**Properties:**

```python
SpecsCount: int
SpecsDirty: bool
```

**Methods:**

```python
Specs() -> list[ImGuiTableColumnSortSpecs]
```

### ImGuiTableColumnSortSpecs

**Properties:**

```python
ColumnUserID: int
ColumnIndex: int
SortOrder: int
SortDirection: ImGuiSortDirection
```

### ImGuiPayload

**Properties:**

```python
DataSize: int
```

**Methods:**

```python
IsDataType(type: str) -> bool
IsPreview() -> bool
IsDelivery() -> bool
```

### ImDrawData

**Properties:**

```python
Valid: bool
CmdListsCount: int
TotalIdxCount: int
TotalVtxCount: int
DisplayPos: tuple[float, float]
DisplaySize: tuple[float, float]
FramebufferScale: tuple[float, float]
```

**Methods:**

```python
ScaleClipRects(fb_scale: tuple[float, float]) -> None
```

### ImGuiViewport

**Properties:**

```python
ID: int
Flags: int
Pos: tuple[float, float]
Size: tuple[float, float]
WorkPos: tuple[float, float]
WorkSize: tuple[float, float]
```

**Methods:**

```python
GetCenter() -> tuple[float, float]
GetWorkCenter() -> tuple[float, float]
```

### ImGuiIO

**Properties:**

```python
ConfigFlags: int
BackendFlags: int
DisplaySize: tuple[float, float]
DeltaTime: float
IniSavingRate: float
IniFilename: str
LogFilename: str
Fonts: ImFontAtlas
FontDefault: ImFont
FontAllowUserScaling: bool
DisplayFramebufferScale: tuple[float, float]
ConfigNavSwapGamepadButtons: bool
ConfigNavMoveSetMousePos: bool
ConfigNavCaptureKeyboard: bool
ConfigNavEscapeClearFocusItem: bool
ConfigNavEscapeClearFocusWindow: bool
ConfigNavCursorVisibleAuto: bool
ConfigNavCursorVisibleAlways: bool
MouseDrawCursor: bool
ConfigMacOSXBehaviors: bool
ConfigInputTrickleEventQueue: bool
ConfigInputTextCursorBlink: bool
ConfigInputTextEnterKeepActive: bool
ConfigDragClickToInputText: bool
ConfigWindowsResizeFromEdges: bool
ConfigWindowsMoveFromTitleBarOnly: bool
ConfigWindowsCopyContentsWithCtrlC: bool
ConfigScrollbarScrollByPage: bool
ConfigMemoryCompactTimer: float
MouseDoubleClickTime: float
MouseDoubleClickMaxDist: float
MouseDragThreshold: float
KeyRepeatDelay: float
KeyRepeatRate: float
ConfigErrorRecovery: bool
ConfigErrorRecoveryEnableAssert: bool
ConfigErrorRecoveryEnableDebugLog: bool
ConfigErrorRecoveryEnableTooltip: bool
ConfigDebugIsDebuggerPresent: bool
ConfigDebugHighlightIdConflicts: bool
ConfigDebugHighlightIdConflictsShowItemPicker: bool
ConfigDebugBeginReturnValueOnce: bool
ConfigDebugBeginReturnValueLoop: bool
ConfigDebugIgnoreFocusLoss: bool
ConfigDebugIniSettings: bool
BackendPlatformName: str
BackendRendererName: str
WantCaptureMouse: bool
WantCaptureKeyboard: bool
WantTextInput: bool
WantSetMousePos: bool
WantSaveIniSettings: bool
NavActive: bool
NavVisible: bool
Framerate: float
MetricsRenderVertices: int
MetricsRenderIndices: int
MetricsRenderWindows: int
MetricsActiveWindows: int
MouseDelta: tuple[float, float]
MousePos: tuple[float, float]
MouseDown: list[bool]
MouseWheel: float
MouseWheelH: float
MouseSource: ImGuiMouseSource
KeyCtrl: bool
KeyShift: bool
KeyAlt: bool
KeySuper: bool
KeyMods: int
WantCaptureMouseUnlessPopupClose: bool
MousePosPrev: tuple[float, float]
MouseClickedPos: list[tuple[float, float]]
MouseClickedTime: list[float]
MouseClicked: list[bool]
MouseDoubleClicked: list[bool]
MouseClickedCount: list[int]
MouseClickedLastCount: list[int]
MouseReleased: list[bool]
MouseDownOwned: list[bool]
MouseDownOwnedUnlessPopupClose: list[bool]
MouseDownDuration: list[float]
MouseDownDurationPrev: list[float]
MouseDragMaxDistanceSqr: list[float]
PenPressure: float
AppFocusLost: bool
InputQueueSurrogate: int
InputQueueCharacters: 'ImVector<unsigned short>'
```

**Methods:**

```python
AddKeyEvent(
    key: ImGuiKey,
    down: bool,
    ) -> None
AddKeyAnalogEvent(
    key: ImGuiKey,
    down: bool,
    v: float,
    ) -> None
AddMousePosEvent(
    x: float,
    y: float,
    ) -> None
AddMouseButtonEvent(
    button: int,
    down: bool,
    ) -> None
AddMouseWheelEvent(
    wheel_x: float,
    wheel_y: float,
    ) -> None
AddMouseSourceEvent(source: ImGuiMouseSource) -> None
AddFocusEvent(focused: bool) -> None
AddInputCharacter(c: int) -> None
AddInputCharacterUTF16(c: int) -> None
AddInputCharactersUTF8(str: str) -> None
SetKeyEventNativeData(
    key: ImGuiKey,
    native_keycode: int,
    native_scancode: int,
    native_legacy_index: int = -1,
    ) -> None
SetAppAcceptingEvents(accepting_events: bool) -> None
ClearEventsQueue() -> None
ClearInputKeys() -> None
ClearInputMouse() -> None
```

### ImGuiStyle

**Properties:**

```python
FontSizeBase: float
FontScaleMain: float
FontScaleDpi: float
Alpha: float
DisabledAlpha: float
WindowPadding: tuple[float, float]
WindowRounding: float
WindowBorderSize: float
WindowBorderHoverPadding: float
WindowMinSize: tuple[float, float]
WindowTitleAlign: tuple[float, float]
WindowMenuButtonPosition: ImGuiDir
ChildRounding: float
ChildBorderSize: float
PopupRounding: float
PopupBorderSize: float
FramePadding: tuple[float, float]
FrameRounding: float
FrameBorderSize: float
ItemSpacing: tuple[float, float]
ItemInnerSpacing: tuple[float, float]
CellPadding: tuple[float, float]
TouchExtraPadding: tuple[float, float]
IndentSpacing: float
ColumnsMinSpacing: float
ScrollbarSize: float
ScrollbarRounding: float
ScrollbarPadding: float
GrabMinSize: float
GrabRounding: float
LogSliderDeadzone: float
ImageBorderSize: float
TabRounding: float
TabBorderSize: float
TabCloseButtonMinWidthSelected: float
TabCloseButtonMinWidthUnselected: float
TabBarBorderSize: float
TabBarOverlineSize: float
TableAngledHeadersAngle: float
TableAngledHeadersTextAlign: tuple[float, float]
TreeLinesFlags: int
TreeLinesSize: float
TreeLinesRounding: float
DragDropTargetRounding: float
DragDropTargetBorderSize: float
DragDropTargetPadding: float
ColorButtonPosition: ImGuiDir
ButtonTextAlign: tuple[float, float]
SelectableTextAlign: tuple[float, float]
SeparatorTextBorderSize: float
SeparatorTextAlign: tuple[float, float]
SeparatorTextPadding: tuple[float, float]
DisplayWindowPadding: tuple[float, float]
DisplaySafeAreaPadding: tuple[float, float]
MouseCursorScale: float
AntiAliasedLines: bool
AntiAliasedLinesUseTex: bool
AntiAliasedFill: bool
CurveTessellationTol: float
CircleTessellationMaxError: float
HoverStationaryDelay: float
HoverDelayShort: float
HoverDelayNormal: float
HoverFlagsForTooltipMouse: int
HoverFlagsForTooltipNav: int
```

**Methods:**

```python
GetColor(idx: int) -> tuple[float, float, float, float]
SetColor(
    idx: int,
    color: tuple[float, float, float, float],
    ) -> None
GetColorCount() -> int
ScaleAllSizes(scale_factor: float) -> None
```

### ImDrawList

**Methods:**

```python
PushClipRect(
    clip_rect_min: tuple[float, float],
    clip_rect_max: tuple[float, float],
    intersect_with_current_clip_rect: bool = False,
    ) -> None
PushClipRectFullScreen() -> None
PopClipRect() -> None
GetClipRectMin() -> tuple[float, float]
GetClipRectMax() -> tuple[float, float]
AddLine(
    p1: tuple[float, float],
    p2: tuple[float, float],
    col: int,
    thickness: float = 1.0,
    ) -> None
AddRect(
    p_min: tuple[float, float],
    p_max: tuple[float, float],
    col: int,
    rounding: float = 0.0,
    flags: int = 0,
    thickness: float = 1.0,
    ) -> None
AddRectFilled(
    p_min: tuple[float, float],
    p_max: tuple[float, float],
    col: int,
    rounding: float = 0.0,
    flags: int = 0,
    ) -> None
AddRectFilledMultiColor(
    p_min: tuple[float, float],
    p_max: tuple[float, float],
    col_upr_left: int,
    col_upr_right: int,
    col_bot_right: int,
    col_bot_left: int,
    ) -> None
AddQuad(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
    col: int,
    thickness: float = 1.0,
    ) -> None
AddQuadFilled(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
    col: int,
    ) -> None
AddTriangle(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    col: int,
    thickness: float = 1.0,
    ) -> None
AddTriangleFilled(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    col: int,
    ) -> None
AddCircle(
    center: tuple[float, float],
    radius: float,
    col: int,
    num_segments: int = 0,
    thickness: float = 1.0,
    ) -> None
AddCircleFilled(
    center: tuple[float, float],
    radius: float,
    col: int,
    num_segments: int = 0,
    ) -> None
AddNgon(
    center: tuple[float, float],
    radius: float,
    col: int,
    num_segments: int,
    thickness: float = 1.0,
    ) -> None
AddNgonFilled(
    center: tuple[float, float],
    radius: float,
    col: int,
    num_segments: int,
    ) -> None
AddEllipse(
    center: tuple[float, float],
    radius: tuple[float, float],
    col: int,
    rot: float = 0.0,
    num_segments: int = 0,
    thickness: float = 1.0,
    ) -> None
AddEllipseFilled(
    center: tuple[float, float],
    radius: tuple[float, float],
    col: int,
    rot: float = 0.0,
    num_segments: int = 0,
    ) -> None
AddText(
    pos: tuple[float, float],
    col: int,
    text: str,
    ) -> None
AddText(
    font: ImFont,
    font_size: float,
    pos: tuple[float, float],
    col: int,
    text_begin: str,
    wrap_width: float = 0.0,
    ) -> None
AddBezierCubic(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
    col: int,
    thickness: float,
    num_segments: int = 0,
    ) -> None
AddBezierQuadratic(
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    col: int,
    thickness: float,
    num_segments: int = 0,
    ) -> None
AddPolyline(
    points: NDArray[numpy.float32],
    col: int,
    flags: int,
    thickness: float,
    ) -> None
AddConvexPolyFilled(
    points: NDArray[numpy.float32],
    col: int,
    ) -> None
AddConcavePolyFilled(
    points: NDArray[numpy.float32],
    col: int,
    ) -> None
AddImage(
    user_texture_ref: ImTextureRef,
    p_min: tuple[float, float],
    p_max: tuple[float, float],
    uv_min: tuple[float, float] = (0.0, 0.0),
    uv_max: tuple[float, float] = (1.0, 1.0),
    col: int = 4294967295,
    ) -> None
AddImageQuad(
    user_texture_ref: ImTextureRef,
    p1: tuple[float, float],
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
    uv1: tuple[float, float] = (0.0, 0.0),
    uv2: tuple[float, float] = (1.0, 0.0),
    uv3: tuple[float, float] = (1.0, 1.0),
    uv4: tuple[float, float] = (0.0, 1.0),
    col: int = 4294967295,
    ) -> None
AddImageRounded(
    user_texture_ref: ImTextureRef,
    p_min: tuple[float, float],
    p_max: tuple[float, float],
    uv_min: tuple[float, float],
    uv_max: tuple[float, float],
    col: int,
    rounding: float,
    flags: int = 0,
    ) -> None
PathClear() -> None
PathLineTo(pos: tuple[float, float]) -> None
PathLineToMergeDuplicate(pos: tuple[float, float]) -> None
PathFillConvex(col: int) -> None
PathFillConcave(col: int) -> None
PathStroke(
    col: int,
    flags: int = 0,
    thickness: float = 1.0,
    ) -> None
PathArcTo(
    center: tuple[float, float],
    radius: float,
    a_min: float,
    a_max: float,
    num_segments: int = 0,
    ) -> None
PathArcToFast(
    center: tuple[float, float],
    radius: float,
    a_min_of_12: int,
    a_max_of_12: int,
    ) -> None
PathEllipticalArcTo(
    center: tuple[float, float],
    radius: tuple[float, float],
    rot: float,
    a_min: float,
    a_max: float,
    num_segments: int = 0,
    ) -> None
PathBezierCubicCurveTo(
    p2: tuple[float, float],
    p3: tuple[float, float],
    p4: tuple[float, float],
    num_segments: int = 0,
    ) -> None
PathBezierQuadraticCurveTo(
    p2: tuple[float, float],
    p3: tuple[float, float],
    num_segments: int = 0,
    ) -> None
PathRect(
    rect_min: tuple[float, float],
    rect_max: tuple[float, float],
    rounding: float = 0.0,
    flags: int = 0,
    ) -> None
ChannelsSplit(count: int) -> None
ChannelsMerge() -> None
ChannelsSetCurrent(n: int) -> None
AddDrawCmd() -> None
CloneOutput() -> ImDrawList
```

### ImFontBaked

**Properties:**

```python
FallbackAdvanceX: float
Size: float
RasterizerDensity: float
Ascent: float
Descent: float
OwnerFont: ImFont
```

**Methods:**

```python
ClearOutputData() -> None
GetCharAdvance(c: int) -> float
IsGlyphLoaded(c: int) -> bool
```

### ImFontAtlas

**Properties:**

```python
Flags: int
TexGlyphPadding: int
TexUvScale: tuple[float, float]
TexUvWhitePixel: tuple[float, float]
```

**Methods:**

```python
AddFontDefault() -> ImFont
AddFontFromFileTTF(
    filename: str,
    size_pixels: float,
    ) -> ImFont
AddFontFromMemoryCompressedBase85TTF(
    compressed_font_data_base85: str,
    size_pixels: float,
    ) -> ImFont
RemoveFont(font: ImFont) -> None
Clear() -> None
CompactCache() -> None
Build() -> bool
```

### ImFont

**Properties:**

```python
Scale: float
OwnerAtlas: ImFontAtlas
```

**Methods:**

```python
IsLoaded() -> bool
GetDebugName() -> str
CalcTextSizeA(
    size: float,
    max_width: float,
    wrap_width: float,
    text_begin: str,
    ) -> tuple[float, float]
CalcWordWrapPosition(
    size: float,
    text: str,
    wrap_width: float,
    ) -> str
GetFontBaked(
    font_size: float,
    density: float = -1.0,
    ) -> ImFontBaked
```

## Enums

### ImGuiDir

```python
ImGuiDir_None = -1
ImGuiDir_Left = 0
ImGuiDir_Right = 1
ImGuiDir_Up = 2
ImGuiDir_Down = 3
ImGuiDir_COUNT = 4
```

### ImGuiSortDirection

```python
ImGuiSortDirection_None = 0
ImGuiSortDirection_Ascending = 1
ImGuiSortDirection_Descending = 2
```

### ImGuiWindowFlags

```python
ImGuiWindowFlags_None = 0
ImGuiWindowFlags_NoTitleBar = 1
ImGuiWindowFlags_NoResize = 2
ImGuiWindowFlags_NoMove = 4
ImGuiWindowFlags_NoScrollbar = 8
ImGuiWindowFlags_NoScrollWithMouse = 16
ImGuiWindowFlags_NoCollapse = 32
ImGuiWindowFlags_AlwaysAutoResize = 64
ImGuiWindowFlags_NoBackground = 128
ImGuiWindowFlags_NoSavedSettings = 256
ImGuiWindowFlags_NoMouseInputs = 512
ImGuiWindowFlags_MenuBar = 1024
ImGuiWindowFlags_HorizontalScrollbar = 2048
ImGuiWindowFlags_NoFocusOnAppearing = 4096
ImGuiWindowFlags_NoBringToFrontOnFocus = 8192
ImGuiWindowFlags_AlwaysVerticalScrollbar = 16384
ImGuiWindowFlags_AlwaysHorizontalScrollbar = 32768
ImGuiWindowFlags_NoNavInputs = 65536
ImGuiWindowFlags_NoNavFocus = 131072
ImGuiWindowFlags_UnsavedDocument = 262144
ImGuiWindowFlags_NoNav = 196608
ImGuiWindowFlags_NoDecoration = 43
ImGuiWindowFlags_NoInputs = 197120
ImGuiWindowFlags_ChildWindow = 16777216
ImGuiWindowFlags_Tooltip = 33554432
ImGuiWindowFlags_Popup = 67108864
ImGuiWindowFlags_Modal = 134217728
ImGuiWindowFlags_ChildMenu = 268435456
```

### ImGuiChildFlags

```python
ImGuiChildFlags_None = 0
ImGuiChildFlags_Borders = 1
ImGuiChildFlags_AlwaysUseWindowPadding = 2
ImGuiChildFlags_ResizeX = 4
ImGuiChildFlags_ResizeY = 8
ImGuiChildFlags_AutoResizeX = 16
ImGuiChildFlags_AutoResizeY = 32
ImGuiChildFlags_AlwaysAutoResize = 64
ImGuiChildFlags_FrameStyle = 128
ImGuiChildFlags_NavFlattened = 256
```

### ImGuiItemFlags

```python
ImGuiItemFlags_None = 0
ImGuiItemFlags_NoTabStop = 1
ImGuiItemFlags_NoNav = 2
ImGuiItemFlags_NoNavDefaultFocus = 4
ImGuiItemFlags_ButtonRepeat = 8
ImGuiItemFlags_AutoClosePopups = 16
ImGuiItemFlags_AllowDuplicateId = 32
```

### ImGuiInputTextFlags

```python
ImGuiInputTextFlags_None = 0
ImGuiInputTextFlags_CharsDecimal = 1
ImGuiInputTextFlags_CharsHexadecimal = 2
ImGuiInputTextFlags_CharsScientific = 4
ImGuiInputTextFlags_CharsUppercase = 8
ImGuiInputTextFlags_CharsNoBlank = 16
ImGuiInputTextFlags_AllowTabInput = 32
ImGuiInputTextFlags_EnterReturnsTrue = 64
ImGuiInputTextFlags_EscapeClearsAll = 128
ImGuiInputTextFlags_CtrlEnterForNewLine = 256
ImGuiInputTextFlags_ReadOnly = 512
ImGuiInputTextFlags_Password = 1024
ImGuiInputTextFlags_AlwaysOverwrite = 2048
ImGuiInputTextFlags_AutoSelectAll = 4096
ImGuiInputTextFlags_ParseEmptyRefVal = 8192
ImGuiInputTextFlags_DisplayEmptyRefVal = 16384
ImGuiInputTextFlags_NoHorizontalScroll = 32768
ImGuiInputTextFlags_NoUndoRedo = 65536
ImGuiInputTextFlags_ElideLeft = 131072
ImGuiInputTextFlags_CallbackCompletion = 262144
ImGuiInputTextFlags_CallbackHistory = 524288
ImGuiInputTextFlags_CallbackAlways = 1048576
ImGuiInputTextFlags_CallbackCharFilter = 2097152
ImGuiInputTextFlags_CallbackResize = 4194304
ImGuiInputTextFlags_CallbackEdit = 8388608
ImGuiInputTextFlags_WordWrap = 16777216
```

### ImGuiTreeNodeFlags

```python
ImGuiTreeNodeFlags_None = 0
ImGuiTreeNodeFlags_Selected = 1
ImGuiTreeNodeFlags_Framed = 2
ImGuiTreeNodeFlags_AllowOverlap = 4
ImGuiTreeNodeFlags_NoTreePushOnOpen = 8
ImGuiTreeNodeFlags_NoAutoOpenOnLog = 16
ImGuiTreeNodeFlags_DefaultOpen = 32
ImGuiTreeNodeFlags_OpenOnDoubleClick = 64
ImGuiTreeNodeFlags_OpenOnArrow = 128
ImGuiTreeNodeFlags_Leaf = 256
ImGuiTreeNodeFlags_Bullet = 512
ImGuiTreeNodeFlags_FramePadding = 1024
ImGuiTreeNodeFlags_SpanAvailWidth = 2048
ImGuiTreeNodeFlags_SpanFullWidth = 4096
ImGuiTreeNodeFlags_SpanLabelWidth = 8192
ImGuiTreeNodeFlags_SpanAllColumns = 16384
ImGuiTreeNodeFlags_LabelSpanAllColumns = 32768
ImGuiTreeNodeFlags_NavLeftJumpsToParent = 131072
ImGuiTreeNodeFlags_CollapsingHeader = 26
ImGuiTreeNodeFlags_DrawLinesNone = 262144
ImGuiTreeNodeFlags_DrawLinesFull = 524288
ImGuiTreeNodeFlags_DrawLinesToNodes = 1048576
```

### ImGuiListClipperFlags

```python
ImGuiListClipperFlags_None = 0
ImGuiListClipperFlags_NoSetTableRowCounters = 1
```

### ImGuiPopupFlags

```python
ImGuiPopupFlags_None = 0
ImGuiPopupFlags_MouseButtonLeft = 0
ImGuiPopupFlags_MouseButtonRight = 1
ImGuiPopupFlags_MouseButtonMiddle = 2
ImGuiPopupFlags_NoReopen = 32
ImGuiPopupFlags_NoOpenOverExistingPopup = 128
ImGuiPopupFlags_NoOpenOverItems = 256
ImGuiPopupFlags_AnyPopupId = 1024
ImGuiPopupFlags_AnyPopupLevel = 2048
ImGuiPopupFlags_AnyPopup = 3072
```

### ImGuiMultiSelectFlags

```python
ImGuiMultiSelectFlags_None = 0
ImGuiMultiSelectFlags_SingleSelect = 1
ImGuiMultiSelectFlags_NoSelectAll = 2
ImGuiMultiSelectFlags_NoRangeSelect = 4
ImGuiMultiSelectFlags_NoAutoSelect = 8
ImGuiMultiSelectFlags_NoAutoClear = 16
ImGuiMultiSelectFlags_NoAutoClearOnReselect = 32
ImGuiMultiSelectFlags_BoxSelect1d = 64
ImGuiMultiSelectFlags_BoxSelect2d = 128
ImGuiMultiSelectFlags_BoxSelectNoScroll = 256
ImGuiMultiSelectFlags_ClearOnEscape = 512
ImGuiMultiSelectFlags_ClearOnClickVoid = 1024
ImGuiMultiSelectFlags_ScopeWindow = 2048
ImGuiMultiSelectFlags_ScopeRect = 4096
ImGuiMultiSelectFlags_SelectOnClick = 8192
ImGuiMultiSelectFlags_SelectOnClickRelease = 16384
ImGuiMultiSelectFlags_NavWrapX = 65536
ImGuiMultiSelectFlags_NoSelectOnRightClick = 131072
```

### ImGuiSelectableFlags

```python
ImGuiSelectableFlags_None = 0
ImGuiSelectableFlags_DontClosePopups = 1
ImGuiSelectableFlags_SpanAllColumns = 2
ImGuiSelectableFlags_AllowDoubleClick = 4
ImGuiSelectableFlags_Disabled = 8
ImGuiSelectableFlags_AllowOverlap = 16
```

### ImGuiComboFlags

```python
ImGuiComboFlags_None = 0
ImGuiComboFlags_PopupAlignLeft = 1
ImGuiComboFlags_HeightSmall = 2
ImGuiComboFlags_HeightRegular = 4
ImGuiComboFlags_HeightLarge = 8
ImGuiComboFlags_HeightLargest = 16
ImGuiComboFlags_NoArrowButton = 32
ImGuiComboFlags_NoPreview = 64
```

### ImGuiTabBarFlags

```python
ImGuiTabBarFlags_None = 0
ImGuiTabBarFlags_Reorderable = 1
ImGuiTabBarFlags_AutoSelectNewTabs = 2
ImGuiTabBarFlags_TabListPopupButton = 4
ImGuiTabBarFlags_NoCloseWithMiddleMouseButton = 8
ImGuiTabBarFlags_NoTabListScrollingButtons = 16
ImGuiTabBarFlags_NoTooltip = 32
ImGuiTabBarFlags_FittingPolicyMixed = 128
ImGuiTabBarFlags_FittingPolicyShrink = 256
ImGuiTabBarFlags_FittingPolicyScroll = 512
```

### ImGuiTabItemFlags

```python
ImGuiTabItemFlags_None = 0
ImGuiTabItemFlags_UnsavedDocument = 1
ImGuiTabItemFlags_SetSelected = 2
ImGuiTabItemFlags_NoCloseWithMiddleMouseButton = 4
ImGuiTabItemFlags_NoPushId = 8
```

### ImGuiFocusedFlags

```python
ImGuiFocusedFlags_None = 0
ImGuiFocusedFlags_ChildWindows = 1
ImGuiFocusedFlags_RootWindow = 2
ImGuiFocusedFlags_AnyWindow = 4
ImGuiFocusedFlags_RootAndChildWindows = 3
```

### ImGuiHoveredFlags

```python
ImGuiHoveredFlags_None = 0
ImGuiHoveredFlags_ChildWindows = 1
ImGuiHoveredFlags_RootWindow = 2
ImGuiHoveredFlags_AnyWindow = 4
ImGuiHoveredFlags_AllowWhenBlockedByPopup = 32
ImGuiHoveredFlags_AllowWhenBlockedByActiveItem = 128
ImGuiHoveredFlags_AllowWhenOverlapped = 768
ImGuiHoveredFlags_AllowWhenDisabled = 1024
ImGuiHoveredFlags_RectOnly = 928
ImGuiHoveredFlags_RootAndChildWindows = 3
```

### ImGuiDragDropFlags

```python
ImGuiDragDropFlags_None = 0
ImGuiDragDropFlags_SourceNoPreviewTooltip = 1
ImGuiDragDropFlags_SourceNoDisableHover = 2
ImGuiDragDropFlags_SourceNoHoldToOpenOthers = 4
ImGuiDragDropFlags_SourceAllowNullID = 8
ImGuiDragDropFlags_SourceExtern = 16
ImGuiDragDropFlags_SourceAutoExpirePayload = 32
ImGuiDragDropFlags_AcceptBeforeDelivery = 1024
ImGuiDragDropFlags_AcceptNoDrawDefaultRect = 2048
ImGuiDragDropFlags_AcceptNoPreviewTooltip = 4096
ImGuiDragDropFlags_AcceptDrawAsHovered = 8192
ImGuiDragDropFlags_AcceptPeekOnly = 3072
```

### ImGuiDataType

```python
ImGuiDataType_S8 = 0
ImGuiDataType_U8 = 1
ImGuiDataType_S16 = 2
ImGuiDataType_U16 = 3
ImGuiDataType_S32 = 4
ImGuiDataType_U32 = 5
ImGuiDataType_S64 = 6
ImGuiDataType_U64 = 7
ImGuiDataType_Float = 8
ImGuiDataType_Double = 9
ImGuiDataType_COUNT = 12
```

### ImGuiInputFlags

```python
ImGuiInputFlags_None = 0
ImGuiInputFlags_Repeat = 1
ImGuiInputFlags_RouteActive = 1024
ImGuiInputFlags_RouteFocused = 2048
ImGuiInputFlags_RouteGlobal = 4096
ImGuiInputFlags_RouteAlways = 8192
ImGuiInputFlags_RouteOverFocused = 16384
ImGuiInputFlags_RouteOverActive = 32768
ImGuiInputFlags_RouteUnlessBgFocused = 65536
ImGuiInputFlags_RouteFromRootWindow = 131072
ImGuiInputFlags_Tooltip = 262144
```

### ImGuiConfigFlags

```python
ImGuiConfigFlags_None = 0
ImGuiConfigFlags_NavEnableKeyboard = 1
ImGuiConfigFlags_NavEnableGamepad = 2
ImGuiConfigFlags_NavEnableSetMousePos = 4
ImGuiConfigFlags_NavNoCaptureKeyboard = 8
ImGuiConfigFlags_NoMouse = 16
ImGuiConfigFlags_NoMouseCursorChange = 32
ImGuiConfigFlags_IsSRGB = 1048576
ImGuiConfigFlags_IsTouchScreen = 2097152
```

### ImGuiBackendFlags

```python
ImGuiBackendFlags_None = 0
ImGuiBackendFlags_HasGamepad = 1
ImGuiBackendFlags_HasMouseCursors = 2
ImGuiBackendFlags_HasSetMousePos = 4
ImGuiBackendFlags_RendererHasVtxOffset = 8
```

### ImGuiCol

```python
ImGuiCol_Text = 0
ImGuiCol_TextDisabled = 1
ImGuiCol_WindowBg = 2
ImGuiCol_ChildBg = 3
ImGuiCol_PopupBg = 4
ImGuiCol_Border = 5
ImGuiCol_BorderShadow = 6
ImGuiCol_FrameBg = 7
ImGuiCol_FrameBgHovered = 8
ImGuiCol_FrameBgActive = 9
ImGuiCol_TitleBg = 10
ImGuiCol_TitleBgActive = 11
ImGuiCol_TitleBgCollapsed = 12
ImGuiCol_MenuBarBg = 13
ImGuiCol_ScrollbarBg = 14
ImGuiCol_ScrollbarGrab = 15
ImGuiCol_ScrollbarGrabHovered = 16
ImGuiCol_ScrollbarGrabActive = 17
ImGuiCol_CheckMark = 18
ImGuiCol_SliderGrab = 19
ImGuiCol_SliderGrabActive = 20
ImGuiCol_Button = 21
ImGuiCol_ButtonHovered = 22
ImGuiCol_ButtonActive = 23
ImGuiCol_Header = 24
ImGuiCol_HeaderHovered = 25
ImGuiCol_HeaderActive = 26
ImGuiCol_Separator = 27
ImGuiConl_SeparatorHovered = 28
ImGuiCol_SeparatorActive = 29
ImGuiCol_ResizeGrip = 30
ImGuiCol_ResizeGripHovered = 31
ImGuiCol_ResizeGripActive = 32
ImGuiCol_InputTextCursor = 33
ImGuiCol_TabHovered = 34
ImGuiCol_Tab = 35
ImGuiCol_TabSelected = 36
ImGuiCol_TabSelectedOverline = 37
ImGuiCol_TabDimmed = 38
ImGuiCol_TabDimmedSelected = 39
ImGuiCol_TabDimmedSelectedOverline = 40
ImGuiCol_TabUnfocused = 38
ImGuiCol_TabUnfocusedActive = 39
ImGuiCol_PlotLines = 41
ImGuiCol_PlotLinesHovered = 42
ImGuiCol_PlotHistogram = 43
ImGuiCol_PlotHistogramHovered = 44
ImGuiCol_TableHeaderBg = 45
ImGuiCol_TableBorderStrong = 46
ImGuiCol_TableBorderLight = 47
ImGuiCol_TableRowBg = 48
ImGuiCol_TableRowBgAlt = 49
ImGuiCol_TextLink = 50
ImGuiCol_TextSelectedBg = 51
ImGuiCol_DragDropTarget = 53
ImGuiCol_NavCursor = 56
ImGuiCol_NavWindowingHighlight = 57
ImGuiCol_NavWindowingDimBg = 58
ImGuiCol_ModalWindowDimBg = 59
ImGuiCol_COUNT = 60
```

### ImGuiStyleVar

```python
ImGuiStyleVar_Alpha = 0
ImGuiStyleVar_DisabledAlpha = 1
ImGuiStyleVar_WindowPadding = 2
ImGuiStyleVar_WindowRounding = 3
ImGuiStyleVar_WindowBorderSize = 4
ImGuiStyleVar_WindowMinSize = 5
ImGuiStyleVar_WindowTitleAlign = 6
ImGuiStyleVar_ChildRounding = 7
ImGuiStyleVar_ChildBorderSize = 8
ImGuiStyleVar_PopupRounding = 9
ImGuiStyleVar_PopupBorderSize = 10
ImGuiStyleVar_FramePadding = 11
ImGuiStyleVar_FrameRounding = 12
ImGuiStyleVar_FrameBorderSize = 13
ImGuiStyleVar_ItemSpacing = 14
ImGuiStyleVar_ItemInnerSpacing = 15
ImGuiStyleVar_IndentSpacing = 16
ImGuiStyleVar_CellPadding = 17
ImGuiStyleVar_ScrollbarSize = 18
ImGuiStyleVar_ScrollbarRounding = 19
ImGuiStyleVar_ScrollbarPadding = 20
ImGuiStyleVar_GrabMinSize = 21
ImGuiStyleVar_GrabRounding = 22
ImGuiStyleVar_ImageBorderSize = 23
ImGuiStyleVar_TabRounding = 24
ImGuiStyleVar_TabBorderSize = 25
ImGuiStyleVar_TabMinWidthBase = 26
ImGuiStyleVar_TabMinWidthShrink = 27
ImGuiStyleVar_TabBarBorderSize = 28
ImGuiStyleVar_TabBarOverlineSize = 29
ImGuiStyleVar_TableAngledHeadersAngle = 30
ImGuiStyleVar_TableAngledHeadersTextAlign = 31
ImGuiStyleVar_TreeLinesSize = 32
ImGuiStyleVar_TreeLinesRounding = 33
ImGuiStyleVar_ButtonTextAlign = 34
ImGuiStyleVar_SelectableTextAlign = 35
ImGuiStyleVar_SeparatorTextBorderSize = 36
ImGuiStyleVar_SeparatorTextAlign = 37
ImGuiStyleVar_SeparatorTextPadding = 38
```

### ImGuiButtonFlags

```python
ImGuiButtonFlags_None = 0
ImGuiButtonFlags_MouseButtonLeft = 1
ImGuiButtonFlags_MouseButtonRight = 2
ImGuiButtonFlags_MouseButtonMiddle = 4
ImGuiButtonFlags_EnableNav = 8
```

### ImGuiColorEditFlags

```python
ImGuiColorEditFlags_None = 0
ImGuiColorEditFlags_NoAlpha = 2
ImGuiColorEditFlags_NoPicker = 4
ImGuiColorEditFlags_NoOptions = 8
ImGuiColorEditFlags_NoSmallPreview = 16
ImGuiColorEditFlags_NoInputs = 32
ImGuiColorEditFlags_NoTooltip = 64
ImGuiColorEditFlags_NoLabel = 128
ImGuiColorEditFlags_NoSidePreview = 256
ImGuiColorEditFlags_NoDragDrop = 512
ImGuiColorEditFlags_NoBorder = 1024
ImGuiColorEditFlags_AlphaBar = 262144
ImGuiColorEditFlags_AlphaPreview = 0
ImGuiColorEditFlags_AlphaPreviewHalf = 16384
ImGuiColorEditFlags_HDR = 524288
ImGuiColorEditFlags_DisplayRGB = 1048576
ImGuiColorEditFlags_DisplayHSV = 2097152
ImGuiColorEditFlags_DisplayHex = 4194304
ImGuiColorEditFlags_Uint8 = 8388608
ImGuiColorEditFlags_Float = 16777216
ImGuiColorEditFlags_PickerHueBar = 33554432
ImGuiColorEditFlags_PickerHueWheel = 67108864
ImGuiColorEditFlags_InputRGB = 134217728
ImGuiColorEditFlags_InputHSV = 268435456
```

### ImGuiSliderFlags

```python
ImGuiSliderFlags_None = 0
ImGuiSliderFlags_Logarithmic = 32
ImGuiSliderFlags_NoRoundToFormat = 64
ImGuiSliderFlags_NoInput = 128
ImGuiSliderFlags_WrapAround = 256
ImGuiSliderFlags_ClampOnInput = 512
ImGuiSliderFlags_ClampZeroRange = 1024
ImGuiSliderFlags_NoSpeedTweaks = 2048
ImGuiSliderFlags_AlwaysClamp = 1536
```

### ImGuiMouseButton

```python
ImGuiMouseButton_Left = 0
ImGuiMouseButton_Right = 1
ImGuiMouseButton_Middle = 2
ImGuiMouseButton_COUNT = 5
```

### ImGuiMouseCursor

```python
ImGuiMouseCursor_None = -1
ImGuiMouseCursor_Arrow = 0
ImGuiMouseCursor_TextInput = 1
ImGuiMouseCursor_ResizeAll = 2
ImGuiMouseCursor_ResizeNS = 3
ImGuiMouseCursor_ResizeEW = 4
ImGuiMouseCursor_ResizeNESW = 5
ImGuiMouseCursor_ResizeNWSE = 6
ImGuiMouseCursor_Hand = 7
ImGuiMouseCursor_NotAllowed = 10
ImGuiMouseCursor_COUNT = 11
```

### ImGuiMouseSource

```python
ImGuiMouseSource_Mouse = 0
ImGuiMouseSource_TouchScreen = 1
ImGuiMouseSource_Pen = 2
ImGuiMouseSource_COUNT = 3
```

### ImGuiCond

```python
ImGuiCond_Always = 1
ImGuiCond_Once = 2
ImGuiCond_FirstUseEver = 4
ImGuiCond_Appearing = 8
```

### ImGuiTableFlags

```python
ImGuiTableFlags_None = 0
ImGuiTableFlags_Resizable = 1
ImGuiTableFlags_Reorderable = 2
ImGuiTableFlags_Hideable = 4
ImGuiTableFlags_Sortable = 8
ImGuiTableFlags_NoSavedSettings = 16
ImGuiTableFlags_ContextMenuInBody = 32
ImGuiTableFlags_RowBg = 64
ImGuiTableFlags_BordersInnerH = 128
ImGuiTableFlags_BordersOuterH = 256
ImGuiTableFlags_BordersInnerV = 512
ImGuiTableFlags_BordersOuterV = 1024
ImGuiTableFlags_BordersH = 384
ImGuiTableFlags_BordersV = 1536
ImGuiTableFlags_BordersInner = 640
ImGuiTableFlags_BordersOuter = 1280
ImGuiTableFlags_Borders = 1920
ImGuiTableFlags_NoBordersInBody = 2048
ImGuiTableFlags_NoBordersInBodyUntilResize = 4096
ImGuiTableFlags_SizingFixedFit = 8192
ImGuiTableFlags_SizingFixedSame = 16384
ImGuiTableFlags_SizingStretchProp = 24576
ImGuiTableFlags_SizingStretchSame = 32768
ImGuiTableFlags_NoHostExtendX = 65536
ImGuiTableFlags_NoHostExtendY = 131072
ImGuiTableFlags_NoKeepColumnsVisible = 262144
ImGuiTableFlags_PreciseWidths = 524288
ImGuiTableFlags_NoClip = 1048576
ImGuiTableFlags_PadOuterX = 2097152
ImGuiTableFlags_NoPadOuterX = 4194304
ImGuiTableFlags_NoPadInnerX = 8388608
ImGuiTableFlags_ScrollX = 16777216
ImGuiTableFlags_ScrollY = 33554432
ImGuiTableFlags_SortMulti = 67108864
ImGuiTableFlags_SortTristate = 134217728
ImGuiTableFlags_HighlightHoveredColumn = 268435456
```

### ImGuiTableColumnFlags

```python
ImGuiTableColumnFlags_None = 0
ImGuiTableColumnFlags_Disabled = 1
ImGuiTableColumnFlags_DefaultHide = 2
ImGuiTableColumnFlags_DefaultSort = 4
ImGuiTableColumnFlags_WidthStretch = 8
ImGuiTableColumnFlags_WidthFixed = 16
ImGuiTableColumnFlags_NoResize = 32
ImGuiTableColumnFlags_NoReorder = 64
ImGuiTableColumnFlags_NoHide = 128
ImGuiTableColumnFlags_NoClip = 256
ImGuiTableColumnFlags_NoSort = 512
ImGuiTableColumnFlags_NoSortAscending = 1024
ImGuiTableColumnFlags_NoSortDescending = 2048
ImGuiTableColumnFlags_NoHeaderLabel = 4096
ImGuiTableColumnFlags_NoHeaderWidth = 8192
ImGuiTableColumnFlags_PreferSortAscending = 16384
ImGuiTableColumnFlags_PreferSortDescending = 32768
ImGuiTableColumnFlags_IndentEnable = 65536
ImGuiTableColumnFlags_IndentDisable = 131072
ImGuiTableColumnFlags_AngledHeader = 262144
ImGuiTableColumnFlags_IsEnabled = 16777216
ImGuiTableColumnFlags_IsVisible = 33554432
ImGuiTableColumnFlags_IsSorted = 67108864
ImGuiTableColumnFlags_IsHovered = 134217728
```

### ImGuiTableRowFlags

```python
ImGuiTableRowFlags_None = 0
ImGuiTableRowFlags_Headers = 1
```

### ImGuiTableBgTarget

```python
ImGuiTableBgTarget_None = 0
ImGuiTableBgTarget_RowBg0 = 1
ImGuiTableBgTarget_RowBg1 = 2
ImGuiTableBgTarget_CellBg = 3
```

### ImDrawFlags

```python
ImDrawFlags_None = 0
ImDrawFlags_Closed = 1
ImDrawFlags_RoundCornersTopLeft = 16
ImDrawFlags_RoundCornersTopRight = 32
ImDrawFlags_RoundCornersBottomLeft = 64
ImDrawFlags_RoundCornersBottomRight = 128
ImDrawFlags_RoundCornersNone = 256
ImDrawFlags_RoundCornersTop = 48
ImDrawFlags_RoundCornersBottom = 192
ImDrawFlags_RoundCornersLeft = 80
ImDrawFlags_RoundCornersRight = 160
ImDrawFlags_RoundCornersAll = 240
```

### ImGuiKey

```python
ImGuiKey_None = 0
ImGuiKey_Tab = 512
ImGuiKey_LeftArrow = 513
ImGuiKey_RightArrow = 514
ImGuiKey_UpArrow = 515
ImGuiKey_DownArrow = 516
ImGuiKey_PageUp = 517
ImGuiKey_PageDown = 518
ImGuiKey_Home = 519
ImGuiKey_End = 520
ImGuiKey_Insert = 521
ImGuiKey_Delete = 522
ImGuiKey_Backspace = 523
ImGuiKey_Space = 524
ImGuiKey_Enter = 525
ImGuiKey_Escape = 526
ImGuiKey_LeftCtrl = 527
ImGuiKey_LeftShift = 528
ImGuiKey_LeftAlt = 529
ImGuiKey_LeftSuper = 530
ImGuiKey_RightCtrl = 531
ImGuiKey_RightShift = 532
ImGuiKey_RightAlt = 533
ImGuiKey_RightSuper = 534
ImGuiKey_Menu = 535
ImGuiKey_0 = 536
ImGuiKey_1 = 537
ImGuiKey_2 = 538
ImGuiKey_3 = 539
ImGuiKey_4 = 540
ImGuiKey_5 = 541
ImGuiKey_6 = 542
ImGuiKey_7 = 543
ImGuiKey_8 = 544
ImGuiKey_9 = 545
ImGuiKey_A = 546
ImGuiKey_B = 547
ImGuiKey_C = 548
ImGuiKey_D = 549
ImGuiKey_E = 550
ImGuiKey_F = 551
ImGuiKey_G = 552
ImGuiKey_H = 553
ImGuiKey_I = 554
ImGuiKey_J = 555
ImGuiKey_K = 556
ImGuiKey_L = 557
ImGuiKey_M = 558
ImGuiKey_N = 559
ImGuiKey_O = 560
ImGuiKey_P = 561
ImGuiKey_Q = 562
ImGuiKey_R = 563
ImGuiKey_S = 564
ImGuiKey_T = 565
ImGuiKey_U = 566
ImGuiKey_V = 567
ImGuiKey_W = 568
ImGuiKey_X = 569
ImGuiKey_Y = 570
ImGuiKey_Z = 571
ImGuiKey_F1 = 572
ImGuiKey_F2 = 573
ImGuiKey_F3 = 574
ImGuiKey_F4 = 575
ImGuiKey_F5 = 576
ImGuiKey_F6 = 577
ImGuiKey_F7 = 578
ImGuiKey_F8 = 579
ImGuiKey_F9 = 580
ImGuiKey_F10 = 581
ImGuiKey_F11 = 582
ImGuiKey_F12 = 583
ImGuiKey_F13 = 584
ImGuiKey_F14 = 585
ImGuiKey_F15 = 586
ImGuiKey_F16 = 587
ImGuiKey_F17 = 588
ImGuiKey_F18 = 589
ImGuiKey_F19 = 590
ImGuiKey_F20 = 591
ImGuiKey_F21 = 592
ImGuiKey_F22 = 593
ImGuiKey_F23 = 594
ImGuiKey_F24 = 595
ImGuiKey_Apostrophe = 596
ImGuiKey_Comma = 597
ImGuiKey_Minus = 598
ImGuiKey_Period = 599
ImGuiKey_Slash = 600
ImGuiKey_Semicolon = 601
ImGuiKey_Equal = 602
ImGuiKey_LeftBracket = 603
ImGuiKey_Backslash = 604
ImGuiKey_RightBracket = 605
ImGuiKey_GraveAccent = 606
ImGuiKey_CapsLock = 607
ImGuiKey_ScrollLock = 608
ImGuiKey_NumLock = 609
ImGuiKey_PrintScreen = 610
ImGuiKey_Pause = 611
ImGuiKey_Keypad0 = 612
ImGuiKey_Keypad1 = 613
ImGuiKey_Keypad2 = 614
ImGuiKey_Keypad3 = 615
ImGuiKey_Keypad4 = 616
ImGuiKey_Keypad5 = 617
ImGuiKey_Keypad6 = 618
ImGuiKey_Keypad7 = 619
ImGuiKey_Keypad8 = 620
ImGuiKey_Keypad9 = 621
ImGuiKey_KeypadDecimal = 622
ImGuiKey_KeypadDivide = 623
ImGuiKey_KeypadMultiply = 624
ImGuiKey_KeypadSubtract = 625
ImGuiKey_KeypadAdd = 626
ImGuiKey_KeypadEnter = 627
ImGuiKey_KeypadEqual = 628
ImGuiKey_AppBack = 629
ImGuiKey_AppForward = 630
ImGuiKey_GamepadStart = 632
ImGuiKey_GamepadBack = 633
ImGuiKey_GamepadFaceUp = 636
ImGuiKey_GamepadFaceDown = 637
ImGuiKey_GamepadFaceLeft = 634
ImGuiKey_GamepadFaceRight = 635
ImGuiKey_GamepadDpadUp = 640
ImGuiKey_GamepadDpadDown = 641
ImGuiKey_GamepadDpadLeft = 638
ImGuiKey_GamepadDpadRight = 639
ImGuiKey_GamepadL1 = 642
ImGuiKey_GamepadR1 = 643
ImGuiKey_GamepadL2 = 644
ImGuiKey_GamepadR2 = 645
ImGuiKey_GamepadL3 = 646
ImGuiKey_GamepadR3 = 647
ImGuiKey_GamepadLStickUp = 650
ImGuiKey_GamepadLStickDown = 651
ImGuiKey_GamepadLStickLeft = 648
ImGuiKey_GamepadLStickRight = 649
ImGuiKey_GamepadRStickUp = 654
ImGuiKey_GamepadRStickDown = 655
ImGuiKey_GamepadRStickLeft = 652
ImGuiKey_GamepadRStickRight = 653
ImGuiMod_None = 0
ImGuiMod_Ctrl = 4096
ImGuiMod_Shift = 8192
ImGuiMod_Alt = 16384
ImGuiMod_Super = 32768
```

### ImTextureFormat

```python
ImTextureFormat_RGBA32 = 0
ImTextureFormat_Alpha8 = 1
```

### ImTextureStatus

```python
ImTextureStatus_OK = 0
ImTextureStatus_Destroyed = 1
ImTextureStatus_WantCreate = 2
ImTextureStatus_WantUpdates = 3
ImTextureStatus_WantDestroy = 4
```

### ImFontAtlasFlags

```python
ImFontAtlasFlags_None = 0
ImFontAtlasFlags_NoPowerOfTwoHeight = 1
ImFontAtlasFlags_NoMouseCursors = 2
ImFontAtlasFlags_NoBakedLines = 4
```

### ImFontFlags

```python
ImFontFlags_None = 0
ImFontFlags_NoLoadError = 2
ImFontFlags_NoLoadGlyphs = 4
ImFontFlags_LockBakedSizes = 8
```

### ImGuiViewportFlags

```python
ImGuiViewportFlags_None = 0
ImGuiViewportFlags_IsPlatformWindow = 1
ImGuiViewportFlags_IsPlatformMonitor = 2
ImGuiViewportFlags_OwnedByApp = 4
```
