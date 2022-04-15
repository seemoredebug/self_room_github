package com.example.selfroom.bean;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class UsageRecord {
    private  String recordNumber;
    private  String seatTime;
    private  String roomNumber;
    private  String score;
}
