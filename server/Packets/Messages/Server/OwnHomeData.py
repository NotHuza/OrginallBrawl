from Utils.Writer import Writer
from database.DataBase import DataBase
from Logic.PlayerHome import PlayerHome
from Utils.Helpers import Helpers


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        #logic = PlayerHome()
        #logic.encodeHome(self)
        #logic.encodeAvatar(self)
        self.writeVint(2018174)
        self.writeVint(43775)
        self.writeVint(15000)
        self.writeVint(15000)
        self.writeVint(0)
        self.writeVint(99) #trophy road reward collect
        self.writeVint(999999)
        
        self.writeVint(28) #thumbnails.csv
        self.writeVint(20) #icon id
        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(0)
        
        self.writeVint(Helpers.LeaderboardTimer(self))
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(4)
        self.writeVint(1)
        self.writeVint(0)
        
        self.writeVint(29)
        self.writeVint(0)
        
        self.writeVint(20)
        self.writeVint(151775)
        self.writeVint(0)
        self.writeVint(115)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(5)
        self.writeVint(100)
        
        self.writeVint(-1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        #shop slot start
        self.writeVint(2018174) #shop timestamp
        self.writeVint(100)
        self.writeVint(15)
        self.writeVint(30) #big box cost
        self.writeVint(3) #big box multiplier
        self.writeVint(80) #mega box cost
        self.writeVint(10) #mega box multiplier
        self.writeVint(50)
        self.writeVint(1000)
        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900) #???
        #shop slot end
        
        self.writeVint(6) #array
        self.writeVint(0)
        self.writeVint(30)
        self.writeVint(80)
        self.writeVint(170)
        self.writeVint(350)
        self.writeVint(0)
        
        self.writeVint(5) #array
        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(3)
        self.writeVint(4)
        self.writeVint(5)

        
        self.writeHexa('''05ecbdd53a0100bfab050a0f0c00ffffffff00ece9f3390200bf080a0f1000ffffffff00ccfb853903009fda020a0f1700ffffffff00efc6ed3804009fc312020f1500000000115449445f5745454b454e445f4556454e5400ec90f3350500bf08000f2500ffffffff0005eb91b73b01bfab05bff10f0a0f0800ffffffff00cccfe73902bf08bfce0a0a0f2c00ffffffff00ece0f938039fda029fa00d0a0f1200ffffffff00cface138049fc3129f891d0a0f0500ffffffff00ccf6e63505bf08bfce0a000f1c00ffffffff000814238b018c02a204a007a00ca2130801020304050a0f14030a1e90010306143c0314328c020396029006b01202ad090100000a00010b0a00000001010a0a00010b0a0000000102140a00010b0a00000001031e0a00010b0a0000000104281400010b0a00000001053c1400010b0a000000010690011400010b0a0000000107a4011400010b0a0000000108b8011400010b0a00000001098c021400010b0a000000010aa0021400010b0a000000010bb4022800010b0a000000010c9c032800010b0a000000010d84042800010b0a000000010eac042800010b0a000000010f94052800010b0a0000000110bc052800010b0a0000000111a4062800010b0a00000001128c072800010b0a0000000500002800010b140000000501283200010b1400000005029a013c00010b1400000005039602860100010b1400000005049c03900100010b140000000505ac049a0100010b1400000005068606a40100010b140000000507aa07ae0100010b1400000005089809b80100010b140000000509900b820200010b14000000050a920d8c0200010b14000000050b9e0f960200010b14000000050cb411a00200010b14000000050d9414aa0200010b14000000050ebe16b40200010b14000000050fb219be0200010b140000000510b01c880300010b140000000511b81f920300010b1400000005128a239c0300010b140000000513a626a60300010b1400000005148c2ab00300010b140000000515bc2dba0300010b140000000516b631840400010b140000000517ba358e0400010b140000000518883a980400010b140000000519a03ea20400010b14000000051a8243ac0400010b14000000051bae47b60400010b14000000051ca44c800500010b14000000051da4518a0500010b14000000051eae56940500010b14000000051f825c9e0500010b140000000520a061a80500010b1400000005218867b20500010b140000000522ba6cbc0500010b140000000523b672860600010b140000000524bc78900600010b1400000005258c7f9a0600010b140000000526a68501a40600010b1400000005278a8c01ae0600010b140000000528b89201b80600010b140000000529b09901820700010b14000000052ab2a0018c0700010b14000000052bbea701960700010b14000000052c94af01a00700010b14000000052db4b601aa0700010b14000000052e9ebe01b40700010b14000000052f92c601be0700010b14000000053090ce01880800010b14000000053198d601920800010b140000000532aade019c0800010b14000000053386e701a60800010b140000000534acef01b00800010b1400000005359cf801ba0800010b140000000536968102840900010b1400000005379a8a028e0900010b140000000538a89302980900010b140000000539809d02a20900010b14000000053aa2a602ac0900010b14000000053b8eb002b60900010b14000000053c84ba02800a00010b14000000053d84c4028a0a00010b14000000053e8ece02940a00010b14000000053fa2d8029e0a00010b1400000005800180e302a80a00010b14000000058101a8ed02b20a00010b140000000582019af802bc0a00010b14000000058301968303860b00010b140000000584019c8e03900b00010b14000000058501ac99039a0b00010b1400000005860186a503a40b00010b14000000058701aab003ae0b00010b1400000005880198bc03b80b00010b1400000005890190c803820c00010b14000000058a0192d4038c0c00010b14000000058b019ee003960c00010b14000000058c01b4ec03a00c00010b14000000058d0194f903aa0c00010b14000000058e01be8504b40c00010b14000000058f01b29204be0c00010b14000000059001b09f04880d00010b14000000059101b8ac04920d00010b140000000592018aba049c0d00010b14000000059301a6c704a60d00010b140000000594018cd504b00d00010b14000000059501bce204ba0d00010b14000000059601b6f004840e00010b14000000059701bafe048e0e00010b14000000059801888d05980e00010b14000000059901a09b05a20e00010b14000000059a0182aa05ac0e00010b14000000059b01aeb805b60e00010b14000000059c01a4c705800f00010b14000000059d01a4d6058a0f00010b14000000059e01aee505940f00010b14000000059f0182f5059e0f00010b1400000005a001a08406a80f00010b1400000005a101889406b20f00010b1400000005a201baa306bc0f00010b1400000005a301b6b306861000010b1400000005a401bcc306901000010b1400000005a5018cd4069a1000010b1400000005a601a6e406a41000010b1400000005a7018af506ae1000010b1400000005a801b88507b81000010b1400000005a901b09607821100010b1400000005aa01b2a7078c1100010b1400000005ab01beb807961100010b1400000005ac0194ca07a01100010b1400000005ad01b4db07aa1100010b1400000005ae019eed07b41100010b1400000005af0192ff07be1100010b1400000005b001909108881200010b1400000005b10198a308921200010b1400000005b201aab5089c1200010b1400000005b30186c808a61200010b1400000005b401acda08b01200010b1400000005b5019ced08ba1200010b1400000005b601968009841300010b1400000005b7019a93098e1300010b1400000005b801a8a609981300010b1400000005b90180ba09a21300010b1400000005ba01a2cd09ac1300010b1400000005bb018ee109b61300010b1400000005bc0184f509801400010b1400000005bd0184890a8a1400010b1400000005be018e9d0a941400010b1400000005bf01a2b10a9e1400010b1400000005800280c60aa81400010b14000000058102a8da0ab21400010b140000000582029aef0abc1400010b1400000005830296840b861500010b140000000584029c990b901500010b14000000058502acae0b9a1500010b1400000005860286c40ba41500010b14000000058702aad90bae1500010b1400000005880298ef0bb81500010b1400000005890290850c821600010b14000000058a02929b0c8c1600010b14000000058b029eb10c961600010b14000000058c02b4c70ca01600010b14000000058d0294de0caa1600010b14000000058e02bef40cb41600010b14000000058f02b28b0dbe1600010b14000000059002b0a20d881700010b14000000059102b8b90d921700010b140000000592028ad10d9c1700010b14000000059302a6e80da61700010b140000000594028c800eb01700010b14000000059502bc970eba1700010b14000000059602b6af0e841800010b14000000059702bac70e8e1800010b1400000005980288e00e981800010b14000000059902a0f80ea21800010b14000000059a0282910fac1800010b14000000059b02aea90fb61800010b14000000059c02a4c20f801900010b14000000059d02a4db0f8a1900010b14000000059e02aef40f941900010b14000000059f02828e109e1900010b1400000005a002a0a710a81900010b1400000005a10288c110b21900010b1400000005a202bada10bc1900010b1400000005a302b6f410861a00010b1400000005a402bc8e11901a00010b1400000005a5028ca9119a1a00010b1400000005a602a6c311a41a00010b1400000005a7028ade11ae1a00010b1400000005a802b8f811b81a00010b1400000005a902b09312821b00010b1400000005aa02b2ae128c1b00010b1400000005ab02bec912961b00010b1400000005ac0294e512a01b00010b1400000005ad02b48013aa1b00010b1400000005ae029e9c13b41b00010b1400000005af0292b813be1b00010b1400000005b00290d413881c00010b1400000005b10298f013921c00010b1400000005b202aa8c149c1c00010b1400000005b30286a914a61c00010b1400000005b402acc514b01c00010b1400000005b5029ce214ba1c00010b1400000005b60296ff14841d00010b1400000005b7029a9c158e1d00010b1400000005b802a8b915981d00010b1400000005b90280d715a21d00010b1400000005ba02a2f415ac1d00010b1400000005bb028e9216b61d00010b1400000005bc0284b016801e00010b1400000005bd0284ce168a1e00010b1400000005be028eec16941e00010b1400000005bf02a28a179e1e00010b1400000005800380a917a81e00010b14000000058103a8c717b21e00010b140000000582039ae617bc1e00010b14000000058303968518861f00010b140000000584039ca418901f00010b14000000058503acc3189a1f00010b1400000005860386e318a41f00010b14000000058703aa8219ae1f00010b1400000005880398a219b81f00010b1400000005890390c219822000010b14000000058a0392e2198c2000010b14000000058b039e821a962000010b14000000058c03b4a21aa02000010b14000000058d0394c31aaa2000010b14000000058e03bee31ab42000010b14000000058f03b2841bbe2000010b14000000059003b0a51b882100010b14000000059103b8c61b922100010b140000000592038ae81b9c2100010b14000000059303a6891ca62100010b140000000594038cab1cb02100010b14000000059503bccc1cba2100010b14000000059603b6ee1c842200010b14000000059703ba901d8e2200010b1400000005980388b31d982200010b14000000059903a0d51da22200010b14000000059a0382f81dac2200010b14000000059b03ae9a1eb62200010b14000000059c03a4bd1e802300010b14000000059d03a4e01e8a2300010b14000000059e03ae831f942300010b14000000059f0382a71f9e2300010b1400000005a003a0ca1fa82300010b1400000005a10388ee1fb22300010b1400000005a203ba9120bc2300010b1400000005a303b6b520862400010b1400000005a403bcd920902400010b1400000005a5038cfe209a2400010b1400000005a603a6a221a42400010b1400000005a7038ac721ae2400010b1400000005a803b8eb21b82400010b1400000005a903b09022822500010b1400000005aa03b2b5228c2500010b1400000005ab03beda22962500010b1400000005ac03948023a02500010b1400000005ad03b4a523aa2500010b1400000005ae039ecb23b42500010b1400000005af0392f123be2500010b1400000005b003909724882600010b1400000005b10398bd24922600010b1400000005b203aae3249c2600010b1400000005b303868a25a62600010b1400000005b403acb025b02600010b1400000005b5039cd725ba2600010b1400000005b60396fe25842700010b1400000005b7039aa5268e2700010b1400000005b803a8cc26982700010b1400000005b90380f426a22700010b1400000005ba03a29b27ac2700010b1400000005bb038ec327b62700010b1400000005bc0384eb27802800010b1400000005bd038493288a2800010b1400000005be038ebb28942800010b1400000005bf03a2e3289e2800010b14000000058004808c29a82800010b14000000058104a8b429b22800010b140000000582049add29bc2800010b1400000005830496862a862900010b140000000584049caf2a902900010b14000000058504acd82a9a2900010b1400000005860486822ba42900010b14000000058704aaab2bae2900010b1400000005880498d52bb82900010b1400000005890490ff2b822a00010b14000000058a0492a92c8c2a00010b14000000058b049ed32c962a00010b14000000058c04b4fd2ca02a00010b14000000058d0494a82daa2a00010b14000000058e04bed22db42a00010b14000000058f04b2fd2dbe2a00010b14000000059004b0a82e882b00010b14000000059104b8d32e922b00010b140000000592048aff2e9c2b00010b14000000059304a6aa2fa62b00010b140000000594048cd62fb02b00010b14000000059504bc8130ba2b00010b14000000059604b6ad30842c00010b14000000059704bad9308e2c00010b14000000059804888631982c00010b14000000059904a0b231a22c00010b14000000059a0482df31ac2c00010b14000000059b04ae8b32b62c00010b14000000059c04a4b832802d00010b14000000059d04a4e5328a2d00010b14000000059e04ae9233942d00010b14000000059f0482c0339e2d00010b1400000005a004a0ed33a82d00010b1400000005a104889b34b22d00010b1400000005a204bac834bc2d00010b1400000005a304b6f634862e00010b1400000005a404bca435902e00010b1400000005a5048cd3359a2e00010b1400000005a604a68136a42e00010b1400000005a7048ab036ae2e00010b1400000005a804b8de36b82e00010b1400000005a904b08d37822f00010b1400000005aa04b2bc378c2f00010b1400000005ab04beeb37962f00010b1400000005ac04949b38a02f00010b1400000005ad04b4ca38aa2f00010b1400000005ae049efa38b42f00010b1400000005af0492aa39be2f00010b1400000005b00490da39883000010b1400000005b104988a3a923000010b1400000005b204aaba3a9c3000010b1400000005b30486eb3aa63000010b1400000005b404ac9b3bb03000010b1400000005b5049ccc3bba3000010b1400000005b60496fd3b843100010b1400000005b7049aae3c8e3100010b1400000005b804a8df3c983100010b1400000005b90480913da23100010b1400000005ba04a2c23dac3100010b1400000005bb048ef43db63100010b1400000005bc0484a63e803200010b1400000005bd0484d83e8a3200010b1400000005be048e8a3f943200010b1400000005bf04a2bc3f9e3200010b1400000005800580ef3fa83200010b14000000058105a8a140b23200010b140000000582059ad440bc3200010b14000000058305968741863300010b140000000584059cba41903300010b14000000058505aced419a3300010b1400000005860586a142a43300010b14000000058705aad442ae3300010b14000000058805988843b83300010b1400000005890590bc43823400010b14000000058a0592f0438c3400010b14000000058b059ea444963400010b14000000058c05b4d844a03400010b14000000058d05948d45aa3400010b14000000058e05bec145b43400010b14000000058f05b2f645be3400010b14000000059005b0ab46883500010b14000000059105b8e046923500010b140000000592058a96479c3500010b14000000059305a6cb47a63500010b140000000594058c8148b03500010b14000000059505bcb648ba3500010b14000000059605b6ec48843600010b14000000059705baa2498e3600010b1400000005980588d949983600010b14000000059905a08f4aa23600010b14000000059a0582c64aac3600010b14000000059b05aefc4ab63600010b14000000059c05a4b34b803700010b14000000059d05a4ea4b8a3700010b14000000059e05aea14c943700010b14000000059f0582d94c9e3700010b1400000005a005a0904da83700010b1400000005a10588c84db23700010b1400000005a205baff4dbc3700010b1400000005a305b6b74e863800010b1400000005a405bcef4e903800010b1400000005a5058ca84f9a3800010b1400000005a605a6e04fa43800010b1400000005a7058a9950ae3800010b1400000005a805b8d150b83800010b1400000005a905b08a51823900010b1400000005aa05b2c3518c3900010b1400000005ab05befc51963900010b1400000005ac0594b652a03900010b1400000005ad05b4ef52aa3900010b1400000005ae059ea953b43900010b1400000005af0592e353be3900010b1400000005b005909d54883a00010b1400000005b10598d754923a00010b1400000005b205aa91559c3a00010b1400000005b30586cc55a63a00010b1400000005b405ac8656b03a00010b1400000005b5059cc156ba3a00010b1400000005b60596fc56843b00010b1400000005b7059ab7578e3b00010b1400000005b805a8f257983b00010b1400000005b90580ae58a23b00010b1400000005ba05a2e958ac3b00010b1400000005bb058ea559b63b00010b1400000005bc0584e159803c00010b1400000005bd05849d5a8a3c00010b1400000005be058ed95a943c00010b1400000005bf05a2955b9e3c00010b1400000005800680d25ba83c00010b14000000058106a88e5cb23c00010b140000000582069acb5cbc3c00010b1400000005830696885d863d00010b140000000584069cc55d903d00010b14000000058506ac825e9a3d00010b1400000005860686c05ea43d00010b14000000058706aafd5eae3d00010b1400000005880698bb5fb83d00010b1400000005890690f95f823e00010b14000000058a0692b7608c3e00010b14000000058b069ef560963e00010b14000000058c06b4b361a03e00010b14000000058d0694f261aa3e00010b14000000058e06beb062b43e00010b14000000058f06b2ef62be3e00010b14000000059006b0ae63883f00010b14000000059106b8ed63923f00010b140000000592068aad649c3f00010b14000000059306a6ec64a63f00010b140000000594068cac65b03f00010b14000000059506bceb65ba3f00010b14000000059606b6ab66844000010b14000000059706baeb668e4000010b1400000005980688ac67984000010b14000000059906a0ec67a24000010b14000000059a0682ad68ac4000010b14000000059b06aeed68b64000010b14000000059c06a4ae69804100010b14000000059d06a4ef698a4100010b14000000059e06aeb06a944100010b14000000059f0682f26a9e4100010b1400000005a006a0b36ba84100010b1400000005a10688f56bb24100010b1400000005a206bab66cbc4100010b1400000005a306b6f86c864200010b1400000005a406bcba6d904200010b1400000005a5068cfd6d9a4200010b1400000005a606a6bf6ea44200010b1400000005a7068a826fae4200010b1400000005a806b8c46fb84200010b1400000005a906b08770824300010b1400000005aa06b2ca708c4300010b1400000005ab06be8d71964300010b1400000005ac0694d171a04300010b1400000005ad06b49472aa4300010b1400000005ae069ed872b44300010b1400000005af06929c73be4300010b1400000005b00690e073884400010b1400000005b10698a474924400010b1400000005b206aae8749c4400010b1400000005b30686ad75a64400010b1400000005b406acf175b04400010b1400000005b5069cb676ba4400010b1400000005b60696fb76844500010b1400000005b7069ac0778e4500010b1400000005b806a88578984500010b1400000005b90680cb78a24500010b1400000005ba06a29079ac4500010b1400000005bb068ed679b64500010b1400000005bc06849c7a804600010b1400000005bd0684e27a8a4600010b1400000005be068ea87b944600010b1400000005bf06a2ee7b9e4600010b1400000005800780b57ca84600010b14000000058107a8fb7cb24600010b140000000582079ac27dbc4600010b1400000005830796897e864700010b140000000584079cd07e904700010b14000000058507ac977f9a4700010b1400000005860786df7fa44700010b14000000058707aaa68001ae4700010b1400000005880798ee8001b84700010b1400000005890790b68101824800010b14000000058a0792fe81018c4800010b14000000058b079ec68201964800010b14000000058c07b48e8301a04800010b14000000058d0794d78301aa4800010b14000000058e07be9f8401b44800010b14000000058f07b2e88401be4800010b14000000059007b0b18501884900010b14000000059107b8fa8501924900010b140000000592078ac486019c4900010b14000000059307a68d8701a64900010b140000000594078cd78701b04900010b14000000059507bca08801ba4900010b14000000059607b6ea8801844a00010b14000000059707bab489018e4a00010b1400000005980788ff8901984a00010b14000000059907a0c98a01a24a00010b14000000059a0782948b01ac4a00010b14000000059b07aede8b01b64a00010b14000000059c07a4a98c01804b00010b14000000059d07a4f48c018a4b00010b14000000059e07aebf8d01944b00010b14000000059f07828b8e019e4b00010b1400000005a007a0d68e01a84b00010b1400000005a10788a28f01b24b00010b1400000005a207baed8f01bc4b00010b1400000005a307b6b99001864c00010b1400000005a407bc859101904c00010b1400000005a5078cd291019a4c00010b1400000005a607a69e9201a44c00010b1400000005a7078aeb9201ae4c00010b1400000005a807b8b79301b84c00010b1400000005a907b0849401824d00010b1400000005aa07b2d194018c4d00010b1400000005ab07be9e9501964d00010b1400000005ac0794ec9501a04d00010b1400000005ad07b4b99601aa4d00010b1400000005ae079e879701b44d00010b1400000005af0792d59701be4d00010b1400000005b00790a39801884e00010b1400000005b10798f19801924e00010b1400000005b207aabf99019c4e00010b1400000006000005000106010000010b00000000000601050a0002030110080006010000010b000000000006020f0a000106010000010b00000000000603190a00010d000002010b00000000000604230a000106010000010b000000000006052d0f0002030110010006010000010b000000000006063c28000106010000010b00000000000607a4013200010988030000010b0000000000060896023200020c19000006010000010b000000000006098803320002030110020006010000010b0000000000060aba0332000106010000010b0000000000060bac043200010d000003010b0000000000060c9e053200020c19000006010000010b0000000000060d900632000106010000010b0000000000060e8207320002030110070006010000010b0000000100060fb40732000101320000010b00000001000610a6083200020c19000006010000010b0000000100061198093200010e010000010b000000010106128a0a32000101320000010b00000001010613bc0a32000106010000010b00000001010614ae0b3200010d000004010b00000001020615a00c3200020c19000006010000010b00000001020616920d32000101320000010b00000001020617840e320001070a0000010b00000001020618b60e320002030110030006010000010b00000002000619a80fa401000101320000010b0000000200061a8c11a401000106010000010b0000000200061bb012a40100020c8b01000006010000010b0000000201061c9414a401000101320000010b0000000201061db815a40100020c19000006010000010b0000000201061e9c17a40100010e010000010b0000000202061f8019a401000101320000010b00000002020620a41aa401000106010000010b00000002020621881ca40100020c19000006010000010b00000002020622ac1da4010002030110090006010000010b00000003000623901fa401000101320000010b00000003000624b420a401000106010000010b000000030006259822a40100020c9602000006010000010b00000003010626bc23a401000101320000010b00000003010627a025a401000106010000010b000000030106288427a40100010196020000010b00000003020629a828a401000106010000010b0000000302062a8c2aa40100020c19000006010000010b0000000302062bb02ba401000101320000010b0000000302062c942da40100020301100e0006010000010ba40100000400062db82ea401000101320000010ba40100000400062e9c30a40100020c19000006010000010ba40100000400062f8032a401000101ac040000010b8c02000004010630a433a401000106010000010b8c020000040106318835a401000101320000010b8c02000004010632ac36a40100010998090000010bb4020000040206339038a401000106010000010bb402000004020634b439a40100020c19000006010000010bb402000004020635983ba401000101320000010bb402000004020636bc3ca40100010a010000010b9c03000005000637a03e960200020c19000006010000010b9c03000005000638b6409602000101320000010b9c030000050006398c43880300010e010000010b840400000501063a9446ba0300020c19000006010000010b840400000501063b8e4aba0300010a010000010bac0400000502063c884e960200020c19000006010000010bac0400000502063d9e509602000106010000010bac0400000502063eb452880300010196020000010b940500000503063fbc55ba0300020c19000006010000010b940500000503068001b659ba0300010a010000010bbc0500000600068101b05d9602000101320000010bbc050000060006820186609602000106010000010bbc05000006000683019c62880300020c8b01000006010000010ba40600000601068401a465ba03000101320000010ba406000006010685019e69ba0300010a010000010b8c0700000602068601986d9602000101320000010b8c0700000602068701ae6f960200020c19000006010000010b8c07000006020688018472880300010e010000010bb407000006030689018c75ba03000101320000010bb40700000603068a018679ba0300010a010000010b9c0800000700068b01807d960200020c19000006010000010b9c0800000700068c01967f9602000106010000010b9c0800000700068d01ac8101880300010196020000010b840900000701068e01b48401ba03000106010000010b840900000701068f01ae8801ba0300010a010000010bac0900000702069001a88c019602000101320000010bac0900000702069101be8e01960200020c19000006010000010bac0900000702069201949101880300010196020000010b940a000007030693019c9401ba03000106010000010b940a00000703069401969801ba0300010a010000010bbc0a00000800069501909c01b40700010196020000010bbc0a0000080006960184a401b407000101ac040000010ba40b00000801069701b8ab01b40700010196020000010ba40b00000801069801acb301b40700010a010000010b8c0c00000802069901a0bb01b40700010196020000010b8c0c00000802069a0194c301b407000101ac040000010bb40c00000803069b0188cb01b40700010196020000010bb40c00000803069c01bcd201b40700010a010000010b9c0d00000804069d01b0da01b40700010196020000010b9c0d0000080407000000000000070100140000000702141e000000070332320000000704a40190010000000705b40282020000000706b604920300000007078808940500000007089c0da608000000a401148087010a000000000016f341019f010081cdb70100000000''')
        self.writeString("<c2>Mr Vitalik</c>")
        self.writeByte(1) #nameset
        self.writeString()
        self.writeVint(8) #commodity
        self.writeVint(24) #array 1
        for x in [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 95, 100]:
            self.writeVint(23)
            self.writeVint(x)
            self.writeVint(1)
        self.writeVint(5)
        self.writeVint(1)
        self.writeVint(99999)
        self.writeVint(5)
        self.writeVint(8)
        self.writeVint(20000) #gold
        self.writeVint(5)
        self.writeVint(9)
        self.writeVint(99999) #big box
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(5)
        self.writeVint(8)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(16)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(9999)
        self.writeVint(9999)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(1529783425)
        
        print("[INFO] Message OwnHomeData has been sent.")