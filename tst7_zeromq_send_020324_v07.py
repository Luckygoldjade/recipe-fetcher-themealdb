#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#
import zmq
import json
context = zmq.Context()
print(f"Current libzmq version is {zmq.zmq_version()}")
print(f"Current  pyzmq version is {zmq.__version__}")


#  Socket to talk to server
def send_message(json_message):
    print("Connecting to zeroMQ server…")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    str_json_mess = json.dumps(json_message)
    socket.send_string(str_json_mess)     # Sends the UTF-8 encoded string as bytes
    reply = socket.recv_string()
    print("Received reply ", reply)
    print(type(reply))
    return reply

    # socket.send(b"Hello")           # Sends the bytes directly
    # reply2 = socket.recv()
    # print("Received reply ", reply2)
    # return reply2


if __name__ == "__main__":
    test_json = [{
      "idIngredient": "534",
      "strIngredient": "Noodles",
      "strDescription": "Noodles are a staple food in many cultures. They are made from unleavened dough which is stretched, extruded, or rolled flat and cut into one of a variety of shapes. While long, thin strips may be the most common, many varieties of noodles are cut into waves, helices, tubes, strings, or shells, or folded over, or cut into other shapes. Noodles are usually cooked in boiling water, sometimes with cooking oil or salt added. They are often pan-fried or deep-fried. Noodles are often served with an accompanying sauce or in a soup. Noodles can be refrigerated for short-term storage or dried and stored for future use. The material composition or geocultural origin must be specified when discussing noodles. The word derives from the German word Nudel.[1]",
      "strType": "Side"
    }, {
      "idIngredient": "535",
      "strIngredient": "Wood Ear Mushrooms",
      "strDescription": "Auricularia auricula-judae, known as the Jew's ear, wood ear, jelly ear or by a number of other common names, is a species of edible Auriculariales fungus found worldwide. The fruiting body is distinguished by its noticeably ear-like shape and brown colouration; it grows upon wood, especially elder. Its specific epithet is derived from the belief that Judas Iscariot hanged himself from an elder tree; the common name \"Judas's ear\" was largely eclipsed by the corruption \"Jew's ear\", while today \"jelly ear\" and other names are sometimes used. The fungus can be found throughout the year in temperate regions worldwide, where it grows upon both dead and living wood.\r\n\r\nIn the West, A. auricula-judae was used in folk medicine as recently as the 19th century for complaints including sore throats, sore eyes and jaundice, and as an astringent. Although it is not widely consumed in the West, it has long been popular in China, to the extent that Australia exported large volumes to China in the early twentieth century. Today, the fungus is a popular ingredient in many Chinese dishes, such as hot and sour soup, and also used in Chinese medicine. It is also used in Ghana, as a blood tonic. Modern research into possible medical applications has variously concluded that A. auricula-judae has antitumour, hypoglycemic, anticoagulant and cholesterol-lowering properties.", 
      "strType": "Vegetable"}]

    send_message(test_json)
    # send_message("Hello")
    print("Done")
