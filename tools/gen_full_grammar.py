#!/usr/bin/env python
# gen_full_grammar.py - add the advanced grammar topics + banks that complete the syllabus.
# Run after tools/gen_grammar_banks.py:
#   python tools/gen_full_grammar.py
#
# Idempotent: removes and re-adds only the FULL_TOPICS below.
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_grammar_banks as base  # noqa: E402

G = base.G
LEX = base.LEX
SUBJ = base.SUBJ
VERBS = base.VERBS
BASE = base.BASE
PATH = base.PATH
TIMES = base.TIMES
CTX = base.CTX
COMMENT = base.COMMENT
PLACES = base.PLACES


def T(tid, cat, level, title, vi, formula, use, signals, en, vi_ex, wrong, right, why, exam):
    return dict(
        id=tid, cat=cat, level=level, title=title, vi=vi, formula=formula,
        use=use, signals=signals,
        examples=[dict(en=en, vi=vi_ex)],
        mistakes=[dict(wrong=wrong, right=right, why=why)],
        exam=exam,
    )


FULL = [
    # ---------- Động từ ----------
    T('verb-patterns', 'Động từ', 'B1', 'Verb Patterns', 'Mẫu động từ',
      'V + to V / V-ing / V (bare)', 'Mỗi động từ có mẫu theo sau riêng: to V, V-ing hoặc động từ nguyên mẫu.',
      ['want to', 'enjoy doing', 'can do', 'decide to', 'avoid doing'],
      'She wants to read the report.', 'Cô ấy muốn đọc báo cáo.',
      'She enjoys to read the report.', 'She enjoys reading the report.', 'Enjoy theo sau là V-ing.',
      'TOEIC: chọn đúng dạng động từ. IELTS: dùng đúng mẫu trong Writing/Speaking.'),
    T('irregular-verbs', 'Động từ', 'A2', 'Irregular Verbs', 'Động từ bất quy tắc',
      'V1 / V2 / V3', 'Động từ bất quy tắc không thêm -ed; cần học V1, V2, V3 theo bảng.',
      ['write-wrote-written', 'take-took-taken', 'send-sent-sent'],
      'She wrote the report yesterday.', 'Cô ấy đã viết báo cáo hôm qua.',
      'She writed the report.', 'She wrote the report.', 'Write có dạng quá khứ là wrote.',
      'TOEIC: thì quá khứ, hiện tại hoàn thành. IELTS: tránh lỗi V2/V3.'),
    T('stative-verbs', 'Động từ', 'B1', 'Stative Verbs', 'Động từ trạng thái',
      'S + stative verb (know, believe, want, belong...)', 'Động từ trạng thái thường không dùng ở thể tiếp diễn vì diễn tả trạng thái, không phải hành động.',
      ['know', 'believe', 'want', 'belong', 'understand'],
      'She knows the answer.', 'Cô ấy biết câu trả lời.',
      'She is knowing the answer.', 'She knows the answer.', 'Know là động từ trạng thái, không dùng tiếp diễn.',
      'TOEIC: phân biệt trạng thái/hành động. IELTS: tránh -ing với stative verbs.'),
    T('linking-verbs', 'Động từ', 'B1', 'Linking Verbs', 'Động từ liên kết',
      'S + linking verb + adj/noun', 'Linking verb nối chủ ngữ với tính từ hoặc danh từ bổ nghĩa, không diễn tả hành động.',
      ['be', 'seem', 'look', 'feel', 'become'],
      'The report seems clear.', 'Báo cáo có vẻ rõ ràng.',
      'The report seems clearly.', 'The report seems clear.', 'Sau linking verb dùng tính từ, không dùng trạng từ.',
      'TOEIC: be/seem/look + adj. IELTS: mô tả và đánh giá.'),
    T('auxiliary-do', 'Động từ', 'A2', 'Auxiliary Do', 'Trợ động từ do/does/did',
      'do/does/did + V', 'Do/does/did dùng để tạo câu hỏi, phủ định và nhấn mạnh ở thì đơn.',
      ['do', 'does', 'did', 'do not', 'does not'],
      'She does read the report every day.', 'Cô ấy thực sự đọc báo cáo mỗi ngày.',
      'She reads not the report.', 'She does not read the report.', 'Phủ định thì hiện tại đơn dùng does not + V.',
      'TOEIC: câu hỏi/phủ định. IELTS: nhấn mạnh trong Speaking.'),
    T('passive-tenses', 'Động từ', 'B1', 'Passive Across Tenses', 'Bị động qua các thì',
      'S + be (chia thì) + V3', 'Bị động thay đổi dạng be theo thì; V3 giữ nguyên.',
      ['is written', 'was written', 'will be written', 'has been written'],
      'The report has been written by the manager.', 'Báo cáo đã được viết bởi quản lý.',
      'The report has wrote by the manager.', 'The report has been written by the manager.', 'Bị động hoàn thành dùng has been + V3.',
      'TOEIC: quy trình, thông báo. IELTS: câu bị động học thuật.'),
    T('get-passive', 'Động từ', 'B2', 'Get-Passive', 'Bị động với get',
      'S + get + V3', 'Get-passive thường dùng trong văn nói, nhấn mạnh sự thay đổi hoặc sự việc bất ngờ.',
      ['get promoted', 'get fired', 'get hurt', 'get paid'],
      'She got promoted last month.', 'Cô ấy được thăng chức tháng trước.',
      'She got promote last month.', 'She got promoted last month.', 'Get-passive dùng V3 sau get.',
      'IELTS Speaking: kể chuyện. TOEIC: ít gặp hơn be-passive.'),
    T('impersonal-passive', 'Động từ', 'C1', 'Impersonal Passive', 'Bị động khách quan',
      'It is said that... / S + is believed to V', 'Bị động khách quan dùng để trình bày ý kiến chung mà không nêu người nói.',
      ['it is said', 'it is believed', 'is thought to', 'is reported to'],
      'It is said that the policy is effective.', 'Người ta nói rằng chính sách này hiệu quả.',
      'It is said that the policy is effect.', 'It is said that the policy is effective.', 'Sau that là một mệnh đề đầy đủ.',
      'IELTS Writing: hedging học thuật. TOEIC: thông báo, báo cáo.'),
    T('past-modals', 'Động từ', 'B2', 'Past Modals', 'Modal + have + V3',
      'modal + have + V3', 'Modal perfect diễn tả suy đoán, tiếc nuối hoặc khả năng trong quá khứ.',
      ['should have', 'must have', 'could have', 'might have'],
      'She should have checked the report.', 'Cô ấy lẽ ra nên kiểm tra báo cáo.',
      'She should has checked the report.', 'She should have checked the report.', 'Sau modal luôn dùng have + V3.',
      'TOEIC: suy đoán quá khứ. IELTS: diễn đạt tiếc nuối, giả định.'),
    T('semi-modals', 'Động từ', 'B1', 'Semi-Modals', 'Bán modal',
      'have to / need to / ought to / be able to', 'Bán modal diễn tả bổn phận, khả năng, sự cần thiết nhưng chia theo chủ ngữ.',
      ['have to', 'need to', 'ought to', 'be able to'],
      'She has to submit the report today.', 'Cô ấy phải nộp báo cáo hôm nay.',
      'She have to submit the report.', 'She has to submit the report.', 'Have to chia has to với chủ ngữ số ít.',
      'TOEIC: nghĩa vụ, khả năng. IELTS: thay thế must/can.'),
    T('deduction-modals', 'Động từ', 'B2', 'Modals of Deduction', 'Modal suy đoán',
      'must / might / can\'t + be / have been', 'Modal suy đoán diễn tả mức độ chắc chắn: must (chắc), might (có thể), can\'t (không thể).',
      ['must be', 'might be', 'can\'t be', 'must have been'],
      'The report must be on the desk.', 'Báo cáo chắc hẳn ở trên bàn.',
      'The report must is on the desk.', 'The report must be on the desk.', 'Sau modal dùng động từ nguyên mẫu be.',
      'TOEIC: suy luận từ manh mối. IELTS: đưa ra dự đoán thận trọng.'),
    T('future-forms', 'Động từ', 'B1', 'Future Forms', 'Các dạng tương lai',
      'will / be going to / present continuous / be to', 'Tiếng Anh có nhiều cách diễn tả tương lai; mỗi dạng mang sắc thái khác nhau.',
      ['will', 'going to', 'present continuous', 'be about to'],
      'We are going to launch the product next month.', 'Chúng tôi sẽ ra mắt sản phẩm tháng sau.',
      'We will going to launch the product.', 'We are going to launch the product.', 'Be going to cần đúng dạng be.',
      'TOEIC: kế hoạch, dự báo. IELTS: mô tả xu hướng tương lai.'),

    # ---------- Cấu trúc câu ----------
    T('zero-conditional', 'Cấu trúc câu', 'A2', 'Zero Conditional', 'Câu điều kiện loại 0',
      'If + present simple, present simple', 'Diễn tả sự thật hiển nhiên, quy luật hoặc thói quen.',
      ['if', 'when', 'unless', 'present simple'],
      'If you heat water, it boils.', 'Nếu bạn đun nước, nó sôi.',
      'If you will heat water, it boils.', 'If you heat water, it boils.', 'Mệnh đề if loại 0 dùng hiện tại đơn.',
      'IELTS: quy luật, xu hướng chung. TOEIC: quy trình.'),
    T('inverted-conditionals', 'Cấu trúc câu', 'C1', 'Inverted Conditionals', 'Đảo ngữ điều kiện',
      'Had / Were / Should + S + V', 'Bỏ if và đảo trợ động từ lên trước chủ ngữ trong câu điều kiện trang trọng.',
      ['had I', 'were I', 'should you'],
      'Had I known, I would have called.', 'Nếu tôi biết, tôi đã gọi.',
      'If I had known, I would have called.', 'Had I known, I would have called.', 'Đảo ngữ loại 3 dùng Had + S + V3.',
      'IELTS Writing: câu điều kiện trang trọng. TOEIC: ít gặp.'),
    T('conditional-linkers', 'Cấu trúc câu', 'B2', 'Conditional Linkers', 'Liên từ điều kiện',
      'provided / as long as / in case / otherwise', 'Các liên từ điều kiện thay thế if với sắc thái khác nhau.',
      ['provided that', 'as long as', 'in case', 'otherwise'],
      'You can leave provided that you finish the report.', 'Bạn có thể về miễn là hoàn thành báo cáo.',
      'You can leave provided that you will finish the report.', 'You can leave provided that you finish the report.', 'Sau provided that dùng hiện tại đơn cho tương lai.',
      'IELTS Writing: điều kiện, giả định. TOEIC: quy định.'),
    T('non-defining-relative', 'Cấu trúc câu', 'B1', 'Non-defining Relative Clauses', 'Mệnh đề quan hệ không xác định',
      'N, who/which + clause', 'Mệnh đề không xác định bổ sung thông tin, đứng sau dấu phẩy và không dùng that.',
      ['who', 'which', 'whose', 'where'],
      'The report, which was written in 2020, is outdated.', 'Báo cáo, được viết năm 2020, đã lỗi thời.',
      'The report, that was written in 2020, is outdated.', 'The report, which was written in 2020, is outdated.', 'Mệnh đề không xác định không dùng that.',
      'IELTS Writing: thêm thông tin phụ. TOEIC: đọc hiểu.'),
    T('reduced-relative', 'Cấu trúc câu', 'B2', 'Reduced Relative Clauses', 'Mệnh đề quan hệ rút gọn',
      'N + V-ing / V3', 'Rút gọn mệnh đề quan hệ bằng cách bỏ đại từ quan hệ và trợ động từ.',
      ['the report written', 'the manager working', 'the client waiting'],
      'The report written in 2020 is outdated.', 'Báo cáo được viết năm 2020 đã lỗi thời.',
      'The report which written in 2020 is outdated.', 'The report written in 2020 is outdated.', 'Rút gọn bị động dùng V3, bỏ which was.',
      'IELTS Writing: câu gọn, học thuật. TOEIC: đọc hiểu.'),
    T('embedded-questions', 'Cấu trúc câu', 'B1', 'Embedded Questions', 'Câu hỏi lồng',
      'I don\'t know + wh-/if + S + V', 'Câu hỏi lồng không đảo trợ động từ; dùng trật tự câu khẳng định.',
      ['I don\'t know', 'Could you tell me', 'Do you know', 'whether', 'if'],
      'Could you tell me where the office is?', 'Bạn có thể cho tôi biết văn phòng ở đâu không?',
      'Could you tell me where is the office?', 'Could you tell me where the office is?', 'Câu hỏi lồng dùng trật tự S + V.',
      'TOEIC: hội thoại lịch sự. IELTS Speaking: câu hỏi gián tiếp.'),
    T('wh-ever-clauses', 'Cấu trúc câu', 'B2', 'Wh-ever Clauses', 'Mệnh đề wh-ever',
      'whatever / whoever / whichever / whenever / wherever', 'Wh-ever diễn tả bất kỳ người, vật, nơi, thời điểm nào.',
      ['whatever', 'whoever', 'whichever', 'whenever'],
      'Whatever you decide, we will support you.', 'Dù bạn quyết định gì, chúng tôi sẽ ủng hộ.',
      'Whatever you will decide, we will support you.', 'Whatever you decide, we will support you.', 'Mệnh đề wh-ever dùng hiện tại đơn cho tương lai.',
      'IELTS Writing/Speaking: mở rộng ý. TOEIC: ít gặp.'),
    T('reduced-adverb-clauses', 'Cấu trúc câu', 'B2', 'Reduced Adverb Clauses', 'Mệnh đề trạng ngữ rút gọn',
      'When / After / Before + V-ing / V3', 'Rút gọn mệnh đề trạng ngữ khi chủ ngữ hai mệnh đề giống nhau.',
      ['when working', 'after finishing', 'before leaving'],
      'When working late, she always checks the report.', 'Khi làm muộn, cô ấy luôn kiểm tra báo cáo.',
      'When work late, she always checks the report.', 'When working late, she always checks the report.', 'Rút gọn chủ động dùng V-ing.',
      'IELTS Writing: câu phức gọn. TOEIC: đọc hiểu.'),

    # ---------- Câu nâng cao ----------
    T('sentence-types', 'Câu nâng cao', 'A2', 'Sentence Types', 'Loại câu',
      'declarative / interrogative / imperative / exclamatory', 'Bốn loại câu theo mục đích giao tiếp; nắm để đặt câu và dấu câu đúng.',
      ['statement', 'question', 'imperative', 'exclamation'],
      'Does the manager approve the plan?', 'Quản lý có phê duyệt kế hoạch không?',
      'Does the manager approves the plan?', 'Does the manager approve the plan?', 'Sau does dùng động từ nguyên mẫu.',
      'TOEIC: câu hỏi, câu mệnh lệnh. IELTS: đa dạng loại câu.'),
    T('ellipsis-substitution', 'Câu nâng cao', 'B2', 'Ellipsis & Substitution', 'Tỉnh lược và thay thế',
      'so do I / neither did she / I can too', 'Tỉnh lược bỏ phần lặp; thay thế dùng do/so/neither/one.',
      ['so do I', 'neither did she', 'I can too', 'one'],
      'She can swim, and I can too.', 'Cô ấy biết bơi, và tôi cũng vậy.',
      'She can swim, and I can either.', 'She can swim, and I can too.', 'Khẳng định đồng tình dùng too/so.',
      'IELTS Speaking: trả lời tự nhiên. TOEIC: hội thoại.'),
    T('pronoun-agreement', 'Câu nâng cao', 'B1', 'Pronoun Agreement', 'Hòa hợp đại từ',
      'everyone + they / each + their', 'Đại từ phải hòa hợp với danh từ mà nó thay thế về số và giống.',
      ['everyone', 'each', 'their', 'its'],
      'Everyone must bring their badge.', 'Mọi người phải mang thẻ của mình.',
      'Everyone must bring its badge.', 'Everyone must bring their badge.', 'Everyone thường dùng they/their trong tiếng Anh hiện đại.',
      'IELTS Writing: tránh lỗi đại từ. TOEIC: đọc hiểu.'),
    T('collective-nouns', 'Câu nâng cao', 'B2', 'Collective Nouns', 'Danh từ tập hợp',
      'team / staff / police + is/are', 'Danh từ tập hợp có thể dùng động từ số ít hoặc số nhiều tùy cách nhìn nhóm.',
      ['team', 'staff', 'police', 'family'],
      'The team is working on the project.', 'Nhóm đang làm việc trên dự án.',
      'The team are working on the project.', 'The team is working on the project.', 'Trong tiếng Anh Mỹ, team thường dùng số ít.',
      'IELTS Writing: mô tả tổ chức. TOEIC: chủ ngữ tập hợp.'),
    T('reporting-verbs', 'Câu nâng cao', 'B2', 'Reporting Verbs', 'Động từ tường thuật',
      'admit / deny / suggest / offer + V-ing/to V', 'Mỗi động từ tường thuật có mẫu theo sau riêng.',
      ['admit', 'deny', 'suggest', 'offer'],
      'She admitted making a mistake.', 'Cô ấy thừa nhận đã mắc lỗi.',
      'She admitted to make a mistake.', 'She admitted making a mistake.', 'Admit theo sau là V-ing.',
      'IELTS Writing: tường thuật nghiên cứu. TOEIC: email, báo cáo.'),
    T('fronting-extraposition', 'Câu nâng cao', 'C1', 'Fronting & Extraposition', 'Đảo thành phần và ngoại vị',
      'What I need is... / It is important that...', 'Fronting đưa thành phần nhấn mạnh lên đầu câu; extraposition dùng it làm chủ ngữ giả.',
      ['what I need', 'it is important', 'on the desk sat'],
      'What we need is a clear plan.', 'Điều chúng tôi cần là một kế hoạch rõ ràng.',
      'What we need are a clear plan.', 'What we need is a clear plan.', 'Chủ ngữ what-clause thường dùng động từ số ít.',
      'IELTS Writing: nhấn mạnh, câu học thuật. TOEIC: ít gặp.'),
    T('punctuation', 'Câu nâng cao', 'B1', 'Punctuation', 'Dấu câu',
      'comma / semicolon / colon / dash / apostrophe', 'Dấu câu phân tách mệnh đề, danh sách, sở hữu và trích dẫn.',
      ['comma', 'semicolon', 'colon', 'apostrophe'],
      'The report was clear; however, it was long.', 'Báo cáo rõ ràng; tuy nhiên, nó dài.',
      'The report was clear, however, it was long.', 'The report was clear; however, it was long.', 'Hai mệnh đề độc lập nối bằng however dùng dấu chấm phẩy.',
      'IELTS Writing: dấu câu chính xác. TOEIC: email, báo cáo.'),

    # ---------- Từ loại ----------
    T('vietnamese-learner-errors', 'C\u00e2u n\u00e2ng cao', 'B1', 'Vietnamese Learner Errors', 'L\u1ed7i ng\u01b0\u1eddi Vi\u1ec7t hay g\u1eb7p',
      'articles / plural / tense / preposition / word order', 'C\u00e1c l\u1ed7i do chuy\u1ec3n tr\u1ef1c ti\u1ebfp t\u1eeb ti\u1ebfng Vi\u1ec7t: thi\u1ebfu m\u1ea1o t\u1eeb, sai s\u1ed1 nhi\u1ec1u, sai th\u00ec, sai gi\u1edbi t\u1eeb, sai tr\u1eadt t\u1ef1 t\u1eeb.',
      ['a/an', 'plural', 'tense', 'preposition'],
      'She has lived here for three years.', 'C\u00f4 \u1ea5y \u0111\u00e3 s\u1ed1ng \u1edf \u0111\u00e2y ba n\u0103m.',
      'She lives here since three years.', 'She has lived here for three years.', 'D\u00f9ng hi\u1ec7n t\u1ea1i ho\u00e0n th\u00e0nh v\u1edbi since/for.',
      'IELTS Writing: gi\u1ea3m l\u1ed7i L1. TOEIC: vi\u1ebft email \u0111\u00fang ng\u1eef ph\u00e1p.'),
    T('both-either-neither', 'Từ loại', 'B1', 'Both / Either / Neither', 'Both / Either / Neither',
      'both...and / either...or / neither...nor', 'Bộ đôi liên từ diễn tả cả hai, một trong hai, không cái nào.',
      ['both', 'either', 'neither', 'nor'],
      'Neither the manager nor the staff were available.', 'Cả quản lý lẫn nhân viên đều không có mặt.',
      'Neither the manager or the staff were available.', 'Neither the manager nor the staff were available.', 'Neither đi với nor.',
      'TOEIC: cấu trúc song song. IELTS: diễn đạt lựa chọn.'),
    T('other-another', 'Từ loại', 'A2', 'Other / Another / The Others', 'Other / Another / The Others',
      'another + N(số ít) / other + N(số nhiều)', 'Phân biệt another, other, others, the other, the others theo số lượng và xác định.',
      ['another', 'other', 'others', 'the others'],
      'I need another report.', 'Tôi cần một báo cáo khác.',
      'I need other report.', 'I need another report.', 'Another đi với danh từ số ít.',
      'TOEIC: lượng từ. IELTS: tránh lẫn another/other.'),
    T('indefinite-pronouns', 'Từ loại', 'A2', 'Indefinite Pronouns', 'Đại từ bất định',
      'somebody / anyone / nobody / everything', 'Đại từ bất định chỉ người/vật không xác định; động từ thường chia số ít.',
      ['somebody', 'anyone', 'nobody', 'everything'],
      'Everyone is ready for the meeting.', 'Mọi người đã sẵn sàng cho cuộc họp.',
      'Everyone are ready for the meeting.', 'Everyone is ready for the meeting.', 'Everyone dùng động từ số ít.',
      'TOEIC: đại từ trong câu. IELTS: tránh lỗi số ít/số nhiều.'),
    T('reciprocal-pronouns', 'Từ loại', 'B1', 'Reciprocal Pronouns', 'Đại từ tương hỗ',
      'each other / one another', 'Each other và one another diễn tả hành động qua lại giữa hai hay nhiều đối tượng.',
      ['each other', 'one another'],
      'The two managers called each other.', 'Hai quản lý gọi cho nhau.',
      'The two managers called themselves.', 'The two managers called each other.', 'Hành động qua lại dùng each other, không dùng themselves.',
      'IELTS Speaking: mô tả tương tác. TOEIC: ít gặp.'),
    T('dummy-it-there', 'Từ loại', 'B1', 'Dummy It / There', 'It / There giả',
      'It is + adj + to V / There is + N', 'It và there làm chủ ngữ giả khi chủ ngữ thật đứng sau.',
      ['it is important to', 'there is', 'there are'],
      'It is important to check the figures.', 'Điều quan trọng là kiểm tra số liệu.',
      'Is important to check the figures.', 'It is important to check the figures.', 'Câu cần chủ ngữ giả it.',
      'TOEIC: câu mô tả, tồn tại. IELTS: câu học thuật.'),
    T('as-as-comparison', 'Từ loại', 'B1', 'As ... As', 'So sánh bằng',
      'as + adj/adv + as', 'So sánh bằng dùng as...as; phủ định dùng not as...as.',
      ['as...as', 'not as...as', 'twice as...as'],
      'This report is as detailed as the previous one.', 'Báo cáo này chi tiết bằng báo cáo trước.',
      'This report is as detailed than the previous one.', 'This report is as detailed as the previous one.', 'So sánh bằng dùng as...as, không dùng than.',
      'TOEIC: so sánh số liệu. IELTS Task 1: mô tả tương đương.'),
    T('adjective-prepositions', 'Từ loại', 'B1', 'Adjective + Preposition', 'Tính từ + giới từ',
      'adj + preposition', 'Nhiều tính từ đi với giới từ cố định; cần học theo cụm.',
      ['responsible for', 'interested in', 'good at', 'worried about'],
      'She is responsible for the budget.', 'Cô ấy chịu trách nhiệm về ngân sách.',
      'She is responsible of the budget.', 'She is responsible for the budget.', 'Responsible đi với for.',
      'TOEIC: collocation. IELTS: dùng đúng giới từ.'),
    T('correlative-conjunctions', 'Từ loại', 'B2', 'Correlative Conjunctions', 'Liên từ tương quan',
      'both...and / not only...but also / either...or', 'Liên từ tương quan đi thành cặp và cần cấu trúc song song.',
      ['both...and', 'not only...but also', 'either...or', 'neither...nor'],
      'She is both efficient and reliable.', 'Cô ấy vừa hiệu quả vừa đáng tin cậy.',
      'She is both efficient and she is reliable.', 'She is both efficient and reliable.', 'Hai vế sau both...and phải song song.',
      'IELTS Writing: câu phức cân đối. TOEIC: cấu trúc song song.'),
    T('discourse-markers', 'Từ loại', 'B2', 'Discourse Markers', 'Dấu hiệu diễn ngôn',
      'however / therefore / moreover / in addition', 'Discourse markers nối ý giữa câu và đoạn, thể hiện quan hệ logic.',
      ['however', 'therefore', 'moreover', 'in addition'],
      'The plan is expensive; however, it is effective.', 'Kế hoạch tốn kém; tuy nhiên, nó hiệu quả.',
      'The plan is expensive, however it is effective.', 'The plan is expensive; however, it is effective.', 'However nối hai mệnh đề độc lập cần dấu chấm phẩy hoặc dấu chấm.',
      'IELTS Writing: cohesion. TOEIC: đọc hiểu.'),
    T('numbers-percentages', 'Từ loại', 'B1', 'Numbers & Percentages', 'Số và phần trăm',
      'a third of / 25 percent of / the majority of', 'Diễn tả số lượng, tỉ lệ, phần trăm; động từ chia theo danh từ sau of.',
      ['percent', 'a third of', 'the majority of', 'twice'],
      'Two thirds of the staff are satisfied.', 'Hai phần ba nhân viên hài lòng.',
      'Two thirds of the staff is satisfied.', 'Two thirds of the staff are satisfied.', 'Động từ chia theo danh từ số nhiều staff.',
      'IELTS Task 1: mô tả số liệu. TOEIC: báo cáo.'),

    # ---------- TOEIC & IELTS ----------
    T('ielts-task1-structures', 'TOEIC & IELTS', 'B2', 'IELTS Task 1 Structures', 'Cấu trúc IELTS Task 1',
      'The chart shows / increased / whereas / accounted for', 'Cấu trúc mô tả biểu đồ: xu hướng, so sánh, số liệu, dự báo.',
      ['the chart shows', 'increased', 'whereas', 'accounted for'],
      'The chart shows that sales increased steadily.', 'Biểu đồ cho thấy doanh số tăng đều.',
      'The chart shows that sales increased steady.', 'The chart shows that sales increased steadily.', 'Sau động từ cần trạng từ steadily.',
      'IELTS Writing Task 1: mô tả số liệu, xu hướng.'),
    T('ielts-task2-structures', 'TOEIC & IELTS', 'C1', 'IELTS Task 2 Structures', 'Cấu trúc IELTS Task 2',
      'While... / Although... / It is argued that...', 'Cấu trúc lập luận: mở bài, thân bài, phản biện, kết luận.',
      ['while', 'although', 'it is argued that', 'in conclusion'],
      'While some people support the policy, others remain concerned.', 'Trong khi một số người ủng hộ chính sách, những người khác vẫn lo ngại.',
      'While some people support the policy, but others remain concerned.', 'While some people support the policy, others remain concerned.', 'While không đi với but.',
      'IELTS Writing Task 2: lập luận, phản biện.'),
]


def add_line_bank(topic_id, lines):
    lines = [x.strip().rstrip('.?!') for x in lines if x.strip()]
    if len(lines) < 50:
        lines = (lines * 50)[:50]
    assert len(lines) >= 50, (topic_id, len(lines))
    entries = [dict(line=x) for x in lines[:50]]
    for e in entries:
        base.lower_fields(e, 'line')
    base.add_bank(topic_id, ['E', 'CTX', 'TIME', 'COMMENT'], [
        '{E_LINE} {CTX} {TIME}.',
        '{COMMENT}, {E_LINE_L} {CTX}.',
        '{E_LINE} {TIME}.',
        'I know that {E_LINE_L} {CTX}.',
        'Do you know that {E_LINE_L} {CTX}?',
        'The teacher said that {E_LINE_L} {CTX}.',
        '{E_LINE}, which is important {CTX}.',
        'In this case, {E_LINE_L} {CTX}.',
    ], dict(E=entries, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))


OBJ = ['the report', 'the email', 'the contract', 'the proposal', 'the invoice']
SUBJ5 = ['She', 'He', 'They', 'We', 'The manager']


def build_banks():
    # verb-patterns
    lines = []
    patterns = [
        'She wants to read {o}.', 'She enjoys reading {o}.', 'She can read {o}.',
        'She decided to read {o}.', 'She avoids making mistakes about {o}.',
        'She suggested taking a break after {o}.', 'She does not mind working late on {o}.',
        'She looks forward to meeting the client about {o}.', 'She used to read {o}.',
        'She is used to reading {o}.',
    ]
    for p in patterns:
        for o in OBJ:
            lines.append(p.format(o=o))
    add_line_bank('verb-patterns', lines)

    # irregular-verbs
    lines = []
    for i, v in enumerate(VERBS):
        s = SUBJ[i % len(SUBJ)]['t']
        o = v['obj'][i % 2]
        lines.append('%s %s %s.' % (s, v['past'], o))
        lines.append('%s %s %s %s.' % (s, 'has' if SUBJ[i % len(SUBJ)]['p'] == '3s' else 'have', v['pp'], o))
    add_line_bank('irregular-verbs', lines)

    # stative-verbs
    lines = []
    stative = [
        ('knows', 'the answer'), ('believes', 'the plan'), ('wants', 'more time'),
        ('needs', 'a break'), ('likes', 'the idea'), ('loves', 'the new office'),
        ('hates', 'long meetings'), ('understands', 'the problem'), ('remembers', 'the deadline'),
        ('belongs to', 'the manager'),
    ]
    for v, o in stative:
        for s in SUBJ5:
            lines.append('%s %s %s.' % (s, v, o))
    add_line_bank('stative-verbs', lines)

    # linking-verbs
    lines = []
    for v in ['seems', 'looks', 'feels', 'sounds', 'tastes', 'smells', 'becomes', 'gets', 'grows', 'stays']:
        for a in ['clear', 'ready', 'tired', 'important', 'useful']:
            lines.append('The report %s %s.' % (v, a))
    add_line_bank('linking-verbs', lines)

    # auxiliary-do
    lines = []
    for s in SUBJ5:
        for o in OBJ:
            lines.append('%s does read %s.' % (s, o))
    for s in SUBJ5:
        for o in OBJ:
            lines.append('%s does not read %s.' % (s, o))
    add_line_bank('auxiliary-do', lines)

    # passive-tenses
    lines = []
    for o in OBJ:
        lines += [
            '%s is checked every day.' % o.capitalize(),
            '%s was checked yesterday.' % o.capitalize(),
            '%s will be checked tomorrow.' % o.capitalize(),
            '%s has been checked.' % o.capitalize(),
            '%s had been checked before the meeting.' % o.capitalize(),
            '%s is being checked now.' % o.capitalize(),
            '%s was being checked at noon.' % o.capitalize(),
            '%s will have been checked by Friday.' % o.capitalize(),
        ]
    add_line_bank('passive-tenses', lines)

    # get-passive
    lines = []
    for s in SUBJ5:
        for p in ['got promoted', 'got fired', 'got hurt', 'got paid', 'got promoted to manager']:
            lines.append('%s %s.' % (s, p))
    add_line_bank('get-passive', lines)

    # impersonal-passive
    lines = []
    for p in [
        'It is said that the policy is effective.',
        'It is believed that the plan will work.',
        'It is reported that sales have increased.',
        'It is thought that the client will agree.',
        'The policy is said to be effective.',
        'The plan is believed to be practical.',
        'The report is reported to be accurate.',
        'The manager is thought to support the plan.',
        'The contract is expected to be signed.',
        'The project is considered to be successful.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('impersonal-passive', lines)

    # past-modals
    lines = []
    for p in [
        'She should have checked the report.', 'She must have checked the report.',
        'She could have checked the report.', 'She might have checked the report.',
        'She need not have checked the report.', 'She would have checked the report.',
        'She cannot have checked the report.', 'She may have checked the report.',
        'She ought to have checked the report.', 'She could not have checked the report.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('past-modals', lines)

    # semi-modals
    lines = []
    for p in [
        'She has to submit the report.', 'She needs to submit the report.',
        'She ought to submit the report.', 'She is able to submit the report.',
        'She is going to submit the report.', 'She used to submit the report.',
        'She is supposed to submit the report.', 'She had to submit the report.',
        'She will be able to submit the report.', 'She is expected to submit the report.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('semi-modals', lines)

    # deduction-modals
    lines = []
    for p in [
        'The report must be on the desk.', 'The report might be on the desk.',
        'The report cannot be on the desk.', 'The report must have been checked.',
        'The report might have been checked.', 'The report cannot have been checked.',
        'The report should be ready.', 'The report should have been ready.',
        'The report could be ready.', 'The report could have been ready.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('deduction-modals', lines)

    # future-forms
    lines = []
    for p in [
        'She will submit the report.', 'She is going to submit the report.',
        'She is submitting the report tomorrow.', 'She submits the report tomorrow.',
        'She is to submit the report.', 'She is about to submit the report.',
        'She will be submitting the report.', 'She will have submitted the report.',
        'She is due to submit the report.', 'She is expected to submit the report.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('future-forms', lines)

    # zero-conditional
    lines = []
    for p in [
        'If you heat water, it boils.', 'If you press this button, the machine starts.',
        'If the client calls, the manager answers.', 'If it rains, the event moves online.',
        'If you mix red and blue, you get purple.', 'If the report is late, the team works overtime.',
        'If the invoice is unpaid, the system sends a reminder.',
        'If you do not water the plant, it dies.',
        'If the traffic is heavy, we take the train.',
        'If the data is incomplete, the report is delayed.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('zero-conditional', lines)

    # inverted-conditionals
    lines = []
    for p in [
        'Had I known, I would have called.', 'Were I the manager, I would change the plan.',
        'Should you need help, please call me.', 'Had she studied, she would have passed.',
        'Were they available, we would invite them.', 'Should the client agree, we will sign.',
        'Had we left earlier, we would not be late.', 'Were it possible, I would join the meeting.',
        'Should it rain, the event will move online.', 'Had he checked, he would have found the error.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('inverted-conditionals', lines)

    # conditional-linkers
    lines = []
    for p in [
        'You can leave provided that you finish the report.',
        'You can join as long as you register first.',
        'Take an umbrella in case it rains.',
        'Finish the report; otherwise, the client will complain.',
        'Unless you call, the order will be cancelled.',
        'Even if it rains, the event will continue.',
        'Only if you submit the form will you be considered.',
        'I will help on condition that you review the plan.',
        'Supposing the client agrees, we will proceed.',
        'We need a backup plan if the supplier delivers late.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('conditional-linkers', lines)

    # non-defining-relative
    lines = []
    for p in [
        'The report, which was written in 2020, is outdated.',
        'The manager, who joined last year, leads the team.',
        'The office, which is on the second floor, is being renovated.',
        'The client, whose contract expires soon, asked for a meeting.',
        'The project, which started in June, is now complete.',
        'The staff, who received training, worked more efficiently.',
        'The invoice, which was sent yesterday, has not been paid.',
        'The policy, which applies to all staff, starts next month.',
        'The supplier, who missed the deadline, apologized.',
        'The proposal, which we reviewed, needs revision.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('non-defining-relative', lines)

    # reduced-relative
    lines = []
    for p in [
        'The report written in 2020 is outdated.',
        'The manager working in the office leads the team.',
        'The client waiting at reception is from London.',
        'The proposal reviewed yesterday needs revision.',
        'The staff trained last month work more efficiently.',
        'The invoice sent yesterday has not been paid.',
        'The office located on the second floor is being renovated.',
        'The project started in June is now complete.',
        'The supplier contacted by the team apologized.',
        'The policy introduced last year reduced costs.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('reduced-relative', lines)

    # embedded-questions
    lines = []
    for p in [
        'I do not know where the office is.',
        'I do not know when the meeting starts.',
        'I am not sure whether the client has agreed.',
        'I wonder if the report is ready.',
        'She asked how the system works.',
        'I am not sure why the shipment was delayed.',
        'I cannot remember who approved the plan.',
        'I do not remember what the client requested.',
        'I do not know how much the service costs.',
        'I wonder whether we should change the schedule.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('embedded-questions', lines)

    # wh-ever
    lines = []
    for p in [
        'Whatever you decide, we will support you.',
        'Whoever calls first will get the ticket.',
        'Whichever option you choose, the result is the same.',
        'Whenever you need help, please call me.',
        'Wherever you go, keep the receipt.',
        'However hard he tried, he could not finish.',
        'Whatever happens, the meeting will continue.',
        'Whoever wrote the report should check the figures.',
        'Whichever train you take, you will arrive by noon.',
        'Whenever the client calls, the manager answers.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('wh-ever-clauses', lines)

    # reduced-adverb-clauses
    lines = []
    for p in [
        'When working late, she always checks the report.',
        'After finishing the report, he went home.',
        'Before leaving the office, she locked the door.',
        'While waiting for the client, we reviewed the plan.',
        'Since joining the company, she has led three projects.',
        'Having completed the training, the staff felt confident.',
        'When asked about the delay, he apologized.',
        'Once approved, the policy will start next month.',
        'After being reviewed, the report was sent to the client.',
        'Before being signed, the contract was checked by legal.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('reduced-adverb-clauses', lines)

    # sentence-types
    types = []
    for c in BASE:
        s, v, o = c['subj'], c['v'], c['o']
        p3 = s['p'] == '3s'
        q_aux = 'does' if p3 else 'do'
        types.append(dict(
            decl='%s %s %s' % (s['t'], v['s'] if p3 else v['b'], o),
            q='%s %s %s %s' % (q_aux, s['t'], v['b'], o),
            q_embed='whether %s %s %s' % (s['t'], v['s'] if p3 else v['b'], o),
            imp='%s %s' % (v['b'], o),
            excl='What a clear report',
        ))
    base.add_bank('sentence-types', ['E', 'CTX', 'TIME', 'COMMENT'], [
        '{E_DECL} {CTX} {TIME}.',
        '{E_Q} {CTX} {TIME}?',
        'Please {E_IMP} {CTX}.',
        '{E_EXCL} {CTX}!',
        'I know that {E_DECL_L} {CTX}.',
        'Could you tell me {E_Q_EMBED} {CTX}?',
        '{E_DECL}, and please {E_IMP_L}.',
        '{COMMENT}, {E_EXCL_L} {CTX}!',
    ], dict(E=types, CTX=CTX, TIME=TIMES, COMMENT=COMMENT))
    for e in types:
        base.lower_fields(e, 'decl', 'imp', 'excl')

    # ellipsis-substitution
    lines = []
    for p in [
        'She can swim, and I can too.',
        'He did not attend, but I did.',
        'They finished the report, and so did we.',
        'She has not called, and neither has he.',
        'I like this report, and she likes it too.',
        'We need a plan, and they need one too.',
        'He will join, and I will too.',
        'She did not complain, and neither did they.',
        'The client agreed, and so did the manager.',
        'I can help, and my team can too.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('ellipsis-substitution', lines)

    # pronoun-agreement
    lines = []
    for p in [
        'Everyone must bring their badge.',
        'Each student must submit their report.',
        'The team has updated its policy.',
        'The company changed its logo.',
        'Every employee receives their schedule.',
        'Nobody should leave their desk unlocked.',
        'The staff members updated their profiles.',
        'Each manager reviewed their budget.',
        'The client sent their feedback.',
        'The committee published its findings.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('pronoun-agreement', lines)

    # collective-nouns
    lines = []
    for p in [
        'The team is working on the project.',
        'The staff are attending the training.',
        'The police are investigating the incident.',
        'The family is moving to a new house.',
        'The committee has approved the plan.',
        'The audience was very quiet.',
        'The company is hiring new staff.',
        'The government has announced a new policy.',
        'The group is meeting at noon.',
        'The class has finished the lesson.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('collective-nouns', lines)

    # reporting-verbs
    lines = []
    for p in [
        'She admitted making a mistake.',
        'He denied taking the file.',
        'She suggested taking a break.',
        'He offered to help the team.',
        'She promised to send the report.',
        'He refused to sign the contract.',
        'She agreed to lead the project.',
        'He warned us about the delay.',
        'She reminded me to call the client.',
        'He complained about the noise.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('reporting-verbs', lines)

    # fronting-extraposition
    lines = []
    for p in [
        'What we need is a clear plan.',
        'It is important that everyone attends.',
        'On the desk sat a large report.',
        'It was the manager who approved the plan.',
        'What she wants is more time.',
        'It is clear that the policy works.',
        'Under the table lay a missing file.',
        'It seems that the client has agreed.',
        'What matters is the quality of the report.',
        'It is likely that sales will increase.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('fronting-extraposition', lines)

    # punctuation
    lines = []
    for p in [
        'The report was clear; however, it was long.',
        'She brought three things: a laptop, a notebook, and a pen.',
        'The manager, who joined last year, leads the team.',
        'It is a well-written report.',
        'The client\'s feedback was useful.',
        'He said, "The report is ready."',
        'The plan is simple: reduce costs and improve quality.',
        'We need two things: time and money.',
        'The meeting was short, but productive.',
        'The staff worked late; the client was pleased.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('punctuation', lines)

    # vietnamese learner errors (corrected forms)
    lines = []
    for p in [
        'She has lived here for three years.',
        'He does not like coffee.',
        'They are working on the project.',
        'I have finished the report.',
        'She is responsible for the budget.',
        'The information is useful.',
        'He gave me a useful advice.',
        'We discussed the problem yesterday.',
        'She is good at solving problems.',
        'The meeting will start at 9 a.m.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('vietnamese-learner-errors', lines)

    # both/either/neither
    lines = []
    for p in [
        'Both the manager and the staff agreed.',
        'Either the client or the supplier will call.',
        'Neither the manager nor the staff was available.',
        'Both reports are accurate.',
        'Either option is acceptable.',
        'Neither option is ideal.',
        'Both the team and the client were satisfied.',
        'Either you or I will attend.',
        'Neither the invoice nor the receipt was sent.',
        'Both the plan and the budget need review.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('both-either-neither', lines)

    # other/another
    lines = []
    for p in [
        'I need another report.',
        'The other report is on the desk.',
        'Other reports are available online.',
        'Some reports are ready; others are not.',
        'The other managers have agreed.',
        'Another client called this morning.',
        'We reviewed two reports; the other one was shorter.',
        'Some staff left; the others stayed.',
        'I have another meeting at noon.',
        'The other option is cheaper.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('other-another', lines)

    # indefinite pronouns
    lines = []
    for p in [
        'Everyone is ready for the meeting.',
        'Somebody left a package at reception.',
        'Nobody knows the answer.',
        'Everything is ready.',
        'Anyone can join the training.',
        'Something went wrong with the system.',
        'Nothing was lost.',
        'Someone called while you were out.',
        'Everybody received the email.',
        'Anything is possible if we plan carefully.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('indefinite-pronouns', lines)

    # reciprocal pronouns
    lines = []
    for p in [
        'The two managers called each other.',
        'The team members helped one another.',
        'They sent each other the reports.',
        'The clients contacted one another.',
        'The two departments support each other.',
        'The students encouraged one another.',
        'They respect each other.',
        'The branches share information with one another.',
        'The two suppliers compete with each other.',
        'The colleagues trust one another.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('reciprocal-pronouns', lines)

    # dummy it / there
    lines = []
    for p in [
        'It is important to check the figures.',
        'There is a report on the desk.',
        'There are three clients in the lobby.',
        'It is difficult to finish today.',
        'There was a delay in the shipment.',
        'There have been several complaints.',
        'It seems that the client has agreed.',
        'There will be a meeting tomorrow.',
        'It is clear that the plan works.',
        'There is no time to waste.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('dummy-it-there', lines)

    # as...as
    lines = []
    for p in [
        'This report is as detailed as the previous one.',
        'The new system is as fast as the old one.',
        'She is not as experienced as the manager.',
        'The office is twice as large as the old one.',
        'This plan is as practical as the first one.',
        'The service is not as reliable as before.',
        'The new laptop is as expensive as the old model.',
        'The meeting was as long as expected.',
        'The client is as satisfied as we hoped.',
        'The team is as ready as ever.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('as-as-comparison', lines)

    # adjective + preposition
    lines = []
    for p in [
        'She is responsible for the budget.',
        'He is interested in the offer.',
        'She is good at solving problems.',
        'He is worried about the deadline.',
        'She is satisfied with the result.',
        'He is famous for his service.',
        'She is ready for the meeting.',
        'He is afraid of making mistakes.',
        'She is proud of the team.',
        'He is disappointed with the service.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('adjective-prepositions', lines)

    # correlative conjunctions
    lines = []
    for p in [
        'She is both efficient and reliable.',
        'He is not only talented but also hardworking.',
        'You can either call or email the client.',
        'Neither the manager nor the staff was available.',
        'Both the plan and the budget need review.',
        'She is not only a manager but also a mentor.',
        'Either you or I will attend the meeting.',
        'The report is both detailed and clear.',
        'He neither called nor sent an email.',
        'The team is both experienced and motivated.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('correlative-conjunctions', lines)

    # discourse markers
    lines = []
    for p in [
        'The plan is expensive; however, it is effective.',
        'Sales increased; therefore, we hired more staff.',
        'The report is clear; moreover, it is detailed.',
        'The service is fast; in addition, it is affordable.',
        'The market is growing; as a result, demand is rising.',
        'The team worked late; nevertheless, the project was completed.',
        'The policy is popular; on the other hand, it needs revision.',
        'The data is limited; in contrast, the findings are clear.',
        'The client complained; consequently, we changed the process.',
        'The training was useful; for example, staff learned new tools.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('discourse-markers', lines)

    # numbers / percentages
    lines = []
    for p in [
        'Two thirds of the staff are satisfied.',
        'Twenty-five percent of the budget was spent.',
        'The majority of clients prefer online service.',
        'A third of the reports were late.',
        'Half of the team works remotely.',
        'The number of complaints increased by ten percent.',
        'Sales rose from 20 to 35 percent.',
        'Three quarters of the office is occupied.',
        'A small number of employees attended.',
        'The figure doubled between 2020 and 2024.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('numbers-percentages', lines)

    # IELTS Task 1
    lines = []
    for p in [
        'The chart shows that sales increased steadily.',
        'The number of visitors rose from 20 to 35 percent.',
        'Sales remained stable throughout the period.',
        'The figure peaked in June before falling slightly.',
        'There was a sharp increase in demand.',
        'The data indicates a gradual decline in costs.',
        'The two figures were almost identical.',
        'The chart compares the performance of three branches.',
        'The percentage of remote workers doubled.',
        'Overall, the trend was upward.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('ielts-task1-structures', lines)

    # IELTS Task 2
    lines = []
    for p in [
        'While some people support the policy, others remain concerned.',
        'Although the plan is expensive, it may be effective.',
        'It is argued that remote work improves productivity.',
        'The benefits of the policy outweigh the costs.',
        'This essay will discuss both sides of the argument.',
        'In conclusion, the policy should be implemented carefully.',
        'One major advantage is the reduction in costs.',
        'A significant disadvantage is the lack of flexibility.',
        'The evidence suggests that further research is needed.',
        'Governments should invest in education and training.',
    ]:
        lines.append(p)
    lines = (lines * 5)
    add_line_bank('ielts-task2-structures', lines)


def main():
    ids = {t['id'] for t in FULL}
    G['topics'] = [t for t in G['topics'] if t['id'] not in ids]
    for tid in ids:
        LEX.get('patterns', {}).pop(tid, None)
    for t in FULL:
        G['topics'].append(t)
    base.TOPICS = {t['id']: t for t in G['topics']}
    build_banks()
    order = ['Thì', 'Động từ', 'Cấu trúc câu', 'Câu nâng cao', 'Từ loại', 'TOEIC & IELTS']
    G['topics'].sort(key=lambda t: order.index(t['cat']) if t['cat'] in order else 99)
    with io.open(PATH, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(G, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('full topics', len(G['topics']))
    print('banks', sum(1 for t in G['topics'] if t.get('gen')))
    print('pattern banks', len(G['lexicon']['patterns']))


if __name__ == '__main__':
    main()
