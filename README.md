# Brainfreeze

![logo](images/brainfreeze_logo.png)

Mind maps for Cisco ISE APIs

![dACLS](/images/example.png)

## Installation

In your project directory, create your virtual environment

``` console
python3 -m venv env
```

Activate (use) your new virtual environment (Linux):

``` console
source env/bin/activate
```

Download or clone the brainfreeze repository:

``` console
git clone https://github.com/automateyournetwork/brainfreeze.git
```

Update your target ISE IP Address on lines 20-21

```python

ise = "10.10.20.70:9060"
mnt = "10.10.20.70:443"

```

Update your target ISE Credentials (find and replace)

```python

auth=('admin', 'C1sco12345!')

```

Change into the MindMaps folder and run the BrainFreeze.py file

```python
python3 BrainFreeze.py
```

## Try it with a Sandbox 

Brainfreeze is ready-to-go with the Cisco DevNet Always On Sandbox 

Simply reserve the PxGrid 2.0 with ISE Sanbox

[Sandbox](https://devnetsandbox.cisco.com/RM/Topology)

![Sandbox](/images/sandbox.png)

Establish the VPN 

### Important! 

Enable the External RESTful Service (ESR) in ISE by visiting

[ISE](https://10.10.20.70/)

Log-in as 

admin
C1sco12345!

Then navigating to 

![ISE_Admin](/images/ISE_Admin.png)

Then select ERS Settings 

Check Enable ERS for Read/Write

Acknoweldge

![ERS_Enable](/images/enable_ers.png)

Save

![Save](/images/save.png)

You are now ready to run Brainfreeze

## View the Mindmaps 

Install the markmap VS Code Extension

![Mark Map](/images/markmap.png)

Open the markdown file and click the "Open as markmap" 
