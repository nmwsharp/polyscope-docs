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

### ImGuiDir

### ImGuiSortDirection

### ImGuiKey

### ImGuiMouseSource

### ImGuiSelectionRequestType

### ImTextureFormat

### ImTextureStatus

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

### ImGuiStyleColorsWrapper

**Methods:**

```python
__getitem__() -> tuple[float, float, float, float]
__setitem__() -> None
__len__() -> int
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
Colors: ImGuiStyleColorsWrapper
HoverStationaryDelay: float
HoverDelayShort: float
HoverDelayNormal: float
HoverFlagsForTooltipMouse: int
HoverFlagsForTooltipNav: int
```

**Methods:**

```python
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
