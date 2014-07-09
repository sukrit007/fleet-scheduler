import fleetctl_wrapper as fleetctl
import fleet_fabric

__author__ = 'sukrit'
__all__ = ['get_provider','get_client','FleetClient']

_DEFAULT_PROVIDER = 'fabric'

_PROVIDER_DICT = {
    'fleetctl': fleetctl.Provider,
    'fabric': fleet_fabric.Provider
}

def get_provider(type=_DEFAULT_PROVIDER, **kwargs):
    if type in _PROVIDER_DICT:
        return _PROVIDER_DICT[type](**kwargs)
    else:
        return None

if __name__ == "__main__":
    client = get_provider(
        hosts='ec2-54-176-123-236.us-west-1.compute.amazonaws.com')
    print(client.client_version())