package com.example.selfroom.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class UserData {
    private String name;
    private String score;
    private int    sex;
    private String mobile;
    private String studentClass;
    private String college;
    private String account;
}
