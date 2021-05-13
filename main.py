import sys
import os

from app.app import App

if __name__ == "__main__":
    try:
        app = App()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            # pylint: disable=W0212
            os._exit(0)
