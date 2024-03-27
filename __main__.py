import toolbox
import os

if __name__ == "__main__":
    annotations = toolbox.read_scripts_annotations()
    toolbox.invoke(annotations)

