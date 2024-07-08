import requests


def select_characters(ip, token):
    url = ip + "/characters?page=1&limit=20"
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        characters = response.json()
        print("请选择一个角色:")
        for i, character in enumerate(characters):
            print(f"{i + 1}. {character['name']} (ID: {character['id']})")

        choice = int(input("请输入角色编号(1,2,3...): ")) - 1
        while True:
            if 0 <= choice < len(characters):
                selected_character = characters[choice]
                return selected_character["id"], selected_character["name"], selected_character["greetings"]
            else:
                print("无效的选择，请输入有效的角色编号。")
                choice = int(input("请输入角色编号(1,2,3...): ")) - 1
    else:
        print(f"获取角色列表失败，状态码: {response.status_code}")
        return None
