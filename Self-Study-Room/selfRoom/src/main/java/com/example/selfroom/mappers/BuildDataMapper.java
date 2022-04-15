package com.example.selfroom.mappers;

import com.example.selfroom.bean.BuildData;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface BuildDataMapper {
    public List<BuildData> getBuildData(int floor);
}
