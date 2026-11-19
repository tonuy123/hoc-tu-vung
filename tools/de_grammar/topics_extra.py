# -*- coding: utf-8 -*-
"""Extra depth for the German grammar topics.

`howto`  = step-by-step usage (what to do, in order)
`notes`  = cautions / exceptions a learner actually trips over
`examples` and `mistakes` are appended to the base record in topics.py.
"""

EXTRA = {
    # ------------------------------------------------------------------ A1
    "de-a1-sein-haben": {
        "howto": [
            "Dùng sein cho danh tính, nghề nghiệp, trạng thái, tuổi: ich bin Lehrer, ich bin müde, ich bin 25 Jahre alt.",
            "Dùng haben cho sở hữu và cụm cố định: ich habe ein Auto, ich habe Hunger / Zeit / Angst.",
            "Nếu câu mở đầu bằng trạng từ, đảo động từ lên trước chủ ngữ: Heute bin ich müde.",
        ],
        "notes": [
            "sein và haben không dùng trợ động từ do/does; phủ định chỉ thêm nicht: ich bin nicht müde.",
            "Tuổi luôn đi với sein + alt (ich bin 30 Jahre alt), không dùng haben.",
        ],
        "examples": [
            ("Hast du morgen Zeit? – Nein, ich habe keine Zeit.",
             "Mai bạn có thời gian không? – Không, tôi không có thời gian."),
            ("Wo bist du? – Ich bin im Büro.",
             "Bạn đang ở đâu? – Tôi đang ở văn phòng."),
        ],
        "mistakes": [
            ("Ich habe 30 Jahre.", "Ich bin 30 Jahre alt.", "Tuổi dùng sein, không dùng haben."),
        ],
    },
    "de-a1-praesens-reg": {
        "howto": [
            "Bỏ đuôi -en (hoặc -n) của nguyên thể để lấy gốc: lernen → lern-.",
            "Thêm đuôi theo ngôi: ich -e, du -st, er/sie/es -t, wir -en, ihr -t, sie/Sie -en.",
            "Gốc kết thúc bằng -t hoặc -d thì chèn -e trước đuôi: du arbeitest, er arbeitet, ihr arbeitet.",
        ],
        "notes": [
            "du và er/sie/es không bao giờ để gốc trống: luôn có -st hoặc -t.",
            "Động từ đuôi -eln/-ern mất -e ở ngôi ich: sammeln → ich sammle.",
        ],
        "examples": [
            ("Wir wohnen in Hamburg und lernen zusammen Deutsch.",
             "Chúng tôi sống ở Hamburg và cùng học tiếng Đức."),
            ("Warum antwortest du nicht?",
             "Sao bạn không trả lời?"),
        ],
        "mistakes": [
            ("Er wohn in Berlin.", "Er wohnt in Berlin.", "Ngôi er luôn có đuôi -t."),
        ],
    },
    "de-a1-praesens-irr": {
        "howto": [
            "Học nguyên thể kèm hai dạng quan trọng nhất: du và er/sie/es.",
            "Nhóm đổi nguyên âm: a → ä, e → i/ie, au → äu, chỉ ở du và er/sie/es.",
            "wir/ihr/sie giữ nguyên gốc, chia như động từ có quy tắc.",
        ],
        "notes": [
            "Umlaut không áp cho ihr: ihr fahrt, không phải ihr fährt.",
            "fahren, nehmen, lesen, sehen, geben, essen là nhóm bắt buộc học thuộc.",
        ],
        "examples": [
            ("Siehst du den Bus? – Ja, er fährt gerade los.",
             "Bạn có thấy xe bus không? – Có, nó vừa chạy."),
            ("Er nimmt den Zug, ich nehme das Auto.",
             "Anh ấy đi tàu, tôi đi ô tô."),
        ],
        "mistakes": [
            ("Ihr fährt nach Hause.", "Ihr fahrt nach Hause.", "Ngôi ihr không có Umlaut."),
        ],
    },
    "de-a1-artikel": {
        "howto": [
            "Học mỗi danh từ mới luôn kèm mạo từ: der Tisch, die Lampe, das Fenster.",
            "Dùng der/die/das khi vật đã xác định hoặc đã nhắc trước đó.",
            "Số nhiều luôn dùng die, không phụ thuộc giống gốc.",
        ],
        "notes": [
            "Đuôi từ chỉ là gợi ý giống, không phải quy tắc tuyệt đối: das Mädchen vẫn giống trung.",
            "Khi ghi từ vựng, ghi cả mạo từ và dạng số nhiều để không phải tra lại.",
        ],
        "examples": [
            ("Das ist der Schlüssel. Wo ist der Schlüssel?",
             "Đây là chìa khóa. Chìa khóa đâu rồi?"),
            ("Die Kinder spielen im Garten, das Haus ist groß.",
             "Bọn trẻ chơi trong vườn, ngôi nhà thì to."),
        ],
        "mistakes": [
            ("Das Tisch ist neu.", "Der Tisch ist neu.", "Tisch là giống đực nên dùng der."),
        ],
    },
    "de-a1-plural": {
        "howto": [
            "Học số nhiều ngay khi học từ, vì không có quy tắc tuyệt đối.",
            "Các đuôi phổ biến: -e, -en, -er, -s, hoặc giữ nguyên kèm Umlaut.",
            "Số nhiều luôn dùng die; tính từ sau mạo từ xác định nhận đuôi -en: die neuen Tische.",
        ],
        "notes": [
            "Umlaut xuất hiện ở nhiều từ một âm tiết (der Stuhl → die Stühle) nhưng không bắt buộc.",
            "Từ vay mượn thường thêm -s: das Auto → die Autos, das Handy → die Handys.",
        ],
        "examples": [
            ("Die Bücher liegen auf dem Tisch, die Hefte sind in der Tasche.",
             "Sách nằm trên bàn, vở thì ở trong cặp."),
            ("Ich kaufe zwei Äpfel und drei Tomaten.",
             "Tôi mua hai quả táo và ba quả cà chua."),
        ],
        "mistakes": [
            ("Die Tisches sind neu.", "Die Tische sind neu.", "Số nhiều không giữ -s của số ít."),
        ],
    },
    "de-a1-akkusativ": {
        "howto": [
            "Xác định tân ngữ trực tiếp bằng câu hỏi Wen? (ai) hoặc Was? (cái gì).",
            "Chỉ giống đực đổi hình thức: der → den, ein → einen, kein → keinen.",
            "Giống cái, giống trung và số nhiều giữ nguyên như Nominativ.",
        ],
        "notes": [
            "Sau für, ohne, gegen, durch, um, bis luôn dùng Akkusativ.",
            "haben, kaufen, sehen, brauchen, lesen, essen nhận tân ngữ Akkusativ.",
        ],
        "examples": [
            ("Ich brauche einen neuen Computer.",
             "Tôi cần một cái máy tính mới."),
            ("Wir kaufen den Tisch, nicht die Lampe.",
             "Chúng tôi mua cái bàn, không mua cái đèn."),
        ],
        "mistakes": [
            ("Ich kaufe der Apfel.", "Ich kaufe den Apfel.", "Apfel giống đực ở Akkusativ thành den."),
        ],
    },
    "de-a1-negation": {
        "howto": [
            "Phủ định danh từ với mạo từ không xác định hoặc không có mạo từ: dùng kein/keine/keinen.",
            "Phủ định động từ, tính từ, trạng từ hoặc cả câu: dùng nicht.",
            "nicht đứng ngay trước thành phần bị phủ định; nếu phủ định cả câu thì đứng cuối.",
        ],
        "notes": [
            "Không nói 'nicht ein' — luôn dùng kein.",
            "kein chia giống hệt ein: keinen (m, Akk), keine (f), kein (n), keine (Pl.).",
        ],
        "examples": [
            ("Ich habe keine Zeit, ich komme nicht.",
             "Tôi không có thời gian, tôi không đến."),
            ("Das ist nicht mein Buch.",
             "Đó không phải sách của tôi."),
        ],
        "mistakes": [
            ("Ich habe nicht ein Auto.", "Ich habe kein Auto.", "Danh từ không xác định phủ định bằng kein."),
        ],
    },
    "de-a1-yesno": {
        "howto": [
            "Đưa động từ chia lên vị trí đầu câu.",
            "Chủ ngữ đứng ngay sau động từ.",
            "Trả lời bằng Ja hoặc Nein, rồi nói câu đầy đủ để lịch sự.",
        ],
        "notes": [
            "Không dùng do/does: Kommst du? chứ không phải 'Do you come?'.",
            "Nếu có modal, modal lên đầu và động từ chính giữ nguyên thể ở cuối.",
        ],
        "examples": [
            ("Kaufst du das Brot? – Ja, ich kaufe es.",
             "Bạn mua bánh mì không? – Có, tôi mua."),
            ("Kannst du mir helfen? – Nein, leider nicht.",
             "Bạn giúp tôi được không? – Không, tiếc là không."),
        ],
        "mistakes": [
            ("Du kommst heute?", "Kommst du heute?", "Câu hỏi yes/no phải đảo động từ lên đầu."),
        ],
    },
    "de-a1-wfragen": {
        "howto": [
            "Chọn từ hỏi đúng: wer (ai), was (gì), wo (ở đâu), wann (khi nào), wie (thế nào).",
            "Từ hỏi đứng đầu, động từ chia đứng thứ hai, chủ ngữ đứng sau động từ.",
            "Phân biệt wohin (đi đâu) · wo (ở đâu) · woher (từ đâu).",
        ],
        "notes": [
            "warum hỏi nguyên nhân, wie hỏi cách thức, wie oft hỏi tần suất.",
            "Không thêm denn vào câu hỏi đơn giản; denn chỉ dùng để nhấn mạnh, thân mật.",
        ],
        "examples": [
            ("Wann fährt der Zug? – Um acht Uhr.",
             "Khi nào tàu chạy? – Lúc 8 giờ."),
            ("Woher kommst du? – Ich komme aus Vietnam.",
             "Bạn từ đâu đến? – Tôi đến từ Việt Nam."),
        ],
        "mistakes": [
            ("Wo gehst du?", "Wohin gehst du?", "wo là vị trí, wohin là hướng đi."),
        ],
    },
    "de-a1-imperativ": {
        "howto": [
            "Với du: bỏ đuôi -st và bỏ luôn du (lernst → Lern!).",
            "Với ihr: dùng đúng dạng ihr hiện tại, bỏ đại từ (lernt → Lernt!).",
            "Với Sie: động từ + Sie (Lernen Sie!).",
        ],
        "notes": [
            "Động từ mạnh mất Umlaut ở du: du fährst → Fahr!, du nimmst → Nimm!.",
            "Tiền tố tách rời ra cuối câu: Mach die Tür zu!",
        ],
        "examples": [
            ("Nimm den Bus und steig am Bahnhof aus.",
             "Đi xe bus và xuống ở ga."),
            ("Bitte rufen Sie mich morgen an.",
             "Xin hãy gọi cho tôi vào ngày mai."),
        ],
        "mistakes": [
            ("Fährst du nach Hause!", "Fahr nach Hause!", "Câu mệnh lệnh du bỏ -st và bỏ Umlaut."),
        ],
    },
    "de-a1-trennbar": {
        "howto": [
            "Nhận diện tiền tố tách rời: auf-, an-, ein-, aus-, mit-, zu-, ab-, fern-.",
            "Trong câu chính, động từ chia ở vị trí 2 và tiền tố xuống cuối câu.",
            "Trong mệnh đề phụ hoặc zu + Infinitiv, động từ không tách.",
        ],
        "notes": [
            "Tiền tố mang nghĩa riêng: anrufen (gọi điện) khác rufen (gọi).",
            "Với zu: zu nằm giữa tiền tố và gốc — aufzustehen, nicht 'zu aufstehen'.",
        ],
        "examples": [
            ("Ich stehe um sechs Uhr auf und fahre zur Arbeit.",
             "Tôi dậy lúc 6 giờ và đi làm."),
            ("Wann kommt der Zug an?",
             "Khi nào tàu đến?"),
        ],
        "mistakes": [
            ("Ich aufstehe um sechs Uhr.", "Ich stehe um sechs Uhr auf.", "Câu chính tách tiền tố ra cuối."),
        ],
    },
    "de-a1-modal": {
        "howto": [
            "Modalverb chia ở vị trí 2, động từ chính để nguyên thể ở cuối câu.",
            "Học 6 modalverb: können, müssen, wollen, sollen, dürfen, mögen.",
            "Modalverb không đi với zu.",
        ],
        "notes": [
            "müssen = bắt buộc; sollen = theo yêu cầu/lời khuyên; dürfen = được phép; können = có khả năng.",
            "mögen thường dùng dạng möchte cho lời đề nghị lịch sự.",
        ],
        "examples": [
            ("Ich muss heute länger arbeiten.",
             "Hôm nay tôi phải làm việc lâu hơn."),
            ("Darf ich hier parken? – Nein, das ist verboten.",
             "Tôi được đỗ xe ở đây không? – Không, cấm."),
        ],
        "mistakes": [
            ("Ich muss zu gehen.", "Ich muss gehen.", "Sau modalverb không dùng zu."),
        ],
    },
    "de-a1-possessiv": {
        "howto": [
            "Chọn gốc sở hữu: mein, dein, sein, ihr, unser, euer, Ihr.",
            "Thêm đuôi theo giống và cách của danh từ: mein Vater, meine Mutter, mein Kind.",
            "Akkusativ giống đực thêm -en: meinen Bruder.",
        ],
        "notes": [
            "sein = của anh ấy/nó; ihr = của cô ấy hoặc của họ — phải dựa vào ngữ cảnh.",
            "Số nhiều luôn dùng meine/deine/seine... bất kể giống gốc.",
        ],
        "examples": [
            ("Meine Schwester besucht ihren Freund.",
             "Chị tôi đến thăm bạn trai cô ấy."),
            ("Wo ist euer Auto?",
             "Xe của các bạn đâu?"),
        ],
        "mistakes": [
            ("Ich besuche mein Bruder.", "Ich besuche meinen Bruder.", "Akkusativ giống đực: meinen."),
        ],
    },
    "de-a1-praepositionen": {
        "howto": [
            "Chọn giới từ theo quan hệ không gian: in (trong), an (sát), auf (trên), bei (chỗ ai), zu (đến chỗ).",
            "in/an/auf + Dativ khi chỉ vị trí đứng yên.",
            "Dùng bei + người, zu + người hoặc cơ sở (zu Hause, zum Arzt).",
        ],
        "notes": [
            "zu Hause = ở nhà; nach Hause = về nhà — hai hướng khác nhau.",
            "bei + Dativ thường mang nghĩa 'ở chỗ làm việc của'.",
        ],
        "examples": [
            ("Ich arbeite in der Stadt und wohne bei meinen Eltern.",
             "Tôi làm việc trong thành phố và sống ở chỗ bố mẹ."),
            ("Wir sind heute zu Hause.",
             "Hôm nay chúng tôi ở nhà."),
        ],
        "mistakes": [
            ("Ich bin in Hause.", "Ich bin zu Hause.", "Cụm cố định là zu Hause."),
        ],
    },

    # ------------------------------------------------------------------ A2
    "de-a2-perfekt-haben": {
        "howto": [
            "Chia haben theo chủ ngữ rồi đặt Partizip II ở cuối câu.",
            "Phần lớn động từ dùng haben, kể cả động từ không chuyển động.",
            "Partizip II quy tắc: ge- + gốc + -t; bất quy tắc: ge- + gốc đổi + -en.",
        ],
        "notes": [
            "Động từ có tiền tố không tách (be-, ver-, er-, ent-, ge-) không thêm ge-: besucht, verstanden.",
            "Trạng từ thời gian đứng sau trợ động từ: Ich habe gestern viel gelernt.",
        ],
        "examples": [
            ("Wir haben den Film gestern gesehen.",
             "Chúng tôi đã xem phim hôm qua."),
            ("Hast du die Hausaufgaben schon gemacht?",
             "Bạn làm bài tập chưa?"),
        ],
        "mistakes": [
            ("Ich habe nach Berlin gefahren.", "Ich bin nach Berlin gefahren.", "fahren chỉ chuyển động nên dùng sein."),
        ],
    },
    "de-a2-perfekt-sein": {
        "howto": [
            "Dùng sein + Partizip II với động từ chuyển động hoặc đổi trạng thái.",
            "Nhóm chính: gehen, fahren, kommen, fliegen, aufstehen, einschlafen, werden, bleiben, passieren.",
            "Chia sein theo chủ ngữ: ich bin, du bist, er ist, wir sind.",
        ],
        "notes": [
            "bleiben và passieren cũng dùng sein dù không chuyển động.",
            "Động từ chuyển động có tân ngữ trực tiếp thì quay lại dùng haben.",
        ],
        "examples": [
            ("Sie ist um sieben Uhr aufgestanden.",
             "Cô ấy đã dậy lúc 7 giờ."),
            ("Wir sind letzte Woche nach Wien geflogen.",
             "Tuần trước chúng tôi đã bay tới Wien."),
        ],
        "mistakes": [
            ("Ich habe zu Hause geblieben.", "Ich bin zu Hause geblieben.", "bleiben dùng sein."),
        ],
    },
    "de-a2-praeteritum": {
        "howto": [
            "Dùng Präteritum khi kể chuyện hoặc viết; khẩu ngữ thường dùng Perfekt.",
            "Động từ yếu: gốc + -te (lernen → lernte, arbeiten → arbeitete).",
            "Động từ mạnh: đổi nguyên âm gốc (gehen → ging, sehen → sah, nehmen → nahm).",
        ],
        "notes": [
            "sein, haben và modalverb gần như luôn dùng Präteritum khi nói.",
            "Ngôi ich và er/sie/es ở Präteritum mạnh trùng nhau: ich ging, er ging.",
        ],
        "examples": [
            ("Früher wohnte ich in Berlin, jetzt wohne ich in Hamburg.",
             "Trước đây tôi sống ở Berlin, giờ tôi sống ở Hamburg."),
            ("Er hatte keine Zeit und kam nicht.",
             "Anh ấy không có thời gian và đã không đến."),
        ],
        "mistakes": [
            ("Ich gehte nach Hause.", "Ich ging nach Hause.", "gehen là động từ mạnh, không thêm -te."),
        ],
    },
    "de-a2-dativ": {
        "howto": [
            "Xác định tân ngữ gián tiếp bằng câu hỏi Wem?.",
            "Giống đực và trung: dem; giống cái: der; số nhiều: den + thêm -n cho danh từ.",
            "Học nhóm động từ Dativ: helfen, danken, gratulieren, folgen, antworten, gehören, vertrauen.",
        ],
        "notes": [
            "Nhóm Dativ không có tân ngữ Akkusativ, nên đừng thêm 'den' sai cách.",
            "Đại từ Dativ: mir, dir, ihm, ihr, uns, euch, ihnen.",
        ],
        "examples": [
            ("Ich helfe meiner Mutter in der Küche.",
             "Tôi giúp mẹ tôi trong bếp."),
            ("Das Buch gehört dem Lehrer.",
             "Cuốn sách thuộc về thầy giáo."),
        ],
        "mistakes": [
            ("Ich helfe meinen Bruder.", "Ich helfe meinem Bruder.", "helfen đi với Dativ: meinem."),
        ],
    },
    "de-a2-wechsel": {
        "howto": [
            "Học 9 giới từ hai cách: in, an, auf, über, unter, vor, hinter, neben, zwischen.",
            "Hỏi Wohin? (đi đâu) → Akkusativ; hỏi Wo? (ở đâu) → Dativ.",
            "Động từ chuyển động + hướng đi dùng Akkusativ; trạng thái đứng yên dùng Dativ.",
        ],
        "notes": [
            "Cùng một giới từ đổi cách là đổi nghĩa: in die Stadt (đi vào) / in der Stadt (ở trong).",
            "gehen, fahren, legen, stellen, setzen → Akkusativ; sein, liegen, stehen, sitzen → Dativ.",
        ],
        "examples": [
            ("Ich gehe in die Küche und stelle die Tasse auf den Tisch.",
             "Tôi vào bếp và đặt cái tách lên bàn."),
            ("Die Tasse steht auf dem Tisch.",
             "Cái tách đang ở trên bàn."),
        ],
        "mistakes": [
            ("Ich gehe in der Schule.", "Ich gehe in die Schule.", "Có hướng đi nên dùng Akkusativ."),
        ],
    },
    "de-a2-nebensatz-weil": {
        "howto": [
            "Đặt weil ở đầu mệnh đề phụ.",
            "Đẩy động từ chia xuống cuối mệnh đề phụ.",
            "Nếu mệnh đề phụ đứng trước, động từ của câu chính đứng ngay sau dấu phẩy.",
        ],
        "notes": [
            "weil khác denn: denn giữ trật tự bình thường, weil đẩy động từ xuống cuối.",
            "Không dùng weil với đảo chủ ngữ — sau weil luôn là chủ ngữ rồi mới tới phần còn lại.",
        ],
        "examples": [
            ("Ich bleibe zu Hause, weil ich krank bin.",
             "Tôi ở nhà vì tôi ốm."),
            ("Weil es regnet, fahren wir mit dem Bus.",
             "Vì trời mưa nên chúng tôi đi xe bus."),
        ],
        "mistakes": [
            ("Ich bleibe zu Hause, weil ich bin krank.", "Ich bleibe zu Hause, weil ich krank bin.", "weil đẩy động từ xuống cuối."),
        ],
    },
    "de-a2-konnektoren": {
        "howto": [
            "und / oder đứng ở vị trí 0, không làm đổi trật tự từ.",
            "aber / denn nối hai mệnh đề độc lập, giữ trật tự bình thường.",
            "deshalb / darum / deswegen là trạng từ: đứng đầu câu và đảo động từ ra trước chủ ngữ.",
        ],
        "notes": [
            "denn không đẩy động từ xuống cuối, khác weil.",
            "sondern chỉ dùng sau phủ định, thay cho aber: nicht ..., sondern ...",
        ],
        "examples": [
            ("Ich bin müde, aber ich arbeite weiter.",
             "Tôi mệt nhưng tôi vẫn làm tiếp."),
            ("Es regnet, deshalb bleiben wir zu Hause.",
             "Trời mưa nên chúng tôi ở nhà."),
        ],
        "mistakes": [
            ("Ich bleibe zu Hause, denn ich bin müde gewesen.", "Ich bleibe zu Hause, denn ich bin müde.", "denn nối mệnh đề độc lập, không cần thì quá khứ."),
        ],
    },
    "de-a2-komparativ": {
        "howto": [
            "Komparativ: tính từ + -er + als (schneller als).",
            "Superlativ: am + tính từ + -sten, hoặc der/die/das + -ste.",
            "Nhiều tính từ ngắn nhận Umlaut: alt → älter, groß → größer, jung → jünger.",
        ],
        "notes": [
            "Bất quy tắc: gut → besser → am besten; viel → mehr → am meisten; gern → lieber → am liebsten.",
            "So sánh bằng dùng so ... wie, không dùng als.",
        ],
        "examples": [
            ("Der Zug ist schneller als der Bus.",
             "Tàu nhanh hơn xe bus."),
            ("Das ist das beste Restaurant in der Stadt.",
             "Đây là nhà hàng ngon nhất thành phố."),
        ],
        "mistakes": [
            ("Er ist größer wie ich.", "Er ist größer als ich.", "So sánh hơn dùng als, không dùng wie."),
        ],
    },
    "de-a2-futur": {
        "howto": [
            "Chia werden theo chủ ngữ, để động từ chính nguyên thể ở cuối.",
            "werden: ich werde, du wirst, er wird, wir werden, ihr werdet, sie werden.",
            "Dùng cho dự đoán, lời hứa hoặc kế hoạch chưa chắc chắn.",
        ],
        "notes": [
            "Tiếng Đức hay dùng hiện tại + trạng từ thời gian để nói tương lai: Morgen fahre ich nach Berlin.",
            "werden cũng là động từ chính mang nghĩa 'trở thành'.",
        ],
        "examples": [
            ("Ich werde dich morgen anrufen.",
             "Mai tôi sẽ gọi cho bạn."),
            ("Es wird wahrscheinlich regnen.",
             "Có lẽ trời sẽ mưa."),
        ],
        "mistakes": [
            ("Ich werde nach Berlin fahren morgen.", "Ich werde morgen nach Berlin fahren.", "Động từ nguyên thể phải ở cuối."),
        ],
    },
    "de-a2-modal-praet": {
        "howto": [
            "Học 6 dạng Präteritum: konnte, musste, wollte, sollte, durfte, mochte.",
            "Dạng Präteritum của modalverb không có Umlaut.",
            "Động từ chính vẫn để nguyên thể ở cuối câu.",
        ],
        "notes": [
            "Ngôi ich và er/sie/es trùng nhau: ich konnte, er konnte.",
            "mögen → mochte mang nghĩa 'thích' trong quá khứ; muốn lịch sự dùng hätte gern.",
        ],
        "examples": [
            ("Als Kind konnte ich nicht schwimmen.",
             "Hồi nhỏ tôi không biết bơi."),
            ("Wir mussten gestern lange warten.",
             "Hôm qua chúng tôi phải chờ lâu."),
        ],
        "mistakes": [
            ("Ich könnte gestern nicht kommen.", "Ich konnte gestern nicht kommen.", "Präteritum thực tế không có Umlaut; könnte là Konjunktiv II."),
        ],
    },
    "de-a2-reflexiv": {
        "howto": [
            "Dùng đại từ phản thân đúng ngôi và đúng cách.",
            "Akkusativ: mich, dich, sich, uns, euch, sich; Dativ: mir, dir, sich, uns, euch, sich.",
            "Đại từ phản thân đứng ngay sau động từ chia.",
        ],
        "notes": [
            "Một số động từ buộc phải reflexiv: sich freuen, sich beeilen, sich erholen.",
            "Nếu câu đã có tân ngữ Akkusativ, đại từ phản thân chuyển sang Dativ: Ich wasche mir die Hände.",
        ],
        "examples": [
            ("Ich freue mich auf den Urlaub.",
             "Tôi mong đến kỳ nghỉ."),
            ("Wir treffen uns um acht Uhr.",
             "Chúng tôi gặp nhau lúc 8 giờ."),
        ],
        "mistakes": [
            ("Ich freue auf den Urlaub.", "Ich freue mich auf den Urlaub.", "sich freuen luôn cần đại từ phản thân."),
        ],
    },
    "de-a2-temporal-praep": {
        "howto": [
            "am + thứ/ngày và buổi trong ngày: am Montag, am Abend.",
            "im + tháng/mùa: im Januar, im Sommer.",
            "um + giờ cụ thể; vor/nach + Dativ cho mốc thời gian; seit + Dativ cho việc kéo dài từ quá khứ.",
        ],
        "notes": [
            "in + năm: in 2020; không dùng am với năm.",
            "seit + Dativ luôn đi với hiện tại, không dùng quá khứ.",
        ],
        "examples": [
            ("Am Wochenende fahren wir ans Meer.",
             "Cuối tuần chúng tôi đi biển."),
            ("Ich lerne seit drei Monaten Deutsch.",
             "Tôi học tiếng Đức được ba tháng."),
        ],
        "mistakes": [
            ("Ich lerne seit drei Monaten Deutsch gelernt.", "Ich lerne seit drei Monaten Deutsch.", "seit đi với hiện tại, không dùng Perfekt."),
        ],
    },
    "de-a2-adj-best": {
        "howto": [
            "Sau der/die/das: giống đực Nom. -e, giống cái -e, giống trung -e.",
            "Sau den/dem/der (Dativ, Genitiv, số nhiều) luôn dùng -en.",
            "Akkusativ giống đực sau den: -en (den neuen Tisch).",
        ],
        "notes": [
            "Đuôi tính từ phụ thuộc vào cả mạo từ đứng trước, không chỉ vào danh từ.",
            "Tính từ kết thúc bằng -er/-el mất -e khi thêm đuôi: teuer → der teure Tisch.",
        ],
        "examples": [
            ("Der neue Tisch ist teuer, aber die alte Lampe ist billig.",
             "Cái bàn mới thì đắt, nhưng cái đèn cũ thì rẻ."),
            ("Ich kaufe den kleinen Tisch.",
             "Tôi mua cái bàn nhỏ."),
        ],
        "mistakes": [
            ("Der neue Tisch ist teuer, aber der alte Lampe ist billig.", "Der neue Tisch ist teuer, aber die alte Lampe ist billig.", "Lampe giống cái nên dùng die."),
        ],
    },
    "de-a2-zu-inf": {
        "howto": [
            "Đặt zu + Infinitiv ở cuối câu.",
            "Động từ tách rời: zu chen vào giữa tiền tố và gốc (aufzustehen, einzukaufen).",
            "Dùng sau versuchen, beginnen, vergessen, hoffen, vorhaben, Lust haben.",
        ],
        "notes": [
            "Không dùng zu sau modalverb: Ich muss gehen, không phải 'zu gehen'.",
            "Nếu hai mệnh đề khác chủ ngữ, dùng damit thay vì um ... zu.",
        ],
        "examples": [
            ("Ich versuche, früher aufzustehen.",
             "Tôi cố dậy sớm hơn."),
            ("Hast du Lust, ins Kino zu gehen?",
             "Bạn có muốn đi xem phim không?"),
        ],
        "mistakes": [
            ("Ich versuche zu früh aufstehen.", "Ich versuche, früh aufzustehen.", "zu phải nằm trong động từ tách rời và ở cuối câu."),
        ],
    },

    # ------------------------------------------------------------------ B1
    "de-b1-passiv": {
        "howto": [
            "Chuyển tân ngữ Akkusativ của câu chủ động thành chủ ngữ câu bị động.",
            "Chia werden theo chủ ngữ mới và đặt Partizip II ở cuối.",
            "Thêm tác nhân nếu cần: von + Dativ (người), durch + Akkusativ (phương tiện).",
        ],
        "notes": [
            "Không phải câu chủ động nào cũng chuyển được — động từ không có tân ngữ Akkusativ thì không có bị động trực tiếp.",
            "Passiv nhấn vào hành động, không nhấn vào người làm.",
        ],
        "examples": [
            ("Die Rechnung wird morgen bezahlt.",
             "Hóa đơn sẽ được thanh toán vào ngày mai."),
            ("Das Haus wurde 1990 gebaut.",
             "Ngôi nhà được xây năm 1990."),
        ],
        "mistakes": [
            ("Die Rechnung wird morgen bezahlt werden von mir.", "Die Rechnung wird morgen von mir bezahlt.", "Partizip II đứng ngay trước tác nhân."),
        ],
    },
    "de-b1-relativ": {
        "howto": [
            "Chọn đại từ quan hệ khớp giống và số với danh từ đứng trước.",
            "Chọn cách theo chức năng của đại từ trong mệnh đề quan hệ.",
            "Đẩy động từ chia xuống cuối mệnh đề quan hệ.",
        ],
        "notes": [
            "der/die/das/die; Akkusativ den/die/das/die; Dativ dem/der/dem/denen.",
            "Giới từ đứng trước đại từ quan hệ quyết định cách: mit dem, für die.",
        ],
        "examples": [
            ("Der Mann, der dort steht, ist mein Lehrer.",
             "Người đàn ông đứng đó là giáo viên của tôi."),
            ("Das Buch, das ich lese, ist spannend.",
             "Cuốn sách tôi đang đọc rất hấp dẫn."),
        ],
        "mistakes": [
            ("Der Mann, der ich sehe, ist mein Lehrer.", "Der Mann, den ich sehe, ist mein Lehrer.", "Đại từ là tân ngữ Akkusativ nên dùng den."),
        ],
    },
    "de-b1-konjunktiv2": {
        "howto": [
            "Dùng würde + Infinitiv cho tình huống giả định hoặc lời đề nghị lịch sự.",
            "Chia würde theo ngôi: würde, würdest, würde, würden, würdet, würden.",
            "Với sein, haben và modalverb dùng dạng riêng: wäre, hätte, könnte.",
        ],
        "notes": [
            "Không dùng würde với sein/haben: 'ich würde sein' nghe sai, dùng ich wäre.",
            "Konjunktiv II dùng cho điều không có thật ở hiện tại.",
        ],
        "examples": [
            ("Ich würde gern nach Deutschland reisen.",
             "Tôi rất muốn đi Đức."),
            ("Was würdest du an meiner Stelle machen?",
             "Nếu là tôi, bạn sẽ làm gì?"),
        ],
        "mistakes": [
            ("Ich würde müde sein.", "Ich wäre müde.", "sein dùng Konjunktiv II riêng là wäre."),
        ],
    },
    "de-b1-hte-waere": {
        "howto": [
            "Dùng hätte/wäre để nói điều kiện không có thật ở hiện tại.",
            "Cấu trúc: Wenn + chủ ngữ + ... + hätte/wäre, (dann) + kết quả.",
            "Có thể bỏ wenn và đảo hätte/wäre lên đầu: Hätte ich Zeit, ...",
        ],
        "notes": [
            "hätte đi với danh từ (Zeit, Geld); wäre đi với tính từ/danh từ nghề nghiệp.",
            "Điều kiện quá khứ không thật dùng hätte/wäre + Partizip II.",
        ],
        "examples": [
            ("Wenn ich mehr Zeit hätte, würde ich mehr lesen.",
             "Nếu tôi có nhiều thời gian hơn, tôi sẽ đọc nhiều hơn."),
            ("Wäre ich reich, würde ich um die Welt reisen.",
             "Nếu tôi giàu, tôi sẽ đi vòng quanh thế giới."),
        ],
        "mistakes": [
            ("Wenn ich Zeit würde haben.", "Wenn ich Zeit hätte.", "Điều kiện không thật dùng hätte, không dùng würde + haben."),
        ],
    },
    "de-b1-genitiv": {
        "howto": [
            "Xác định quan hệ sở hữu bằng câu hỏi Wessen?.",
            "Giống đực và trung: des + thêm -s/-es cho danh từ.",
            "Giống cái và số nhiều: der + danh từ không đổi.",
        ],
        "notes": [
            "Genitiv hay gặp trong văn viết; khẩu ngữ thường thay bằng von + Dativ.",
            "Danh từ một âm tiết thường thêm -es: des Mannes, des Kindes.",
        ],
        "examples": [
            ("Das ist das Auto meines Bruders.",
             "Đây là xe của anh trai tôi."),
            ("Die Farbe der Wand gefällt mir.",
             "Tôi thích màu của bức tường."),
        ],
        "mistakes": [
            ("Das ist das Auto von meines Bruders.", "Das ist das Auto meines Bruders.", "Không trộn von với Genitiv."),
        ],
    },
    "de-b1-adj-unbest": {
        "howto": [
            "Sau ein: giống đực Nom. -er, giống cái -e, giống trung -es.",
            "Akkusativ giống đực sau einen: -en.",
            "Không có mạo từ thì tính từ nhận đuôi mạnh (guter Wein, frisches Brot).",
        ],
        "notes": [
            "Đuôi tính từ thay vai trò của mạo từ khi mạo từ không mang thông tin giống.",
            "Số nhiều không có mạo từ: gute Freunde.",
        ],
        "examples": [
            ("Ich habe einen guten Freund in Berlin.",
             "Tôi có một người bạn tốt ở Berlin."),
            ("Das ist ein interessantes Buch.",
             "Đây là một cuốn sách thú vị."),
        ],
        "mistakes": [
            ("Ich habe ein guten Freund.", "Ich habe einen guten Freund.", "Akkusativ giống đực: einen."),
        ],
    },
    "de-b1-verben-praep": {
        "howto": [
            "Học động từ luôn kèm giới từ và cách: warten auf + Akk, denken an + Akk.",
            "Đặt giới từ + tân ngữ sau động từ, trước phần cuối câu.",
            "Thay bằng đại từ: darauf, daran, worauf, woran.",
        ],
        "notes": [
            "Giới từ không dịch theo nghĩa đen — phải học nguyên cụm.",
            "sich freuen auf (tương lai) khác sich freuen über (đã xảy ra).",
        ],
        "examples": [
            ("Ich warte auf den Bus.",
             "Tôi đang chờ xe bus."),
            ("Wir sprechen über das Projekt.",
             "Chúng tôi nói về dự án."),
        ],
        "mistakes": [
            ("Ich warte für den Bus.", "Ich warte auf den Bus.", "warten đi với auf + Akkusativ."),
        ],
    },
    "de-b1-um-zu": {
        "howto": [
            "Dùng um ... zu + Infinitiv để diễn tả mục đích khi hai mệnh đề cùng chủ ngữ.",
            "um đứng đầu mệnh đề mục đích, zu + Infinitiv ở cuối.",
            "Nếu khác chủ ngữ, dùng damit thay vì um ... zu.",
        ],
        "notes": [
            "Không dùng um ... zu cho mục đích phủ định phức tạp — chuyển sang damit.",
            "Động từ tách rời: um einzukaufen, um aufzustehen.",
        ],
        "examples": [
            ("Ich lerne Deutsch, um in Deutschland zu studieren.",
             "Tôi học tiếng Đức để học đại học ở Đức."),
            ("Sie steht früh auf, um den Bus zu nehmen.",
             "Cô ấy dậy sớm để bắt xe bus."),
        ],
        "mistakes": [
            ("Ich lerne Deutsch, um in Deutschland studieren.", "Ich lerne Deutsch, um in Deutschland zu studieren.", "Thiếu zu trước Infinitiv."),
        ],
    },
    "de-b1-konzessiv": {
        "howto": [
            "obwohl + động từ xuống cuối để diễn tả nhượng bộ.",
            "weil + động từ xuống cuối để diễn tả nguyên nhân.",
            "deshalb/deswegen đứng đầu câu chính và đảo động từ ra trước chủ ngữ.",
        ],
        "notes": [
            "obwohl khác trotzdem: obwohl mở mệnh đề phụ, trotzdem là trạng từ đứng đầu câu.",
            "Không dùng 'aber obwohl' trong cùng một câu.",
        ],
        "examples": [
            ("Obwohl es regnet, gehen wir spazieren.",
             "Dù trời mưa, chúng tôi vẫn đi dạo."),
            ("Ich bin müde, deshalb gehe ich früh ins Bett.",
             "Tôi mệt nên đi ngủ sớm."),
        ],
        "mistakes": [
            ("Obwohl es regnet, aber wir gehen spazieren.", "Obwohl es regnet, gehen wir spazieren.", "obwohl đã mang nghĩa nhượng bộ, không thêm aber."),
        ],
    },
    "de-b1-plusquam": {
        "howto": [
            "Dùng nachdem + Plusquamperfekt cho hành động xảy ra trước.",
            "Plusquamperfekt: hatte/war + Partizip II.",
            "Câu chính dùng Präteritum hoặc Perfekt.",
        ],
        "notes": [
            "Không dùng Plusquamperfekt cho cả hai vế — chỉ vế xảy ra trước.",
            "Nếu chủ ngữ hai vế giống nhau, có thể lược ở vế sau.",
        ],
        "examples": [
            ("Nachdem ich gegessen hatte, ging ich spazieren.",
             "Sau khi ăn xong, tôi đi dạo."),
            ("Nachdem sie angekommen war, rief sie mich an.",
             "Sau khi cô ấy đến, cô ấy gọi cho tôi."),
        ],
        "mistakes": [
            ("Nachdem ich gegessen habe, ging ich spazieren.", "Nachdem ich gegessen hatte, ging ich spazieren.", "Hành động trước dùng Plusquamperfekt."),
        ],
    },
    "de-b1-temporal-ns": {
        "howto": [
            "als cho một sự việc xảy ra một lần trong quá khứ.",
            "wenn cho sự việc lặp lại, hoặc ở hiện tại/tương lai.",
            "während cho hai hành động diễn ra song song.",
        ],
        "notes": [
            "als không dùng cho hiện tại/tương lai.",
            "Sau als/wenn/während, động từ chia xuống cuối.",
        ],
        "examples": [
            ("Als ich Kind war, wohnte ich in Berlin.",
             "Khi tôi còn nhỏ, tôi sống ở Berlin."),
            ("Während ich koche, hört sie Musik.",
             "Trong khi tôi nấu ăn, cô ấy nghe nhạc."),
        ],
        "mistakes": [
            ("Wenn ich Kind war, wohnte ich in Berlin.", "Als ich Kind war, wohnte ich in Berlin.", "Sự việc một lần trong quá khứ dùng als."),
        ],
    },
    "de-b1-indirekte-frage": {
        "howto": [
            "Đặt câu hỏi gián tiếp sau mệnh đề dẫn (ich weiß nicht, kannst du mir sagen...).",
            "Nếu câu gốc có từ hỏi, giữ từ hỏi; nếu không, dùng ob.",
            "Đẩy động từ chia xuống cuối mệnh đề gián tiếp.",
        ],
        "notes": [
            "Dấu hỏi chỉ đặt ở câu chính nếu câu chính là câu hỏi.",
            "Không đảo chủ ngữ trong mệnh đề gián tiếp.",
        ],
        "examples": [
            ("Ich weiß nicht, ob er heute kommt.",
             "Tôi không biết hôm nay anh ấy có đến không."),
            ("Kannst du mir sagen, wo der Bahnhof ist?",
             "Bạn có thể chỉ tôi ga tàu ở đâu không?"),
        ],
        "mistakes": [
            ("Ich weiß nicht, ob kommt er heute.", "Ich weiß nicht, ob er heute kommt.", "Mệnh đề gián tiếp đẩy động từ xuống cuối."),
        ],
    },
    "de-b1-n-deklination": {
        "howto": [
            "Nhận diện danh từ giống đực chỉ người/động vật thuộc nhóm n-Deklination.",
            "Thêm -en/-n ở Akkusativ, Dativ và Genitiv.",
            "Số ít Nominativ giữ nguyên: der Student, den Studenten, dem Studenten, des Studenten.",
        ],
        "notes": [
            "Nhóm này gồm nhiều từ đuôi -e (der Junge, der Kollege) và một số từ đặc biệt (der Mensch, der Herr).",
            "Không nhầm với danh từ giống cái — nhóm này chỉ giống đực.",
        ],
        "examples": [
            ("Ich kenne den Studenten gut.",
             "Tôi biết sinh viên đó rõ."),
            ("Wir helfen dem Nachbarn.",
             "Chúng tôi giúp người hàng xóm."),
        ],
        "mistakes": [
            ("Ich kenne den Student.", "Ich kenne den Studenten.", "Akkusativ của nhóm n-Deklination thêm -en."),
        ],
    },

    # ------------------------------------------------------------------ B2
    "de-b2-passiv-modal": {
        "howto": [
            "Cấu trúc: modalverb (chia) + ... + Partizip II + werden.",
            "werden để nguyên thể vì đã có modalverb.",
            "Chọn modalverb theo sắc thái: muss (bắt buộc), kann (có thể), soll (nên), darf (được phép).",
        ],
        "notes": [
            "Không chia werden khi đã có modalverb.",
            "Câu bị động với modal hay dùng trong quy định, hướng dẫn.",
        ],
        "examples": [
            ("Das Formular muss bis Freitag abgegeben werden.",
             "Mẫu đơn phải được nộp trước thứ Sáu."),
            ("Hier darf nicht geraucht werden.",
             "Ở đây không được hút thuốc."),
        ],
        "mistakes": [
            ("Das Formular muss abgegeben wird.", "Das Formular muss abgegeben werden.", "Sau modalverb, werden ở dạng nguyên thể."),
        ],
    },
    "de-b2-k2-vergangenheit": {
        "howto": [
            "Cấu trúc: hätte/wäre + Partizip II.",
            "Dùng để nói điều đã không xảy ra trong quá khứ.",
            "Thường đi với wenn, beinahe, fast, sonst.",
        ],
        "notes": [
            "Động từ chuyển động dùng wäre, phần lớn còn lại dùng hätte.",
            "Không dùng würde + Partizip II.",
        ],
        "examples": [
            ("Wenn ich mehr gelernt hätte, hätte ich die Prüfung bestanden.",
             "Nếu tôi học nhiều hơn, tôi đã đỗ kỳ thi."),
            ("Ich wäre fast zu spät gekommen.",
             "Suýt nữa thì tôi đến muộn."),
        ],
        "mistakes": [
            ("Ich würde das gemacht haben.", "Ich hätte das gemacht.", "Konjunktiv II quá khứ dùng hätte + Partizip II."),
        ],
    },
    "de-b2-k1-indirekt": {
        "howto": [
            "Dùng Konjunktiv I khi tường thuật lời người khác mà không khẳng định đó là sự thật.",
            "sein → sei, haben → habe, modalverb → könne/müsse/wolle.",
            "Động từ thường: thêm -e (er komme, sie arbeite).",
        ],
        "notes": [
            "Nếu dạng Konjunktiv I trùng với hiện tại, dùng Konjunktiv II để tránh nhầm.",
            "Konjunktiv I chủ yếu dùng trong báo chí, văn bản trang trọng.",
        ],
        "examples": [
            ("Er sagt, er habe keine Zeit.",
             "Anh ấy nói anh ấy không có thời gian."),
            ("Die Firma behauptet, der Test sei einfach.",
             "Công ty khẳng định bài kiểm tra dễ."),
        ],
        "mistakes": [
            ("Er sagt, er hat keine Zeit.", "Er sagt, er habe keine Zeit.", "Tường thuật dùng Konjunktiv I: habe."),
        ],
    },
    "de-b2-nominalisierung": {
        "howto": [
            "Biến động từ thành danh từ: lernen → das Lernen, essen → das Essen.",
            "Dùng giới từ + danh từ hóa thay cho mệnh đề phụ: beim Essen, nach der Arbeit.",
            "Danh từ hóa luôn giống trung nếu từ động từ nguyên thể.",
        ],
        "notes": [
            "Văn phong nominal hay dùng trong văn bản hành chính, khoa học.",
            "Không lạm dụng — câu sẽ nặng và khó hiểu nếu danh từ hóa quá nhiều.",
        ],
        "examples": [
            ("Beim Lernen höre ich Musik.",
             "Khi học tôi nghe nhạc."),
            ("Nach dem Essen gehen wir spazieren.",
             "Sau bữa ăn chúng tôi đi dạo."),
        ],
        "mistakes": [
            ("Beim lernen höre ich Musik.", "Beim Lernen höre ich Musik.", "Danh từ hóa phải viết hoa."),
        ],
    },
    "de-b2-partizip-adj": {
        "howto": [
            "Partizip II + đuôi tính từ diễn tả kết quả/bị động: der gekaufte Tisch.",
            "Partizip I (Infinitiv + -d) + đuôi diễn tả đang diễn ra: der laufende Prozess.",
            "Đuôi tính từ chia theo mạo từ và cách như tính từ thường.",
        ],
        "notes": [
            "Partizip II mang nghĩa bị động hoàn thành; Partizip I mang nghĩa chủ động đang tiếp diễn.",
            "Không phải động từ nào cũng dùng tự nhiên ở dạng này.",
        ],
        "examples": [
            ("Der gebuchte Flug wurde gestrichen.",
             "Chuyến bay đã đặt bị hủy."),
            ("Das ist eine interessante Frage.",
             "Đây là một câu hỏi thú vị."),
        ],
        "mistakes": [
            ("Der gekauft Tisch ist neu.", "Der gekaufte Tisch ist neu.", "Partizip làm tính từ phải có đuôi."),
        ],
    },
    "de-b2-zweiteilig": {
        "howto": [
            "sowohl ... als auch: cả hai đều đúng.",
            "weder ... noch: phủ định kép, không cái nào.",
            "entweder ... oder: một trong hai; nicht nur ... sondern auch: không chỉ mà còn.",
        ],
        "notes": [
            "weder ... noch đã mang nghĩa phủ định, không thêm nicht.",
            "Hai vế phải cùng loại từ (cùng là danh từ, cùng là trạng từ...).",
        ],
        "examples": [
            ("Sie spricht sowohl Deutsch als auch Englisch.",
             "Cô ấy nói cả tiếng Đức và tiếng Anh."),
            ("Ich habe weder Zeit noch Geld.",
             "Tôi không có thời gian lẫn tiền."),
        ],
        "mistakes": [
            ("Ich habe weder Zeit noch kein Geld.", "Ich habe weder Zeit noch Geld.", "weder ... noch không đi với kein."),
        ],
    },
    "de-b2-relativ-praep": {
        "howto": [
            "Đặt giới từ ngay trước đại từ quan hệ.",
            "Cách của đại từ do giới từ quyết định.",
            "Động từ chia xuống cuối mệnh đề quan hệ.",
        ],
        "notes": [
            "Giới từ + đại từ: mit dem, über das, für die.",
            "Khẩu ngữ đôi khi tách giới từ ra cuối, nhưng văn viết chuẩn giữ trước đại từ.",
        ],
        "examples": [
            ("Der Kollege, mit dem ich arbeite, ist sehr nett.",
             "Đồng nghiệp mà tôi làm cùng rất tốt."),
            ("Das Thema, über das wir sprechen, ist wichtig.",
             "Chủ đề chúng ta đang nói rất quan trọng."),
        ],
        "mistakes": [
            ("Der Kollege, dem ich mit arbeite, ist nett.", "Der Kollege, mit dem ich arbeite, ist nett.", "Giới từ đứng trước đại từ quan hệ."),
        ],
    },
    "de-b2-genitiv-praep": {
        "howto": [
            "Học các giới từ luôn đi với Genitiv: wegen, trotz, während, statt, aufgrund, innerhalb, außerhalb, mangels.",
            "Giống đực/trung: des + -s; giống cái và số nhiều: der.",
            "Đặt cụm giới từ ở đầu câu hoặc sau động từ.",
        ],
        "notes": [
            "Khẩu ngữ đôi khi dùng Dativ với wegen, nhưng chuẩn viết vẫn là Genitiv.",
            "mangels thường dùng không có mạo từ: mangels Erfahrung.",
        ],
        "examples": [
            ("Wegen des Regens bleiben wir zu Hause.",
             "Vì trời mưa nên chúng tôi ở nhà."),
            ("Trotz der Kälte gehen wir spazieren.",
             "Dù lạnh, chúng tôi vẫn đi dạo."),
        ],
        "mistakes": [
            ("Wegen dem Regen bleiben wir zu Hause.", "Wegen des Regens bleiben wir zu Hause.", "wegen chuẩn mực đi với Genitiv."),
        ],
    },
    "de-b2-je-desto": {
        "howto": [
            "Cấu trúc: Je + so sánh hơn + ..., desto + so sánh hơn + ...",
            "Cả hai vế đảo động từ ra trước chủ ngữ.",
            "desto luôn đứng đầu vế thứ hai.",
        ],
        "notes": [
            "Không dùng als trong cấu trúc này.",
            "Có thể thay desto bằng umso, nghĩa không đổi.",
        ],
        "examples": [
            ("Je mehr ich lerne, desto besser verstehe ich.",
             "Tôi càng học nhiều, tôi càng hiểu rõ."),
            ("Je früher du kommst, desto mehr Zeit haben wir.",
             "Bạn đến càng sớm, chúng ta càng có nhiều thời gian."),
        ],
        "mistakes": [
            ("Je mehr ich lerne, desto besser ich verstehe.", "Je mehr ich lerne, desto besser verstehe ich.", "Vế desto phải đảo động từ."),
        ],
    },
    "de-b2-verben-dativ": {
        "howto": [
            "Học nhóm động từ chỉ nhận Dativ: helfen, danken, gratulieren, folgen, gehorchen, widersprechen.",
            "Nếu có cả tân ngữ Dativ và Akkusativ, Dativ (người) đứng trước Akkusativ (vật).",
            "Đại từ Dativ: mir, dir, ihm, ihr, uns, euch, ihnen.",
        ],
        "notes": [
            "Nhóm này không dùng Akkusativ cho người nhận.",
            "Một số động từ như danken có thể thêm Akkusativ cho nội dung: Ich danke dir für die Hilfe.",
        ],
        "examples": [
            ("Ich danke dir für deine Hilfe.",
             "Tôi cảm ơn bạn vì đã giúp."),
            ("Der Hund folgt dem Kind.",
             "Con chó đi theo đứa trẻ."),
        ],
        "mistakes": [
            ("Ich danke dich für die Hilfe.", "Ich danke dir für die Hilfe.", "danken đi với Dativ: dir."),
        ],
    },
    "de-b2-passiv-ersatz": {
        "howto": [
            "sein + zu + Infinitiv: nghĩa 'cần phải' hoặc 'có thể' tùy ngữ cảnh.",
            "sich lassen + Infinitiv: nghĩa 'có thể làm được'.",
            "Tính từ đuôi -bar: machbar, lösbar, essbar.",
        ],
        "notes": [
            "Các cấu trúc này thay bị động khi không muốn nêu tác nhân.",
            "sein + zu + Infinitiv thường mang nghĩa bắt buộc hơn sich lassen.",
        ],
        "examples": [
            ("Das Problem ist leicht zu lösen.",
             "Vấn đề này dễ giải quyết."),
            ("Die Tür lässt sich nicht öffnen.",
             "Cửa này không mở được."),
        ],
        "mistakes": [
            ("Das Problem lässt sich leicht lösen werden.", "Das Problem lässt sich leicht lösen.", "sich lassen đã thay bị động, không thêm werden."),
        ],
    },
}
