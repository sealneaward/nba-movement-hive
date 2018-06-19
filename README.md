# nba-movement-hive
Tutorial on creating cloud infrastructure to store and use SportVU movement data. This tutorial was made for linux users.

### Package Setup

1. Modify the `movement/constant.py` file for the cloned repo location.

```py
import os
# change this data_dir for personal path
if os.environ['HOME'] == '/home/neil':
    data_dir = '/home/neil/projects/nba-movement-hive'
else:
    raise Exception("Unspecified data_dir, unknown environment")
```

2. Install the Python package

```
python setup.py build
sudo python setup.py install
```

### Data Setup

1. Extract the data from the `data` folder
```
cd data/
sudo ./setup.sh
```

2. Convert the json files to the proper csv files

```
python movement/json_to_csv.py
```

# Amazon Setup

### PEM Setup

AWS requires a secure key in order to SSH into the EMR instances. In order to do so, instructions are provided to create a pem key on the EC2 console below.

![pem key](img/pem-creation.png)

### S3 and EMR Setup

1. Create an S3 bucket on AWS and upload the csv documents extracted to the bucket. Make sure each item in the bucket is public.

![item public](s3-public.png)

2. Create a default EMR cluster on m1.medium instances (cheapest available) with one master and 2 core nodes. Wait until the cluster has a `waiting` status.

3. SSH into the EMR cluster.
