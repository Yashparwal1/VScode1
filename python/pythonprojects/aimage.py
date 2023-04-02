import requests, json, time
api = "ac735035-f3a8-40d4-a37c-f466e77c24e7"

headers = {
    "accept":"application/json",
    "content-type":"application/json",
    "authorization":f"Bearer {api}"
}

images =[ 
    "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLJxGIkwpMeDQ4-_wjgCXi6_57yiupD52gI3v7P600uv-Wp19ni-VwFQlNwq3EqxBcb1So1H_MzKflH7_lX2BUqzODWpiB-7NN_tYItifa-QgVKZ4JQIGe0GuoV6BaOf3wILb1_0ETUrDDkp7uPJ1iAWCP3Ao9wO9yEv7UL9N8tGaWCkyOXVO0NSMjkQ/s320/10.jpg",
    "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHzAwZ8hid3592BicrQu7if2VBccqtaKawWIQaQMSSPw89lTwT_1S7j3X47fTDVYYQbSzi-j3yWCb3Bb3huVYO2fKMdjjP2x_K9oMgHzPpF35mPgPPEf_Ms9irnbSYVJ2O162iVM2DGW9sahDOpDA9LB0rGBPeBUc_1Kl5gfq_SArlKB1kkKT5N-jNuQ/s1952/1.jpg",
    "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhZUIaaIjfLNjYalsgRDT1J5DdjgCerlopfMXMHWk_sE0gyA_WH1WR_AogPj7iV2qHIkETiM0scYXr-lCIO3EldFLWvFa-r4OtodqAJgBqCa8y1VDN4ixIDiO4BW0onu2SrDZySeeZi1XGhx7xVYuNcVbtBLBCS7utTVxZI0OT6wnWCiRPfCttb_e4bnQ/s864/2.jpg",
    "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgGDgqVQrdkNbqi8nuv62B53KRtqDJpdbdWi7oPmo90KDn46g9rBnUp3_aVaD0fZTLVP3xNmObz8XKt3TTue0moBSh1uj4aIwPRwHcnzqATF-Dz7jBC1wcvqkIF3Qu9NnonQlFv8OAOFehctl-pHoEUHn3c8G-f9VL3Qebj5C2jNdMQmkEorNPcpTl23g/s1337/4.jpg"
]

def model(title):
    url = "https://api.tryleap.ai/api/v1/images/models/"
    payload = {
        "title":title,
        "subjectKeyword":"@me"
    }
    resp = requests.post(url,json=payload,headers=headers)
    model_id = json.loads(resp.text)["id"]
    return model_id

def image_dataset(model_id):
    url=f"https://api.tryleap.ai/api/v1/images/models/{model_id}/samples/url"
    payload = {"images":images}
    resp = requests.post(url, json=payload, headers=headers)

def queue_training(model_id):
    url=f"https://api.tryleap.ai/api/v1/images/models/{model_id}/queue"
    resp = requests.post(url, headers=headers)
    data = json.loads(resp.text)
    print(data)
    version_id = data["id"]
    status = data["status"]
    print(f"Version ID: {version_id}. Status: {status}")
    return version_id, status

def get_model_version(model_id, version_id):
    url=f"https://api.tryleap.ai/api/v1/images/models/{model_id}/versions/{version_id}"
    resp = requests.get(url, headers=headers)
    data = json.loads(resp.text)
    version_id = data["id"]
    status = data["status"]
    print(f"Version ID: {version_id}. Status: {status}")
    return version_id, status

def genetare_image(model_id, prompt):
    url=f"https://api.tryleap.ai/api/v1/images/models/{model_id}/inferences"
    payload = {
        "prompt":prompt,
        "steps":50,
        "width":512,
        "height":512,
        "noOfImages":1,
        "seed":4532184
    }
    resp = requests.post(url, json=payload, headers=headers)
    data = json.loads(resp.text)
    inference_id = data["id"]
    status = data["status"]
    print(f"Inference ID: {inference_id}. Status: {status}")
    return inference_id, status

def get_inference_job(model_id, inference_id):
    url=f"https://api.tryleap.ai/api/v1/images/models/{model_id}/inferences/{inference_id}"
    resp = requests.get(url, headers=headers)
    data = json.loads[resp.text]
    inference_id = data["id"]
    state = data["state"]
    image = None
    if len(data["images"]):
        image = data["images"][0]["uri"]
    print(f"Inference ID: {inference_id}. State: {state}")
    return inference_id, state

model_id = model("Sample")
# print(model_id)
# image_dataset(model_id)
# queue_training(model_id)
# version_id, status = queue_training(model_id) #done

# while status != "finished":
#     time.sleep(10)
#     version_id, status = get_model_version(model_id, version_id) #done

# prompt = input("Enter the prompt: ")
prompt = "A photo of @me on a beach wearing sun glasses, a brown hat, an orange shirt and short pants"
genetare_image(model_id, prompt)
inference_id, status = genetare_image(model_id, prompt)

while status != "finished":
    time.sleep(10)
    inference_id, status, image = get_inference_job(model_id,inference_id)

print(image)