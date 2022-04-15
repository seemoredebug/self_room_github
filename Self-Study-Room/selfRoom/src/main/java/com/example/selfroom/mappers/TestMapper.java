package com.example.selfroom.mappers;


import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface TestMapper {
    public String getTest(String score);
}
