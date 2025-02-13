def update_server(FileName, Key, Value):
    with open(FileName,"r") as file:
        lines = file.readline()
    with open(FileName, "w") as file:
        for line in lines:
            if Key in line:
                file.write(Key+" = "+Value)
            else:
                file.write(line)
server_config_file = "Server.conf"
key_to_update = "Max_Connections"
value_to_update = "500"
update_server(server_config_file,key_to_update,value_to_update)

