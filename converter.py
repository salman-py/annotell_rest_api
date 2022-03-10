# TODO: logic of __main
import json


class ReadFile():

    def fixkey(self, key):
        # key replace implementation
        # print("fixing {}".format(key))
        return key.replace("@", "")

    def normalize(self, data):
        # print("normalizing {}".format(data))
        if isinstance(data, dict):
            data = {ReadFile().fixkey(key): ReadFile().normalize(value) for key, value in data.items()}
        elif isinstance(data, list):
            data = [ReadFile().normalize(item) for item in data]
        return data

    def convert(self,data):
        output_data = {"data":{"openlabel":{"objects":{},"frames":{"0":{"objects":{}}}}}}
        if not data:
            raise ValueError("data is not found.")
        if 'shapeProperties' not in data:
            raise ValueError("shapeProperties is not found in given data: Format Issue")
        for object in data['shapeProperties']:
            updated_object = ReadFile().normalize(data['shapeProperties'][object])
            output_data["data"]["openlabel"]["objects"][object] = {"name": object, "type":updated_object["all"]["class"]}
            output_data["data"]["openlabel"]["frames"]["0"]["objects"][object] = {"object_data":{"bbox": [{"name":"bbox - "+object.split("-")[0],"stream":"Cam","val":[]}],"boolean":[{"name":"unclear","val":False}],"text":[{"name":"ObjectType","val":"car"}]}}
        result = json.dumps(output_data)
        return result