# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['/Users/martin/Downloads/fbs_demo/src/main/python/main.py'],
             pathex=['/Users/martin/Downloads/fbs_demo/target/PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['/Users/martin/.local/share/virtualenvs/fbs_demo-TWheggSV/lib/python3.6/site-packages/fbs/freeze/hooks'],
             runtime_hooks=['/Users/martin/Downloads/fbs_demo/target/PyInstaller/fbs_pyinstaller_hook.py'],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='fbs_demo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='/Users/martin/Downloads/fbs_demo/target/Icon.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='fbs_demo')
app = BUNDLE(coll,
             name='fbs_demo.app',
             icon='/Users/martin/Downloads/fbs_demo/target/Icon.icns',
             bundle_identifier=None)
