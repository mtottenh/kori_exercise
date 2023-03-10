from validator.validator import validate_parens

def test_single_brackets():
    assert(validate_parens("{}"))

def test_multiple_brackets():
    assert(validate_parens("{{}}"))

def test_invalid_string():
    assert(not validate_parens("{{"))
 
config_file_example="\
    menuentry 'Ubuntu'  { \
        recordfail \
        load_video \
        gfxmode $linux_gfx_mode \
        insmod gzio \
        linux   /boot/vmlinuz-5.4.0-139-generic root=/dev/mapper/ubuntu--vg-root ro \
        initrd  /boot/initrd.img-5.4.0-139-generic \
    }"
def test_config_file():
    assert(validate_parens(config_file_example))
