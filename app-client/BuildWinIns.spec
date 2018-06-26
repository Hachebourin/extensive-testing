# -*- mode: python -*-

block_cipher = None


a = Analysis(['Main.py'],
             pathex=[ '.', './Dlls64/' ],
             binaries=[],
             datas=[ 
<<<<<<< HEAD
                        ('./Resources/releasenotes.txt', '.'),
                        ('./Resources/small_installer.bmp', '.'),
                        ( './Files', 'Files' ),
                        ('./HISTORY', '.'),
                        ('./LICENSE-LGPLv21', '.'),
                        ( './Dlls64/opengl32sw.dll', '.' ),
                        ( './Dlls64/imageformats', 'imageformats' ),
                        ( './Files', 'Files' )
=======
                        ( './Resources/releasenotes.txt', '.'),
                        ( './Resources/small_installer.bmp', '.'),
                        ( './Files', 'Files' ),
                        ( './HISTORY', '.'),
                        ( './LICENSE-LGPLv21', '.'),
                        ( './Dlls64/opengl32sw.dll', '.' ),
                        ( './Dlls64/libeay32.dll', '.' ),
                        ( './Dlls64/ssleay32.dll', '.' ),
                        ( './Dlls64/imageformats', 'imageformats' ),
                        ( './Files', 'Files' ),
                        ( './Resources/ExtensiveTestingClient.ico', '.' )
>>>>>>> upstream1/master
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ExtensiveTestingClient',
<<<<<<< HEAD
          debug=False,
          strip=False,
          upx=True,
          console=False,
=======
          debug=0,
          strip=0,
          upx=1,
          console=0,
>>>>>>> upstream1/master
          icon='./Resources/ExtensiveTestingClient.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
<<<<<<< HEAD
               strip=False,
               upx=True,
=======
               strip=0,
               upx=1,
>>>>>>> upstream1/master
               name='ExtensiveTestingClient')
