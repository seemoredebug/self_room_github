package com.example.selfroom.control;
import com.example.selfroom.service.UserDataService;
import com.example.selfroom.until.JwtUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@RestController
public class TestController {
    @Autowired
    UserDataService userDataService = new UserDataService();

    @RequestMapping("/author/hello")
    public String hello() {
        return "hello world";
    }

    @RequestMapping("/auth/login")
    public String login(String username, String pass) {
        if(userDataService.findPassword(username).equals(pass)){
        //假设数据库中查询到了该用户，这里测试先所及生成一个UUID，作为用户的id
        String userId = UUID.randomUUID().toString();

        //准备存放在IWT中的自定义数据
        Map<String, Object> info = new HashMap<>();
        info.put("username", "tom");
        info.put("pass", "admin");

        //生成JWT字符串
        String token = JwtUtil.sign(userId, info);

        return "token:" + token;}
        else
            return "false";
    }
}

