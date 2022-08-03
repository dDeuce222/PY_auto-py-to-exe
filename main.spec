# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:/Work/Python/desktopApp/video_file/main.py'],
             pathex=['D:\\Work\\Python\\auto-py-to-exe-master'],
             binaries=[],
             datas=[('D:/Work/Python/desktopApp/video_file/images', 'images/'), ('D:/Work/Python/desktopApp/video_file/UI', 'UI/'), ('D:/Work/Python/desktopApp/video_file/windowdragger.py', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='D:\\Work\\Python\\desktopApp\\video_file\\mail.ico')
