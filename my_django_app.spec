import os
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

a = Analysis(
    ['run_django.py'],
    pathex=['C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot'],
    binaries=[],
    datas=[
        # Include the templates directory
        (os.path.join('C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot\\templates'), 'templates'),

        # Include the registration templates
        (os.path.join('C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot\\templates\\registration'), 'templates/registration'),

        # Include the custom crispy forms tags directory
        (os.path.join('C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot\\templatetags\\crispy_forms_tags'), 'templatetags/crispy_forms_tags'),

        # Include crispy_forms templates
        *collect_data_files('crispy_forms', subdir='templates'),

        # Include crispy_bootstrap5 templates
        *collect_data_files('crispy_bootstrap5', subdir='templates'),

        # Include the static files directory
        (os.path.join('C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot\\static'), 'static'),

        # Include specific static files
        ('C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot\\static\\css\\style.css', 'static/css'),
        ('C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot\\static\\css\\1.png', 'static/css'),

        # Include the .env file
        ('C:\\Users\\Manju\\Desktop\\gemini\\chatbot_project\\chatbot\\.env', '.env'),
    ],
    hiddenimports=[
        'crispy_forms',
        'crispy_bootstrap5',
        'crispy_forms.templatetags.crispy_forms_tags',
        'crispy_forms.templatetags.crispy_forms_field',
        'google.generativeai',
        'dotenv',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='my_django_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='my_django_app',
)
