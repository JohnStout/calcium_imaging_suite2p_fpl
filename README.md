# Jupyter-notebooks to support calcium imaging preprocessing with suite2p and visualizations with fastplotlib

The suite2p_run notebook is currently geared towards metadata from Thorlabs equipment, so this would need to be changed accordingly. These notebooks were designed on macbook M2 and haven't been tested on PC nor linux.

Follow these instructions to use (replace env_name with your desired name)

        git clone https://github.com/JohnStout/suite2p_fastplotlib_notebooks
        cd suite2p_fastplotlib_notebooks
        conda env create -n <env_name> -f environment.yml


Suite2P has very fast algorithms and an incredible GUI. Fastplotlib has an incredible interactive plot to work with in jupyter. I combined these packages to:
1) Run suite2p
2) Use fastplotlib plots to guide the suite2p manual curation process

Please contact John Stout at john.j.stout.jr@gmail.com for questions.
