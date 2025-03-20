# bd-a1
```
PS C:\Users\abdelrahman\Desktop\DockerStuff\bd-a1> docker build -t bd-a1-image .
[+] Building 2.3s (12/12) FINISHED                                                                                                     docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                   0.0s
 => => transferring dockerfile: 748B                                                                                                                   0.0s
 => [internal] load metadata for docker.io/library/ubuntu:latest                                                                                       0.0s
 => [internal] load .dockerignore                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                        0.0s
 => [1/6] FROM docker.io/library/ubuntu:latest@sha256:72297848456d5d37d1262630108ab308d3e9ec7ed1c3286a32fe09856619a782                                 2.0s
 => => resolve docker.io/library/ubuntu:latest@sha256:72297848456d5d37d1262630108ab308d3e9ec7ed1c3286a32fe09856619a782                                 2.0s
 => [internal] load build context                                                                                                                      0.0s
 => => transferring context: 40B                                                                                                                       0.0s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                                          0.0s
 => CACHED [2/6] RUN apt-get update && apt-get install -y python3 python3-pip python3-venv                                                             0.0s
 => CACHED [3/6] RUN python3 -m venv /opt/venv &&     /opt/venv/bin/pip install --no-cache-dir pandas numpy seaborn matplotlib scikit-learn scipy      0.0s
 => CACHED [4/6] RUN mkdir -p /home/doc-bd-a1/                                                                                                         0.0s
 => CACHED [5/6] COPY train_titanic.csv /home/doc-bd-a1/train_titanic.csv                                                                              0.0s
 => CACHED [6/6] WORKDIR /home/doc-bd-a1/                                                                                                              0.0s
 => exporting to image                                                                                                                                 0.1s
 => => exporting layers                                                                                                                                0.0s
 => => exporting manifest sha256:b1c20357bf8c82656414b958770f4febcf13a2f07423c4e31810d822b251d774                                                      0.0s
 => => exporting config sha256:107a47d256f0aaeaf9bdacd1efd3f0c31699f146a36a46a9f23d213cb10fea42                                                        0.0s
 => => exporting attestation manifest sha256:e59e4f96d59868141d2c6817a631f652872c9eafec862242c230d371a1e0b81c                                          0.0s
 => => exporting manifest list sha256:b4c31b53e39ae3baf0f2c37e14405b9d155ac3876e18446c95eb33f8ffdc28ce                                                 0.0s
 => => naming to docker.io/library/bd-a1-image:latest                                                                                                  0.0s
 => => unpacking to docker.io/library/bd-a1-image:latest                                                                                               0.0s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/f30uxeag2gcuvica48pq3m62f
PS C:\Users\abdelrahman\Desktop\DockerStuff\bd-a1> docker start -ai bd-a1-container
root@3628c55fd7b1:/home/doc-bd-a1# python3 load.py /home/doc-bd-a1/train_titanic.csv
Dataset loaded successfully!
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  891 non-null    int64
 1   Survived     891 non-null    int64
 2   Pclass       891 non-null    int64
 3   Name         891 non-null    object
 4   Sex          891 non-null    object
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64
 7   Parch        891 non-null    int64
 8   Ticket       891 non-null    object
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object
 11  Embarked     889 non-null    object
dtypes: float64(2), int64(5), object(5)
memory usage: 83.7+ KB
/home/doc-bd-a1/dpre.py:20: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df.Embarked[df.Embarked.isna()] = df.Embarked.mode()[0]
/home/doc-bd-a1/dpre.py:20: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
  df.Embarked[df.Embarked.isna()] = df.Embarked.mode()[0]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 891 entries, 0 to 890
Data columns (total 11 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   PassengerId  891 non-null    int64
 1   Survived     891 non-null    int64
 2   Pclass       891 non-null    int64
 3   Name         891 non-null    object
 4   Sex          891 non-null    object
 5   Age          891 non-null    float64
 6   SibSp        891 non-null    int64
 7   Parch        891 non-null    int64
 8   Ticket       891 non-null    object
 9   Fare         891 non-null    float64
 10  Embarked     891 non-null    object
dtypes: float64(2), int64(5), object(4)
memory usage: 76.7+ KB
DataFrame saved to res_dpre.csv
   PassengerId  Survived  Pclass   Age  SibSp  ...  Sex_male  Embarked_C  Embarked_Q  Embarked_S  Age_category_
0            1         0       3  22.0      1  ...         1           0           0           1    Young Adult
1            2         1       1  38.0      1  ...         0           1           0           0          Adult
2            3         1       3  26.0      0  ...         0           0           0           1    Young Adult
3            4         1       1  35.0      1  ...         0           0           0           1          Adult
4            5         0       3  35.0      0  ...         1           0           0           1          Adult

[5 rows x 13 columns]
Visualization saved as vis.png.
```
