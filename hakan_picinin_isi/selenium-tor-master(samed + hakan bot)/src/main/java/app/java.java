/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package app;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import com.subgraph.orchid.TorClient;
import java.util.Random;
import com.google.gson.Gson;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.*;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.Select;
import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Set;
import java.util.List;
import org.eclipse.jetty.util.log.Log;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxBinary;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.FirefoxProfile;
import org.openqa.selenium.remote.DriverCommand;

class java {
    static FirefoxDriver driver;

    public static void main(String[] args) throws InterruptedException {

        try {
            run();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void run() throws InterruptedException, IOException {

        List<String> prosList = new ArrayList<>();
        prosList.add("C:\\Profile\\00001.default");
        prosList.add("C:\\Profile\\00002.default");
        prosList.add("C:\\Profile\\00003.default");
        prosList.add("C:\\Profile\\00004.default");
        prosList.add("C:\\Profile\\00005.default");
        prosList.add("C:\\Profile\\00006.default");
        prosList.add("C:\\Profile\\00008.default");

        List<String> adsList = new ArrayList<>();
        adsList.add("Don't miss your share on pie, follow supreme pumps channel to be aware of greatest pumps every monday, you never want to miss!! ");
        adsList.add("Supreme pumps manipulates crypto market for your profits, we are stronger together, please follow our telegram channel and don't miss anything.");
        adsList.add("S U P R E M E _ P U M P S! the best market manipulator group in cryptopia. You can follow us from telegram. We manipulate coins successfully.");
        adsList.add("If you have lost because of last decreases at coin prices, you can make up with us. Supreme pumps is our telegram channel.");
        adsList.add("Supreme pumps : you need to follow these guys on telegram." );
        adsList.add("hello8"        );

        String adslink;
        adslink = adsList.get(0);

        List<String> groupnameList = new ArrayList<>();
        groupnameList.add("simpletoken");
        groupnameList.add("alphaprotocol");
        groupnameList.add("Dccofficial");
        groupnameList.add("soft2b");
        groupnameList.add("icc_community");
        groupnameList.add("tbtcoingroup");
        groupnameList.add("satoshigame_en8");
        groupnameList.add("fishchain");
        groupnameList.add("monacocard");
        groupnameList.add("rcnchat");
        groupnameList.add("telcoincommunity");
        groupnameList.add("airswap");
        groupnameList.add("Deepbrainchain");
        groupnameList.add("decentralandkorea");
        groupnameList.add("htmlcoinofficial");
        groupnameList.add("ins_ecosystem");
        groupnameList.add("ins_ecosystem_ko");
        groupnameList.add("ins_ecosystem_ru");
        groupnameList.add("appcoinsofficial");
        groupnameList.add("emc2_official");
        groupnameList.add("counterparty");
        groupnameList.add("counterparty_xcp");
        groupnameList.add("realistatoken");
        groupnameList.add("hotchain6");
        groupnameList.add("hydroprotocol");
        groupnameList.add("leekicooficial");
        groupnameList.add("acuteanglecloud_thailand");
        groupnameList.add("realchainEnglish");
        groupnameList.add("iotchain");
        groupnameList.add("xtrabytes_official");
        groupnameList.add("zencash");
        groupnameList.add("tierion");
        groupnameList.add("peercoin");
        groupnameList.add("unikrn");
        groupnameList.add("adex_trading");
        groupnameList.add("centratech");
        groupnameList.add("cybermiles");
        groupnameList.add("cybermilesvn");
        groupnameList.add("cybermiles");
        groupnameList.add("utrust");
        groupnameList.add("nulsio");
        groupnameList.add("spankchain");
        groupnameList.add("metaverse_blockchain");
        groupnameList.add("steamrdata");
        groupnameList.add("etherparty");
        groupnameList.add("medisharesen");
        groupnameList.add("trinitystatechannels");
        groupnameList.add("breadchat");
        groupnameList.add("district0x");
        groupnameList.add("coindash");
        groupnameList.add("wingschat");
        groupnameList.add("wingschatru");
        groupnameList.add("guldentalk");
        groupnameList.add("qlinkmobile");
        groupnameList.add("qlinkcommunity");
        groupnameList.add("electracoin");
        groupnameList.add("viacoin");
        groupnameList.add("decent");
        groupnameList.add("lunyrcommunity");
        groupnameList.add("nagaico");
        groupnameList.add("nagacoincommunity");
        groupnameList.add("nagacurrency");
        groupnameList.add("burstcoin");
        groupnameList.add("horizonstate");
        groupnameList.add("oysterprotocol");
        groupnameList.add("mobilego");
        groupnameList.add("giftoofficial");
        groupnameList.add("wagerrcoin");
        groupnameList.add("tokencard");
        groupnameList.add("shiftnrg");
        groupnameList.add("groestl");
        groupnameList.add("lykke");
        groupnameList.add("selfkeyfoundation");
        groupnameList.add("voxelaps");
        groupnameList.add("minexcoin");
        groupnameList.add("paywithink");
        groupnameList.add("bitdegree");
        groupnameList.add("wetrustplatform");
        groupnameList.add("taasfund");
        groupnameList.add("cossunofficial");
        groupnameList.add("mycoss");
        groupnameList.add("quoine");
        groupnameList.add("sharecoin");
        groupnameList.add("cortexlabszh");
        groupnameList.add("cpg_cn");
        groupnameList.add("beekan_org");
        groupnameList.add("btcaso_cn");
        groupnameList.add("Atn_blockchain");
        groupnameList.add("Officialyoulive");
        groupnameList.add("iqbgroup");




//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        FirefoxProfile profile = new FirefoxProfile(new File(prosList.get(0)));
        FirefoxDriver driver = new FirefoxDriver(profile);

//++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        int max, min, max2, min2, i, r, p;

        max = 120000;
        min = 70000;
        max2 = 19000;
        min2 = 6000;

        i=0;
        r=6;
        p=0;
        while(true){
        for(String groupname:groupnameList) {

            try {
                Thread.sleep(2000);
                i++;
                Thread.sleep(2000);
                System.out.print(i);
                if (i % r == 0) {
                    try {

                        Thread.sleep(3000);
                        driver.quit();
                        Thread.sleep(56000);
                        driver = new FirefoxDriver(profile);
                        Thread.sleep(4000);
                        FileUtils.deleteDirectory(new File("C:\\Users\\Mavi\\AppData\\Local\\Mozilla\\updates"));
                        Thread.sleep(2000);

                    } catch (Exception e) {
                        Thread.sleep(3000);
                    }
                }

                Thread.sleep(6000);
                driver.get("https://web.telegram.org/#/im?p=@" + groupname);
                Thread.sleep(5000);
                Random uzun = new Random();
                Thread.sleep(2000);
                Random kisa = new Random();
                Thread.sleep(3000);
                int uzunNumber = uzun.nextInt(max + 1 - min) + min;
                System.out.print(uzunNumber);
                Thread.sleep(2000);
                int kisaNumber = kisa.nextInt(max2 + 1 - min2) + min2;
                System.out.print(kisaNumber);
                Thread.sleep(2000);

                if (driver.findElementsByXPath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[1]/div[2]/div/a").size() != 0){
                    try {

                        Thread.sleep(2000);
                        driver.findElement(By.xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[1]/div[2]/div/a")).click();
                        Thread.sleep(uzunNumber);

                    } catch (Exception e) {
                        Thread.sleep(30000);
                    }

                }

                driver.findElement(By.xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]")).sendKeys(adslink);
                Thread.sleep(kisaNumber);
                driver.findElement(By.xpath("/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]")).sendKeys(Keys.ENTER);
                Thread.sleep(kisaNumber);

                if (driver.findElementsByXPath("/html/body/div[5]/div[2]/div/div/div[1]/div[2]/div").size() != 0){
                    try {

                        Thread.sleep(4500);
                        driver.findElement(By.xpath("/html/body/div[5]/div[2]/div/div/div[1]/div[2]/div/a")).click();
                        Thread.sleep(4000);
                        String mesaj;
                        mesaj = driver.findElement(By.xpath("/html/body/div[5]/div[2]/div/div/div[1]/div[2]/textarea")).getText();
                        Thread.sleep(3000);
                        System.out.print(mesaj);
                        Thread.sleep(3000);
                        Calendar cal = Calendar.getInstance();
                        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
                        System.out.println( sdf.format(cal.getTime()) );

                        if(mesaj.equals("Method: messages.sendMessage\n" +
                                "Result: {\"_\":\"rpc_error\",\"error_code\":400,\"error_message\":\"USER_BANNED_IN_CHANNEL\"}")){try{

                            Thread.sleep(3000);
                            p++;
                            Thread.sleep(3000);
                            profile = new FirefoxProfile(new File(prosList.get(p)));
                            Thread.sleep(3000);
                            driver.quit();
                            Thread.sleep(3000);
                            driver = new FirefoxDriver(profile);
                            Thread.sleep(3000);
                            adslink = adsList.get(p);
                            Thread.sleep(3000);


                        }catch (Exception e){
                            Thread.sleep(13000);
                        }


                        }


                    } catch (Exception e) {

                        Thread.sleep(23000);

                    }

                }










            } catch (Exception e) {Thread.sleep(4000);}









        }





        }}


    protected static void clickElementByXPathViaJavascript(String xPath){
        if (driver instanceof JavascriptExecutor) {
        }
    }

}
