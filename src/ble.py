import asyncio
from contextlib import suppress
from bleak import BleakClient, BleakScanner

status_uuid = "8d376736-3011-4f93-acbc-5bc8f49c8c00"

#class commands(enum.IntEnum):
#    CMD_SYNC = 0,
#    CMD_START = 1,
#    CMD_OVERRIDE = 2,
#    CMD_STOP = 3

class Ble(object):
    def __init__(self):
        self.node_status = []

    async def connect(self, address):
        self.address = address
        self.client = BleakClient(self.address)
        try:
            await self.client.connect()
            return True
        except Exception as e:
            print(f"An error occurred while connecting: {e}")
            return False

    async def poll_devices(self):
        devices = await BleakScanner.discover(timeout=20)
        return devices
    
    async def asynctest(self):
        await asyncio.sleep(5)  # Sleep for a short duration

    async def request_status(self):
        try:
            result = await self.client.read_gatt_char(status_uuid)
            return result
        except Exception as e:
            # Handle the exception
            print(f"An error occurred while requesting status: {e}")
            return None