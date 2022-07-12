from demoblaze_client import DemoblazeClient


class TestDemoblaze:
    def test_cart(self):
        client = DemoblazeClient("rotem_ofer", "123454321")
        items_in_cart = client.get_cart_items_id_list()
        assert len(items_in_cart) == 1
        item_id = items_in_cart[0]
        assert item_id == 3
        assert client.get_item_price(item_id) == 650
        assert client.get_item_title(item_id) == "Nexus 6"



