from KalturaClient import *
from KalturaClient.Plugins.Core import *

config = KalturaConfiguration(2637961)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
ks = client.session.start(
      "0ef822be27e43834cd2e7c22e4d76399",
      "dselasi4u@gmail.com",
      KalturaSessionType.ADMIN,
      "2637961")
client.setKs(ks)
