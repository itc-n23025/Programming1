import time


def sleep_for_a_while():
    """しばらく眠る"""
    print("Sleeping ..")
    time.sleep(2)
    print("Done Sleeping")
    sleep_for_a_while()


@show_begin_end
def sleep_for_a_while():
    """しばらく眠る"""
    print("sleeping ..")
    time.sleep(2)
    print("Done Sleeping")
