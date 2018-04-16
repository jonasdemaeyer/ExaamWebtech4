package edu.ap.spring.controllers;

import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import edu.ap.spring.redis.RedisService;

public class RedisController {

	private RedisService service;
	
	   @Autowired
		public void setRedisService(RedisService service) {
			this.service = service;
	   }
	   
	   @RequestMapping("/list")
	   @ResponseBody
	   public String list() {
		   String html = "<HTML>";
		   
		   Set<byte[]> studenten = service.setKey(key, html);
		   Set<byte[]> examen = service.setKey(key, html);
		   Set<byte[]> reden = service.setKey(key, html);
		   Set<byte[]> datum = service;
		   
	   }
	   
	   
}
