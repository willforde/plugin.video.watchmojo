import sys
import os

lib = os.path.join(os.path.dirname(__file__), "resources", "lib")
sys.path.append(lib)

if __name__ == "__main__":
    import main
    main.run()
