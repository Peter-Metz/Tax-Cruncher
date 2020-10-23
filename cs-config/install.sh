# bash commands for installing your package

git clone https://github.com/Peter-Metz/Tax-Cruncher
cd Tax-Cruncher
git checkout biden-local
conda install "conda-forge::paramtools>=0.15.1" "bokeh<2.0.0"
pip install -e .
cd taxcalc_biden
pip install -e .