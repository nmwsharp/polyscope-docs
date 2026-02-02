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

## Constants

```python
ImGuiWindowFlags_None: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_None
ImGuiWindowFlags_NoTitleBar: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoTitleBar
ImGuiWindowFlags_NoResize: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoResize
ImGuiWindowFlags_NoMove: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoMove
ImGuiWindowFlags_NoScrollbar: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoScrollbar
ImGuiWindowFlags_NoScrollWithMouse: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_NoCollapse: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoCollapse
ImGuiWindowFlags_AlwaysAutoResize: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_NoBackground: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoBackground
ImGuiWindowFlags_NoSavedSettings: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_NoMouseInputs: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoMouseInputs
ImGuiWindowFlags_MenuBar: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_MenuBar
ImGuiWindowFlags_HorizontalScrollbar: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_NoFocusOnAppearing: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_NoBringToFrontOnFocus: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_AlwaysVerticalScrollbar: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_AlwaysHorizontalScrollbar: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_NoNavInputs: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoNavInputs
ImGuiWindowFlags_NoNavFocus: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoNavFocus
ImGuiWindowFlags_UnsavedDocument: ImGuiWindowFlags_ = ...
ImGuiWindowFlags_NoNav: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoNav
ImGuiWindowFlags_NoDecoration: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoDecoration
ImGuiWindowFlags_NoInputs: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_NoInputs
ImGuiWindowFlags_ChildWindow: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_ChildWindow
ImGuiWindowFlags_Tooltip: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_Tooltip
ImGuiWindowFlags_Popup: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_Popup
ImGuiWindowFlags_Modal: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_Modal
ImGuiWindowFlags_ChildMenu: ImGuiWindowFlags_ = ImGuiWindowFlags_.ImGuiWindowFlags_ChildMenu
ImGuiChildFlags_None: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_None
ImGuiChildFlags_Borders: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_Borders
ImGuiChildFlags_AlwaysUseWindowPadding: ImGuiChildFlags_ = ...
ImGuiChildFlags_ResizeX: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_ResizeX
ImGuiChildFlags_ResizeY: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_ResizeY
ImGuiChildFlags_AutoResizeX: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_AutoResizeX
ImGuiChildFlags_AutoResizeY: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_AutoResizeY
ImGuiChildFlags_AlwaysAutoResize: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_AlwaysAutoResize
ImGuiChildFlags_FrameStyle: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_FrameStyle
ImGuiChildFlags_NavFlattened: ImGuiChildFlags_ = ImGuiChildFlags_.ImGuiChildFlags_NavFlattened
ImGuiItemFlags_None: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_None
ImGuiItemFlags_NoTabStop: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_NoTabStop
ImGuiItemFlags_NoNav: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_NoNav
ImGuiItemFlags_NoNavDefaultFocus: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_NoNavDefaultFocus
ImGuiItemFlags_ButtonRepeat: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_ButtonRepeat
ImGuiItemFlags_AutoClosePopups: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_AutoClosePopups
ImGuiItemFlags_AllowDuplicateId: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_AllowDuplicateId
ImGuiItemFlags_Disabled: ImGuiItemFlags_ = ImGuiItemFlags_.ImGuiItemFlags_Disabled
ImGuiInputTextFlags_None: ImGuiInputTextFlags_ = ImGuiInputTextFlags_.ImGuiInputTextFlags_None
ImGuiInputTextFlags_CharsDecimal: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CharsHexadecimal: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CharsScientific: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CharsUppercase: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CharsNoBlank: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_AllowTabInput: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_EnterReturnsTrue: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_EscapeClearsAll: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CtrlEnterForNewLine: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_ReadOnly: ImGuiInputTextFlags_ = ImGuiInputTextFlags_.ImGuiInputTextFlags_ReadOnly
ImGuiInputTextFlags_Password: ImGuiInputTextFlags_ = ImGuiInputTextFlags_.ImGuiInputTextFlags_Password
ImGuiInputTextFlags_AlwaysOverwrite: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_AutoSelectAll: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_ParseEmptyRefVal: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_DisplayEmptyRefVal: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_NoHorizontalScroll: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_NoUndoRedo: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_ElideLeft: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CallbackCompletion: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CallbackHistory: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CallbackAlways: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CallbackCharFilter: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CallbackResize: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_CallbackEdit: ImGuiInputTextFlags_ = ...
ImGuiInputTextFlags_WordWrap: ImGuiInputTextFlags_ = ImGuiInputTextFlags_.ImGuiInputTextFlags_WordWrap
ImGuiTreeNodeFlags_None: ImGuiTreeNodeFlags_ = ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_None
ImGuiTreeNodeFlags_Selected: ImGuiTreeNodeFlags_ = ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Selected
ImGuiTreeNodeFlags_Framed: ImGuiTreeNodeFlags_ = ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Framed
ImGuiTreeNodeFlags_AllowOverlap: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_NoTreePushOnOpen: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_NoAutoOpenOnLog: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_DefaultOpen: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_OpenOnDoubleClick: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_OpenOnArrow: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_Leaf: ImGuiTreeNodeFlags_ = ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Leaf
ImGuiTreeNodeFlags_Bullet: ImGuiTreeNodeFlags_ = ImGuiTreeNodeFlags_.ImGuiTreeNodeFlags_Bullet
ImGuiTreeNodeFlags_FramePadding: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_SpanAvailWidth: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_SpanFullWidth: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_SpanLabelWidth: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_SpanAllColumns: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_LabelSpanAllColumns: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_NavLeftJumpsToParent: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_CollapsingHeader: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_DrawLinesNone: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_DrawLinesFull: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_DrawLinesToNodes: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_NavLeftJumpsBackHere: ImGuiTreeNodeFlags_ = ...
ImGuiTreeNodeFlags_SpanTextWidth: ImGuiTreeNodeFlags_ = ...
ImGuiPopupFlags_None: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_None
ImGuiPopupFlags_MouseButtonLeft: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_None
ImGuiPopupFlags_MouseButtonRight: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_MouseButtonRight
ImGuiPopupFlags_MouseButtonMiddle: ImGuiPopupFlags_ = ...
ImGuiPopupFlags_NoReopen: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_NoReopen
ImGuiPopupFlags_NoOpenOverExistingPopup: ImGuiPopupFlags_ = ...
ImGuiPopupFlags_NoOpenOverItems: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_NoOpenOverItems
ImGuiPopupFlags_AnyPopupId: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupId
ImGuiPopupFlags_AnyPopupLevel: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopupLevel
ImGuiPopupFlags_AnyPopup: ImGuiPopupFlags_ = ImGuiPopupFlags_.ImGuiPopupFlags_AnyPopup
ImGuiSelectableFlags_None: ImGuiSelectableFlags_ = ImGuiSelectableFlags_.ImGuiSelectableFlags_None
ImGuiSelectableFlags_NoAutoClosePopups: ImGuiSelectableFlags_ = ...
ImGuiSelectableFlags_SpanAllColumns: ImGuiSelectableFlags_ = ...
ImGuiSelectableFlags_AllowDoubleClick: ImGuiSelectableFlags_ = ...
ImGuiSelectableFlags_Disabled: ImGuiSelectableFlags_ = ...
ImGuiSelectableFlags_AllowOverlap: ImGuiSelectableFlags_ = ...
ImGuiSelectableFlags_Highlight: ImGuiSelectableFlags_ = ...
ImGuiSelectableFlags_SelectOnNav: ImGuiSelectableFlags_ = ...
ImGuiSelectableFlags_DontClosePopups: ImGuiSelectableFlags_ = ...
ImGuiComboFlags_None: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_None
ImGuiComboFlags_PopupAlignLeft: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_PopupAlignLeft
ImGuiComboFlags_HeightSmall: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_HeightSmall
ImGuiComboFlags_HeightRegular: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_HeightRegular
ImGuiComboFlags_HeightLarge: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_HeightLarge
ImGuiComboFlags_HeightLargest: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_HeightLargest
ImGuiComboFlags_NoArrowButton: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_NoArrowButton
ImGuiComboFlags_NoPreview: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_NoPreview
ImGuiComboFlags_WidthFitPreview: ImGuiComboFlags_ = ImGuiComboFlags_.ImGuiComboFlags_WidthFitPreview
ImGuiTabBarFlags_None: ImGuiTabBarFlags_ = ImGuiTabBarFlags_.ImGuiTabBarFlags_None
ImGuiTabBarFlags_Reorderable: ImGuiTabBarFlags_ = ImGuiTabBarFlags_.ImGuiTabBarFlags_Reorderable
ImGuiTabBarFlags_AutoSelectNewTabs: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_TabListPopupButton: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_NoCloseWithMiddleMouseButton: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_NoTabListScrollingButtons: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_NoTooltip: ImGuiTabBarFlags_ = ImGuiTabBarFlags_.ImGuiTabBarFlags_NoTooltip
ImGuiTabBarFlags_DrawSelectedOverline: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_FittingPolicyMixed: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_FittingPolicyShrink: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_FittingPolicyScroll: ImGuiTabBarFlags_ = ...
ImGuiTabBarFlags_FittingPolicyResizeDown: ImGuiTabBarFlags_ = ...
ImGuiTabItemFlags_None: ImGuiTabItemFlags_ = ImGuiTabItemFlags_.ImGuiTabItemFlags_None
ImGuiTabItemFlags_UnsavedDocument: ImGuiTabItemFlags_ = ...
ImGuiTabItemFlags_SetSelected: ImGuiTabItemFlags_ = ImGuiTabItemFlags_.ImGuiTabItemFlags_SetSelected
ImGuiTabItemFlags_NoCloseWithMiddleMouseButton: ImGuiTabItemFlags_ = ...
ImGuiTabItemFlags_NoPushId: ImGuiTabItemFlags_ = ImGuiTabItemFlags_.ImGuiTabItemFlags_NoPushId
ImGuiTabItemFlags_NoTooltip: ImGuiTabItemFlags_ = ImGuiTabItemFlags_.ImGuiTabItemFlags_NoTooltip
ImGuiTabItemFlags_NoReorder: ImGuiTabItemFlags_ = ImGuiTabItemFlags_.ImGuiTabItemFlags_NoReorder
ImGuiTabItemFlags_Leading: ImGuiTabItemFlags_ = ImGuiTabItemFlags_.ImGuiTabItemFlags_Leading
ImGuiTabItemFlags_Trailing: ImGuiTabItemFlags_ = ImGuiTabItemFlags_.ImGuiTabItemFlags_Trailing
ImGuiTabItemFlags_NoAssumedClosure: ImGuiTabItemFlags_ = ...
ImGuiFocusedFlags_None: ImGuiFocusedFlags_ = ImGuiFocusedFlags_.ImGuiFocusedFlags_None
ImGuiFocusedFlags_ChildWindows: ImGuiFocusedFlags_ = ImGuiFocusedFlags_.ImGuiFocusedFlags_ChildWindows
ImGuiFocusedFlags_RootWindow: ImGuiFocusedFlags_ = ImGuiFocusedFlags_.ImGuiFocusedFlags_RootWindow
ImGuiFocusedFlags_AnyWindow: ImGuiFocusedFlags_ = ImGuiFocusedFlags_.ImGuiFocusedFlags_AnyWindow
ImGuiFocusedFlags_NoPopupHierarchy: ImGuiFocusedFlags_ = ...
ImGuiFocusedFlags_RootAndChildWindows: ImGuiFocusedFlags_ = ...
ImGuiHoveredFlags_None: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_None
ImGuiHoveredFlags_ChildWindows: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_ChildWindows
ImGuiHoveredFlags_RootWindow: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_RootWindow
ImGuiHoveredFlags_AnyWindow: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_AnyWindow
ImGuiHoveredFlags_NoPopupHierarchy: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_AllowWhenBlockedByPopup: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_AllowWhenBlockedByActiveItem: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_AllowWhenOverlappedByItem: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_AllowWhenOverlappedByWindow: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_AllowWhenDisabled: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_NoNavOverride: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_AllowWhenOverlapped: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_RectOnly: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_RectOnly
ImGuiHoveredFlags_RootAndChildWindows: ImGuiHoveredFlags_ = ...
ImGuiHoveredFlags_ForTooltip: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_ForTooltip
ImGuiHoveredFlags_Stationary: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_Stationary
ImGuiHoveredFlags_DelayNone: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNone
ImGuiHoveredFlags_DelayShort: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayShort
ImGuiHoveredFlags_DelayNormal: ImGuiHoveredFlags_ = ImGuiHoveredFlags_.ImGuiHoveredFlags_DelayNormal
ImGuiHoveredFlags_NoSharedDelay: ImGuiHoveredFlags_ = ...
ImGuiDragDropFlags_None: ImGuiDragDropFlags_ = ImGuiDragDropFlags_.ImGuiDragDropFlags_None
ImGuiDragDropFlags_SourceNoPreviewTooltip: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_SourceNoDisableHover: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_SourceNoHoldToOpenOthers: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_SourceAllowNullID: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_SourceExtern: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_PayloadAutoExpire: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_PayloadNoCrossContext: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_PayloadNoCrossProcess: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_AcceptBeforeDelivery: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_AcceptNoDrawDefaultRect: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_AcceptNoPreviewTooltip: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_AcceptDrawAsHovered: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_AcceptPeekOnly: ImGuiDragDropFlags_ = ...
ImGuiDragDropFlags_SourceAutoExpirePayload: ImGuiDragDropFlags_ = ...
ImGuiDataType_S8: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_S8
ImGuiDataType_U8: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_U8
ImGuiDataType_S16: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_S16
ImGuiDataType_U16: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_U16
ImGuiDataType_S32: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_S32
ImGuiDataType_U32: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_U32
ImGuiDataType_S64: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_S64
ImGuiDataType_U64: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_U64
ImGuiDataType_Float: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_Float
ImGuiDataType_Double: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_Double
ImGuiDataType_Bool: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_Bool
ImGuiDataType_String: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_String
ImGuiDataType_COUNT: ImGuiDataType_ = ImGuiDataType_.ImGuiDataType_COUNT
ImGuiDir_None: ImGuiDir = ImGuiDir.ImGuiDir_None
ImGuiDir_Left: ImGuiDir = ImGuiDir.ImGuiDir_Left
ImGuiDir_Right: ImGuiDir = ImGuiDir.ImGuiDir_Right
ImGuiDir_Up: ImGuiDir = ImGuiDir.ImGuiDir_Up
ImGuiDir_Down: ImGuiDir = ImGuiDir.ImGuiDir_Down
ImGuiDir_COUNT: ImGuiDir = ImGuiDir.ImGuiDir_COUNT
ImGuiSortDirection_None: ImGuiSortDirection = ImGuiSortDirection.ImGuiSortDirection_None
ImGuiSortDirection_Ascending: ImGuiSortDirection = ImGuiSortDirection.ImGuiSortDirection_Ascending
ImGuiSortDirection_Descending: ImGuiSortDirection = ImGuiSortDirection.ImGuiSortDirection_Descending
ImGuiKey_None: ImGuiKey = ImGuiKey.ImGuiKey_None
ImGuiKey_NamedKey_BEGIN: ImGuiKey = ImGuiKey.ImGuiKey_NamedKey_BEGIN
ImGuiKey_Tab: ImGuiKey = ImGuiKey.ImGuiKey_NamedKey_BEGIN
ImGuiKey_LeftArrow: ImGuiKey = ImGuiKey.ImGuiKey_LeftArrow
ImGuiKey_RightArrow: ImGuiKey = ImGuiKey.ImGuiKey_RightArrow
ImGuiKey_UpArrow: ImGuiKey = ImGuiKey.ImGuiKey_UpArrow
ImGuiKey_DownArrow: ImGuiKey = ImGuiKey.ImGuiKey_DownArrow
ImGuiKey_PageUp: ImGuiKey = ImGuiKey.ImGuiKey_PageUp
ImGuiKey_PageDown: ImGuiKey = ImGuiKey.ImGuiKey_PageDown
ImGuiKey_Home: ImGuiKey = ImGuiKey.ImGuiKey_Home
ImGuiKey_End: ImGuiKey = ImGuiKey.ImGuiKey_End
ImGuiKey_Insert: ImGuiKey = ImGuiKey.ImGuiKey_Insert
ImGuiKey_Delete: ImGuiKey = ImGuiKey.ImGuiKey_Delete
ImGuiKey_Backspace: ImGuiKey = ImGuiKey.ImGuiKey_Backspace
ImGuiKey_Space: ImGuiKey = ImGuiKey.ImGuiKey_Space
ImGuiKey_Enter: ImGuiKey = ImGuiKey.ImGuiKey_Enter
ImGuiKey_Escape: ImGuiKey = ImGuiKey.ImGuiKey_Escape
ImGuiKey_LeftCtrl: ImGuiKey = ImGuiKey.ImGuiKey_LeftCtrl
ImGuiKey_LeftShift: ImGuiKey = ImGuiKey.ImGuiKey_LeftShift
ImGuiKey_LeftAlt: ImGuiKey = ImGuiKey.ImGuiKey_LeftAlt
ImGuiKey_LeftSuper: ImGuiKey = ImGuiKey.ImGuiKey_LeftSuper
ImGuiKey_RightCtrl: ImGuiKey = ImGuiKey.ImGuiKey_RightCtrl
ImGuiKey_RightShift: ImGuiKey = ImGuiKey.ImGuiKey_RightShift
ImGuiKey_RightAlt: ImGuiKey = ImGuiKey.ImGuiKey_RightAlt
ImGuiKey_RightSuper: ImGuiKey = ImGuiKey.ImGuiKey_RightSuper
ImGuiKey_Menu: ImGuiKey = ImGuiKey.ImGuiKey_Menu
ImGuiKey_0: ImGuiKey = ImGuiKey.ImGuiKey_0
ImGuiKey_1: ImGuiKey = ImGuiKey.ImGuiKey_1
ImGuiKey_2: ImGuiKey = ImGuiKey.ImGuiKey_2
ImGuiKey_3: ImGuiKey = ImGuiKey.ImGuiKey_3
ImGuiKey_4: ImGuiKey = ImGuiKey.ImGuiKey_4
ImGuiKey_5: ImGuiKey = ImGuiKey.ImGuiKey_5
ImGuiKey_6: ImGuiKey = ImGuiKey.ImGuiKey_6
ImGuiKey_7: ImGuiKey = ImGuiKey.ImGuiKey_7
ImGuiKey_8: ImGuiKey = ImGuiKey.ImGuiKey_8
ImGuiKey_9: ImGuiKey = ImGuiKey.ImGuiKey_9
ImGuiKey_A: ImGuiKey = ImGuiKey.ImGuiKey_A
ImGuiKey_B: ImGuiKey = ImGuiKey.ImGuiKey_B
ImGuiKey_C: ImGuiKey = ImGuiKey.ImGuiKey_C
ImGuiKey_D: ImGuiKey = ImGuiKey.ImGuiKey_D
ImGuiKey_E: ImGuiKey = ImGuiKey.ImGuiKey_E
ImGuiKey_F: ImGuiKey = ImGuiKey.ImGuiKey_F
ImGuiKey_G: ImGuiKey = ImGuiKey.ImGuiKey_G
ImGuiKey_H: ImGuiKey = ImGuiKey.ImGuiKey_H
ImGuiKey_I: ImGuiKey = ImGuiKey.ImGuiKey_I
ImGuiKey_J: ImGuiKey = ImGuiKey.ImGuiKey_J
ImGuiKey_K: ImGuiKey = ImGuiKey.ImGuiKey_K
ImGuiKey_L: ImGuiKey = ImGuiKey.ImGuiKey_L
ImGuiKey_M: ImGuiKey = ImGuiKey.ImGuiKey_M
ImGuiKey_N: ImGuiKey = ImGuiKey.ImGuiKey_N
ImGuiKey_O: ImGuiKey = ImGuiKey.ImGuiKey_O
ImGuiKey_P: ImGuiKey = ImGuiKey.ImGuiKey_P
ImGuiKey_Q: ImGuiKey = ImGuiKey.ImGuiKey_Q
ImGuiKey_R: ImGuiKey = ImGuiKey.ImGuiKey_R
ImGuiKey_S: ImGuiKey = ImGuiKey.ImGuiKey_S
ImGuiKey_T: ImGuiKey = ImGuiKey.ImGuiKey_T
ImGuiKey_U: ImGuiKey = ImGuiKey.ImGuiKey_U
ImGuiKey_V: ImGuiKey = ImGuiKey.ImGuiKey_V
ImGuiKey_W: ImGuiKey = ImGuiKey.ImGuiKey_W
ImGuiKey_X: ImGuiKey = ImGuiKey.ImGuiKey_X
ImGuiKey_Y: ImGuiKey = ImGuiKey.ImGuiKey_Y
ImGuiKey_Z: ImGuiKey = ImGuiKey.ImGuiKey_Z
ImGuiKey_F1: ImGuiKey = ImGuiKey.ImGuiKey_F1
ImGuiKey_F2: ImGuiKey = ImGuiKey.ImGuiKey_F2
ImGuiKey_F3: ImGuiKey = ImGuiKey.ImGuiKey_F3
ImGuiKey_F4: ImGuiKey = ImGuiKey.ImGuiKey_F4
ImGuiKey_F5: ImGuiKey = ImGuiKey.ImGuiKey_F5
ImGuiKey_F6: ImGuiKey = ImGuiKey.ImGuiKey_F6
ImGuiKey_F7: ImGuiKey = ImGuiKey.ImGuiKey_F7
ImGuiKey_F8: ImGuiKey = ImGuiKey.ImGuiKey_F8
ImGuiKey_F9: ImGuiKey = ImGuiKey.ImGuiKey_F9
ImGuiKey_F10: ImGuiKey = ImGuiKey.ImGuiKey_F10
ImGuiKey_F11: ImGuiKey = ImGuiKey.ImGuiKey_F11
ImGuiKey_F12: ImGuiKey = ImGuiKey.ImGuiKey_F12
ImGuiKey_F13: ImGuiKey = ImGuiKey.ImGuiKey_F13
ImGuiKey_F14: ImGuiKey = ImGuiKey.ImGuiKey_F14
ImGuiKey_F15: ImGuiKey = ImGuiKey.ImGuiKey_F15
ImGuiKey_F16: ImGuiKey = ImGuiKey.ImGuiKey_F16
ImGuiKey_F17: ImGuiKey = ImGuiKey.ImGuiKey_F17
ImGuiKey_F18: ImGuiKey = ImGuiKey.ImGuiKey_F18
ImGuiKey_F19: ImGuiKey = ImGuiKey.ImGuiKey_F19
ImGuiKey_F20: ImGuiKey = ImGuiKey.ImGuiKey_F20
ImGuiKey_F21: ImGuiKey = ImGuiKey.ImGuiKey_F21
ImGuiKey_F22: ImGuiKey = ImGuiKey.ImGuiKey_F22
ImGuiKey_F23: ImGuiKey = ImGuiKey.ImGuiKey_F23
ImGuiKey_F24: ImGuiKey = ImGuiKey.ImGuiKey_F24
ImGuiKey_Apostrophe: ImGuiKey = ImGuiKey.ImGuiKey_Apostrophe
ImGuiKey_Comma: ImGuiKey = ImGuiKey.ImGuiKey_Comma
ImGuiKey_Minus: ImGuiKey = ImGuiKey.ImGuiKey_Minus
ImGuiKey_Period: ImGuiKey = ImGuiKey.ImGuiKey_Period
ImGuiKey_Slash: ImGuiKey = ImGuiKey.ImGuiKey_Slash
ImGuiKey_Semicolon: ImGuiKey = ImGuiKey.ImGuiKey_Semicolon
ImGuiKey_Equal: ImGuiKey = ImGuiKey.ImGuiKey_Equal
ImGuiKey_LeftBracket: ImGuiKey = ImGuiKey.ImGuiKey_LeftBracket
ImGuiKey_Backslash: ImGuiKey = ImGuiKey.ImGuiKey_Backslash
ImGuiKey_RightBracket: ImGuiKey = ImGuiKey.ImGuiKey_RightBracket
ImGuiKey_GraveAccent: ImGuiKey = ImGuiKey.ImGuiKey_GraveAccent
ImGuiKey_CapsLock: ImGuiKey = ImGuiKey.ImGuiKey_CapsLock
ImGuiKey_ScrollLock: ImGuiKey = ImGuiKey.ImGuiKey_ScrollLock
ImGuiKey_NumLock: ImGuiKey = ImGuiKey.ImGuiKey_NumLock
ImGuiKey_PrintScreen: ImGuiKey = ImGuiKey.ImGuiKey_PrintScreen
ImGuiKey_Pause: ImGuiKey = ImGuiKey.ImGuiKey_Pause
ImGuiKey_Keypad0: ImGuiKey = ImGuiKey.ImGuiKey_Keypad0
ImGuiKey_Keypad1: ImGuiKey = ImGuiKey.ImGuiKey_Keypad1
ImGuiKey_Keypad2: ImGuiKey = ImGuiKey.ImGuiKey_Keypad2
ImGuiKey_Keypad3: ImGuiKey = ImGuiKey.ImGuiKey_Keypad3
ImGuiKey_Keypad4: ImGuiKey = ImGuiKey.ImGuiKey_Keypad4
ImGuiKey_Keypad5: ImGuiKey = ImGuiKey.ImGuiKey_Keypad5
ImGuiKey_Keypad6: ImGuiKey = ImGuiKey.ImGuiKey_Keypad6
ImGuiKey_Keypad7: ImGuiKey = ImGuiKey.ImGuiKey_Keypad7
ImGuiKey_Keypad8: ImGuiKey = ImGuiKey.ImGuiKey_Keypad8
ImGuiKey_Keypad9: ImGuiKey = ImGuiKey.ImGuiKey_Keypad9
ImGuiKey_KeypadDecimal: ImGuiKey = ImGuiKey.ImGuiKey_KeypadDecimal
ImGuiKey_KeypadDivide: ImGuiKey = ImGuiKey.ImGuiKey_KeypadDivide
ImGuiKey_KeypadMultiply: ImGuiKey = ImGuiKey.ImGuiKey_KeypadMultiply
ImGuiKey_KeypadSubtract: ImGuiKey = ImGuiKey.ImGuiKey_KeypadSubtract
ImGuiKey_KeypadAdd: ImGuiKey = ImGuiKey.ImGuiKey_KeypadAdd
ImGuiKey_KeypadEnter: ImGuiKey = ImGuiKey.ImGuiKey_KeypadEnter
ImGuiKey_KeypadEqual: ImGuiKey = ImGuiKey.ImGuiKey_KeypadEqual
ImGuiKey_AppBack: ImGuiKey = ImGuiKey.ImGuiKey_AppBack
ImGuiKey_AppForward: ImGuiKey = ImGuiKey.ImGuiKey_AppForward
ImGuiKey_Oem102: ImGuiKey = ImGuiKey.ImGuiKey_Oem102
ImGuiKey_GamepadStart: ImGuiKey = ImGuiKey.ImGuiKey_GamepadStart
ImGuiKey_GamepadBack: ImGuiKey = ImGuiKey.ImGuiKey_GamepadBack
ImGuiKey_GamepadFaceLeft: ImGuiKey = ImGuiKey.ImGuiKey_GamepadFaceLeft
ImGuiKey_GamepadFaceRight: ImGuiKey = ImGuiKey.ImGuiKey_GamepadFaceRight
ImGuiKey_GamepadFaceUp: ImGuiKey = ImGuiKey.ImGuiKey_GamepadFaceUp
ImGuiKey_GamepadFaceDown: ImGuiKey = ImGuiKey.ImGuiKey_GamepadFaceDown
ImGuiKey_GamepadDpadLeft: ImGuiKey = ImGuiKey.ImGuiKey_GamepadDpadLeft
ImGuiKey_GamepadDpadRight: ImGuiKey = ImGuiKey.ImGuiKey_GamepadDpadRight
ImGuiKey_GamepadDpadUp: ImGuiKey = ImGuiKey.ImGuiKey_GamepadDpadUp
ImGuiKey_GamepadDpadDown: ImGuiKey = ImGuiKey.ImGuiKey_GamepadDpadDown
ImGuiKey_GamepadL1: ImGuiKey = ImGuiKey.ImGuiKey_GamepadL1
ImGuiKey_GamepadR1: ImGuiKey = ImGuiKey.ImGuiKey_GamepadR1
ImGuiKey_GamepadL2: ImGuiKey = ImGuiKey.ImGuiKey_GamepadL2
ImGuiKey_GamepadR2: ImGuiKey = ImGuiKey.ImGuiKey_GamepadR2
ImGuiKey_GamepadL3: ImGuiKey = ImGuiKey.ImGuiKey_GamepadL3
ImGuiKey_GamepadR3: ImGuiKey = ImGuiKey.ImGuiKey_GamepadR3
ImGuiKey_GamepadLStickLeft: ImGuiKey = ImGuiKey.ImGuiKey_GamepadLStickLeft
ImGuiKey_GamepadLStickRight: ImGuiKey = ImGuiKey.ImGuiKey_GamepadLStickRight
ImGuiKey_GamepadLStickUp: ImGuiKey = ImGuiKey.ImGuiKey_GamepadLStickUp
ImGuiKey_GamepadLStickDown: ImGuiKey = ImGuiKey.ImGuiKey_GamepadLStickDown
ImGuiKey_GamepadRStickLeft: ImGuiKey = ImGuiKey.ImGuiKey_GamepadRStickLeft
ImGuiKey_GamepadRStickRight: ImGuiKey = ImGuiKey.ImGuiKey_GamepadRStickRight
ImGuiKey_GamepadRStickUp: ImGuiKey = ImGuiKey.ImGuiKey_GamepadRStickUp
ImGuiKey_GamepadRStickDown: ImGuiKey = ImGuiKey.ImGuiKey_GamepadRStickDown
ImGuiKey_MouseLeft: ImGuiKey = ImGuiKey.ImGuiKey_MouseLeft
ImGuiKey_MouseRight: ImGuiKey = ImGuiKey.ImGuiKey_MouseRight
ImGuiKey_MouseMiddle: ImGuiKey = ImGuiKey.ImGuiKey_MouseMiddle
ImGuiKey_MouseX1: ImGuiKey = ImGuiKey.ImGuiKey_MouseX1
ImGuiKey_MouseX2: ImGuiKey = ImGuiKey.ImGuiKey_MouseX2
ImGuiKey_MouseWheelX: ImGuiKey = ImGuiKey.ImGuiKey_MouseWheelX
ImGuiKey_MouseWheelY: ImGuiKey = ImGuiKey.ImGuiKey_MouseWheelY
ImGuiKey_ReservedForModCtrl: ImGuiKey = ImGuiKey.ImGuiKey_ReservedForModCtrl
ImGuiKey_ReservedForModShift: ImGuiKey = ImGuiKey.ImGuiKey_ReservedForModShift
ImGuiKey_ReservedForModAlt: ImGuiKey = ImGuiKey.ImGuiKey_ReservedForModAlt
ImGuiKey_ReservedForModSuper: ImGuiKey = ImGuiKey.ImGuiKey_ReservedForModSuper
ImGuiKey_NamedKey_END: ImGuiKey = ImGuiKey.ImGuiKey_NamedKey_END
ImGuiKey_NamedKey_COUNT: ImGuiKey = ImGuiKey.ImGuiKey_NamedKey_COUNT
ImGuiMod_None: ImGuiKey = ImGuiKey.ImGuiKey_None
ImGuiMod_Ctrl: ImGuiKey = ImGuiKey.ImGuiMod_Ctrl
ImGuiMod_Shift: ImGuiKey = ImGuiKey.ImGuiMod_Shift
ImGuiMod_Alt: ImGuiKey = ImGuiKey.ImGuiMod_Alt
ImGuiMod_Super: ImGuiKey = ImGuiKey.ImGuiMod_Super
ImGuiKey_COUNT: ImGuiKey = ImGuiKey.ImGuiKey_NamedKey_END
ImGuiMod_Shortcut: ImGuiKey = ImGuiKey.ImGuiMod_Ctrl
ImGuiInputFlags_None: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_None
ImGuiInputFlags_Repeat: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_Repeat
ImGuiInputFlags_RouteActive: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_RouteActive
ImGuiInputFlags_RouteFocused: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_RouteFocused
ImGuiInputFlags_RouteGlobal: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_RouteGlobal
ImGuiInputFlags_RouteAlways: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_RouteAlways
ImGuiInputFlags_RouteOverFocused: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_RouteOverFocused
ImGuiInputFlags_RouteOverActive: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_RouteOverActive
ImGuiInputFlags_RouteUnlessBgFocused: ImGuiInputFlags_ = ...
ImGuiInputFlags_RouteFromRootWindow: ImGuiInputFlags_ = ...
ImGuiInputFlags_Tooltip: ImGuiInputFlags_ = ImGuiInputFlags_.ImGuiInputFlags_Tooltip
ImGuiConfigFlags_None: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_None
ImGuiConfigFlags_NavEnableKeyboard: ImGuiConfigFlags_ = ...
ImGuiConfigFlags_NavEnableGamepad: ImGuiConfigFlags_ = ...
ImGuiConfigFlags_NoMouse: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_NoMouse
ImGuiConfigFlags_NoMouseCursorChange: ImGuiConfigFlags_ = ...
ImGuiConfigFlags_NoKeyboard: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_NoKeyboard
ImGuiConfigFlags_IsSRGB: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_IsSRGB
ImGuiConfigFlags_IsTouchScreen: ImGuiConfigFlags_ = ImGuiConfigFlags_.ImGuiConfigFlags_IsTouchScreen
ImGuiConfigFlags_NavEnableSetMousePos: ImGuiConfigFlags_ = ...
ImGuiConfigFlags_NavNoCaptureKeyboard: ImGuiConfigFlags_ = ...
ImGuiBackendFlags_None: ImGuiBackendFlags_ = ImGuiBackendFlags_.ImGuiBackendFlags_None
ImGuiBackendFlags_HasGamepad: ImGuiBackendFlags_ = ImGuiBackendFlags_.ImGuiBackendFlags_HasGamepad
ImGuiBackendFlags_HasMouseCursors: ImGuiBackendFlags_ = ...
ImGuiBackendFlags_HasSetMousePos: ImGuiBackendFlags_ = ...
ImGuiBackendFlags_RendererHasVtxOffset: ImGuiBackendFlags_ = ...
ImGuiBackendFlags_RendererHasTextures: ImGuiBackendFlags_ = ...
ImGuiCol_Text: ImGuiCol_ = ImGuiCol_.ImGuiCol_Text
ImGuiCol_TextDisabled: ImGuiCol_ = ImGuiCol_.ImGuiCol_TextDisabled
ImGuiCol_WindowBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_WindowBg
ImGuiCol_ChildBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_ChildBg
ImGuiCol_PopupBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_PopupBg
ImGuiCol_Border: ImGuiCol_ = ImGuiCol_.ImGuiCol_Border
ImGuiCol_BorderShadow: ImGuiCol_ = ImGuiCol_.ImGuiCol_BorderShadow
ImGuiCol_FrameBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_FrameBg
ImGuiCol_FrameBgHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_FrameBgHovered
ImGuiCol_FrameBgActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_FrameBgActive
ImGuiCol_TitleBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_TitleBg
ImGuiCol_TitleBgActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_TitleBgActive
ImGuiCol_TitleBgCollapsed: ImGuiCol_ = ImGuiCol_.ImGuiCol_TitleBgCollapsed
ImGuiCol_MenuBarBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_MenuBarBg
ImGuiCol_ScrollbarBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_ScrollbarBg
ImGuiCol_ScrollbarGrab: ImGuiCol_ = ImGuiCol_.ImGuiCol_ScrollbarGrab
ImGuiCol_ScrollbarGrabHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_ScrollbarGrabHovered
ImGuiCol_ScrollbarGrabActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_ScrollbarGrabActive
ImGuiCol_CheckMark: ImGuiCol_ = ImGuiCol_.ImGuiCol_CheckMark
ImGuiCol_SliderGrab: ImGuiCol_ = ImGuiCol_.ImGuiCol_SliderGrab
ImGuiCol_SliderGrabActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_SliderGrabActive
ImGuiCol_Button: ImGuiCol_ = ImGuiCol_.ImGuiCol_Button
ImGuiCol_ButtonHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_ButtonHovered
ImGuiCol_ButtonActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_ButtonActive
ImGuiCol_Header: ImGuiCol_ = ImGuiCol_.ImGuiCol_Header
ImGuiCol_HeaderHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_HeaderHovered
ImGuiCol_HeaderActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_HeaderActive
ImGuiCol_Separator: ImGuiCol_ = ImGuiCol_.ImGuiCol_Separator
ImGuiCol_SeparatorHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_SeparatorHovered
ImGuiCol_SeparatorActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_SeparatorActive
ImGuiCol_ResizeGrip: ImGuiCol_ = ImGuiCol_.ImGuiCol_ResizeGrip
ImGuiCol_ResizeGripHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_ResizeGripHovered
ImGuiCol_ResizeGripActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_ResizeGripActive
ImGuiCol_InputTextCursor: ImGuiCol_ = ImGuiCol_.ImGuiCol_InputTextCursor
ImGuiCol_TabHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabHovered
ImGuiCol_Tab: ImGuiCol_ = ImGuiCol_.ImGuiCol_Tab
ImGuiCol_TabSelected: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabSelected
ImGuiCol_TabSelectedOverline: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabSelectedOverline
ImGuiCol_TabDimmed: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabDimmed
ImGuiCol_TabDimmedSelected: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabDimmedSelected
ImGuiCol_TabDimmedSelectedOverline: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabDimmedSelectedOverline
ImGuiCol_PlotLines: ImGuiCol_ = ImGuiCol_.ImGuiCol_PlotLines
ImGuiCol_PlotLinesHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_PlotLinesHovered
ImGuiCol_PlotHistogram: ImGuiCol_ = ImGuiCol_.ImGuiCol_PlotHistogram
ImGuiCol_PlotHistogramHovered: ImGuiCol_ = ImGuiCol_.ImGuiCol_PlotHistogramHovered
ImGuiCol_TableHeaderBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_TableHeaderBg
ImGuiCol_TableBorderStrong: ImGuiCol_ = ImGuiCol_.ImGuiCol_TableBorderStrong
ImGuiCol_TableBorderLight: ImGuiCol_ = ImGuiCol_.ImGuiCol_TableBorderLight
ImGuiCol_TableRowBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_TableRowBg
ImGuiCol_TableRowBgAlt: ImGuiCol_ = ImGuiCol_.ImGuiCol_TableRowBgAlt
ImGuiCol_TextLink: ImGuiCol_ = ImGuiCol_.ImGuiCol_TextLink
ImGuiCol_TextSelectedBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_TextSelectedBg
ImGuiCol_TreeLines: ImGuiCol_ = ImGuiCol_.ImGuiCol_TreeLines
ImGuiCol_DragDropTarget: ImGuiCol_ = ImGuiCol_.ImGuiCol_DragDropTarget
ImGuiCol_DragDropTargetBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_DragDropTargetBg
ImGuiCol_UnsavedMarker: ImGuiCol_ = ImGuiCol_.ImGuiCol_UnsavedMarker
ImGuiCol_NavCursor: ImGuiCol_ = ImGuiCol_.ImGuiCol_NavCursor
ImGuiCol_NavWindowingHighlight: ImGuiCol_ = ImGuiCol_.ImGuiCol_NavWindowingHighlight
ImGuiCol_NavWindowingDimBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_NavWindowingDimBg
ImGuiCol_ModalWindowDimBg: ImGuiCol_ = ImGuiCol_.ImGuiCol_ModalWindowDimBg
ImGuiCol_COUNT: ImGuiCol_ = ImGuiCol_.ImGuiCol_COUNT
ImGuiCol_TabActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabSelected
ImGuiCol_TabUnfocused: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabDimmed
ImGuiCol_TabUnfocusedActive: ImGuiCol_ = ImGuiCol_.ImGuiCol_TabDimmedSelected
ImGuiCol_NavHighlight: ImGuiCol_ = ImGuiCol_.ImGuiCol_NavCursor
ImGuiStyleVar_Alpha: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_Alpha
ImGuiStyleVar_DisabledAlpha: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_DisabledAlpha
ImGuiStyleVar_WindowPadding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_WindowPadding
ImGuiStyleVar_WindowRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_WindowRounding
ImGuiStyleVar_WindowBorderSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_WindowBorderSize
ImGuiStyleVar_WindowMinSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_WindowMinSize
ImGuiStyleVar_WindowTitleAlign: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_WindowTitleAlign
ImGuiStyleVar_ChildRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ChildRounding
ImGuiStyleVar_ChildBorderSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ChildBorderSize
ImGuiStyleVar_PopupRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_PopupRounding
ImGuiStyleVar_PopupBorderSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_PopupBorderSize
ImGuiStyleVar_FramePadding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_FramePadding
ImGuiStyleVar_FrameRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_FrameRounding
ImGuiStyleVar_FrameBorderSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_FrameBorderSize
ImGuiStyleVar_ItemSpacing: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ItemSpacing
ImGuiStyleVar_ItemInnerSpacing: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ItemInnerSpacing
ImGuiStyleVar_IndentSpacing: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_IndentSpacing
ImGuiStyleVar_CellPadding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_CellPadding
ImGuiStyleVar_ScrollbarSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ScrollbarSize
ImGuiStyleVar_ScrollbarRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ScrollbarRounding
ImGuiStyleVar_ScrollbarPadding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ScrollbarPadding
ImGuiStyleVar_GrabMinSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_GrabMinSize
ImGuiStyleVar_GrabRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_GrabRounding
ImGuiStyleVar_ImageBorderSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ImageBorderSize
ImGuiStyleVar_TabRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TabRounding
ImGuiStyleVar_TabBorderSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TabBorderSize
ImGuiStyleVar_TabMinWidthBase: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TabMinWidthBase
ImGuiStyleVar_TabMinWidthShrink: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TabMinWidthShrink
ImGuiStyleVar_TabBarBorderSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TabBarBorderSize
ImGuiStyleVar_TabBarOverlineSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TabBarOverlineSize
ImGuiStyleVar_TableAngledHeadersAngle: ImGuiStyleVar_ = ...
ImGuiStyleVar_TableAngledHeadersTextAlign: ImGuiStyleVar_ = ...
ImGuiStyleVar_TreeLinesSize: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TreeLinesSize
ImGuiStyleVar_TreeLinesRounding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_TreeLinesRounding
ImGuiStyleVar_ButtonTextAlign: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_ButtonTextAlign
ImGuiStyleVar_SelectableTextAlign: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_SelectableTextAlign
ImGuiStyleVar_SeparatorTextBorderSize: ImGuiStyleVar_ = ...
ImGuiStyleVar_SeparatorTextAlign: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextAlign
ImGuiStyleVar_SeparatorTextPadding: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_SeparatorTextPadding
ImGuiStyleVar_COUNT: ImGuiStyleVar_ = ImGuiStyleVar_.ImGuiStyleVar_COUNT
ImGuiButtonFlags_None: ImGuiButtonFlags_ = ImGuiButtonFlags_.ImGuiButtonFlags_None
ImGuiButtonFlags_MouseButtonLeft: ImGuiButtonFlags_ = ...
ImGuiButtonFlags_MouseButtonRight: ImGuiButtonFlags_ = ...
ImGuiButtonFlags_MouseButtonMiddle: ImGuiButtonFlags_ = ...
ImGuiButtonFlags_EnableNav: ImGuiButtonFlags_ = ImGuiButtonFlags_.ImGuiButtonFlags_EnableNav
ImGuiColorEditFlags_None: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_None
ImGuiColorEditFlags_NoAlpha: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_NoAlpha
ImGuiColorEditFlags_NoPicker: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_NoPicker
ImGuiColorEditFlags_NoOptions: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_NoSmallPreview: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_NoInputs: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_NoInputs
ImGuiColorEditFlags_NoTooltip: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_NoLabel: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_NoLabel
ImGuiColorEditFlags_NoSidePreview: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_NoDragDrop: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_NoBorder: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_NoBorder
ImGuiColorEditFlags_NoColorMarkers: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_AlphaOpaque: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_AlphaNoBg: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_AlphaPreviewHalf: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_AlphaBar: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_AlphaBar
ImGuiColorEditFlags_HDR: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_HDR
ImGuiColorEditFlags_DisplayRGB: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_DisplayHSV: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_DisplayHex: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_Uint8: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_Uint8
ImGuiColorEditFlags_Float: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_Float
ImGuiColorEditFlags_PickerHueBar: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_PickerHueWheel: ImGuiColorEditFlags_ = ...
ImGuiColorEditFlags_InputRGB: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_InputRGB
ImGuiColorEditFlags_InputHSV: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_InputHSV
ImGuiColorEditFlags_AlphaPreview: ImGuiColorEditFlags_ = ImGuiColorEditFlags_.ImGuiColorEditFlags_None
ImGuiSliderFlags_None: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_None
ImGuiSliderFlags_Logarithmic: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_Logarithmic
ImGuiSliderFlags_NoRoundToFormat: ImGuiSliderFlags_ = ...
ImGuiSliderFlags_NoInput: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_NoInput
ImGuiSliderFlags_WrapAround: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_WrapAround
ImGuiSliderFlags_ClampOnInput: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_ClampOnInput
ImGuiSliderFlags_ClampZeroRange: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_ClampZeroRange
ImGuiSliderFlags_NoSpeedTweaks: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_NoSpeedTweaks
ImGuiSliderFlags_ColorMarkers: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_ColorMarkers
ImGuiSliderFlags_AlwaysClamp: ImGuiSliderFlags_ = ImGuiSliderFlags_.ImGuiSliderFlags_AlwaysClamp
ImGuiMouseButton_Left: ImGuiMouseButton_ = ImGuiMouseButton_.ImGuiMouseButton_Left
ImGuiMouseButton_Right: ImGuiMouseButton_ = ImGuiMouseButton_.ImGuiMouseButton_Right
ImGuiMouseButton_Middle: ImGuiMouseButton_ = ImGuiMouseButton_.ImGuiMouseButton_Middle
ImGuiMouseButton_COUNT: ImGuiMouseButton_ = ImGuiMouseButton_.ImGuiMouseButton_COUNT
ImGuiMouseCursor_None: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_None
ImGuiMouseCursor_Arrow: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_Arrow
ImGuiMouseCursor_TextInput: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_TextInput
ImGuiMouseCursor_ResizeAll: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_ResizeAll
ImGuiMouseCursor_ResizeNS: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNS
ImGuiMouseCursor_ResizeEW: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_ResizeEW
ImGuiMouseCursor_ResizeNESW: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNESW
ImGuiMouseCursor_ResizeNWSE: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_ResizeNWSE
ImGuiMouseCursor_Hand: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_Hand
ImGuiMouseCursor_Wait: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_Wait
ImGuiMouseCursor_Progress: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_Progress
ImGuiMouseCursor_NotAllowed: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_NotAllowed
ImGuiMouseCursor_COUNT: ImGuiMouseCursor_ = ImGuiMouseCursor_.ImGuiMouseCursor_COUNT
ImGuiMouseSource_Mouse: ImGuiMouseSource = ImGuiMouseSource.ImGuiMouseSource_Mouse
ImGuiMouseSource_TouchScreen: ImGuiMouseSource = ImGuiMouseSource.ImGuiMouseSource_TouchScreen
ImGuiMouseSource_Pen: ImGuiMouseSource = ImGuiMouseSource.ImGuiMouseSource_Pen
ImGuiMouseSource_COUNT: ImGuiMouseSource = ImGuiMouseSource.ImGuiMouseSource_COUNT
ImGuiCond_None: ImGuiCond_ = ImGuiCond_.ImGuiCond_None
ImGuiCond_Always: ImGuiCond_ = ImGuiCond_.ImGuiCond_Always
ImGuiCond_Once: ImGuiCond_ = ImGuiCond_.ImGuiCond_Once
ImGuiCond_FirstUseEver: ImGuiCond_ = ImGuiCond_.ImGuiCond_FirstUseEver
ImGuiCond_Appearing: ImGuiCond_ = ImGuiCond_.ImGuiCond_Appearing
ImGuiTableFlags_None: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_None
ImGuiTableFlags_Resizable: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_Resizable
ImGuiTableFlags_Reorderable: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_Reorderable
ImGuiTableFlags_Hideable: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_Hideable
ImGuiTableFlags_Sortable: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_Sortable
ImGuiTableFlags_NoSavedSettings: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_NoSavedSettings
ImGuiTableFlags_ContextMenuInBody: ImGuiTableFlags_ = ...
ImGuiTableFlags_RowBg: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_RowBg
ImGuiTableFlags_BordersInnerH: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersInnerH
ImGuiTableFlags_BordersOuterH: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersOuterH
ImGuiTableFlags_BordersInnerV: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersInnerV
ImGuiTableFlags_BordersOuterV: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersOuterV
ImGuiTableFlags_BordersH: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersH
ImGuiTableFlags_BordersV: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersV
ImGuiTableFlags_BordersInner: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersInner
ImGuiTableFlags_BordersOuter: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_BordersOuter
ImGuiTableFlags_Borders: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_Borders
ImGuiTableFlags_NoBordersInBody: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_NoBordersInBody
ImGuiTableFlags_NoBordersInBodyUntilResize: ImGuiTableFlags_ = ...
ImGuiTableFlags_SizingFixedFit: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_SizingFixedFit
ImGuiTableFlags_SizingFixedSame: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_SizingFixedSame
ImGuiTableFlags_SizingStretchProp: ImGuiTableFlags_ = ...
ImGuiTableFlags_SizingStretchSame: ImGuiTableFlags_ = ...
ImGuiTableFlags_NoHostExtendX: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendX
ImGuiTableFlags_NoHostExtendY: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_NoHostExtendY
ImGuiTableFlags_NoKeepColumnsVisible: ImGuiTableFlags_ = ...
ImGuiTableFlags_PreciseWidths: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_PreciseWidths
ImGuiTableFlags_NoClip: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_NoClip
ImGuiTableFlags_PadOuterX: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_PadOuterX
ImGuiTableFlags_NoPadOuterX: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_NoPadOuterX
ImGuiTableFlags_NoPadInnerX: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_NoPadInnerX
ImGuiTableFlags_ScrollX: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_ScrollX
ImGuiTableFlags_ScrollY: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_ScrollY
ImGuiTableFlags_SortMulti: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_SortMulti
ImGuiTableFlags_SortTristate: ImGuiTableFlags_ = ImGuiTableFlags_.ImGuiTableFlags_SortTristate
ImGuiTableFlags_HighlightHoveredColumn: ImGuiTableFlags_ = ...
ImGuiTableColumnFlags_None: ImGuiTableColumnFlags_ = ImGuiTableColumnFlags_.ImGuiTableColumnFlags_None
ImGuiTableColumnFlags_Disabled: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_DefaultHide: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_DefaultSort: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_WidthStretch: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_WidthFixed: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoResize: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoReorder: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoHide: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoClip: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoSort: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoSortAscending: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoSortDescending: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoHeaderLabel: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_NoHeaderWidth: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_PreferSortAscending: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_PreferSortDescending: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_IndentEnable: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_IndentDisable: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_AngledHeader: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_IsEnabled: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_IsVisible: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_IsSorted: ImGuiTableColumnFlags_ = ...
ImGuiTableColumnFlags_IsHovered: ImGuiTableColumnFlags_ = ...
ImGuiTableRowFlags_None: ImGuiTableRowFlags_ = ImGuiTableRowFlags_.ImGuiTableRowFlags_None
ImGuiTableRowFlags_Headers: ImGuiTableRowFlags_ = ImGuiTableRowFlags_.ImGuiTableRowFlags_Headers
ImGuiTableBgTarget_None: ImGuiTableBgTarget_ = ImGuiTableBgTarget_.ImGuiTableBgTarget_None
ImGuiTableBgTarget_RowBg0: ImGuiTableBgTarget_ = ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg0
ImGuiTableBgTarget_RowBg1: ImGuiTableBgTarget_ = ImGuiTableBgTarget_.ImGuiTableBgTarget_RowBg1
ImGuiTableBgTarget_CellBg: ImGuiTableBgTarget_ = ImGuiTableBgTarget_.ImGuiTableBgTarget_CellBg
ImGuiListClipperFlags_None: ImGuiListClipperFlags_ = ImGuiListClipperFlags_.ImGuiListClipperFlags_None
ImGuiListClipperFlags_NoSetTableRowCounters: ImGuiListClipperFlags_ = ...
ImGuiMultiSelectFlags_None: ImGuiMultiSelectFlags_ = ImGuiMultiSelectFlags_.ImGuiMultiSelectFlags_None
ImGuiMultiSelectFlags_SingleSelect: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_NoSelectAll: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_NoRangeSelect: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_NoAutoSelect: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_NoAutoClear: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_NoAutoClearOnReselect: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_BoxSelect1d: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_BoxSelect2d: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_BoxSelectNoScroll: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_ClearOnEscape: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_ClearOnClickVoid: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_ScopeWindow: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_ScopeRect: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_SelectOnClick: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_SelectOnClickRelease: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_NavWrapX: ImGuiMultiSelectFlags_ = ...
ImGuiMultiSelectFlags_NoSelectOnRightClick: ImGuiMultiSelectFlags_ = ...
ImGuiSelectionRequestType_None: ImGuiSelectionRequestType = ...
ImGuiSelectionRequestType_SetAll: ImGuiSelectionRequestType = ...
ImGuiSelectionRequestType_SetRange: ImGuiSelectionRequestType = ...
ImDrawFlags_None: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_None
ImDrawFlags_Closed: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_Closed
ImDrawFlags_RoundCornersTopLeft: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersTopLeft
ImDrawFlags_RoundCornersTopRight: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersTopRight
ImDrawFlags_RoundCornersBottomLeft: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersBottomLeft
ImDrawFlags_RoundCornersBottomRight: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersBottomRight
ImDrawFlags_RoundCornersNone: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersNone
ImDrawFlags_RoundCornersTop: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersTop
ImDrawFlags_RoundCornersBottom: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersBottom
ImDrawFlags_RoundCornersLeft: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersLeft
ImDrawFlags_RoundCornersRight: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersRight
ImDrawFlags_RoundCornersAll: ImDrawFlags_ = ImDrawFlags_.ImDrawFlags_RoundCornersAll
ImDrawListFlags_None: ImDrawListFlags_ = ImDrawListFlags_.ImDrawListFlags_None
ImDrawListFlags_AntiAliasedLines: ImDrawListFlags_ = ImDrawListFlags_.ImDrawListFlags_AntiAliasedLines
ImDrawListFlags_AntiAliasedLinesUseTex: ImDrawListFlags_ = ...
ImDrawListFlags_AntiAliasedFill: ImDrawListFlags_ = ImDrawListFlags_.ImDrawListFlags_AntiAliasedFill
ImDrawListFlags_AllowVtxOffset: ImDrawListFlags_ = ImDrawListFlags_.ImDrawListFlags_AllowVtxOffset
ImTextureFormat_RGBA32: ImTextureFormat = ImTextureFormat.ImTextureFormat_RGBA32
ImTextureFormat_Alpha8: ImTextureFormat = ImTextureFormat.ImTextureFormat_Alpha8
ImTextureStatus_OK: ImTextureStatus = ImTextureStatus.ImTextureStatus_OK
ImTextureStatus_Destroyed: ImTextureStatus = ImTextureStatus.ImTextureStatus_Destroyed
ImTextureStatus_WantCreate: ImTextureStatus = ImTextureStatus.ImTextureStatus_WantCreate
ImTextureStatus_WantUpdates: ImTextureStatus = ImTextureStatus.ImTextureStatus_WantUpdates
ImTextureStatus_WantDestroy: ImTextureStatus = ImTextureStatus.ImTextureStatus_WantDestroy
ImFontAtlasFlags_None: ImFontAtlasFlags_ = ImFontAtlasFlags_.ImFontAtlasFlags_None
ImFontAtlasFlags_NoPowerOfTwoHeight: ImFontAtlasFlags_ = ...
ImFontAtlasFlags_NoMouseCursors: ImFontAtlasFlags_ = ImFontAtlasFlags_.ImFontAtlasFlags_NoMouseCursors
ImFontAtlasFlags_NoBakedLines: ImFontAtlasFlags_ = ImFontAtlasFlags_.ImFontAtlasFlags_NoBakedLines
ImFontFlags_None: ImFontFlags_ = ImFontFlags_.ImFontFlags_None
ImFontFlags_NoLoadError: ImFontFlags_ = ImFontFlags_.ImFontFlags_NoLoadError
ImFontFlags_NoLoadGlyphs: ImFontFlags_ = ImFontFlags_.ImFontFlags_NoLoadGlyphs
ImFontFlags_LockBakedSizes: ImFontFlags_ = ImFontFlags_.ImFontFlags_LockBakedSizes
ImGuiViewportFlags_None: ImGuiViewportFlags_ = ImGuiViewportFlags_.ImGuiViewportFlags_None
ImGuiViewportFlags_IsPlatformWindow: ImGuiViewportFlags_ = ...
ImGuiViewportFlags_IsPlatformMonitor: ImGuiViewportFlags_ = ...
ImGuiViewportFlags_OwnedByApp: ImGuiViewportFlags_ = ImGuiViewportFlags_.ImGuiViewportFlags_OwnedByApp
```
