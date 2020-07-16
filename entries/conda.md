# Conda
Tác dụng của virtual env: https://www.freecodecamp.org/news/why-you-need-python-environments-and-how-to-manage-them-with-conda-85f155f4353c/

Conda documetation: https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html

## Why you need multiple Python environments
**1. Các package trên git đc down xuống có thể yêu cầu các bản python khác nhau**

**2. Vì update này nọ mà code trước chạy đc h thì ko**

**3. Làm việc nhóm code phải chạy trên mọi máy**


## Conda strength
**1. Clear structure**

**2. Transparent File Management: It doesn’t install files outside its directory**

**3. Flexibility**

**4. Multipurpose:Can be used for R**

Miniconda nhẹ hơn nhưng ít pkg hơn Anaconda.

## Directory structure: bên trong miniconda3

**1. Root environment**

**2. pkgs**: chứa các packages

**3. envs**: chứa các môi trường khác trừ root.

## Useful command:
**1. conda list**: liệt kê các package trong env.

**2. conda install [package]**: install package, vẫn có thể dùng pip (nếu như các channel của conda ko tìm thấy pack)

**3. conda create --name myenv python=3.6**

**4. conda remove --name myenv --all**

**5. conda info --envs**: xem thong tin cac envs

