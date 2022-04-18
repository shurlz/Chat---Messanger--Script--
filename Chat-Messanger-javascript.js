class Chat_App {
    constructor(){
        this.users = {};
        this.logged_in = false;
        this.Current_User = null;
    }
    sign_up(user_name,password){
        if(user_name in Object.keys(this.users)){
            return 'username already taken by another user !'
        }
        else{
            this.users[user_name] = [password , [] , {'chatty': 'welcome to the network...'}]
            return 'sign-up successful!'
        }
    }
    log_in(user_name,password){
        var all_users = Object.keys(this.users)
        for (var all_names of all_users){
            if (all_names == user_name && password == this.users[user_name][0] && this.logged_in == false){
                this.logged_in = true;
                this.Current_User = user_name;
                var messages = this.users[user_name][2];
                console.log('login successful '+ user_name +' Here are your messages')
                for (var sender of Object.keys(messages)){
                    return sender +' : '+ messages[sender]
                }
            }
            if (this.logged_in == true){
                return 'Log-in unsuccessful.. Another user still online'
            }
            return 'Invalid log-in credentials'
        }
    }

    send_message(reciever_username,message){
        if (this.logged_in == true){
            for (var x in this.users[this.Current_User][1]){
                if (reciever_username == this.users[this.Current_User][1][x]){
                    this.users[reciever_username][2][this.Current_User] = message
                    return 'Message sent successfully !'
                }
            }
            return  'you have no friend named ' + reciever_username
        }
    }
    add_friends(friend_username){
        for (var x=0;x<=Object.keys(this.users).length;x++){
            if (this.logged_in == true && friend_username == Object.keys(this.users)[x]){
                this.users[this.Current_User][1].push(friend_username)
                return 'Friend added successfully...'
            }
        }
        return 'Unsuccessful...'
    }

    log_out(username){
        if (username == this.Current_User){
            this.logged_in = false
            return 'Logged out successfully'
        }
        return 'logout unsuccessful'
    }

    display_users_info(){
        return this.users
    }
}

