import json
from pathlib import Path
base=Path(__file__).resolve().parents[1];source=base.parent/'wisteria-blush-theme'
for name in ['themes','assets','store-assets']:(base/name).mkdir(exist_ok=True)
def write(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
rows='''
editor.background tab.activeBackground|F6F1E5|302A34
foreground editor.foreground terminal.foreground|514A52|EAE3D7
titleBar.activeBackground|EAE3E9|25212A
titleBar.activeForeground|574B60|D2C7D7
titleBar.inactiveBackground|F0EBED|211E26
titleBar.inactiveForeground|958A98|8E8196
activityBar.background|DED5E2|211D27
activityBar.foreground|78628B|CCC2D1
activityBar.inactiveForeground|9B8BA3|918099
activityBar.activeBorder|826F95|B29CC5
sideBar.background|EEE7E2|2C2528
sideBar.foreground|65564F|CDBDB4
sideBarSectionHeader.background|E5DCD6|382E31
sideBarSectionHeader.foreground|78665C|DECCC0
editorGroupHeader.tabsBackground tab.inactiveBackground|E8E0E6|26212C
tab.inactiveForeground|948695|A193A7
tab.activeForeground|6D577F|F6F1E5
tab.activeBorderTop|826F95|B29CC5
panel.background terminal.background|F0EADF|29242D
statusBar.background statusBar.noFolderBackground|DCD1E1|46384F
statusBar.foreground statusBar.noFolderForeground|614D73|E5D9EC
panel.border sideBar.border editorGroup.border tab.border titleBar.border|D8CDD5|4B3E50
editor.lineHighlightBackground|EEE7DC|3A313E
editor.lineHighlightBorder|E6DCD0|493C50
editorLineNumber.foreground|A69A99|807184
editorLineNumber.activeForeground|826F95|CCC2D1
editorCursor.foreground|826F95|F6F1E5
selection.background editor.selectionBackground terminal.selectionBackground|DCD1E2|5A4766
editor.inactiveSelectionBackground|E4DDE4|463A4E
editor.wordHighlightBackground editor.wordHighlightStrongBackground editor.selectionHighlightBackground|E9E0EB80|45374D99
list.activeSelectionBackground|CCC2D1|57434E
list.activeSelectionForeground list.inactiveSelectionForeground|574361|F0E1DB
list.inactiveSelectionBackground|E4DDE4|463A4E
list.hoverBackground|E5DDE3|3C3037
editor.findMatchHighlightBackground|E8D3B9|65503D
editor.findMatchBackground|D6B890|85694D
editor.findMatchBorder|A08058|D6BEB3
editorBracketMatch.background|E2D6E7|51405E
editorBracketMatch.border|A38AAE|B59DC6
editorIndentGuide.background1|E0D8CD|463A4B
editorIndentGuide.activeBackground1|B3A1BA|8F759F
quickInput.background editorWidget.background editorHoverWidget.background editorSuggestWidget.background notifications.background|F8F3EA|39303F
input.background dropdown.background|FBF7EF|25202B
input.border dropdown.border|CEBECD|6B5578
focusBorder|947DA6|B29CC5
editorSuggestWidget.selectedBackground|DDD1E3|574568
editorSuggestWidget.selectedForeground|574361|F0E1DB
button.background|826F95|CCC2D1
button.foreground|FFFFFF|3F314A
button.hoverBackground|725E86|DED1E5
button.secondaryBackground|E4D9D1|51423C
button.secondaryForeground|6C574B|EAE3D7
badge.background activityBarBadge.background|826F95|CCC2D1
badge.foreground activityBarBadge.foreground|FFFFFF|3F314A
errorForeground editorError.foreground problemsErrorIcon.foreground|AF5E69|E3A0AC
editorWarning.foreground problemsWarningIcon.foreground|98743C|DDC18D
editorInfo.foreground problemsInfoIcon.foreground|617A96|B8CBE1
gitDecoration.addedResourceForeground gitDecoration.untrackedResourceForeground editorGutter.addedBackground|74885E|B6CCA2
gitDecoration.modifiedResourceForeground editorGutter.modifiedBackground|A0845C|D9BF98
gitDecoration.deletedResourceForeground editorGutter.deletedBackground|AE7780|D9A3AE
diffEditor.insertedTextBackground diffEditor.insertedLineBackground|E7EDDD99|34402E99
diffEditor.removedTextBackground diffEditor.removedLineBackground|F0E0E599|47303999
'''
palette={'comment':('9A9185','A39785'),'keyword,storage':('82608F','C5A7D7'),'string':('687955','BECCA9'),'entity.name.function,support.function':('6C7397','BDC4E2'),'entity.name.type,support.type,support.class':('946C88','D7B5CC'),'constant.numeric,constant.language,variable.other.constant':('9B7357','D6BEB3'),'variable':('514A52','EAE3D7'),'variable.parameter':('837461','D1C2AE'),'variable.other.property,support.variable.property':('587D7B','B1CFCA'),'keyword.operator':('84708D','C3AFCB'),'punctuation':('978A98','AD9AAF'),'entity.name.tag':('82608F','CCC2D1'),'entity.other.attribute-name':('9B7357','DECAAB')}
m=json.loads((source/'package.json').read_text());m.update(name='lavender-parchment-theme',displayName='Lavender Parchment Theme',description='Quiet lavender, warm parchment and muted beige in coordinated light and dark themes.',keywords=['theme','light','dark','lavender','parchment','vintage','muted']);m['galleryBanner']['color']='#302A34'
for t in m['contributes']['themes']:t['label']=t['label'].replace('Wisteria Blush','Lavender Parchment');t['path']=t['path'].replace('wisteria-blush','lavender-parchment')
write(base/'package.json',m)
for i,v in enumerate(['light','dark']):
    t=json.loads((source/'themes'/f'wisteria-blush-{v}-color-theme.json').read_text());t['name']=f'Lavender Parchment Theme {v.title()}'
    for row in rows.strip().splitlines():
        keys,l,d=row.split('|')
        for key in keys.split():t['colors'][key]='#'+[l,d][i]
    for rule in t['tokenColors']:
        key=','.join(rule['scope'])
        if key in palette:rule['settings']['foreground']='#'+palette[key][i]
    for key,scope in {'variable':'variable','parameter':'variable.parameter','property':'variable.other.property,support.variable.property','function':'entity.name.function,support.function','method':'entity.name.function,support.function','class':'entity.name.type,support.type,support.class','type':'entity.name.type,support.type,support.class','interface':'entity.name.type,support.type,support.class','variable.readonly':'constant.numeric,constant.language,variable.other.constant'}.items():t['semanticTokenColors'][key]='#'+palette[scope][i]
    write(base/'themes'/f'lavender-parchment-{v}-color-theme.json',t)
for name in ['LICENSE','CHANGELOG.md','.vscodeignore']:(base/name).write_text((source/name).read_text(encoding='utf-8').replace('Wisteria Blush','Lavender Parchment'),encoding='utf-8')
for name in ['capture-real-screenshots.py','validate.py']:(base/'scripts'/name).write_text((source/'scripts'/name).read_text(encoding='utf-8').replace('Wisteria Blush','Lavender Parchment').replace('wisteria-blush','lavender-parchment'),encoding='utf-8')
demo=base/'scripts/demo-project';demo.mkdir(exist_ok=True)
text=(source/'scripts/demo-project/index.js').read_text(encoding='utf-8').replace('Wisteria Blush','Lavender Parchment').replace('WisteriaBlush','LavenderParchment').replace('wisteria violet, dusty blush and peach','quiet lavender, parchment and warm beige').replace('FLOWER_PALETTE','PAPER_PALETTE').replace('flower-inspired','parchment-inspired')
start=text.index('const PAPER_PALETTE');end=text.index('};',start)+2
text=text[:start]+"const PAPER_PALETTE = {\n  lavender: '#CCC2D1',\n  parchment: '#F6F1E5',\n  beige: '#D6BEB3',\n  violet: '#826F95',\n};"+text[end:]
text=text.replace('.wisteria','.lavender').replace('.peach','.parchment')
(demo/'index.js').write_text(text,encoding='utf-8')
write(demo/'palette.json',{'name':'Lavender Parchment Theme','colors':['#CCC2D1','#F6F1E5','#D6BEB3','#826F95']})
(demo/'styles.css').write_text(':root { --paper: #f6f1e5; --violet: #826f95; --beige: #d6beb3; }\n')
(demo/'README.md').write_text('# Lavender Parchment\n\nQuiet lavender and warm paper.\n')
(base/'README.md').write_text('''# Lavender Parchment Theme

Quiet lavender, warm parchment and muted beige in coordinated light and dark themes.

薰衣草羊皮纸：奶油纸色、沉静灰紫与暖米棕，柔和复古。

- **Lavender Parchment Theme Light** — warm parchment editor, muted lavender controls and beige panels.
- **Lavender Parchment Theme Dark** — charcoal violet editor, warm paper text and muted pastel syntax.

| Region | Light | Dark |
| --- | --- | --- |
| Editor | `#F6F1E5` | `#302A34` |
| Text | `#514A52` | `#EAE3D7` |
| Sidebar | `#EEE7E2` | `#2C2528` |
| Title bar | `#EAE3E9` | `#25212A` |
| Status bar | `#DCD1E1` | `#46384F` |

Brand palette: `#CCC2D1`, `#F6F1E5`, `#D6BEB3`, `#826F95`.

## Installation

Use **Extensions: Install from VSIX**, then choose either appearance with **Preferences: Color Theme**.

Includes semantic highlighting, coordinated terminal colors, Git decorations, search and selection colors. Full UI colors are listed in `COLOR-SPEC.md`; real VS Code previews are included in `store-assets/screenshots/en/`.

Publisher: **lilinhuang** · Version: **1.0.0**

[Marketplace](https://marketplace.visualstudio.com/items?itemName=lilinhuang.lavender-parchment-theme)
''',encoding='utf-8')
print('Created',base)
