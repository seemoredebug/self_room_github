package com.example.selfroom.bean;


import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class RoomData {
    private String roomNumber;
    private  int margin;
    private String floor;
}
