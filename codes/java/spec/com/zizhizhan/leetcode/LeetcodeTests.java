package com.zizhizhan.leetcode;

import lombok.extern.slf4j.Slf4j;
import org.junit.Test;

@Slf4j
public class LeetcodeTests {

    @Test
    public void testLogging() {
        //日志输出
        log.error("error");
        log.warn("wring");
        log.info("info");
        log.debug("debug");
        log.trace("trance");

        //异常处理
        try {
            int i = 1 / 0;
        } catch (Exception e) {
            log.error("发生异常：{}", e.getMessage(), e);
        }
    }
}
