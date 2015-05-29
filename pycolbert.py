import os
import sys
import subprocess

testP = {
  "2005": [
    {
      "date": "2005-10-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/61f6xj/intro---10-17-05",
        "http://thecolbertreport.cc.com/videos/w9dr6d/first-show",
        "http://thecolbertreport.cc.com/videos/63ite2/the-word---truthiness",
        "http://thecolbertreport.cc.com/videos/2hvbwp/threatdown---bird-flu",
        "http://thecolbertreport.cc.com/videos/ydz3a0/stone-phillips",
        "http://thecolbertreport.cc.com/videos/4ewylv/gravitas-off-with-stone-phillips",
        "http://thecolbertreport.cc.com/videos/e3mrnm/sign-off---commemorating-chewbacca-s-american-citizenship"
      ],
      "guest": "Stone Phillips"
    },
    {
      "date": "2005-10-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u39l6v/intro---10-18-05",
        "http://thecolbertreport.cc.com/videos/kzin67/the-word---bacchanalia",
        "http://thecolbertreport.cc.com/videos/5icgst/all-you-need-to-know---illegal-immigration",
        "http://thecolbertreport.cc.com/videos/fydq17/lesley-stahl",
        "http://thecolbertreport.cc.com/videos/235ftw/better-know-a-district---georgia-s-1st---jack-kingston",
        "http://thecolbertreport.cc.com/videos/joj31r/sign-off---a-fax-from-james-brady"
      ],
      "guest": "Lesley Stahl"
    },
    {
      "date": "2005-10-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vmoc19/intro---10-19-05",
        "http://thecolbertreport.cc.com/videos/gpmykq/the-word---disappointed",
        "http://thecolbertreport.cc.com/videos/95k30i/stephen-settles-the-debate---whales-and-cod-vs--polar-bears-and-seal-hunters",
        "http://thecolbertreport.cc.com/videos/p42ju6/on-notice---bobby-s-candy-apples",
        "http://thecolbertreport.cc.com/videos/malmcz/tip-wag---teen-pregnancy---katie-s-no-lady",
        "http://thecolbertreport.cc.com/videos/db0w9q/fareed-zakaria",
        "http://thecolbertreport.cc.com/videos/8kkcau/sign-off---the-in-box---you-re-great"
      ],
      "guest": "Fareed Zakaria"
    },
    {
      "date": "2005-10-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rwhdnt/intro---10-20-05",
        "http://thecolbertreport.cc.com/videos/p1n8k4/avian-flu",
        "http://thecolbertreport.cc.com/videos/mk7yrx/russ-lieber---candy-and-air",
        "http://thecolbertreport.cc.com/videos/cz3euw/un-american-news---the-foreign-press",
        "http://thecolbertreport.cc.com/videos/j1b7vj/jim-cramer",
        "http://thecolbertreport.cc.com/videos/rohluc/sign-off---credit-cards",
        "http://thecolbertreport.cc.com/videos/24lb41/the-word---love-handles"
      ],
      "guest": "Jim Cramer"
    },
    {
      "date": "2005-10-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/67cs19/intro---10-24-05",
        "http://thecolbertreport.cc.com/videos/gv2cjs/the-word---pussy",
        "http://thecolbertreport.cc.com/videos/i491tt/lou-dobbs",
        "http://thecolbertreport.cc.com/videos/dd1sbx/fract---the-wright-brothers",
        "http://thecolbertreport.cc.com/videos/wtqx4r/bring--em-back-or-leave--em-dead---inquisition",
        "http://thecolbertreport.cc.com/videos/qgvny1/mug-shot",
        "http://thecolbertreport.cc.com/videos/vuftif/against-the-pundocracy"
      ],
      "guest": "Lou Dobbs"
    },
    {
      "date": "2005-10-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lldiq0/intro---10-25-05",
        "http://thecolbertreport.cc.com/videos/whvmzj/benjamin-shalom-bernanke",
        "http://thecolbertreport.cc.com/videos/iqvyat/the-word---overrated",
        "http://thecolbertreport.cc.com/videos/qwe0c7/threatdown---anti-bacterial-soap",
        "http://thecolbertreport.cc.com/videos/7ioxmq/greg-behrendt",
        "http://thecolbertreport.cc.com/videos/nwkm8y/greg-behrendt-fields-calls",
        "http://thecolbertreport.cc.com/videos/vzk1ho/yet-another-day---soup-and-pets"
      ],
      "guest": "Greg Behrendt"
    },
    {
      "date": "2005-10-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nxsljd/intro---10-26-05",
        "http://thecolbertreport.cc.com/videos/39lnsj/outsourcing",
        "http://thecolbertreport.cc.com/videos/7o86ff/the-word---perspective",
        "http://thecolbertreport.cc.com/videos/yuq4bm/neil-degrasse-tyson",
        "http://thecolbertreport.cc.com/videos/5fyjl2/tip-wag---public-nudity-advice",
        "http://thecolbertreport.cc.com/videos/wsfpru/the-pulse"
      ],
      "guest": "Neil deGrasse Tyson"
    },
    {
      "date": "2005-10-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ap807f/intro---10-27-05",
        "http://thecolbertreport.cc.com/videos/nb6dxf/lieber---white-pumpkins",
        "http://thecolbertreport.cc.com/videos/llj5fu/the-word---quitter",
        "http://thecolbertreport.cc.com/videos/1vbs16/bookshelf-of-broken-dreams",
        "http://thecolbertreport.cc.com/videos/ynldrg/fract---the-states",
        "http://thecolbertreport.cc.com/videos/zyop79/better-know-a-district---massachusetts--4th---barney-frank",
        "http://thecolbertreport.cc.com/videos/h9zw2j/jeff-daniels",
        "http://thecolbertreport.cc.com/videos/3eb29d/yet-another-day---checking-in-with-christina-and-ernesto"
      ],
      "guest": "Jeff Daniels"
    },
    {
      "date": "2005-10-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/11fva6/intro---10-31-05",
        "http://thecolbertreport.cc.com/videos/mqoacz/criminal-intent",
        "http://thecolbertreport.cc.com/videos/p3782h/patrick-fitzgerald-s-press-conference",
        "http://thecolbertreport.cc.com/videos/ey4w8s/the-word---alito",
        "http://thecolbertreport.cc.com/videos/jfbl04/monica-crowley",
        "http://thecolbertreport.cc.com/videos/sxj08u/fract---greatest-lakes",
        "http://thecolbertreport.cc.com/videos/5d63df/stephen-settles-the-debate---ramadan-or-halloween-",
        "http://thecolbertreport.cc.com/videos/qc29ld/rocktober"
      ],
      "guest": "Monica Crowley"
    },
    {
      "date": "2005-11-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1zu9d3/intro---11-1-05",
        "http://thecolbertreport.cc.com/videos/r7fmyb/the-word---camilla-mania",
        "http://thecolbertreport.cc.com/videos/ufgobt/emergency-evacuation-plan",
        "http://thecolbertreport.cc.com/videos/b7u1wy/ken-burns",
        "http://thecolbertreport.cc.com/videos/kpjrtm/formidable-opponent---charity"
      ],
      "guest": "Ken Burns"
    },
    {
      "date": "2005-11-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1kskdq/intro---11-2-05",
        "http://thecolbertreport.cc.com/videos/xp1gbs/fatwa",
        "http://thecolbertreport.cc.com/videos/8e6qo8/c-span-coverage",
        "http://thecolbertreport.cc.com/videos/ayw8g9/the-word---cat",
        "http://thecolbertreport.cc.com/videos/ey3oos/fract---civil-war",
        "http://thecolbertreport.cc.com/videos/9438aw/the-war-on-wal-mart",
        "http://thecolbertreport.cc.com/videos/nvopei/bruce-feiler",
        "http://thecolbertreport.cc.com/videos/6v0azb/lieber---one-testicle"
      ],
      "guest": "Bruce Feiler"
    },
    {
      "date": "2005-11-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4g6fdp/intro---11-3-05",
        "http://thecolbertreport.cc.com/videos/9lmjfq/the-word---shhhh----",
        "http://thecolbertreport.cc.com/videos/tq3k8n/bradley-whitford",
        "http://thecolbertreport.cc.com/videos/wwof8g/fract---karl-marx",
        "http://thecolbertreport.cc.com/videos/cxtvxm/better-know-a-district---ohio-s-11th---stephanie-tubbs-jones",
        "http://thecolbertreport.cc.com/videos/86juj9/judge-tubbs",
        "http://thecolbertreport.cc.com/videos/mkig56/the-in-box---kicking-ass"
      ],
      "guest": "Bradley Whitford"
    },
    {
      "date": "2005-11-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lbtbtl/intro---11-7-05",
        "http://thecolbertreport.cc.com/videos/s0yn8n/rioting-do-s-and-don-ts",
        "http://thecolbertreport.cc.com/videos/2iezg1/the-word---hoser",
        "http://thecolbertreport.cc.com/videos/dzis1b/fract---frnap--the-freedom-snap",
        "http://thecolbertreport.cc.com/videos/1xhewi/threatdown---pirates",
        "http://thecolbertreport.cc.com/videos/fjfr4z/eliot-spitzer",
        "http://thecolbertreport.cc.com/videos/ufqqpc/rock--em-sock--em-robots"
      ],
      "guest": "Eliot Spitzer"
    },
    {
      "date": "2005-11-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2lgs12/intro---11-8-05",
        "http://thecolbertreport.cc.com/videos/5lxdom/america-doesn-t-torture",
        "http://thecolbertreport.cc.com/videos/xul3qa/intercepted-satellite-feed",
        "http://thecolbertreport.cc.com/videos/huzs1z/the-word---t-o-",
        "http://thecolbertreport.cc.com/videos/7nl1pw/fract---franagram--american-patriot",
        "http://thecolbertreport.cc.com/videos/wgvsjo/tip-wag---convicted-murderers",
        "http://thecolbertreport.cc.com/videos/0l19is/catherine-crier",
        "http://thecolbertreport.cc.com/videos/6zdr9d/wilford-brimley-calls---cocoon",
        "http://thecolbertreport.cc.com/videos/ykxirt/yet-another-day---flesh-eating-virus"
      ],
      "guest": "Catherine Crier"
    },
    {
      "date": "2005-11-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s6miz8/intro---11-9-05",
        "http://thecolbertreport.cc.com/videos/5fvmyv/next-question",
        "http://thecolbertreport.cc.com/videos/bcmkct/the-word---willy-loman",
        "http://thecolbertreport.cc.com/videos/43es16/all-you-need-to-know---kansas-education",
        "http://thecolbertreport.cc.com/videos/nzfogn/mary-roach",
        "http://thecolbertreport.cc.com/videos/gqeqrk/better-know-a-district---florida-s-7th---john-mica"
      ],
      "guest": "Mary Roach"
    },
    {
      "date": "2005-11-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jqfk3o/intro---11-10-05",
        "http://thecolbertreport.cc.com/videos/8c7dra/swear-to-god",
        "http://thecolbertreport.cc.com/videos/9kcrqk/the-word---armistice",
        "http://thecolbertreport.cc.com/videos/o63fqi/cokie-roberts",
        "http://thecolbertreport.cc.com/videos/bd1uuq/the-in-box---asian-stereotypes",
        "http://thecolbertreport.cc.com/videos/c0bksd/the-dacolbert-code---samuel-alito"
      ],
      "guest": "Cokie Roberts"
    },
    {
      "date": "2005-11-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e5zymg/intro---11-14-05",
        "http://thecolbertreport.cc.com/videos/gfzikt/cma-buzz",
        "http://thecolbertreport.cc.com/videos/jaukv1/the-word---testosterone",
        "http://thecolbertreport.cc.com/videos/oel1ef/bob-kerrey",
        "http://thecolbertreport.cc.com/videos/2lpp85/tip-line---flag-sticker",
        "http://thecolbertreport.cc.com/videos/1wb4cs/un-american-news---shame-cotton",
        "http://thecolbertreport.cc.com/videos/kuqe6u/internets-anniversary"
      ],
      "guest": "Sen. Bob Kerrey"
    },
    {
      "date": "2005-11-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c8h749/intro---11-15-05",
        "http://thecolbertreport.cc.com/videos/9jy462/sayako-s-wedding",
        "http://thecolbertreport.cc.com/videos/yctr24/the-word---the-orient",
        "http://thecolbertreport.cc.com/videos/4z4p4o/bring--em-back-or-leave--em-dead---asian-history",
        "http://thecolbertreport.cc.com/videos/94g5r1/al-sharpton",
        "http://thecolbertreport.cc.com/videos/9disf3/fract---mt--rushmore",
        "http://thecolbertreport.cc.com/videos/w11pi7/formidable-opponent---torture"
      ],
      "guest": "Rev. Al Sharpton"
    },
    {
      "date": "2005-11-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nl3o0c/intro---11-16-05",
        "http://thecolbertreport.cc.com/videos/ebxyv5/the-word---information",
        "http://thecolbertreport.cc.com/videos/eh69qj/on-notice-dead-to-me---juan-gabriel",
        "http://thecolbertreport.cc.com/videos/h1e498/better-know-a-district---colorado-s-2nd---mark-udall",
        "http://thecolbertreport.cc.com/videos/ddef4x/matt-taibbi",
        "http://thecolbertreport.cc.com/videos/4kvhir/america--sleep-safe"
      ],
      "guest": "Matt Taibbi"
    },
    {
      "date": "2005-11-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zl8rtq/intro---11-17-05",
        "http://thecolbertreport.cc.com/videos/f8fusi/no-good-deed",
        "http://thecolbertreport.cc.com/videos/pxeto4/the-word---mcconaughey-",
        "http://thecolbertreport.cc.com/videos/bypiaq/threatdown---children",
        "http://thecolbertreport.cc.com/videos/smm3x9/tim-robbins",
        "http://thecolbertreport.cc.com/videos/wk6dps/here-today--more-tomorrow",
        "http://thecolbertreport.cc.com/videos/8sxlv8/thanksgiving-vacation"
      ],
      "guest": "Tim Robbins"
    },
    {
      "date": "2005-11-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sf87bf/intro---11-28-05",
        "http://thecolbertreport.cc.com/videos/nrf3km/cyber-monday",
        "http://thecolbertreport.cc.com/videos/sqsdz6/the-word---never",
        "http://thecolbertreport.cc.com/videos/r6xqra/viewer-phone-calls",
        "http://thecolbertreport.cc.com/videos/vdncvg/stephen-settles-the-debate---science-vs--faith",
        "http://thecolbertreport.cc.com/videos/507rw4/brian-greene",
        "http://thecolbertreport.cc.com/videos/ngo5nh/sign-off---check-your-local-listings"
      ],
      "guest": "Brian Greene"
    },
    {
      "date": "2005-11-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4yku0o/intro---11-29-05",
        "http://thecolbertreport.cc.com/videos/zaot6p/better-know-a-district---california-s-50th---randy--duke--cunningham",
        "http://thecolbertreport.cc.com/videos/o2kdz0/the-word---confidence",
        "http://thecolbertreport.cc.com/videos/6f1i25/was-it-really-that-bad----black-death",
        "http://thecolbertreport.cc.com/videos/75dr62/the--duke-s--things",
        "http://thecolbertreport.cc.com/videos/rtbpes/richard-preston"
      ],
      "guest": "Richard Preston"
    },
    {
      "date": "2005-11-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/951mir/intro---11-30-05",
        "http://thecolbertreport.cc.com/videos/jsl09o/the-word---gay-gay-gay-gay-gay",
        "http://thecolbertreport.cc.com/videos/h7okp1/fract---nobody-messes-with-house",
        "http://thecolbertreport.cc.com/videos/ut6y25/katrina-vanden-heuvel",
        "http://thecolbertreport.cc.com/videos/0frx2n/around-the-world-in-11-6-seconds---media"
      ],
      "guest": "Katrina Vanden Heuvel"
    },
    {
      "date": "2005-12-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j4tan3/intro---12-1-05",
        "http://thecolbertreport.cc.com/videos/bocj8y/giant-gold-washer",
        "http://thecolbertreport.cc.com/videos/w4dblj/the-word---spectacle",
        "http://thecolbertreport.cc.com/videos/3yvygm/tip-wag---seattle",
        "http://thecolbertreport.cc.com/videos/idpn3b/richard-clarke",
        "http://thecolbertreport.cc.com/videos/9icneu/face-transplant"
      ],
      "guest": "Richard Clarke"
    },
    {
      "date": "2005-12-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0yxnmj/intro---12-5-05",
        "http://thecolbertreport.cc.com/videos/utqsnp/kennedy-center-honors",
        "http://thecolbertreport.cc.com/videos/278dqm/the-word---xmas",
        "http://thecolbertreport.cc.com/videos/6ulwwh/apology",
        "http://thecolbertreport.cc.com/videos/sg4wi3/this-week-in-history---december-4th-10th",
        "http://thecolbertreport.cc.com/videos/p01a0h/colbert-nation-citizen-award",
        "http://thecolbertreport.cc.com/videos/djl273/maureen-dowd"
      ],
      "guest": "Maureen Dowd"
    },
    {
      "date": "2005-12-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ad0e3u/intro---12-6-05",
        "http://thecolbertreport.cc.com/videos/l23e5t/the-word---backsies",
        "http://thecolbertreport.cc.com/videos/c6b939/better-know-a-district---virginia-s-8th---jim-moran",
        "http://thecolbertreport.cc.com/videos/bgq83k/fract---the-star-spangled-banner",
        "http://thecolbertreport.cc.com/videos/mjqiqk/anderson-cooper",
        "http://thecolbertreport.cc.com/videos/jo01oi/season-of-giving"
      ],
      "guest": "Anderson Cooper"
    },
    {
      "date": "2005-12-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uvfu4h/intro---12-7-05",
        "http://thecolbertreport.cc.com/videos/k5nni4/burritos-happy-holidays",
        "http://thecolbertreport.cc.com/videos/rmm1zo/the-word---hell--no-",
        "http://thecolbertreport.cc.com/videos/5ti5hp/threatdown---threats",
        "http://thecolbertreport.cc.com/videos/1buius/craig-crawford"
      ],
      "guest": "Craig Crawford"
    },
    {
      "date": "2005-12-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/muvtpz/intro---12-8-07",
        "http://thecolbertreport.cc.com/videos/zo8qem/the-mallomar",
        "http://thecolbertreport.cc.com/videos/9zltfz/the-word---satisfied-",
        "http://thecolbertreport.cc.com/videos/zc6wzp/papa-bear-nailed-him",
        "http://thecolbertreport.cc.com/videos/0k58ru/movies-that-are-destroying-america---christmas",
        "http://thecolbertreport.cc.com/videos/f63xob/peggy-noonan",
        "http://thecolbertreport.cc.com/videos/huxiwh/nationwide-secret-santa"
      ],
      "guest": "Peggy Noonan"
    },
    {
      "date": "2005-12-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/26ln5h/intro---12-12-05",
        "http://thecolbertreport.cc.com/videos/th38l3/the-real-christmas",
        "http://thecolbertreport.cc.com/videos/xld8bn/the-word---belly-achin-",
        "http://thecolbertreport.cc.com/videos/4qrc6w/un-american-news---tootsie",
        "http://thecolbertreport.cc.com/videos/gljaa1/fract---war",
        "http://thecolbertreport.cc.com/videos/tos96b/harry-smith",
        "http://thecolbertreport.cc.com/videos/onf96q/the-in-box---custom-stamps"
      ],
      "guest": "Harry Smith"
    },
    {
      "date": "2005-12-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hh6w14/intro---12-13-05",
        "http://thecolbertreport.cc.com/videos/f3vpvn/the-de-ballification-of-the-american-sportscape",
        "http://thecolbertreport.cc.com/videos/omscph/the-word---lombardi",
        "http://thecolbertreport.cc.com/videos/53a836/sports-update",
        "http://thecolbertreport.cc.com/videos/reee2h/formidable-opponent---steroids",
        "http://thecolbertreport.cc.com/videos/raw18i/fract---nba",
        "http://thecolbertreport.cc.com/videos/mopfat/bob-costas",
        "http://thecolbertreport.cc.com/videos/97uhmb/sign-off---excellence-in-everything"
      ],
      "guest": "Bob Costas"
    },
    {
      "date": "2005-12-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/irtzij/intro---12-14-05",
        "http://thecolbertreport.cc.com/videos/rxzsfq/king-kong",
        "http://thecolbertreport.cc.com/videos/g7vs24/the-word---travolta",
        "http://thecolbertreport.cc.com/videos/j8pyop/tip-wag---redefining-cruel-and-unusual",
        "http://thecolbertreport.cc.com/videos/po8ta2/dermot-mulroney",
        "http://thecolbertreport.cc.com/videos/nf6l8d/sign-off---three-stockings"
      ],
      "guest": "Dermot Mulroney"
    },
    {
      "date": "2005-12-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/12ie90/intro---12-15-05",
        "http://thecolbertreport.cc.com/videos/7x2gjd/war-on-holiday",
        "http://thecolbertreport.cc.com/videos/1286w8/the-word---jetpack",
        "http://thecolbertreport.cc.com/videos/4epy8c/better-know-a-district---new-york-s-11th---major-owens",
        "http://thecolbertreport.cc.com/videos/gn64jt/mark-cuban",
        "http://thecolbertreport.cc.com/videos/9d08kf/tax-deductions"
      ],
      "guest": "Mark Cuban"
    }
  ],
  "2006": [
    {
      "date": "2006-01-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ccm8j9/intro---1-9-2006",
        "http://thecolbertreport.cc.com/videos/gfhklq/merry-christmas",
        "http://thecolbertreport.cc.com/videos/k2b0t4/going-at-it",
        "http://thecolbertreport.cc.com/videos/tfsnjk/the-lusk-alito-connection",
        "http://thecolbertreport.cc.com/videos/zvszwh/the-word---there-is-no-word",
        "http://thecolbertreport.cc.com/videos/wm808s/tip-wag---addicted-to-cute",
        "http://thecolbertreport.cc.com/videos/fx17nm/fract---columbus",
        "http://thecolbertreport.cc.com/videos/nctzb0/nancy-grace",
        "http://thecolbertreport.cc.com/videos/vt9veh/on-notice-dead-to-me---word-of-the-year"
      ],
      "guest": "Nancy Grace"
    },
    {
      "date": "2006-01-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zffhux/intro---1-10-02",
        "http://thecolbertreport.cc.com/videos/znlsxv/off-notice---the-e-street-band",
        "http://thecolbertreport.cc.com/videos/jz3vjq/the-word---sleeper-cell",
        "http://thecolbertreport.cc.com/videos/fzr3d5/balls-for-kidz---bear-hunting",
        "http://thecolbertreport.cc.com/videos/uk2dty/carl-bernstein",
        "http://thecolbertreport.cc.com/videos/lppcfe/the-in-box---taking-a-bullet"
      ],
      "guest": "Carl Bernstein"
    },
    {
      "date": "2006-01-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yq13d1/intro---1-11-06",
        "http://thecolbertreport.cc.com/videos/kci614/colbert-report-consumer-alert",
        "http://thecolbertreport.cc.com/videos/ho8xgd/alito-haters",
        "http://thecolbertreport.cc.com/videos/vko8sm/the-word---whatever",
        "http://thecolbertreport.cc.com/videos/bbh162/threatdown---fathers-and-sons",
        "http://thecolbertreport.cc.com/videos/o71qa3/fract---colbert-trivia",
        "http://thecolbertreport.cc.com/videos/4z25yz/john-stossel",
        "http://thecolbertreport.cc.com/videos/gsuxni/sign-off---future-money"
      ],
      "guest": "John Stossel"
    },
    {
      "date": "2006-01-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vkw0ea/intro---1-12-06",
        "http://thecolbertreport.cc.com/videos/smz33e/the-oscars",
        "http://thecolbertreport.cc.com/videos/hldbza/the-word---double-stick-tape",
        "http://thecolbertreport.cc.com/videos/ycx56p/better-know-a-district---new-jersey-s-9th---steven-rothman",
        "http://thecolbertreport.cc.com/videos/4huh6w/fract---frnap--monarchy",
        "http://thecolbertreport.cc.com/videos/2qbk3w/kenneth-miller",
        "http://thecolbertreport.cc.com/videos/393ez5/michael-adams--apology"
      ],
      "guest": "Ken Miller"
    },
    {
      "date": "2006-01-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hk33gu/intro---1-16-06",
        "http://thecolbertreport.cc.com/videos/sfiw6u/martin-luther-king-jr--day",
        "http://thecolbertreport.cc.com/videos/a3wcdf/the-word---cerrado-",
        "http://thecolbertreport.cc.com/videos/7te5id/movies-that-are-destroying-america---transamerica",
        "http://thecolbertreport.cc.com/videos/2zgm7q/fract---captain-north-korea",
        "http://thecolbertreport.cc.com/videos/39qjdh/george-stephanopoulos",
        "http://thecolbertreport.cc.com/videos/1jvqfi/sign-off---i-have-a-dreamsicle"
      ],
      "guest": "George Stephanopoulos"
    },
    {
      "date": "2006-01-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/btjtm2/intro---1-17-2006",
        "http://thecolbertreport.cc.com/videos/uhh2bv/the-golden-globes",
        "http://thecolbertreport.cc.com/videos/lqd06o/age-defying-pancakes",
        "http://thecolbertreport.cc.com/videos/pxy8xm/the-word---old-school",
        "http://thecolbertreport.cc.com/videos/3wpryl/tip-wag---eminem",
        "http://thecolbertreport.cc.com/videos/l2yoxp/andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/lpdbmt/wilford-brimley-calls---oatmeal"
      ],
      "guest": "Andrew Sullivan"
    },
    {
      "date": "2006-01-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nh5ji3/intro---1-18-06",
        "http://thecolbertreport.cc.com/videos/z3vrpl/the-de-edumacation-of-the-american-brainscape",
        "http://thecolbertreport.cc.com/videos/ti5lsj/the-word---smarterer",
        "http://thecolbertreport.cc.com/videos/92rf9j/bring--em-back-or-leave--em-dead---teacher-s-edition",
        "http://thecolbertreport.cc.com/videos/rnpcxp/frank-mccourt",
        "http://thecolbertreport.cc.com/videos/86d7fs/sign-off---the-bully-system"
      ],
      "guest": "Frank McCourt"
    },
    {
      "date": "2006-01-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1ibsf9/intro---1-19-06",
        "http://thecolbertreport.cc.com/videos/9s67zo/who-s-attacking-me-now----humane-society",
        "http://thecolbertreport.cc.com/videos/xguuix/the-word---public-see",
        "http://thecolbertreport.cc.com/videos/lidn3n/better-know-a-district---new-york-s-17th---eliot-engel",
        "http://thecolbertreport.cc.com/videos/11mx9e/nina-totenberg",
        "http://thecolbertreport.cc.com/videos/9g8c9i/sign-off---drink-on"
      ],
      "guest": "Nina Totenberg"
    },
    {
      "date": "2006-01-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rnxq1m/intro---1-23-06",
        "http://thecolbertreport.cc.com/videos/k046s8/oprah-s-book-club",
        "http://thecolbertreport.cc.com/videos/ruzjfq/the-word---charlie-daniels",
        "http://thecolbertreport.cc.com/videos/0wj0h7/threatdown---hamas",
        "http://thecolbertreport.cc.com/videos/puj7cw/david-gregory",
        "http://thecolbertreport.cc.com/videos/ipkxy5/dr--love"
      ],
      "guest": "David Gregory"
    },
    {
      "date": "2006-01-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4cxurq/intro---1-24-06",
        "http://thecolbertreport.cc.com/videos/63ywy8/most-depressing-day-of-the-year",
        "http://thecolbertreport.cc.com/videos/xpxm3x/the-word---chernobyl",
        "http://thecolbertreport.cc.com/videos/bpx4o0/formidable-opponent---superpowers",
        "http://thecolbertreport.cc.com/videos/44x8vn/robin-givhan",
        "http://thecolbertreport.cc.com/videos/meshre/the-in-box---dvds"
      ],
      "guest": "Robin Givhan"
    },
    {
      "date": "2006-01-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fcwdw2/intro---1-25-06",
        "http://thecolbertreport.cc.com/videos/sc546i/bill-o-reilly--fan-of-the-show",
        "http://thecolbertreport.cc.com/videos/dg5r31/the-word---remote-control",
        "http://thecolbertreport.cc.com/videos/d7q9f6/better-know-a-district---new-jersey-s-8th---bill-pascrell",
        "http://thecolbertreport.cc.com/videos/e7x760/norah-vincent"
      ],
      "guest": "Norah Vincent"
    },
    {
      "date": "2006-01-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lquo7k/intro---1-26-06",
        "http://thecolbertreport.cc.com/videos/xh484k/thundersnow",
        "http://thecolbertreport.cc.com/videos/qdqpdn/who-s-attacking-me-now----marina-core",
        "http://thecolbertreport.cc.com/videos/9v3sqy/the-word---wham-o",
        "http://thecolbertreport.cc.com/videos/qnlt2s/one-of-the-heroes--lily-s-",
        "http://thecolbertreport.cc.com/videos/lca5rm/colbert-cruise---write-off",
        "http://thecolbertreport.cc.com/videos/gimvpm/paul-begala"
      ],
      "guest": "Paul Begala"
    },
    {
      "date": "2006-01-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fhkpsg/intro---1-30-06",
        "http://thecolbertreport.cc.com/videos/vbdym4/james-frey-s-truthiness",
        "http://thecolbertreport.cc.com/videos/e6nijq/the-word---abortion",
        "http://thecolbertreport.cc.com/videos/5se9xj/tip-wag---google",
        "http://thecolbertreport.cc.com/videos/3f4m4d/annie-duke"
      ],
      "guest": "Annie Duke"
    },
    {
      "date": "2006-01-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2cxabn/intro---1-31-06",
        "http://thecolbertreport.cc.com/videos/d5gebw/the-word---jesi",
        "http://thecolbertreport.cc.com/videos/fo1pme/all-you-need-to-know---samuel-alito",
        "http://thecolbertreport.cc.com/videos/165jzf/fract---the-american-flag",
        "http://thecolbertreport.cc.com/videos/2uduhl/david-maresh",
        "http://thecolbertreport.cc.com/videos/iddejj/sign-off---god-bless",
        "http://thecolbertreport.cc.com/videos/2na088/craziest-f--king-thing-i-ve-ever-heard---snake-and-hamster"
      ],
      "guest": "Dave Marash"
    },
    {
      "date": "2006-02-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dk9yev/intro---2-1-06",
        "http://thecolbertreport.cc.com/videos/y6qr8t/the-american-worker--a-hero-s-salute-to-the-besieged-heroes-of-the-american-jobscape",
        "http://thecolbertreport.cc.com/videos/u7tnek/the-word---you-re-welcome",
        "http://thecolbertreport.cc.com/videos/zfo99j/lieber---minimum-wage",
        "http://thecolbertreport.cc.com/videos/qm6xwf/emily-yoffe",
        "http://thecolbertreport.cc.com/videos/359g3f/sign-off---blue-collar-workday"
      ],
      "guest": "Emily Yoffe"
    },
    {
      "date": "2006-02-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1dag2u/intro---2-2-06",
        "http://thecolbertreport.cc.com/videos/ad4eb4/groundhog-day-forecast",
        "http://thecolbertreport.cc.com/videos/3bftnm/stephen-s-famous-five-meat-chili",
        "http://thecolbertreport.cc.com/videos/xbb82c/the-word---aggravated-assault",
        "http://thecolbertreport.cc.com/videos/lggm23/better-know-a-district---new-york-s-8th---jerrold-nadler",
        "http://thecolbertreport.cc.com/videos/waxwaq/christine-todd-whitman",
        "http://thecolbertreport.cc.com/videos/1q178e/sign-off---tivo"
      ],
      "guest": "Gov. Christine Todd Whitman"
    },
    {
      "date": "2006-02-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dpnfel/intro---2-6-06",
        "http://thecolbertreport.cc.com/videos/x1tmbw/birth-day-off",
        "http://thecolbertreport.cc.com/videos/1gk1h5/the-golden-corner",
        "http://thecolbertreport.cc.com/videos/r9ih4w/the-word---metaphorically",
        "http://thecolbertreport.cc.com/videos/4xxw86/threatdown---killer-bees",
        "http://thecolbertreport.cc.com/videos/kckjlf/fract---native-american-state-names",
        "http://thecolbertreport.cc.com/videos/lynt84/barbara-boxer",
        "http://thecolbertreport.cc.com/videos/xaj1wb/to-be-continued"
      ],
      "guest": "Barbara Boxer"
    },
    {
      "date": "2006-02-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/aa2a90/intro---2-7-06",
        "http://thecolbertreport.cc.com/videos/nzdokc/math-is-hard",
        "http://thecolbertreport.cc.com/videos/iwl7g4/the-word---kidding",
        "http://thecolbertreport.cc.com/videos/pc9syn/fract---frnap--royalty",
        "http://thecolbertreport.cc.com/videos/uvx8kk/james-woolsey",
        "http://thecolbertreport.cc.com/videos/xx0m7n/western-union"
      ],
      "guest": "R. James Woolsey"
    },
    {
      "date": "2006-02-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3vblh5/intro---2-8-06",
        "http://thecolbertreport.cc.com/videos/zmpne2/b-b-b-l-t-",
        "http://thecolbertreport.cc.com/videos/0qolhd/electronic-surveillance",
        "http://thecolbertreport.cc.com/videos/pi8m0r/the-word---eureka",
        "http://thecolbertreport.cc.com/videos/29usyw/better-know-a-district---pennsylvania-s-2nd---chaka-fattah",
        "http://thecolbertreport.cc.com/videos/flyja7/fract---bush-s-height",
        "http://thecolbertreport.cc.com/videos/6jmw8z/alan-dershowitz",
        "http://thecolbertreport.cc.com/videos/96mt5f/the-in-box---terry"
      ],
      "guest": "Alan Dershowitz"
    },
    {
      "date": "2006-02-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/afiwhq/intro---2-9-06",
        "http://thecolbertreport.cc.com/videos/qryfzw/big-brass-balls-award",
        "http://thecolbertreport.cc.com/videos/c00cpa/the-word---u-s-a---u-s-a--",
        "http://thecolbertreport.cc.com/videos/wpi1k4/stephen-s-laws-of-love",
        "http://thecolbertreport.cc.com/videos/8rwy8k/george-packer",
        "http://thecolbertreport.cc.com/videos/33a8tw/charlene--i-m-right-behind-you-"
      ],
      "guest": "George Packer"
    },
    {
      "date": "2006-02-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z5opi6/intro---2-21-06",
        "http://thecolbertreport.cc.com/videos/uo23hp/accidental-shooting",
        "http://thecolbertreport.cc.com/videos/loo817/the-word---u-s-a---u-s-a--",
        "http://thecolbertreport.cc.com/videos/u7vgjy/better-know-a-district---new-jersey-s-13th",
        "http://thecolbertreport.cc.com/videos/gb5q2m/fract---americana",
        "http://thecolbertreport.cc.com/videos/zyrf0h/lama-surya-das",
        "http://thecolbertreport.cc.com/videos/501uix/sign-off---dna"
      ],
      "guest": "Lama Surya Das"
    },
    {
      "date": "2006-02-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i0btk9/intro---2-22-06",
        "http://thecolbertreport.cc.com/videos/9a1fo6/speed-skating-debacle",
        "http://thecolbertreport.cc.com/videos/0g837q/the-word---absolutely-maybe",
        "http://thecolbertreport.cc.com/videos/mvtu98/threatdown---gay-adoption",
        "http://thecolbertreport.cc.com/videos/jkkvih/michael-eric-dyson"
      ],
      "guest": "Michael Eric Dyson"
    },
    {
      "date": "2006-02-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v60d4d/intro---2-23-06",
        "http://thecolbertreport.cc.com/videos/rr6syc/threatdown---bears",
        "http://thecolbertreport.cc.com/videos/754igf/presidential-visions",
        "http://thecolbertreport.cc.com/videos/s0zne3/the-word---hippocratical",
        "http://thecolbertreport.cc.com/videos/kftjaw/pharmaceuticals--prescription-for-progress",
        "http://thecolbertreport.cc.com/videos/rsogzl/david-brooks",
        "http://thecolbertreport.cc.com/videos/azjwel/sign-off---pause-your-tvs"
      ],
      "guest": "David Brooks"
    },
    {
      "date": "2006-02-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/te5not/intro---2-27-06",
        "http://thecolbertreport.cc.com/videos/a6q20s/the-de-deification-of-the-american-faithscape",
        "http://thecolbertreport.cc.com/videos/opnyg5/who-hates-whom-in-the-name-of-god",
        "http://thecolbertreport.cc.com/videos/2hdt17/the-word---trial-separation",
        "http://thecolbertreport.cc.com/videos/5ggers/pick-your-apocalypse",
        "http://thecolbertreport.cc.com/videos/oop06i/tony-campolo",
        "http://thecolbertreport.cc.com/videos/14uaa2/confess-your-sins-to-stephen"
      ],
      "guest": "Tony Campolo"
    },
    {
      "date": "2006-02-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cebyqr/intro---2-28-06",
        "http://thecolbertreport.cc.com/videos/roej3y/who-s-attacking-me-now----anderson-cooper",
        "http://thecolbertreport.cc.com/videos/bdairu/the-word---laissez-les-bons-temps-rouler-",
        "http://thecolbertreport.cc.com/videos/2v3htj/tip-wag---wheeled-transportation",
        "http://thecolbertreport.cc.com/videos/sz96fe/brett-o-donnell"
      ],
      "guest": "Brett O'Donnell"
    },
    {
      "date": "2006-03-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ldd32b/intro---3-1-06",
        "http://thecolbertreport.cc.com/videos/jndc1b/better-know-a-district---california-s-50th",
        "http://thecolbertreport.cc.com/videos/4j8lfp/the-word---faith",
        "http://thecolbertreport.cc.com/videos/1bozfl/better-know-a-founder---benjamin-franklin",
        "http://thecolbertreport.cc.com/videos/11m5ii/arianna-huffington"
      ],
      "guest": "Arianna Huffington"
    },
    {
      "date": "2006-03-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ubq51o/intro---3-2-06",
        "http://thecolbertreport.cc.com/videos/stez1k/the-word---homo-sapien-agenda",
        "http://thecolbertreport.cc.com/videos/3k2tf6/the-dacolbert-code---the-oscars",
        "http://thecolbertreport.cc.com/videos/gltobj/jeffrey-sachs",
        "http://thecolbertreport.cc.com/videos/wx4nw0/sign-off---end-of-an-era"
      ],
      "guest": "Jeffrey Sachs"
    },
    {
      "date": "2006-03-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/404ffy/intro---3-6-06",
        "http://thecolbertreport.cc.com/videos/l42kmx/hollywood-decontamination",
        "http://thecolbertreport.cc.com/videos/tsfsdu/never-say-die",
        "http://thecolbertreport.cc.com/videos/5tdn6m/the-word---spoiler-alert-",
        "http://thecolbertreport.cc.com/videos/tua61a/threatdown---non-blondes",
        "http://thecolbertreport.cc.com/videos/rlta2z/bob-schieffer",
        "http://thecolbertreport.cc.com/videos/iwpji5/sign-off---narnia"
      ],
      "guest": "Bob Schieffer"
    },
    {
      "date": "2006-03-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ca0riz/intro---3-7-06",
        "http://thecolbertreport.cc.com/videos/4cutks/colbert-manor",
        "http://thecolbertreport.cc.com/videos/mtcb44/the-word---the-long-war",
        "http://thecolbertreport.cc.com/videos/g0hyvn/all-you-need-to-know---video-games",
        "http://thecolbertreport.cc.com/videos/8n27zq/norman-ornstein"
      ],
      "guest": "Norman Ornstean"
    },
    {
      "date": "2006-03-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xbwofw/intro---3-8-06",
        "http://thecolbertreport.cc.com/videos/x1smyo/colbert-manor-revisited",
        "http://thecolbertreport.cc.com/videos/to3c41/the-word---monopoly",
        "http://thecolbertreport.cc.com/videos/qhlrjh/stephen-s-sound-advice---civil-war-do-s---don-ts",
        "http://thecolbertreport.cc.com/videos/1ggda8/fract---america-rocks",
        "http://thecolbertreport.cc.com/videos/ovaery/james-webb",
        "http://thecolbertreport.cc.com/videos/vggdk5/used-flag-offer"
      ],
      "guest": "James Webb"
    },
    {
      "date": "2006-03-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vaflyt/intro---3-9-06",
        "http://thecolbertreport.cc.com/videos/dx0yti/canadian-baseball-",
        "http://thecolbertreport.cc.com/videos/6l67tv/the-word---d-i-y-",
        "http://thecolbertreport.cc.com/videos/7oy8db/better-know-a-district---california-s-39th-district---linda-sanchez",
        "http://thecolbertreport.cc.com/videos/15d41c/lorraine-bracco"
      ],
      "guest": "Lorraine Bracco"
    },
    {
      "date": "2006-03-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d7ebhg/intro---3-13-06",
        "http://thecolbertreport.cc.com/videos/lmy7oh/predictions",
        "http://thecolbertreport.cc.com/videos/lykn1c/not-gay",
        "http://thecolbertreport.cc.com/videos/so8v2i/the-word---sidney-poitier",
        "http://thecolbertreport.cc.com/videos/ufh2rw/christopher-buckley",
        "http://thecolbertreport.cc.com/videos/k79bmy/sign-off---mad-magazine"
      ],
      "guest": "Christopher Buckley"
    },
    {
      "date": "2006-03-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9rlemm/intro---3-14-06",
        "http://thecolbertreport.cc.com/videos/i3ouk4/trusting-the-media",
        "http://thecolbertreport.cc.com/videos/i5bwzw/the-word---scapegoat",
        "http://thecolbertreport.cc.com/videos/kiwto1/was-it-really-that-bad----before-unions",
        "http://thecolbertreport.cc.com/videos/402x36/fract---hawaii",
        "http://thecolbertreport.cc.com/videos/loh9en/keith-olbermann",
        "http://thecolbertreport.cc.com/videos/8vssl2/hiphopketball-ii--the-rejazzebration-remix--06"
      ],
      "guest": "Keith Olbermann"
    },
    {
      "date": "2006-03-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wt5xpw/intro---3-15-06",
        "http://thecolbertreport.cc.com/videos/u8eaqc/sperm-donor",
        "http://thecolbertreport.cc.com/videos/g4bu6e/the-word---none-of-the-above",
        "http://thecolbertreport.cc.com/videos/kruphn/al-franken",
        "http://thecolbertreport.cc.com/videos/usnoo7/al-franken-fields-calls",
        "http://thecolbertreport.cc.com/videos/z5ir97/craziest-f--king-thing-i-ve-ever-heard---bear-wrestling"
      ],
      "guest": "Al Franken"
    },
    {
      "date": "2006-03-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yna7fv/intro---3-16-06",
        "http://thecolbertreport.cc.com/videos/ecjm4u/who-s-attacking-me-now----commander-coconut",
        "http://thecolbertreport.cc.com/videos/2m2cs5/the-word---sweet-dreams",
        "http://thecolbertreport.cc.com/videos/kgsuha/better-know-a-protectorate---the-virgin-islands---donna-christensen",
        "http://thecolbertreport.cc.com/videos/6o7ym9/frank-vincent",
        "http://thecolbertreport.cc.com/videos/cycayo/sign-off---i-ll-miss-you"
      ],
      "guest": "Frank Vincent"
    },
    {
      "date": "2006-03-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nnadg0/intro---3-20-06",
        "http://thecolbertreport.cc.com/videos/isowuv/movies-that-are-destroying-america---post-oscar-wrap-up",
        "http://thecolbertreport.cc.com/videos/vr4vvt/connie-chung",
        "http://thecolbertreport.cc.com/videos/yuth1j/jessica-simpson-turns-down-gop",
        "http://thecolbertreport.cc.com/videos/6xoiww/war-in-iraq---third-anniversary",
        "http://thecolbertreport.cc.com/videos/b7697r/the-word---stop-it"
      ],
      "guest": "Connie Chung"
    },
    {
      "date": "2006-03-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xvs8w8/intro---3-21-06",
        "http://thecolbertreport.cc.com/videos/zze24r/world-baseball-classic",
        "http://thecolbertreport.cc.com/videos/teon93/the-word---eat-it",
        "http://thecolbertreport.cc.com/videos/eh7h1y/employee-performance-reviews",
        "http://thecolbertreport.cc.com/videos/nbiu6f/steve-kroft",
        "http://thecolbertreport.cc.com/videos/jt1thw/the-in-box---corrections"
      ],
      "guest": "Steve Kroft"
    },
    {
      "date": "2006-03-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/70ntar/intro---3-22-06",
        "http://thecolbertreport.cc.com/videos/nw6pi6/advice-for-jennifer-anniston",
        "http://thecolbertreport.cc.com/videos/gx67le/better-know-a-district---california-s-27th---brad-sherman",
        "http://thecolbertreport.cc.com/videos/c3fb4g/the-word---i-am-the-great-and-powerful-oz",
        "http://thecolbertreport.cc.com/videos/uqd7r1/dan-senor",
        "http://thecolbertreport.cc.com/videos/qay3pj/sign-off---thank-you--america"
      ],
      "guest": "Dan Senor"
    },
    {
      "date": "2006-03-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ou0ql7/intro---3-23-06",
        "http://thecolbertreport.cc.com/videos/rxxsf1/home--hearth--heart-and-heartland---this-land-is-your-land",
        "http://thecolbertreport.cc.com/videos/1q0pl8/miss-manners",
        "http://thecolbertreport.cc.com/videos/jeurtc/stephen-s-sound-advice---how-to-raise-a-hero",
        "http://thecolbertreport.cc.com/videos/3x5mhp/john-kasich",
        "http://thecolbertreport.cc.com/videos/tgvvyb/sign-off---the-reason-for-the-hearth"
      ],
      "guest": "John Kasich"
    },
    {
      "date": "2006-03-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yvu55b/intro---3-27-06",
        "http://thecolbertreport.cc.com/videos/lu2x91/off-the-market",
        "http://thecolbertreport.cc.com/videos/b1jlbx/immigration-protests",
        "http://thecolbertreport.cc.com/videos/hizymr/exercise-routine",
        "http://thecolbertreport.cc.com/videos/fafxll/the-word---tense",
        "http://thecolbertreport.cc.com/videos/jmwqn6/letter-to-the-judge",
        "http://thecolbertreport.cc.com/videos/6zqqyf/threatdown---drug-candy",
        "http://thecolbertreport.cc.com/videos/hx3fbe/fract---bald-eagle",
        "http://thecolbertreport.cc.com/videos/i44o34/gary-hart",
        "http://thecolbertreport.cc.com/videos/bwhjyd/sign-off---tomorrow-s-guest"
      ],
      "guest": "Gary Hart"
    },
    {
      "date": "2006-03-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9tw416/intro---3-28-06",
        "http://thecolbertreport.cc.com/videos/wm4vs8/baby-eagle",
        "http://thecolbertreport.cc.com/videos/4s1h3q/the-word---easter-under-attack---marketing",
        "http://thecolbertreport.cc.com/videos/erxj6i/lieber---school-vouchers",
        "http://thecolbertreport.cc.com/videos/3ejtt4/fract---commemorative-spoons",
        "http://thecolbertreport.cc.com/videos/tyfnef/michael-brown",
        "http://thecolbertreport.cc.com/videos/t4qaaf/sign-off---goodnight--stephen-jr-"
      ],
      "guest": "Michael Brown"
    },
    {
      "date": "2006-03-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4mdlim/intro---3-29-06",
        "http://thecolbertreport.cc.com/videos/r9z4ro/eclipse",
        "http://thecolbertreport.cc.com/videos/mqt5m8/the-word---merrier",
        "http://thecolbertreport.cc.com/videos/3xpeh4/better-know-a-district---california-s-29th---adam-schiff",
        "http://thecolbertreport.cc.com/videos/k1c0hq/bruce-bartlett"
      ],
      "guest": "Bruce Bartlett"
    },
    {
      "date": "2006-03-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uaktnl/intro---3-30-06",
        "http://thecolbertreport.cc.com/videos/89u375/what-jill-carroll-missed",
        "http://thecolbertreport.cc.com/videos/nuwaus/women-s-history-month---soledad-o-brien",
        "http://thecolbertreport.cc.com/videos/smbaky/tip-wag---the-templeton-prize",
        "http://thecolbertreport.cc.com/videos/n7sm3g/fract---drug-testing-standards",
        "http://thecolbertreport.cc.com/videos/b95nrh/robert-greenwald",
        "http://thecolbertreport.cc.com/videos/0vbmc1/million-man-march",
        "http://thecolbertreport.cc.com/videos/zcqswd/the-word---f--k"
      ],
      "guest": "Robert Greenwald"
    },
    {
      "date": "2006-04-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r2tcqv/intro---4-3-06",
        "http://thecolbertreport.cc.com/videos/cckn97/who-s-honoring-me-now----southern-poverty-law-center",
        "http://thecolbertreport.cc.com/videos/j51p1g/the-word---stay-the-course",
        "http://thecolbertreport.cc.com/videos/mq3zja/stephen-s-sound-advice---taxes",
        "http://thecolbertreport.cc.com/videos/ci41dt/michael-smerconish",
        "http://thecolbertreport.cc.com/videos/716068/sign-off---nutz"
      ],
      "guest": "Michael Smerconish"
    },
    {
      "date": "2006-04-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9ew48u/intro---4-4-06",
        "http://thecolbertreport.cc.com/videos/ouryux/delay-retires",
        "http://thecolbertreport.cc.com/videos/3pmhdv/the-word---birdie",
        "http://thecolbertreport.cc.com/videos/fgj62q/balls-for-kidz---plastic-surgery",
        "http://thecolbertreport.cc.com/videos/3sqfo3/jesse-jackson"
      ],
      "guest": "Jesse Jackson"
    },
    {
      "date": "2006-04-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pxrtxy/intro---4-5-06",
        "http://thecolbertreport.cc.com/videos/1sxrid/crying",
        "http://thecolbertreport.cc.com/videos/alac6s/the-word---martyr",
        "http://thecolbertreport.cc.com/videos/6ythy9/formidable-opponent---immigration",
        "http://thecolbertreport.cc.com/videos/4ipowz/fract---russian-girls",
        "http://thecolbertreport.cc.com/videos/7hiane/harvey-mansfield",
        "http://thecolbertreport.cc.com/videos/7q90hr/sign-off---en-espanol"
      ],
      "guest": "Harvey Mansfield"
    },
    {
      "date": "2006-04-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4p2khi/intro---4-6-06",
        "http://thecolbertreport.cc.com/videos/yy1ecn/who-s-not-honoring-me-now----peabody-award",
        "http://thecolbertreport.cc.com/videos/wh4nku/easter-under-attack---recalled-eggs",
        "http://thecolbertreport.cc.com/videos/h6f8ks/the-word---nazis",
        "http://thecolbertreport.cc.com/videos/hqbc11/better-know-a-district---oregon-s-5th---darlene-hooley",
        "http://thecolbertreport.cc.com/videos/2v5yd4/markos-moulitsas",
        "http://thecolbertreport.cc.com/videos/a2gy6a/sign-off---spring-break"
      ],
      "guest": "Markos Moulitsas"
    },
    {
      "date": "2006-04-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rho2b5/intro---4-17-06",
        "http://thecolbertreport.cc.com/videos/jh0t6d/dime-boycott",
        "http://thecolbertreport.cc.com/videos/nyextq/on-notice---journal-of-paleolimnology",
        "http://thecolbertreport.cc.com/videos/swdzeg/was-it-really-that-bad----san-francisco-earthquake",
        "http://thecolbertreport.cc.com/videos/8ydrv2/reza-aslan",
        "http://thecolbertreport.cc.com/videos/nfyuyx/craziest-f--king-thing-i-ve-ever-heard---fly-glasses"
      ],
      "guest": "Reza Aslan"
    },
    {
      "date": "2006-04-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mwy60m/intro---4-18-06",
        "http://thecolbertreport.cc.com/videos/8zlfj4/stephen-jr--hatches-",
        "http://thecolbertreport.cc.com/videos/gi0de7/the-word---sir--yes--sir",
        "http://thecolbertreport.cc.com/videos/6epoa4/threatdown---pooh",
        "http://thecolbertreport.cc.com/videos/5peygv/anthony-romero",
        "http://thecolbertreport.cc.com/videos/9g88m0/baby-monitor",
        "http://thecolbertreport.cc.com/videos/sdky8q/who-s-not-honoring-me-now----pulitzer-prize"
      ],
      "guest": "Anthony Romero"
    },
    {
      "date": "2006-04-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/msbasq/intro---4-19-06",
        "http://thecolbertreport.cc.com/videos/8e53yj/white-house-press-secretary",
        "http://thecolbertreport.cc.com/videos/usn2co/global-warming-tv",
        "http://thecolbertreport.cc.com/videos/ai2zb9/the-word---save-it",
        "http://thecolbertreport.cc.com/videos/0nrquc/tip-wag---tom-cruise-and-katie-holmes",
        "http://thecolbertreport.cc.com/videos/x40hn2/caitlin-flanagan"
      ],
      "guest": "Caitlin Flanagan"
    },
    {
      "date": "2006-04-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ejbl27/intro---4-20-06",
        "http://thecolbertreport.cc.com/videos/qw6of6/protecting-kids-from-papers",
        "http://thecolbertreport.cc.com/videos/agw4nc/the-word---bard",
        "http://thecolbertreport.cc.com/videos/yrza7w/better-know-a-district---maryland-s-4th---albert-wynn",
        "http://thecolbertreport.cc.com/videos/isrl05/ralph-nader"
      ],
      "guest": "Ralph Nader"
    },
    {
      "date": "2006-04-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ed2ifv/intro---4-24-06",
        "http://thecolbertreport.cc.com/videos/yd10jl/wok-this-way",
        "http://thecolbertreport.cc.com/videos/nhj8qv/money---politics--the-machine-that-ain-t-broke",
        "http://thecolbertreport.cc.com/videos/z1f4bz/duke-obilia-auction",
        "http://thecolbertreport.cc.com/videos/svw55c/hugh-hewitt",
        "http://thecolbertreport.cc.com/videos/qzp0e4/sign-off---chatty-cathy"
      ],
      "guest": "Hugh Hewitt"
    },
    {
      "date": "2006-04-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h6j9ry/intro---4-25-06",
        "http://thecolbertreport.cc.com/videos/y1ry7v/contacting-john-lennon",
        "http://thecolbertreport.cc.com/videos/ef5fdk/the-word---panama",
        "http://thecolbertreport.cc.com/videos/6iaobq/threatdown---tom-hanks",
        "http://thecolbertreport.cc.com/videos/6smo0z/fract---middle-name",
        "http://thecolbertreport.cc.com/videos/gael38/sam-harris",
        "http://thecolbertreport.cc.com/videos/f00cpp/sign-off---bush-clock"
      ],
      "guest": "Sam Harris"
    },
    {
      "date": "2006-04-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xo40za/intro---4-26-06",
        "http://thecolbertreport.cc.com/videos/pjxlyg/armed-and-ready",
        "http://thecolbertreport.cc.com/videos/hhuez9/the-word---english",
        "http://thecolbertreport.cc.com/videos/ydqtim/better-know-a-district---georgia-s-11th---phil-gingrey",
        "http://thecolbertreport.cc.com/videos/thlh72/sebastian-junger",
        "http://thecolbertreport.cc.com/videos/8puf3y/sign-off---yellowcake"
      ],
      "guest": "Sebastian Junger"
    },
    {
      "date": "2006-04-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5ry4l9/intro---4-27-06",
        "http://thecolbertreport.cc.com/videos/z7tcn4/snow--informer",
        "http://thecolbertreport.cc.com/videos/6lr3t0/the-word---white-gloves",
        "http://thecolbertreport.cc.com/videos/b4nnko/plagiarism",
        "http://thecolbertreport.cc.com/videos/g4i72k/all-you-need-to-know---sleight-of-hand",
        "http://thecolbertreport.cc.com/videos/u54lrz/bill-kristol",
        "http://thecolbertreport.cc.com/videos/efk2x7/sign-off---the-nfl-draft"
      ],
      "guest": "Bill Kristol"
    },
    {
      "date": "2006-05-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/w2hp62/intro---5-1-06",
        "http://thecolbertreport.cc.com/videos/7jined/white-house-correspondents--dinner",
        "http://thecolbertreport.cc.com/videos/8uzt2n/the-word---drug-fueled-sex-crime",
        "http://thecolbertreport.cc.com/videos/yzcgdu/tip-wag---exxon",
        "http://thecolbertreport.cc.com/videos/5ptkiy/jon-meacham",
        "http://thecolbertreport.cc.com/videos/i3oqoh/sign-off---spam"
      ],
      "guest": "Jon Meacham"
    },
    {
      "date": "2006-05-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/341pc6/intro---5-2-06",
        "http://thecolbertreport.cc.com/videos/y9f7ks/magic-",
        "http://thecolbertreport.cc.com/videos/fdtzal/the-word---healthy-appetite",
        "http://thecolbertreport.cc.com/videos/hl6b8d/stephen-for-press-secretary",
        "http://thecolbertreport.cc.com/videos/lh3j87/mike-huckabee"
      ],
      "guest": "Governor Mike Huckabee"
    },
    {
      "date": "2006-05-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wjeu9g/intro---5-3-06",
        "http://thecolbertreport.cc.com/videos/72mru6/alan-town",
        "http://thecolbertreport.cc.com/videos/gdu7ux/the-word---name-game",
        "http://thecolbertreport.cc.com/videos/f8iv5g/stephen-s-sound-advice---gas-prices",
        "http://thecolbertreport.cc.com/videos/3pdcz2/paul-rieckhoff",
        "http://thecolbertreport.cc.com/videos/65gltn/betterer-know-a-district---georgia-s-11th---phil-gingrey-bonus-edition"
      ],
      "guest": "Paul Rieckhoff"
    },
    {
      "date": "2006-05-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mtzlgi/exclusive---better-know-a-district---oregon-s-3rd---earl-blumenauer",
        "http://thecolbertreport.cc.com/videos/pgiz58/intro---5-4-06",
        "http://thecolbertreport.cc.com/videos/ox5eqb/national-day-of-prayer",
        "http://thecolbertreport.cc.com/videos/38ws3t/the-word---indulgence",
        "http://thecolbertreport.cc.com/videos/h6w8h9/better-know-a-district---oregon-s-3rd---earl-blumenauer",
        "http://thecolbertreport.cc.com/videos/71jv5y/rick-reilly",
        "http://thecolbertreport.cc.com/videos/4uy12b/stephen-s-keys"
      ],
      "guest": "Rick Reilly"
    },
    {
      "date": "2006-05-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6p8qc0/intro---5-8-06",
        "http://thecolbertreport.cc.com/videos/gk0182/stegul",
        "http://thecolbertreport.cc.com/videos/fyqj80/porter-goss-resignation",
        "http://thecolbertreport.cc.com/videos/3ig0g8/the-word---not",
        "http://thecolbertreport.cc.com/videos/zdkg2i/shere-hite",
        "http://thecolbertreport.cc.com/videos/7581zo/sign-off---thank-you--stephen-"
      ],
      "guest": "Shere Hite"
    },
    {
      "date": "2006-05-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v9p03c/intro---5-9-06",
        "http://thecolbertreport.cc.com/videos/t6b1ke/double-or-nothing",
        "http://thecolbertreport.cc.com/videos/mjq9vh/the-word---superegomaniac",
        "http://thecolbertreport.cc.com/videos/9w4u9e/movies-that-are-destroying-america---summer-movies",
        "http://thecolbertreport.cc.com/videos/s2q4vq/frank-rich",
        "http://thecolbertreport.cc.com/videos/hofw72/sign-off---closing-credits-contest"
      ],
      "guest": "Frank Rich"
    },
    {
      "date": "2006-05-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j0109g/exclusive---better-know-a-district---nebraska-s-2nd---lee-terry",
        "http://thecolbertreport.cc.com/videos/z0wmkf/intro---5-10-06",
        "http://thecolbertreport.cc.com/videos/pc9isx/the-bird-flu",
        "http://thecolbertreport.cc.com/videos/6olwle/the-word---athletes-are-above-the-law",
        "http://thecolbertreport.cc.com/videos/m1vdpp/better-know-a-district---nebraska-s-2nd---lee-terry",
        "http://thecolbertreport.cc.com/videos/kuohzs/william-bastone",
        "http://thecolbertreport.cc.com/videos/pksza0/sign-off---what-you-deserve"
      ],
      "guest": "Bill Bastone"
    },
    {
      "date": "2006-05-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3oo94k/intro---5-11-06",
        "http://thecolbertreport.cc.com/videos/jn8cw4/the-west-wing",
        "http://thecolbertreport.cc.com/videos/j7pjuz/the-word---fill--er-up",
        "http://thecolbertreport.cc.com/videos/yy27qi/madeleine-albright",
        "http://thecolbertreport.cc.com/videos/8nl4m3/tip-wag---gold"
      ],
      "guest": "Madeleine Albright"
    },
    {
      "date": "2006-05-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uhk7yp/intro---5-15-06",
        "http://thecolbertreport.cc.com/videos/nxszdr/ahmadinejad-s-letter",
        "http://thecolbertreport.cc.com/videos/g2h9yx/the-word---lunchables",
        "http://thecolbertreport.cc.com/videos/pn3k09/summaries-of-summaries",
        "http://thecolbertreport.cc.com/videos/f5iuwt/all-you-need-to-know---dick-cheney",
        "http://thecolbertreport.cc.com/videos/qrt5tg/kevin-phillips",
        "http://thecolbertreport.cc.com/videos/lww1s9/craziest-f--king-thing-i-ve-ever-heard---gas-prices"
      ],
      "guest": "Kevin Phillips"
    },
    {
      "date": "2006-05-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x3193a/intro---5-16-06",
        "http://thecolbertreport.cc.com/videos/swctyt/the-word---inoculation",
        "http://thecolbertreport.cc.com/videos/5qdvts/billboard",
        "http://thecolbertreport.cc.com/videos/r5u8hp/body-parts-for-sale",
        "http://thecolbertreport.cc.com/videos/kdtmpm/tyson-slocum",
        "http://thecolbertreport.cc.com/videos/53mwdm/search-for-a-new-black-friend"
      ],
      "guest": "Tyson Slocum"
    },
    {
      "date": "2006-05-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8b6qml/exclusive---better-know-a-president---theodore-roosevelt",
        "http://thecolbertreport.cc.com/videos/x3193a/intro---5-16-06",
        "http://thecolbertreport.cc.com/videos/swctyt/the-word---inoculation",
        "http://thecolbertreport.cc.com/videos/5qdvts/billboard",
        "http://thecolbertreport.cc.com/videos/r5u8hp/body-parts-for-sale",
        "http://thecolbertreport.cc.com/videos/kdtmpm/tyson-slocum",
        "http://thecolbertreport.cc.com/videos/53mwdm/search-for-a-new-black-friend"
      ],
      "guest": "Jonathan Alter"
    },
    {
      "date": "2006-05-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wnj4cc/intro---5-17-06",
        "http://thecolbertreport.cc.com/videos/xie8nv/the-word---democrats",
        "http://thecolbertreport.cc.com/videos/3w6t72/better-know-a-president---theodore-roosevelt",
        "http://thecolbertreport.cc.com/videos/1pm4i8/jonathan-alter",
        "http://thecolbertreport.cc.com/videos/3f6dmg/boycott",
        "http://thecolbertreport.cc.com/videos/bqqkk9/reagan-dimes"
      ],
      "guest": "Jonathan Alter"
    },
    {
      "date": "2006-05-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ddjyzq/intro---5-18-06",
        "http://thecolbertreport.cc.com/videos/q374t3/stephen-colbert-s-guardian-eagles",
        "http://thecolbertreport.cc.com/videos/91osyo/the-word---libya",
        "http://thecolbertreport.cc.com/videos/rvxfth/difference-makers---tim-donnelly",
        "http://thecolbertreport.cc.com/videos/lga95g/fract---this-day-in-stephen-history",
        "http://thecolbertreport.cc.com/videos/jl63dd/ted-daeschler",
        "http://thecolbertreport.cc.com/videos/ddobv8/bears-eat-monkey"
      ],
      "guest": "Ted Daeschler"
    },
    {
      "date": "2006-06-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/63cmgz/my-first-100-shows--how-i-changed-the-world",
        "http://thecolbertreport.cc.com/videos/dk29ec/the-word---me",
        "http://thecolbertreport.cc.com/videos/sygeud/stone-phillips",
        "http://thecolbertreport.cc.com/videos/oqbssv/helium-balloon-drop",
        "http://thecolbertreport.cc.com/videos/n2keyu/the-in-box---100th-episode"
      ],
      "guest": "Stone Phillips"
    },
    {
      "date": "2006-06-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0jvvnp/intro---6-6-06",
        "http://thecolbertreport.cc.com/videos/zo00tb/666",
        "http://thecolbertreport.cc.com/videos/fvrhwv/the-word---military",
        "http://thecolbertreport.cc.com/videos/ohdrye/stephen-s-sound-advice---graduation",
        "http://thecolbertreport.cc.com/videos/j42g38/christiane-amanpour",
        "http://thecolbertreport.cc.com/videos/5pxetf/sign-off---666-almost-over"
      ],
      "guest": "Christiane Amanpour"
    },
    {
      "date": "2006-06-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4y1ae4/intro---6-7-06",
        "http://thecolbertreport.cc.com/videos/krcfjp/balrog",
        "http://thecolbertreport.cc.com/videos/8enhyk/search-for-a-new-black-friend---first-submissions",
        "http://thecolbertreport.cc.com/videos/b9ck5g/the-word---big-deal",
        "http://thecolbertreport.cc.com/videos/q5rrxq/threatdown---bad-heroin",
        "http://thecolbertreport.cc.com/videos/g6gwcq/steve-squyres",
        "http://thecolbertreport.cc.com/videos/l4kbi3/sign-off---vaughniston"
      ],
      "guest": "Steve Squyres"
    },
    {
      "date": "2006-06-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s8vv3c/intro---6-8-06",
        "http://thecolbertreport.cc.com/videos/5h2hdf/good-news-about-terror",
        "http://thecolbertreport.cc.com/videos/9s5g2f/the-word---goooooaaaaaal-",
        "http://thecolbertreport.cc.com/videos/tb1qzm/better-know-a-district---texas--22nd---tom-delay",
        "http://thecolbertreport.cc.com/videos/l9x3is/steve-johnson",
        "http://thecolbertreport.cc.com/videos/irk0rv/honorary-doctor"
      ],
      "guest": "Steve Johnson"
    },
    {
      "date": "2006-06-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kjiw2u/intro---6-12-06",
        "http://thecolbertreport.cc.com/videos/6ev021/tony-awards",
        "http://thecolbertreport.cc.com/videos/m292m0/on-notice---mort-zuckerman",
        "http://thecolbertreport.cc.com/videos/g6su9g/the-word---tom-delay-s-farewell-address",
        "http://thecolbertreport.cc.com/videos/e9sys9/tip-wag---college-students",
        "http://thecolbertreport.cc.com/videos/1zagcw/robert-f--kennedy-jr-",
        "http://thecolbertreport.cc.com/videos/rklfpc/a-tip-from-stephen-colbert-s-gardening-almanac"
      ],
      "guest": "Robert F. Kennedy Jr."
    },
    {
      "date": "2006-06-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/04ejnu/intro---6-13-06",
        "http://thecolbertreport.cc.com/videos/g9ijaq/stephen-jr--update",
        "http://thecolbertreport.cc.com/videos/qieya3/the-word---great-f---ing-idea",
        "http://thecolbertreport.cc.com/videos/c3pmq2/nsa-wiretapping",
        "http://thecolbertreport.cc.com/videos/2z4g9m/tim-flannery",
        "http://thecolbertreport.cc.com/videos/15yb0t/feline-bravery"
      ],
      "guest": "Tim Flannery"
    },
    {
      "date": "2006-06-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6tm6zq/exclusive---better-know-a-district---georgia-s-8th---lynn-westmoreland",
        "http://thecolbertreport.cc.com/videos/ddmy1c/intro---6-14-06",
        "http://thecolbertreport.cc.com/videos/3lnns6/surprise-visit-to-iraq",
        "http://thecolbertreport.cc.com/videos/l28ig3/the-word---license-renewal",
        "http://thecolbertreport.cc.com/videos/tlf8t3/better-know-a-district---georgia-s-8th---lynn-westmoreland",
        "http://thecolbertreport.cc.com/videos/4xe4qw/david-sirota",
        "http://thecolbertreport.cc.com/videos/g3hppv/sign-off---disappearing-act"
      ],
      "guest": "David Sirota"
    },
    {
      "date": "2006-06-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b9zn8f/intro---6-15-06",
        "http://thecolbertreport.cc.com/videos/69j400/search-for-a-new-black-friend----miami-vice--premiere",
        "http://thecolbertreport.cc.com/videos/kt2s9v/the-word---lock---load",
        "http://thecolbertreport.cc.com/videos/mqgxig/formidable-opponent---guantanamo-bay",
        "http://thecolbertreport.cc.com/videos/p118td/michael-pollan",
        "http://thecolbertreport.cc.com/videos/avxgi1/biggie-ness"
      ],
      "guest": "Michael Pollan"
    },
    {
      "date": "2006-06-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1zww1j/intro---6-19-06",
        "http://thecolbertreport.cc.com/videos/hsj6mj/bill-gates",
        "http://thecolbertreport.cc.com/videos/dattp1/the-word---risky-business",
        "http://thecolbertreport.cc.com/videos/q5w5ph/threatdown---the-homo-sexy-edition",
        "http://thecolbertreport.cc.com/videos/vaw7tx/gustavo-arellano"
      ],
      "guest": "Gustavo Arellano"
    },
    {
      "date": "2006-06-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wanyh5/intro---6-20-06",
        "http://thecolbertreport.cc.com/videos/t2udf0/marrying-snakes",
        "http://thecolbertreport.cc.com/videos/5kkfzf/the-word---everything-must-go",
        "http://thecolbertreport.cc.com/videos/m05b1x/american-goal",
        "http://thecolbertreport.cc.com/videos/qitmnq/stephen-makes-it-simple---government",
        "http://thecolbertreport.cc.com/videos/yji71b/bart-ehrman",
        "http://thecolbertreport.cc.com/videos/cahdxo/sign-off---i-ll-call-you"
      ],
      "guest": "Bart Ehrman"
    },
    {
      "date": "2006-06-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ghd1lj/intro---6-21-06",
        "http://thecolbertreport.cc.com/videos/sx1i4m/truthiness-cheer",
        "http://thecolbertreport.cc.com/videos/o652yy/don-t-mess-with-jesus",
        "http://thecolbertreport.cc.com/videos/alty3q/world-cup-trash-talk---alexi-lalas",
        "http://thecolbertreport.cc.com/videos/n3wvrq/tip-wag---episcopal-church",
        "http://thecolbertreport.cc.com/videos/qjlwml/bay-buchanan",
        "http://thecolbertreport.cc.com/videos/k5qunl/sign-off---insane-clown"
      ],
      "guest": "Bay Buchanan"
    },
    {
      "date": "2006-06-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q057ll/exclusive---better-know-a-district---colorado-s-1st---diana-degette",
        "http://thecolbertreport.cc.com/videos/wjjbzb/intro---6-22-06",
        "http://thecolbertreport.cc.com/videos/f4jomt/stephen-s-fault",
        "http://thecolbertreport.cc.com/videos/21iu1g/stephen-hawking-is-an-a-hole",
        "http://thecolbertreport.cc.com/videos/hfgyhs/the-word---cut-and-run",
        "http://thecolbertreport.cc.com/videos/abdpyq/better-know-a-district---colorado-s-1st---diana-degette",
        "http://thecolbertreport.cc.com/videos/2oh72f/douglas-brinkley",
        "http://thecolbertreport.cc.com/videos/vh4cyy/sign-off---not-winning-prizes"
      ],
      "guest": "Doug Brinkley"
    },
    {
      "date": "2006-06-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nxwjfg/intro---6-26-06",
        "http://thecolbertreport.cc.com/videos/0au60f/buffett-hires-gates",
        "http://thecolbertreport.cc.com/videos/7xr6qc/medal-of-audacity",
        "http://thecolbertreport.cc.com/videos/wzsdxf/the-word---class-warfare",
        "http://thecolbertreport.cc.com/videos/gb7vwl/all-you-need-to-know---hot-planet",
        "http://thecolbertreport.cc.com/videos/ny0s7o/mark-bowden",
        "http://thecolbertreport.cc.com/videos/7zeule/sign-off---highlights-magazine"
      ],
      "guest": "Mark Bowden"
    },
    {
      "date": "2006-06-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fqk84n/intro---6-27-06",
        "http://thecolbertreport.cc.com/videos/wmi0fy/flammo-mcburny",
        "http://thecolbertreport.cc.com/videos/jgpsp4/greatest-conservative-rock-songs",
        "http://thecolbertreport.cc.com/videos/5xzyo9/the-word---cold--dead-fingers",
        "http://thecolbertreport.cc.com/videos/nnrjlz/movies-that-are-destroying-america---a-scanner-darkly",
        "http://thecolbertreport.cc.com/videos/360rgd/chris-matthews",
        "http://thecolbertreport.cc.com/videos/iiom30/sign-off---rubber-mop"
      ],
      "guest": "Chris Matthews"
    },
    {
      "date": "2006-06-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iehmr9/intro---6-28-06",
        "http://thecolbertreport.cc.com/videos/mdix0g/the-smoking-side-dish",
        "http://thecolbertreport.cc.com/videos/luor1n/american-flags",
        "http://thecolbertreport.cc.com/videos/ygvw1r/the-word---superman",
        "http://thecolbertreport.cc.com/videos/9i4qz9/citizens-in-action---fondue-it-yourself",
        "http://thecolbertreport.cc.com/videos/pt4qqj/robert-baer",
        "http://thecolbertreport.cc.com/videos/h13p5y/sign-off---mr--potato-head"
      ],
      "guest": "Robert Baer"
    },
    {
      "date": "2006-06-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/edzwgb/intro---6-29-06",
        "http://thecolbertreport.cc.com/videos/voqmme/farewell--supreme-court",
        "http://thecolbertreport.cc.com/videos/z39ivs/the-president-s-bff",
        "http://thecolbertreport.cc.com/videos/qzor72/the-word---monkey-butter",
        "http://thecolbertreport.cc.com/videos/ncmucg/difference-makers---steve-pelkey",
        "http://thecolbertreport.cc.com/videos/facpb9/christopher-noxon",
        "http://thecolbertreport.cc.com/videos/9y1lrr/star-jones"
      ],
      "guest": "Christopher Noxon"
    },
    {
      "date": "2006-07-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lp1b85/intro---7-10-06",
        "http://thecolbertreport.cc.com/videos/fweavv/world-cup-co-champions",
        "http://thecolbertreport.cc.com/videos/gud4ld/the-word---silver-foxes",
        "http://thecolbertreport.cc.com/videos/ul4u7x/stephen-s-sound-advice---avoiding-wildfires",
        "http://thecolbertreport.cc.com/videos/hfxzg3/amy-sedaris",
        "http://thecolbertreport.cc.com/videos/izyjak/wilford-brimley-calls---mexico"
      ],
      "guest": "Amy Sedaris"
    },
    {
      "date": "2006-07-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2clwx9/intro---7-11-06",
        "http://thecolbertreport.cc.com/videos/iqeepf/coddling-our-kids",
        "http://thecolbertreport.cc.com/videos/d006ym/the-word---psychopharmaparenting",
        "http://thecolbertreport.cc.com/videos/0go470/stephen-r-a-p-s----talkin--to-kids",
        "http://thecolbertreport.cc.com/videos/wpkhsp/tony-hawk",
        "http://thecolbertreport.cc.com/videos/0eibi7/stephen-colbert-s-world-of-colbertcraft"
      ],
      "guest": "Tony Hawk"
    },
    {
      "date": "2006-07-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ov83sj/exclusive---better-know-a-district---washington-s-2nd---rick-larsen",
        "http://thecolbertreport.cc.com/videos/xl7bdt/intro---7-12-06",
        "http://thecolbertreport.cc.com/videos/t0dd3g/massachusetts---gaysrael",
        "http://thecolbertreport.cc.com/videos/pey6is/the-word---the-america-conventions",
        "http://thecolbertreport.cc.com/videos/67j2yk/better-know-a-district---washington-s-2nd---rick-larsen",
        "http://thecolbertreport.cc.com/videos/pabesh/mort-zuckerman",
        "http://thecolbertreport.cc.com/videos/c4tuhx/sign-off---space-open"
      ],
      "guest": "Mort Zuckerman"
    },
    {
      "date": "2006-07-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rlgq2q/intro---7-13-06",
        "http://thecolbertreport.cc.com/videos/d3xq4i/tv-s-new-low",
        "http://thecolbertreport.cc.com/videos/d45lww/the-word---inquisition",
        "http://thecolbertreport.cc.com/videos/mu9fov/threatdown---gay-clones",
        "http://thecolbertreport.cc.com/videos/42xxhd/ron-suskind"
      ],
      "guest": "Ron Suskind"
    },
    {
      "date": "2006-07-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q6xn0v/intro---7-17-06",
        "http://thecolbertreport.cc.com/videos/8g7ft7/microphone-on",
        "http://thecolbertreport.cc.com/videos/9s23g8/one-american-dollar",
        "http://thecolbertreport.cc.com/videos/ne3cif/the-word---t---a",
        "http://thecolbertreport.cc.com/videos/mn3izi/tip-wag---arizona",
        "http://thecolbertreport.cc.com/videos/udm6or/lee-silver",
        "http://thecolbertreport.cc.com/videos/yz4kpe/sign-off---lemons"
      ],
      "guest": "Lee Silver"
    },
    {
      "date": "2006-07-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6nca03/intro---7-18-06",
        "http://thecolbertreport.cc.com/videos/zipmr4/column-width",
        "http://thecolbertreport.cc.com/videos/r9fvrq/wwiii",
        "http://thecolbertreport.cc.com/videos/y08094/the-word---solidarity",
        "http://thecolbertreport.cc.com/videos/dz7igl/stephen-colbert-s-problems-without-solutions---bears",
        "http://thecolbertreport.cc.com/videos/j9c7t7/dhani-jones",
        "http://thecolbertreport.cc.com/videos/eaenq6/try-at-goodbye"
      ],
      "guest": "Dhani Jones"
    },
    {
      "date": "2006-07-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2v2a4w/intro---7-19-06",
        "http://thecolbertreport.cc.com/videos/wzyudz/veto-virginity",
        "http://thecolbertreport.cc.com/videos/vmqv4k/oprah-and-gayle",
        "http://thecolbertreport.cc.com/videos/zjmkqr/the-word---r-e-s-p-e-c-t",
        "http://thecolbertreport.cc.com/videos/yluk0n/the-convenientest-truth",
        "http://thecolbertreport.cc.com/videos/xndme2/joe-scarborough",
        "http://thecolbertreport.cc.com/videos/3os5ld/sign-off---buck-o-neil"
      ],
      "guest": "Joe Scarborough"
    },
    {
      "date": "2006-07-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vx02e0/exclusive---better-know-a-district---florida-s-19th---robert-wexler",
        "http://thecolbertreport.cc.com/videos/e2w8gi/intro---7-20-06",
        "http://thecolbertreport.cc.com/videos/bpcz93/search-for-a-new-black-friend---friend-exchange-rate",
        "http://thecolbertreport.cc.com/videos/flwcdv/julian-bond",
        "http://thecolbertreport.cc.com/videos/8oaiw2/better-know-a-district---florida-s-19th---robert-wexler",
        "http://thecolbertreport.cc.com/videos/naagf7/tom-brokaw",
        "http://thecolbertreport.cc.com/videos/8yx1of/one-regret"
      ],
      "guest": "Tom Brokaw"
    },
    {
      "date": "2006-07-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8l2dhx/intro---7-24-06",
        "http://thecolbertreport.cc.com/videos/b9z8jn/celebrating-america-s-kick-assedness",
        "http://thecolbertreport.cc.com/videos/mchynh/war---",
        "http://thecolbertreport.cc.com/videos/qpue58/the-word---moral-minority",
        "http://thecolbertreport.cc.com/videos/zo2o8b/threatdown---camp",
        "http://thecolbertreport.cc.com/videos/0xazqv/howell-raines",
        "http://thecolbertreport.cc.com/videos/530hq6/sign-off---proud"
      ],
      "guest": "Howell Raines"
    },
    {
      "date": "2006-07-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3bdqam/intro---7-25-06",
        "http://thecolbertreport.cc.com/videos/qik373/all-red-states",
        "http://thecolbertreport.cc.com/videos/mdzpjk/morning-shows",
        "http://thecolbertreport.cc.com/videos/e4fmv9/the-word---opposite-day",
        "http://thecolbertreport.cc.com/videos/bqr3op/formidable-opponent---stem-cell-research",
        "http://thecolbertreport.cc.com/videos/6xp57g/william-donohue",
        "http://thecolbertreport.cc.com/videos/wfh0qw/sign-off---food-for-thought"
      ],
      "guest": "William Donohue"
    },
    {
      "date": "2006-07-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sz2q6w/intro---7-26-06",
        "http://thecolbertreport.cc.com/videos/a62j0l/stephen-s-family-tree",
        "http://thecolbertreport.cc.com/videos/nxih1e/rescue-stephen-jr-",
        "http://thecolbertreport.cc.com/videos/b9kj0d/the-word---democrazy",
        "http://thecolbertreport.cc.com/videos/2wr9gw/stephen-s-sound-advice---blackouts",
        "http://thecolbertreport.cc.com/videos/ym3t0d/neal-katyal",
        "http://thecolbertreport.cc.com/videos/9nk4r7/sign-off---super-hero-stamps"
      ],
      "guest": "Neal Katyal"
    },
    {
      "date": "2006-07-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bgxe8v/exclusive---better-know-a-district---district-of-columbia---eleanor-holmes-norton",
        "http://thecolbertreport.cc.com/videos/jdsi7h/intro---7-27-06",
        "http://thecolbertreport.cc.com/videos/2pti2w/floyd-landis--balls",
        "http://thecolbertreport.cc.com/videos/0qi0dm/the-word---secretary-general-bolton",
        "http://thecolbertreport.cc.com/videos/6quypd/better-know-a-district---district-of-columbia---eleanor-holmes-norton",
        "http://thecolbertreport.cc.com/videos/a2w76v/joe-quesada"
      ],
      "guest": "Joe Quesada"
    },
    {
      "date": "2006-07-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2k66vv/intro---7-31-06",
        "http://thecolbertreport.cc.com/videos/ipm2dm/book-club",
        "http://thecolbertreport.cc.com/videos/3jl3pu/bicycle-theft",
        "http://thecolbertreport.cc.com/videos/z1aahs/the-word---wikiality",
        "http://thecolbertreport.cc.com/videos/zqod1f/tip-wag---lance-bass",
        "http://thecolbertreport.cc.com/videos/6tak7c/ned-lamont"
      ],
      "guest": "Ned Lamont"
    },
    {
      "date": "2006-08-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b1r2b5/intro---8-1-06",
        "http://thecolbertreport.cc.com/videos/advrej/courting-joe-lieberman",
        "http://thecolbertreport.cc.com/videos/n4ao8r/cuba-libre",
        "http://thecolbertreport.cc.com/videos/uqnkmr/the-word---uncool",
        "http://thecolbertreport.cc.com/videos/kxcfet/balls-for-kidz---carnivals",
        "http://thecolbertreport.cc.com/videos/pcfi97/peter-beinart",
        "http://thecolbertreport.cc.com/videos/wm5ib9/sign-off---energy"
      ],
      "guest": "Peter Beinart"
    },
    {
      "date": "2006-08-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7ofk8i/intro---8-2-06",
        "http://thecolbertreport.cc.com/videos/1jctl5/chair-for-joe-lieberman",
        "http://thecolbertreport.cc.com/videos/tc2zff/on-notice---how-the-on-notice-board-is-made",
        "http://thecolbertreport.cc.com/videos/9f950b/the-word---single-serving",
        "http://thecolbertreport.cc.com/videos/1gkx3r/no-joe-lieberman",
        "http://thecolbertreport.cc.com/videos/m7siat/linda-hirshman",
        "http://thecolbertreport.cc.com/videos/kx6zql/sign-off---cocoa-puffs"
      ],
      "guest": "Linda Hirshman"
    },
    {
      "date": "2006-08-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dij1sw/war--what-it-s-good-for---intro",
        "http://thecolbertreport.cc.com/videos/gdp73x/war--what-it-s-good-for---russ-lieber",
        "http://thecolbertreport.cc.com/videos/xzhg3v/meet-an-ally---palau",
        "http://thecolbertreport.cc.com/videos/o6s4zb/paul-hackett",
        "http://thecolbertreport.cc.com/videos/cujsej/war--what-it-s-good-for---the-eternal-flame"
      ],
      "guest": "Paul Hackett"
    },
    {
      "date": "2006-08-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ggdajm/intro---8-8-06",
        "http://thecolbertreport.cc.com/videos/oafdpt/lieberman-no-show",
        "http://thecolbertreport.cc.com/videos/kend9g/press-room-renovations",
        "http://thecolbertreport.cc.com/videos/cru76e/the-word---ten-hut-",
        "http://thecolbertreport.cc.com/videos/ywy5cq/tek-jansen---operation--heart-of-the-phoenix---dead-or-alive",
        "http://thecolbertreport.cc.com/videos/y3ycer/bill-rhoden",
        "http://thecolbertreport.cc.com/videos/h498ah/sign-off---toss-to-jon"
      ],
      "guest": "Bill Rhoden"
    },
    {
      "date": "2006-08-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8ku3ic/intro---8-9-06",
        "http://thecolbertreport.cc.com/videos/m3m7kz/lieberman-loses",
        "http://thecolbertreport.cc.com/videos/coxidl/delay-and-jesus",
        "http://thecolbertreport.cc.com/videos/9jopn4/the-word---pencils-down",
        "http://thecolbertreport.cc.com/videos/hpijh0/tip-wag---hungarian-bridge",
        "http://thecolbertreport.cc.com/videos/p3g7eb/alexandra-robbins"
      ],
      "guest": "Alexandra Robbins"
    },
    {
      "date": "2006-08-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/75wf4h/exclusive---better-know-a-district---california-s-6th---lynn-woolsey-pt--1",
        "http://thecolbertreport.cc.com/videos/m276r1/exclusive---better-know-a-district---california-s-6th---lynn-woolsey-pt--2",
        "http://thecolbertreport.cc.com/videos/8ku3ic/intro---8-9-06",
        "http://thecolbertreport.cc.com/videos/m3m7kz/lieberman-loses",
        "http://thecolbertreport.cc.com/videos/coxidl/delay-and-jesus",
        "http://thecolbertreport.cc.com/videos/9jopn4/the-word---pencils-down",
        "http://thecolbertreport.cc.com/videos/hpijh0/tip-wag---hungarian-bridge",
        "http://thecolbertreport.cc.com/videos/p3g7eb/alexandra-robbins"
      ],
      "guest": "Eli Pariser"
    },
    {
      "date": "2006-08-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qehfxb/intro---8-10-06",
        "http://thecolbertreport.cc.com/videos/6kvez0/liquids-on-planes",
        "http://thecolbertreport.cc.com/videos/b2svxe/the-word---cappuccino",
        "http://thecolbertreport.cc.com/videos/fyj6zj/better-know-a-district---california-s-6th---lynn-woolsey",
        "http://thecolbertreport.cc.com/videos/d573ty/eli-pariser",
        "http://thecolbertreport.cc.com/videos/hjpfzb/sign-off---remedy-for-insomnia"
      ],
      "guest": "Eli Pariser"
    },
    {
      "date": "2006-08-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/voo1ci/intro---8-14-06",
        "http://thecolbertreport.cc.com/videos/8c9998/peaceland",
        "http://thecolbertreport.cc.com/videos/mjxd75/french-fries",
        "http://thecolbertreport.cc.com/videos/bghbjx/jon-s-apology",
        "http://thecolbertreport.cc.com/videos/ozm5pk/stephen-s-sound-advice---protecting-your-online-identity",
        "http://thecolbertreport.cc.com/videos/u393jw/ramesh-ponnuru",
        "http://thecolbertreport.cc.com/videos/2b5c2u/sign-off---e-mail-password"
      ],
      "guest": "Ramesh Ponnuru"
    },
    {
      "date": "2006-08-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s8rzc5/intro---8-15-06",
        "http://thecolbertreport.cc.com/videos/95fbpq/sharing-the-spotlight-with-ahmadinejad",
        "http://thecolbertreport.cc.com/videos/6qb0k5/the-word---dumb-ocracy",
        "http://thecolbertreport.cc.com/videos/2evzvd/hungarian-bridge-progress-report",
        "http://thecolbertreport.cc.com/videos/mjhnvj/all-you-need-to-know---proper-condom-use",
        "http://thecolbertreport.cc.com/videos/jdgp1k/david-gergen"
      ],
      "guest": "David Gergen"
    },
    {
      "date": "2006-08-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5nmn6o/intro---8-16-06",
        "http://thecolbertreport.cc.com/videos/ic96lx/alan-schlesinger",
        "http://thecolbertreport.cc.com/videos/lsglfu/the-word---el-comandante",
        "http://thecolbertreport.cc.com/videos/gb4665/let-s-make-this-happen",
        "http://thecolbertreport.cc.com/videos/2ap7v2/was-it-really-that-bad----cold-war",
        "http://thecolbertreport.cc.com/videos/5uanam/morgan-spurlock",
        "http://thecolbertreport.cc.com/videos/9nqss3/sign-off---historic-hoax"
      ],
      "guest": "Morgan Spurlock"
    },
    {
      "date": "2006-08-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b66unq/intro---8-17-06",
        "http://thecolbertreport.cc.com/videos/xzzu7h/continuity",
        "http://thecolbertreport.cc.com/videos/75yefr/neil-degrasse-tyson",
        "http://thecolbertreport.cc.com/videos/kc21ru/better-know-a-district---california-s-31st",
        "http://thecolbertreport.cc.com/videos/8n3z7e/better-know-a-district---california-s-31st---javier-becerra",
        "http://thecolbertreport.cc.com/videos/nsqwib/neil-young"
      ],
      "guest": "Neil Young"
    },
    {
      "date": "2006-08-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uz7rxo/intro---8-21-06",
        "http://thecolbertreport.cc.com/videos/vzigy3/green-screen-challenge---the-announcement",
        "http://thecolbertreport.cc.com/videos/u468bk/atheists-in-foxholes",
        "http://thecolbertreport.cc.com/videos/pqlyj1/the-word---side-effects",
        "http://thecolbertreport.cc.com/videos/euqtan/threatdown---drivers-eat",
        "http://thecolbertreport.cc.com/videos/btgfsr/geoffrey-nunberg",
        "http://thecolbertreport.cc.com/videos/6p8hy2/sign-off---pants-off"
      ],
      "guest": "Geoffrey Nunberg"
    },
    {
      "date": "2006-08-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h5huhm/intro---8-22-06",
        "http://thecolbertreport.cc.com/videos/xr6owy/cheating-death---fields-medal",
        "http://thecolbertreport.cc.com/videos/p4wf5t/the-word---99-problems",
        "http://thecolbertreport.cc.com/videos/8t1wv1/stephen-colbert-salutes-hungary",
        "http://thecolbertreport.cc.com/videos/6iv4i1/paul-krugman"
      ],
      "guest": "Paul Krugman"
    },
    {
      "date": "2006-08-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rsqkbw/american-pop-culture--it-s-crumbelievable----intro",
        "http://thecolbertreport.cc.com/videos/85w92g/american-pop-culture--it-s-crumbelievable----pop-culture-icons",
        "http://thecolbertreport.cc.com/videos/l7z3b3/damian-kulash",
        "http://thecolbertreport.cc.com/videos/19r90f/american-pop-culture--it-s-crumbelievable----cable-tv-vs--the-american-family",
        "http://thecolbertreport.cc.com/videos/9h0pam/gideon-yago",
        "http://thecolbertreport.cc.com/videos/l29lto/american-pop-culture--it-s-crumbelievable----stephen-steps-up"
      ],
      "guest": "Gideon Yago"
    },
    {
      "date": "2006-08-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/86h1lx/intro---8-24-06",
        "http://thecolbertreport.cc.com/videos/j3gjfh/national-peach-month",
        "http://thecolbertreport.cc.com/videos/8avj2z/fart-jokes",
        "http://thecolbertreport.cc.com/videos/ejrivu/the-word---bad-boys",
        "http://thecolbertreport.cc.com/videos/sui137/30-days-with-the-colbert-report",
        "http://thecolbertreport.cc.com/videos/dw0hc5/janna-levin",
        "http://thecolbertreport.cc.com/videos/8v6ak5/green-screen-challenge---socialized-medicine"
      ],
      "guest": "Janna Levin"
    },
    {
      "date": "2006-09-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e2o0vm/intro---9-11-06",
        "http://thecolbertreport.cc.com/videos/ryb1sd/manilow-s-emmy",
        "http://thecolbertreport.cc.com/videos/vnwrl5/the-word---shall",
        "http://thecolbertreport.cc.com/videos/epkjf1/the-path-to-9-11",
        "http://thecolbertreport.cc.com/videos/dpqisf/martin-short",
        "http://thecolbertreport.cc.com/videos/0giino/sign-off---lullaby-clap"
      ],
      "guest": "Martin Short"
    },
    {
      "date": "2006-09-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zj5aco/exclusive---better-know-a-challenger---new-jersey-s-3rd---richard-sexton",
        "http://thecolbertreport.cc.com/videos/2vdm17/intro---9-12-06",
        "http://thecolbertreport.cc.com/videos/fuhxnz/green-screen-challenge---entry",
        "http://thecolbertreport.cc.com/videos/464nde/the-word---missed-opportunity",
        "http://thecolbertreport.cc.com/videos/03wv59/better-know-a-challenger---new-jersey-s-3rd---richard-sexton",
        "http://thecolbertreport.cc.com/videos/uyjgfx/toby-keith",
        "http://thecolbertreport.cc.com/videos/df7axm/sign-off---special-episode"
      ],
      "guest": "Toby Keith"
    },
    {
      "date": "2006-09-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9h47r2/intro---9-13-06",
        "http://thecolbertreport.cc.com/videos/a7pf2u/the-colmandos",
        "http://thecolbertreport.cc.com/videos/fftk8t/the-word---caveat-emptor",
        "http://thecolbertreport.cc.com/videos/yr3sze/formidable-opponent---iraq-withdrawal",
        "http://thecolbertreport.cc.com/videos/io94jl/ken-jennings",
        "http://thecolbertreport.cc.com/videos/m6mk95/sign-off---cigarettes"
      ],
      "guest": "Ken Jennings"
    },
    {
      "date": "2006-09-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3i56pi/intro---9-14-06",
        "http://thecolbertreport.cc.com/videos/m82cj5/sexy-photo",
        "http://thecolbertreport.cc.com/videos/39njye/george-allen",
        "http://thecolbertreport.cc.com/videos/dmk6s2/hungarian-bridge---andras-simonyi",
        "http://thecolbertreport.cc.com/videos/ogtff2/tip-wag---nasa",
        "http://thecolbertreport.cc.com/videos/6xq5fv/bill-simmons",
        "http://thecolbertreport.cc.com/videos/czqyfe/sign-off---get-on-it--nation",
        "http://thecolbertreport.cc.com/videos/g844xc/bridge-contest"
      ],
      "guest": "Bill Simmons"
    },
    {
      "date": "2006-09-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wteen9/intro---9-18-06",
        "http://thecolbertreport.cc.com/videos/51grfw/whitney-houston",
        "http://thecolbertreport.cc.com/videos/82m3g9/the-word---wiper-fluid",
        "http://thecolbertreport.cc.com/videos/cyd2um/tek-jansen---operation--destiny-s-underbelly--entrapped-",
        "http://thecolbertreport.cc.com/videos/r7b7p1/will-power",
        "http://thecolbertreport.cc.com/videos/j44oq1/sign-off---bust"
      ],
      "guest": "Will Power"
    },
    {
      "date": "2006-09-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/spzrjp/intro---9-19-06",
        "http://thecolbertreport.cc.com/videos/dbmjaj/u-n--week",
        "http://thecolbertreport.cc.com/videos/5v40iy/the-word---tribalism",
        "http://thecolbertreport.cc.com/videos/qloab5/threatdown---toby-keith",
        "http://thecolbertreport.cc.com/videos/kf8re4/frank-rich",
        "http://thecolbertreport.cc.com/videos/ezwrh0/sign-off---fantasy-colbert-report-league"
      ],
      "guest": "Frank Rich"
    },
    {
      "date": "2006-09-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lj5z86/green-screen-challenge---the-challenge-continues",
        "http://thecolbertreport.cc.com/videos/o1qorx/who-s-not-honoring-me-now----the-macarthur-foundation",
        "http://thecolbertreport.cc.com/videos/pz60rq/green-screen-challenge---typical-democrats",
        "http://thecolbertreport.cc.com/videos/vkr39r/stephen-s-sound-advice---high-school",
        "http://thecolbertreport.cc.com/videos/fn9d5q/james-carville",
        "http://thecolbertreport.cc.com/videos/g7hl0x/the-word---lose"
      ],
      "guest": "James Carville"
    },
    {
      "date": "2006-09-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yujezq/intro---9-21-06",
        "http://thecolbertreport.cc.com/videos/tvrtdg/days-of-repentance-hotline",
        "http://thecolbertreport.cc.com/videos/kxvydq/better-know-a-challenger---new-jersey-s-5th---paul-aronsohn",
        "http://thecolbertreport.cc.com/videos/u1txo4/daniel-ellsberg",
        "http://thecolbertreport.cc.com/videos/42tk7e/sign-off---pentagon-papers",
        "http://thecolbertreport.cc.com/videos/yxzh84/daniel-golden"
      ],
      "guest": "Daniel Ellsberg"
    },
    {
      "date": "2006-09-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ubu45l/intro---9-25-06",
        "http://thecolbertreport.cc.com/videos/918nqn/heritage",
        "http://thecolbertreport.cc.com/videos/s08yij/buy-this-book",
        "http://thecolbertreport.cc.com/videos/1tds5k/the-word---opposition-party",
        "http://thecolbertreport.cc.com/videos/az74i4/green-screen-challenge---goodbye--darth-maul-",
        "http://thecolbertreport.cc.com/videos/te8evq/fun-in-the-sun",
        "http://thecolbertreport.cc.com/videos/c88j0x/arianna-huffington"
      ],
      "guest": "Arianna Huffington"
    },
    {
      "date": "2006-09-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/13qtu2/intro---9-26-06",
        "http://thecolbertreport.cc.com/videos/76ov53/frank-rich-calls-in",
        "http://thecolbertreport.cc.com/videos/navjpx/the-word---good-morning",
        "http://thecolbertreport.cc.com/videos/22kzkk/four-horsemen-of-the-a-pop-calypse---justin-timberlake",
        "http://thecolbertreport.cc.com/videos/kertmr/ted-danson",
        "http://thecolbertreport.cc.com/videos/en1nzg/alpha-dog-of-the-week---tom-selleck"
      ],
      "guest": "Ted Danson"
    },
    {
      "date": "2006-09-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dkn6is/intro---9-27-06",
        "http://thecolbertreport.cc.com/videos/w75za8/oprah-and-friends",
        "http://thecolbertreport.cc.com/videos/2zj0db/mort-zuckerman-dials-the-atone-phone",
        "http://thecolbertreport.cc.com/videos/wq2mkf/the-word---iraq",
        "http://thecolbertreport.cc.com/videos/p20mpr/tip-wag---george-clooney",
        "http://thecolbertreport.cc.com/videos/g1anyj/lowell-bergman",
        "http://thecolbertreport.cc.com/videos/8v25i1/sign-off---world-of-colbertcraft"
      ],
      "guest": "Lowell Bergman"
    },
    {
      "date": "2006-09-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b0od22/intro---9-28-06",
        "http://thecolbertreport.cc.com/videos/mechk8/green-screen-challenge---ipod---colbert",
        "http://thecolbertreport.cc.com/videos/jl58qd/blitzkrieg-on-grinchitude---santa-claus--in",
        "http://thecolbertreport.cc.com/videos/a23i2j/jon-stewart-calls-in",
        "http://thecolbertreport.cc.com/videos/kby4hb/un-american-news---spain",
        "http://thecolbertreport.cc.com/videos/c2vyau/steve-wozniak"
      ],
      "guest": "Steve Wozniak"
    },
    {
      "date": "2006-10-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vaflyc/intro---10-2-06",
        "http://thecolbertreport.cc.com/videos/ak0wmf/mark-foley",
        "http://thecolbertreport.cc.com/videos/clzwmu/the-word---copycat",
        "http://thecolbertreport.cc.com/videos/0f7zu5/threatdown---saudi-arabia",
        "http://thecolbertreport.cc.com/videos/6cuxj4/michael-lewis",
        "http://thecolbertreport.cc.com/videos/gwcer9/sign-off---actual-apologies"
      ],
      "guest": "Michael Lewis"
    },
    {
      "date": "2006-10-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fkksjm/intro---10-3-06",
        "http://thecolbertreport.cc.com/videos/85po0w/drunk-dialing",
        "http://thecolbertreport.cc.com/videos/hnt52c/lucifer",
        "http://thecolbertreport.cc.com/videos/ap05bd/the-word---experience",
        "http://thecolbertreport.cc.com/videos/oojn49/steagle-colbeagle-the-eagle---mascot",
        "http://thecolbertreport.cc.com/videos/xqpdbq/andy-stern",
        "http://thecolbertreport.cc.com/videos/tbnr4f/sign-off---retire-the-jersey"
      ],
      "guest": "Andy Stern"
    },
    {
      "date": "2006-10-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pi53om/intro---10-4-06",
        "http://thecolbertreport.cc.com/videos/t3hp8a/mark-foley-the-rino",
        "http://thecolbertreport.cc.com/videos/2n2oat/the-word---must-not-see-tv",
        "http://thecolbertreport.cc.com/videos/536mbt/nobel-prize-sweep",
        "http://thecolbertreport.cc.com/videos/ga8yja/green-screen-challenge---d-d",
        "http://thecolbertreport.cc.com/videos/ps5fh4/byron-dorgan",
        "http://thecolbertreport.cc.com/videos/vbbgif/-20-million-victory-party"
      ],
      "guest": "Byron Dorgan"
    },
    {
      "date": "2006-10-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r5fn7m/intro---10-5-06",
        "http://thecolbertreport.cc.com/videos/t7lg5x/handling-sex-scandals",
        "http://thecolbertreport.cc.com/videos/2pcxy7/behavioral-profiling",
        "http://thecolbertreport.cc.com/videos/6qs8dt/maz-jobrani",
        "http://thecolbertreport.cc.com/videos/8vhk9f/better-know-a-district---florida-s-16th---mark-foley",
        "http://thecolbertreport.cc.com/videos/cg4ud6/amy-goodman",
        "http://thecolbertreport.cc.com/videos/mex37x/starbucks-price-hike"
      ],
      "guest": "Amy Goodman"
    },
    {
      "date": "2006-10-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uz4y5r/intro---10-9-06",
        "http://thecolbertreport.cc.com/videos/vcdu14/stephen-greets-kim-jong-il",
        "http://thecolbertreport.cc.com/videos/94jsyv/the-word---safety",
        "http://thecolbertreport.cc.com/videos/oqybt6/sport-report---saginaw-spirit-3-0-with-steagle-colbeagle",
        "http://thecolbertreport.cc.com/videos/sxcbbt/randy-newman"
      ],
      "guest": "Randy Newman"
    },
    {
      "date": "2006-10-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7x9ixq/a-salute-to-the-american-lady",
        "http://thecolbertreport.cc.com/videos/2jugk2/stephen-r-a-p-s----gender-issues",
        "http://thecolbertreport.cc.com/videos/tab5oc/jane-fonda-and-gloria-steinem",
        "http://thecolbertreport.cc.com/videos/vglnl3/ariel-levy",
        "http://thecolbertreport.cc.com/videos/6ooly1/sign-off---mrs--colbert"
      ],
      "guest": "Ariel Levy"
    },
    {
      "date": "2006-10-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m063rn/intro---10-11-06",
        "http://thecolbertreport.cc.com/videos/bmktr8/shout-out----from-baghdad-to-the-report",
        "http://thecolbertreport.cc.com/videos/lbop8f/stephen-cashes-in",
        "http://thecolbertreport.cc.com/videos/kpo74v/green-screen-challenge---the-final-cut",
        "http://thecolbertreport.cc.com/videos/fxyspp/green-screen-challenge---the-finalists",
        "http://thecolbertreport.cc.com/videos/n67d6e/green-screen-challenge---the-winner",
        "http://thecolbertreport.cc.com/videos/pkbxv2/tek-jansen---space-station-theta-zeus-aquarius",
        "http://thecolbertreport.cc.com/videos/8hq3dq/lightsaber-duel",
        "http://thecolbertreport.cc.com/videos/nkr8wo/green-screen---george-lucas"
      ],
      "guest": "Andrew Sullivan"
    },
    {
      "date": "2006-10-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d5jz3y/exclusive---better-know-a-challenger---new-jersey-s-4th---carol-gay",
        "http://thecolbertreport.cc.com/videos/yw8t41/intro---10-12-06",
        "http://thecolbertreport.cc.com/videos/dikrto/congratulatory-mail",
        "http://thecolbertreport.cc.com/videos/9dfgke/north-korean-weapons-test-scare",
        "http://thecolbertreport.cc.com/videos/htaz1s/gay-republicans---andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/gtnan5/better-know-a-challenger---new-jersey-s-4th---carol-gay",
        "http://thecolbertreport.cc.com/videos/f57spg/brian-schweitzer",
        "http://thecolbertreport.cc.com/videos/o1sfrf/sign-off---revved-up"
      ],
      "guest": "Larry Miller"
    },
    {
      "date": "2006-10-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/plp18s/intro---10-16-06",
        "http://thecolbertreport.cc.com/videos/q81oyv/bush-impersonator-impersonator",
        "http://thecolbertreport.cc.com/videos/3yuat5/cbgb-s",
        "http://thecolbertreport.cc.com/videos/7i1kaz/the-word---russian-dolls",
        "http://thecolbertreport.cc.com/videos/rxjbs7/tip-wag---midterm-elections-edition",
        "http://thecolbertreport.cc.com/videos/2he8tk/barry-scheck",
        "http://thecolbertreport.cc.com/videos/xuvjmp/the-wave"
      ],
      "guest": "Barry Scheck"
    },
    {
      "date": "2006-10-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ae5ru6/intro---10-17-06",
        "http://thecolbertreport.cc.com/videos/fo3bt3/one-year-anniversary",
        "http://thecolbertreport.cc.com/videos/r8tksi/descending-screen",
        "http://thecolbertreport.cc.com/videos/18nq18/the-word---irreconcilable-differences",
        "http://thecolbertreport.cc.com/videos/hlfrbf/anniversary-cake",
        "http://thecolbertreport.cc.com/videos/is87vo/judge-tubbs",
        "http://thecolbertreport.cc.com/videos/7fe2ut/richard-dawkins",
        "http://thecolbertreport.cc.com/videos/g41j5d/second-year-portrait"
      ],
      "guest": "Richard Dawkins"
    },
    {
      "date": "2006-10-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nm42tm/intro---10-18-06",
        "http://thecolbertreport.cc.com/videos/szo4co/elephant-vasectomies",
        "http://thecolbertreport.cc.com/videos/bl7nra/the-word---sherlock",
        "http://thecolbertreport.cc.com/videos/jpgqk0/jeopardy",
        "http://thecolbertreport.cc.com/videos/wu6d7x/sport-report---smack-talk",
        "http://thecolbertreport.cc.com/videos/0usw0u/david-kuo",
        "http://thecolbertreport.cc.com/videos/pun0an/santorum-s-iraqi-lord-of-the-rings"
      ],
      "guest": "Deepak Chopra"
    },
    {
      "date": "2006-10-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/63h5y0/exclusive---better-know-a-challenger---new-york-s-19th---john-hall",
        "http://thecolbertreport.cc.com/videos/simwwd/intro---10-19-06",
        "http://thecolbertreport.cc.com/videos/zzoxmj/ebay-portrait-bid",
        "http://thecolbertreport.cc.com/videos/55o9xl/jim-gilchrist",
        "http://thecolbertreport.cc.com/videos/eh02b8/better-know-a-challenger---new-york-s-19th---john-hall",
        "http://thecolbertreport.cc.com/videos/484q7z/peter-agre"
      ],
      "guest": "Matthew Dowd"
    },
    {
      "date": "2006-10-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xsr78j/intro---10-30-06",
        "http://thecolbertreport.cc.com/videos/501yrw/get-ready-for-barry",
        "http://thecolbertreport.cc.com/videos/fokcta/stay-the-course",
        "http://thecolbertreport.cc.com/videos/2ffwy9/the-word---shameless",
        "http://thecolbertreport.cc.com/videos/3644s2/threatdown---greatdown",
        "http://thecolbertreport.cc.com/videos/h5ly2o/barry-manilow"
      ],
      "guest": "Barry Manilow"
    },
    {
      "date": "2006-10-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vll3lh/intro---10-31-06",
        "http://thecolbertreport.cc.com/videos/ixb36k/costumes-for-the-girls",
        "http://thecolbertreport.cc.com/videos/qrw2en/the-word---thanks--gays-",
        "http://thecolbertreport.cc.com/videos/ya17xq/portrait-auction",
        "http://thecolbertreport.cc.com/videos/crxtpi/welcome-to-the-house-of-horrors---nancy-pelosi",
        "http://thecolbertreport.cc.com/videos/2g6dhj/tim-robbins",
        "http://thecolbertreport.cc.com/videos/9z7u1s/freak-show---log-cabin-republican"
      ],
      "guest": "Tim Robbins"
    },
    {
      "date": "2006-11-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fio9x5/exclusive---better-know-a-challenger---california-s-30th---david-nelson-jones",
        "http://thecolbertreport.cc.com/videos/ngeqml/intro---11-1-06",
        "http://thecolbertreport.cc.com/videos/07l6jg/john-kerry",
        "http://thecolbertreport.cc.com/videos/5a62pu/the-word---rip-off",
        "http://thecolbertreport.cc.com/videos/j449s5/better-know-a-challenger---california-s-30th---david-nelson-jones",
        "http://thecolbertreport.cc.com/videos/80bjyk/penn-jillette",
        "http://thecolbertreport.cc.com/videos/7w23zw/big-in--06"
      ],
      "guest": "Penn Jillette"
    },
    {
      "date": "2006-11-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c1jp7z/intro---11-2-06",
        "http://thecolbertreport.cc.com/videos/ryl8xd/a-historidocufictiomentary-of-george-allen",
        "http://thecolbertreport.cc.com/videos/ypv3hz/p-k--winsome---black-republican",
        "http://thecolbertreport.cc.com/videos/e8pbai/sport-report---the-spirit-shop",
        "http://thecolbertreport.cc.com/videos/o5x0ja/chad-walldorf--portrait-winner",
        "http://thecolbertreport.cc.com/videos/vchsrw/ron-reagan"
      ],
      "guest": "Ron Reagan Jr."
    },
    {
      "date": "2006-11-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5l9ww2/intro---11-6-06",
        "http://thecolbertreport.cc.com/videos/3x1o1e/saddam-s-hanging",
        "http://thecolbertreport.cc.com/videos/mfycn0/vote-your-conscience",
        "http://thecolbertreport.cc.com/videos/xjsetj/the-word---happy-ending",
        "http://thecolbertreport.cc.com/videos/yu4stw/ted-haggard-s-media-field-day",
        "http://thecolbertreport.cc.com/videos/qtoavw/what-to-expect-when-you-re-electing",
        "http://thecolbertreport.cc.com/videos/de4hy0/mark-halperin",
        "http://thecolbertreport.cc.com/videos/iuqlez/absentee-voting"
      ],
      "guest": "Mark Halperin"
    },
    {
      "date": "2006-11-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rdhken/midterm-midtacular---beatty---bening-confirmation-call",
        "http://thecolbertreport.cc.com/videos/vmt5dv/better-know-a-district---midterm-midtacular",
        "http://thecolbertreport.cc.com/videos/42n9bh/midterm-midtacular---update-from-the-daily-show",
        "http://thecolbertreport.cc.com/videos/gmknl3/midterm-midtacular---democrat-majority",
        "http://thecolbertreport.cc.com/videos/1qhm06/stephen-s-final-thoughts",
        "http://thecolbertreport.cc.com/videos/3fzd37/robert-wexler-and-eleanor-holmes-norton"
      ],
      "guest": "Election Night Live Show"
    },
    {
      "date": "2006-11-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/veyf2a/intro---11-8-06",
        "http://thecolbertreport.cc.com/videos/0085n8/the-word---sigh",
        "http://thecolbertreport.cc.com/videos/8tjdnz/better-know-a-district---new-york-s-19th---john-hall",
        "http://thecolbertreport.cc.com/videos/n1c32a/tek-jansen---theme-song",
        "http://thecolbertreport.cc.com/videos/vzb4w6/jeff-greenfield",
        "http://thecolbertreport.cc.com/videos/3yplp6/special-memories"
      ],
      "guest": "Jeff Greenfield"
    },
    {
      "date": "2006-11-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vsle8s/intro---11-9-06",
        "http://thecolbertreport.cc.com/videos/ec6t9w/shout-out----michael-rehm",
        "http://thecolbertreport.cc.com/videos/0osdbo/the-word---putin--08",
        "http://thecolbertreport.cc.com/videos/ro28cv/p-k--winsome---a-journey-home",
        "http://thecolbertreport.cc.com/videos/sff21j/dean-kamen",
        "http://thecolbertreport.cc.com/videos/y6jo9b/sign-off---buy-american"
      ],
      "guest": "Dean Kamen"
    },
    {
      "date": "2006-11-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xhi69f/intro---11-13-06",
        "http://thecolbertreport.cc.com/videos/tq9pyg/mccain-s-depression",
        "http://thecolbertreport.cc.com/videos/wze0m8/the-word---back-off--old-man",
        "http://thecolbertreport.cc.com/videos/3l0etr/tip-wag---quitters-edition",
        "http://thecolbertreport.cc.com/videos/v04ko8/dan-rather",
        "http://thecolbertreport.cc.com/videos/39thdv/alpha-dog-of-the-week---ronald-reagan"
      ],
      "guest": "Dan Rather"
    },
    {
      "date": "2006-11-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2xysq8/intro---10-14-06",
        "http://thecolbertreport.cc.com/videos/41uzjx/lesbian-roles",
        "http://thecolbertreport.cc.com/videos/njn4f1/stephen-jr--in-canada",
        "http://thecolbertreport.cc.com/videos/x9bnw7/the-word---expecting",
        "http://thecolbertreport.cc.com/videos/mx7sjh/vote-for-gail-jingle",
        "http://thecolbertreport.cc.com/videos/xokq2b/jeff-swartz",
        "http://thecolbertreport.cc.com/videos/cnxqlb/kid-activity-corner---nancy-pelosi-hand-turkeys"
      ],
      "guest": "Jeff Swartz"
    },
    {
      "date": "2006-11-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9sc11a/exclusive---better-know-a-founder---thomas-jefferson",
        "http://thecolbertreport.cc.com/videos/2xysq8/intro---10-14-06",
        "http://thecolbertreport.cc.com/videos/41uzjx/lesbian-roles",
        "http://thecolbertreport.cc.com/videos/njn4f1/stephen-jr--in-canada",
        "http://thecolbertreport.cc.com/videos/x9bnw7/the-word---expecting",
        "http://thecolbertreport.cc.com/videos/mx7sjh/vote-for-gail-jingle",
        "http://thecolbertreport.cc.com/videos/xokq2b/jeff-swartz",
        "http://thecolbertreport.cc.com/videos/cnxqlb/kid-activity-corner---nancy-pelosi-hand-turkeys"
      ],
      "guest": "Al Franken, Dr. Michael Novacek"
    },
    {
      "date": "2006-11-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zmp3r0/intro---11-15-06",
        "http://thecolbertreport.cc.com/videos/kl1xl0/rush-limbaugh-s-comments",
        "http://thecolbertreport.cc.com/videos/w5bgh2/democrats--victory-dance---al-franken",
        "http://thecolbertreport.cc.com/videos/47a505/better-know-a-founder---thomas-jefferson",
        "http://thecolbertreport.cc.com/videos/cnf5lf/mike-novacek"
      ],
      "guest": "Al Franken, Dr. Michael Novacek"
    },
    {
      "date": "2006-11-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hstabl/intro---11-16-06",
        "http://thecolbertreport.cc.com/videos/zyzp0g/minority-whip",
        "http://thecolbertreport.cc.com/videos/euzyuf/sexiest-man-alive",
        "http://thecolbertreport.cc.com/videos/olggdr/the-word---play-ball-",
        "http://thecolbertreport.cc.com/videos/oplysq/movies-that-are-destroying-america---xmas",
        "http://thecolbertreport.cc.com/videos/3il1eo/richard-linklater",
        "http://thecolbertreport.cc.com/videos/s716ap/sign-off---strawberry"
      ],
      "guest": "Richard Linklater"
    },
    {
      "date": "2006-11-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1xjoh6/intro---11-27-06",
        "http://thecolbertreport.cc.com/videos/z4h5jm/putin--08",
        "http://thecolbertreport.cc.com/videos/k3p09y/tivo-cleaning",
        "http://thecolbertreport.cc.com/videos/dg34l1/the-word---jacksquat",
        "http://thecolbertreport.cc.com/videos/ckqxms/threatdown---100-hoops",
        "http://thecolbertreport.cc.com/videos/lqdkhe/jim-lehrer",
        "http://thecolbertreport.cc.com/videos/y3zgee/sign-off---love"
      ],
      "guest": "Jim Lehrer"
    },
    {
      "date": "2006-11-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0tspod/intro---11-28-06",
        "http://thecolbertreport.cc.com/videos/47xxe1/who-s-honoring-me-now----gq",
        "http://thecolbertreport.cc.com/videos/voj40k/the-word---ecu-menace",
        "http://thecolbertreport.cc.com/videos/fenw0v/alabama-miracle---helen-keller-museum",
        "http://thecolbertreport.cc.com/videos/xi41md/harry-shearer",
        "http://thecolbertreport.cc.com/videos/iate4s/sign-off---exceptional-audience"
      ],
      "guest": "Harry Shearer"
    },
    {
      "date": "2006-11-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mr063e/intro---11-29-06",
        "http://thecolbertreport.cc.com/videos/wanzdw/who-s-riding-my-coattails-now----jeopardy",
        "http://thecolbertreport.cc.com/videos/bp43w6/the-word---killing-two-birds",
        "http://thecolbertreport.cc.com/videos/49jjmd/alabama-miracle---the-stephen-colbert-museum---gift-shop--grand-opening",
        "http://thecolbertreport.cc.com/videos/8rjs2g/nora-ephron"
      ],
      "guest": "Nora Ephron"
    },
    {
      "date": "2006-11-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wzpzqs/intro---11-30-06",
        "http://thecolbertreport.cc.com/videos/4c2tdv/vilsack-attack",
        "http://thecolbertreport.cc.com/videos/z88s3n/p-k--winsome---if-p-k--winsome-did-it",
        "http://thecolbertreport.cc.com/videos/0inrmr/colbert-nation-merchandise",
        "http://thecolbertreport.cc.com/videos/jotybg/alabama-miracle---the-morning-after",
        "http://thecolbertreport.cc.com/videos/hv1lim/mike-lupica",
        "http://thecolbertreport.cc.com/videos/k1wdp2/sign-off---wall-notch"
      ],
      "guest": "Mike Lupica"
    },
    {
      "date": "2006-12-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9s5cs9/intro---12-4-06",
        "http://thecolbertreport.cc.com/videos/ozd0a8/sherman-wedding",
        "http://thecolbertreport.cc.com/videos/sjup2k/the-word---american-orthodox",
        "http://thecolbertreport.cc.com/videos/shtpb9/tip-wag---christmas",
        "http://thecolbertreport.cc.com/videos/tc5d1m/will-wright",
        "http://thecolbertreport.cc.com/videos/xpx8ua/sign-off---extra-special-comment---tie-stain"
      ],
      "guest": "Will Wright"
    },
    {
      "date": "2006-12-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z40k91/intro---12-5-06",
        "http://thecolbertreport.cc.com/videos/6ixmt6/-return--to-the-moon",
        "http://thecolbertreport.cc.com/videos/mz0h4p/robert-gates--confirmation",
        "http://thecolbertreport.cc.com/videos/msrwcg/the-word---honest-injun",
        "http://thecolbertreport.cc.com/videos/3odbkp/sport-report---coach-mancini",
        "http://thecolbertreport.cc.com/videos/tjdbeu/sign-off---number-one-source",
        "http://thecolbertreport.cc.com/videos/c1sa92/steven-levitt"
      ],
      "guest": "Steven D. Leavitt"
    },
    {
      "date": "2006-12-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fe08hq/intro---12-6-06",
        "http://thecolbertreport.cc.com/videos/oamjbp/life-size-nativity",
        "http://thecolbertreport.cc.com/videos/ikcmp0/mary-cheney",
        "http://thecolbertreport.cc.com/videos/4fr9o9/the-word---words",
        "http://thecolbertreport.cc.com/videos/76wnkt/tek-jansen---tek-the-halls",
        "http://thecolbertreport.cc.com/videos/0wqkww/john-sexton",
        "http://thecolbertreport.cc.com/videos/8suoui/sign-off---cardboard-box"
      ],
      "guest": "John Sexton"
    },
    {
      "date": "2006-12-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/k9wcbv/intro---12-7-06",
        "http://thecolbertreport.cc.com/videos/ebabt9/david-gregory",
        "http://thecolbertreport.cc.com/videos/kvccyn/the-word---case-closed",
        "http://thecolbertreport.cc.com/videos/tk750r/elizabeth-de-la-vega",
        "http://thecolbertreport.cc.com/videos/dntxcy/green-screen-challenge---counter-challenge",
        "http://thecolbertreport.cc.com/videos/4koanp/alpha-dog-of-the-week---john-bolton",
        "http://thecolbertreport.cc.com/videos/dqyz7h/francis-collins",
        "http://thecolbertreport.cc.com/videos/rqe98q/sign-off---tgit"
      ],
      "guest": "Dr. Francis S. Collins"
    },
    {
      "date": "2006-12-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ri4vbo/intro---12-11-06",
        "http://thecolbertreport.cc.com/videos/t0abnh/defending-rosie",
        "http://thecolbertreport.cc.com/videos/uea9ov/jack-kingston",
        "http://thecolbertreport.cc.com/videos/k0a3hu/the-white-christmas-album",
        "http://thecolbertreport.cc.com/videos/2cea2e/threatdown---christmas-style",
        "http://thecolbertreport.cc.com/videos/bqpkoy/peter-singer",
        "http://thecolbertreport.cc.com/videos/5alg6c/got-your-back"
      ],
      "guest": "Dr. Peter Singer"
    },
    {
      "date": "2006-12-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/35u0ts/intro---12-12-06",
        "http://thecolbertreport.cc.com/videos/kn0mlp/augusto-pinochet-s-coup",
        "http://thecolbertreport.cc.com/videos/dctycd/shout-out----beef-hammer-flag",
        "http://thecolbertreport.cc.com/videos/1o4xvk/the-word---casualty-of-war",
        "http://thecolbertreport.cc.com/videos/e1504w/who-s-honoring-me-now----merriam-webster-s-word-of-the-year",
        "http://thecolbertreport.cc.com/videos/xd9itr/better-know-a-district---new-members-of-congress-at-the-kennedy-school",
        "http://thecolbertreport.cc.com/videos/j01zz1/dan-savage",
        "http://thecolbertreport.cc.com/videos/s3gs7u/sign-off---post-show-taco-bell-chalupa-chow-down"
      ],
      "guest": "Dan Savage"
    },
    {
      "date": "2006-12-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6ohkja/intro---12-13-06",
        "http://thecolbertreport.cc.com/videos/yl018s/stephen-jr--s-christmas-miracle",
        "http://thecolbertreport.cc.com/videos/suc40d/the-word---it-s-a-small-world",
        "http://thecolbertreport.cc.com/videos/5uk9gs/replenishing-the-eggnog-supply",
        "http://thecolbertreport.cc.com/videos/d0ml1u/sea-tac-s-christmas-trees-restored",
        "http://thecolbertreport.cc.com/videos/x1f8dg/doris-kearns-goodwin",
        "http://thecolbertreport.cc.com/videos/0kcywr/charge-me-twice-for-stephen"
      ],
      "guest": "Doris Kearns Goodwin"
    },
    {
      "date": "2006-12-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lwojc9/intro---12-14-06",
        "http://thecolbertreport.cc.com/videos/3moulc/finger-strengthening",
        "http://thecolbertreport.cc.com/videos/5dvej7/the-american-people-are-to-blame",
        "http://thecolbertreport.cc.com/videos/60ds73/the-word---clarity",
        "http://thecolbertreport.cc.com/videos/klp05i/blood-in-the-water---bruce-tinsley-s-dui",
        "http://thecolbertreport.cc.com/videos/wauy3f/caesar-honeybee-or-tyrone-hunnibi-",
        "http://thecolbertreport.cc.com/videos/yaoen5/daniel-pinchbeck",
        "http://thecolbertreport.cc.com/videos/ua9gte/letter-to-representative-jack-kingston"
      ],
      "guest": "Daniel Pinchbeck"
    },
    {
      "date": "2006-12-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t66x66/intro---12-18-06",
        "http://thecolbertreport.cc.com/videos/j56gn9/diy-cold-medicine",
        "http://thecolbertreport.cc.com/videos/ndrsqu/profiles-in-balls",
        "http://thecolbertreport.cc.com/videos/mv0dai/the-word---the-draft",
        "http://thecolbertreport.cc.com/videos/c4vji3/tip-wag---art-edition",
        "http://thecolbertreport.cc.com/videos/nnpc32/jack-welch",
        "http://thecolbertreport.cc.com/videos/yy82av/the-jingle-terns"
      ],
      "guest": "Jack Welch"
    },
    {
      "date": "2006-12-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/an4q7j/intro---12-19-06",
        "http://thecolbertreport.cc.com/videos/q9o6sw/person-of-the-year",
        "http://thecolbertreport.cc.com/videos/qh5kz9/stephen-goes-to-harvard",
        "http://thecolbertreport.cc.com/videos/v81egv/deepak-chopra",
        "http://thecolbertreport.cc.com/videos/3fhkpv/face-off-preview",
        "http://thecolbertreport.cc.com/videos/kza2d8/the-word---tit-for-tat"
      ],
      "guest": "Deepak Chopra"
    },
    {
      "date": "2006-12-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ouau0r/intro---12-20-06",
        "http://thecolbertreport.cc.com/videos/8t5vas/rock-and-awe--countdown-to-guitarmageddon",
        "http://thecolbertreport.cc.com/videos/lyahfg/shreddown",
        "http://thecolbertreport.cc.com/videos/iocz1g/chris-funk",
        "http://thecolbertreport.cc.com/videos/4hpbzt/peter-frampton",
        "http://thecolbertreport.cc.com/videos/m75mj9/shreddown---the-judgment"
      ],
      "guest": "Howard Zinn"
    }
  ],
  "2007": [
    {
      "date": "2007-01-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/35rb23/intro---1-8-07",
        "http://thecolbertreport.cc.com/videos/liauyt/the-gallotastic-executacular---hangin--with-mr--hussein",
        "http://thecolbertreport.cc.com/videos/2eciiy/the-word---facts",
        "http://thecolbertreport.cc.com/videos/vfxu06/who-s-attacking-me-now----lake-superior-state-university",
        "http://thecolbertreport.cc.com/videos/ya0sji/who-s-honoring-me-now----gay-com",
        "http://thecolbertreport.cc.com/videos/uuhxlg/stephen-s-sound-advice---surviving-the-winter-blues",
        "http://thecolbertreport.cc.com/videos/duytly/ethan-nadelmann"
      ],
      "guest": "Ethan Nadelmann"
    },
    {
      "date": "2007-01-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oxq1cl/not-a-sex-scandal",
        "http://thecolbertreport.cc.com/videos/rsuyoo/intro---1-9-07",
        "http://thecolbertreport.cc.com/videos/a9e13e/the-word---texas-hold--em",
        "http://thecolbertreport.cc.com/videos/bmmv86/ohio-state-loses",
        "http://thecolbertreport.cc.com/videos/1yhdmp/we-the-mediator---celebrity-feuds",
        "http://thecolbertreport.cc.com/videos/ezqjm4/jim-cramer",
        "http://thecolbertreport.cc.com/videos/q6rkb3/sign-off---farewell--james-brown"
      ],
      "guest": "Jim Cramer"
    },
    {
      "date": "2007-01-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b3d5l1/intro---1-10-07",
        "http://thecolbertreport.cc.com/videos/j5htgu/president-s-speech",
        "http://thecolbertreport.cc.com/videos/crgbvq/invasion-of-the-country-snatchers",
        "http://thecolbertreport.cc.com/videos/ie5gtu/the-word---worry",
        "http://thecolbertreport.cc.com/videos/048s3c/tek-jansen---hounds-of-hell--ragtime-billy-peaches",
        "http://thecolbertreport.cc.com/videos/ku9y06/david-kamp",
        "http://thecolbertreport.cc.com/videos/9nuye7/sign-off---thawing-meat"
      ],
      "guest": "David Kamp"
    },
    {
      "date": "2007-01-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/21xsg9/intro---1-11-07",
        "http://thecolbertreport.cc.com/videos/nhwjcd/what-number-is-stephen-thinking-of----doubled-up",
        "http://thecolbertreport.cc.com/videos/7v6i3c/ken-roth",
        "http://thecolbertreport.cc.com/videos/jxfsrm/tip-wag---science-and-technology",
        "http://thecolbertreport.cc.com/videos/fxnp1o/judy-woodruff"
      ],
      "guest": "Judy Woodruff"
    },
    {
      "date": "2007-01-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tpjoll/intro---1-15-07",
        "http://thecolbertreport.cc.com/videos/bemyqb/inspired-by-dr--king",
        "http://thecolbertreport.cc.com/videos/ni7g5j/a-man-s-touch",
        "http://thecolbertreport.cc.com/videos/xb55y0/the-word---victory-",
        "http://thecolbertreport.cc.com/videos/eamlaf/bears---balls---gas",
        "http://thecolbertreport.cc.com/videos/o7xhwp/alex-kuczynski"
      ],
      "guest": "Alex Kuczynski"
    },
    {
      "date": "2007-01-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/795pdp/intro---1-16-07",
        "http://thecolbertreport.cc.com/videos/ycpx4s/squeaky-chair",
        "http://thecolbertreport.cc.com/videos/r7kinv/pesos-for-pizza",
        "http://thecolbertreport.cc.com/videos/hwlhus/the-word---symbolic",
        "http://thecolbertreport.cc.com/videos/6q6sy0/sport-report---bend-it-like-beckham",
        "http://thecolbertreport.cc.com/videos/2tdkm8/dinesh-d-souza"
      ],
      "guest": "Dinesh D'Souza"
    },
    {
      "date": "2007-01-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ufcy26/intro---1-17-07",
        "http://thecolbertreport.cc.com/videos/8amkmh/200th-episode",
        "http://thecolbertreport.cc.com/videos/wjuko4/lynn-swann",
        "http://thecolbertreport.cc.com/videos/xv8tlv/better-know-a-district---washington-s-3rd---brian-baird",
        "http://thecolbertreport.cc.com/videos/1qdsbp/richard-clarke"
      ],
      "guest": "Richard Clarke"
    },
    {
      "date": "2007-01-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z0tcp1/intro---1-18-07",
        "http://thecolbertreport.cc.com/videos/kyc2cd/the-advent-of-o-reilly",
        "http://thecolbertreport.cc.com/videos/qtrfgo/the-word---go-it-alone",
        "http://thecolbertreport.cc.com/videos/dre6df/we-the-mediator---trump-v--o-donnell",
        "http://thecolbertreport.cc.com/videos/9seimt/bill-o-reilly",
        "http://thecolbertreport.cc.com/videos/cuouel/o-reilly-s-microwave"
      ],
      "guest": "Bill O'Reilly"
    },
    {
      "date": "2007-01-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9vl9tx/intro---1-22-07",
        "http://thecolbertreport.cc.com/videos/1t56vq/the-bears",
        "http://thecolbertreport.cc.com/videos/itbxtv/who-s-riding-my-coattails-now----terence-koh",
        "http://thecolbertreport.cc.com/videos/mfzk22/the-word---exact-words",
        "http://thecolbertreport.cc.com/videos/opisk9/balls-for-kidz---gambling",
        "http://thecolbertreport.cc.com/videos/rnd3lf/tom-schaller",
        "http://thecolbertreport.cc.com/videos/6mgw6m/sign-off---zeppelin-reunion"
      ],
      "guest": "Tom Schaller"
    },
    {
      "date": "2007-01-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xjsnlx/intro---1-23-07",
        "http://thecolbertreport.cc.com/videos/ebff8o/pre-tape",
        "http://thecolbertreport.cc.com/videos/vm00zm/lieber-vs--lieber",
        "http://thecolbertreport.cc.com/videos/jv328p/threatdown---the-weather-channel",
        "http://thecolbertreport.cc.com/videos/y849ls/michael-steele",
        "http://thecolbertreport.cc.com/videos/xxwpqf/wednesday-today"
      ],
      "guest": "Michael Steele"
    },
    {
      "date": "2007-01-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/goh39c/intro---1-24-07",
        "http://thecolbertreport.cc.com/videos/gzqy8i/state-of-the-union---cheney-wins",
        "http://thecolbertreport.cc.com/videos/e17mq9/the-word---great-news",
        "http://thecolbertreport.cc.com/videos/3525mn/better-know-a-district---pennsylvania-s-4th---jason-altmire",
        "http://thecolbertreport.cc.com/videos/r5j10b/lou-dobbs"
      ],
      "guest": "Lou Dobbs"
    },
    {
      "date": "2007-01-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n139mj/intro---1-25-07",
        "http://thecolbertreport.cc.com/videos/7z0x1m/right-away-",
        "http://thecolbertreport.cc.com/videos/5rmbin/the-word---smafu",
        "http://thecolbertreport.cc.com/videos/hkzk11/sport-report---more-with-coach-mancini",
        "http://thecolbertreport.cc.com/videos/tufln6/mike-wallace"
      ],
      "guest": "Mike Wallace"
    },
    {
      "date": "2007-01-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/o0maxx/intro---1-29-07",
        "http://thecolbertreport.cc.com/videos/1m6mdm/new-york-grieves",
        "http://thecolbertreport.cc.com/videos/z0b9vz/stephen-colbert-day",
        "http://thecolbertreport.cc.com/videos/6p6df7/the-word---wikilobbying",
        "http://thecolbertreport.cc.com/videos/11js13/tip-wag---tom-cruise",
        "http://thecolbertreport.cc.com/videos/zqi973/barry-lando"
      ],
      "guest": "Barry M. Lando"
    },
    {
      "date": "2007-01-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/np3o3k/intro---1-30-07",
        "http://thecolbertreport.cc.com/videos/j1sd5a/new-military-weapon",
        "http://thecolbertreport.cc.com/videos/cv6q8o/david-leonhardt",
        "http://thecolbertreport.cc.com/videos/ttzs6x/caviar-omelets-for-the-troops",
        "http://thecolbertreport.cc.com/videos/bsbad5/judge--jury---executioner---adultery",
        "http://thecolbertreport.cc.com/videos/eyhp38/donna-shalala",
        "http://thecolbertreport.cc.com/videos/dwv24s/sign-off---microwave-gift-to-o-reilly"
      ],
      "guest": "Donna Shalala"
    },
    {
      "date": "2007-01-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/84e6zh/exclusive---better-know-a-district---new-york-s-6th---gregory-meeks",
        "http://thecolbertreport.cc.com/videos/4mp2yh/intro---1-31-07",
        "http://thecolbertreport.cc.com/videos/v1la3q/global-warming",
        "http://thecolbertreport.cc.com/videos/3emlxq/on-notice---jane-fonda-fantasies",
        "http://thecolbertreport.cc.com/videos/qg7l5c/the-word---black-sheep",
        "http://thecolbertreport.cc.com/videos/4lodkc/better-know-a-district---new-york-s-6th---gregory-meeks",
        "http://thecolbertreport.cc.com/videos/npjb41/jed-babbin"
      ],
      "guest": "Jed Babbin"
    },
    {
      "date": "2007-02-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/89lmed/intro---2-1-07",
        "http://thecolbertreport.cc.com/videos/mzq0ue/cartoon-terrorism",
        "http://thecolbertreport.cc.com/videos/492fjx/ending-racism",
        "http://thecolbertreport.cc.com/videos/rbb68f/the-word---we-shall-overcome",
        "http://thecolbertreport.cc.com/videos/2m3ntu/movies-that-are-destroying-america---oscars-edition",
        "http://thecolbertreport.cc.com/videos/s2k3ll/chuck-schumer",
        "http://thecolbertreport.cc.com/videos/b1j62r/the-most-poetic-f--king-thing-i-ve-ever-heard"
      ],
      "guest": "Sen. Chuck Schumer"
    },
    {
      "date": "2007-02-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qonzal/intro---2-5-07",
        "http://thecolbertreport.cc.com/videos/raqy45/peyton-manseed",
        "http://thecolbertreport.cc.com/videos/1ppbxw/save-stephen-jr-",
        "http://thecolbertreport.cc.com/videos/pkx5sp/the-word---second-opinion",
        "http://thecolbertreport.cc.com/videos/cu6q1h/threatdown---giant-mexican-babies",
        "http://thecolbertreport.cc.com/videos/qj7ov5/wendy-kopp"
      ],
      "guest": "Wendy Kopp"
    },
    {
      "date": "2007-02-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/irg0ck/exclusive---better-know-a-district---ohio-s-18th---zack-space-pt--1",
        "http://thecolbertreport.cc.com/videos/7vpqnl/exclusive---better-know-a-district---ohio-s-18th---zack-space-pt--2",
        "http://thecolbertreport.cc.com/videos/w05aan/intro---2-6-07",
        "http://thecolbertreport.cc.com/videos/rirgzz/pray-for-stephen",
        "http://thecolbertreport.cc.com/videos/ronvu0/the-word---making-a-killing",
        "http://thecolbertreport.cc.com/videos/sh2kz6/better-know-a-district---ohio-s-18th---zack-space",
        "http://thecolbertreport.cc.com/videos/vnbq6e/charles-leduff"
      ],
      "guest": "Charlie LeDuff"
    },
    {
      "date": "2007-02-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lh3p6z/intro---2-7-07",
        "http://thecolbertreport.cc.com/videos/skowle/the-san-francisco-treat",
        "http://thecolbertreport.cc.com/videos/hx3kkt/california-values-watch",
        "http://thecolbertreport.cc.com/videos/fykjnf/the-word---silence",
        "http://thecolbertreport.cc.com/videos/pp2kiz/tek-jansen---from-the-future",
        "http://thecolbertreport.cc.com/videos/n36pgb/steven-pinker"
      ],
      "guest": "Steven Pinker"
    },
    {
      "date": "2007-02-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5l6ygo/intro---2-8-07",
        "http://thecolbertreport.cc.com/videos/btxrus/space-madness",
        "http://thecolbertreport.cc.com/videos/q5bcg9/stephen-for-president---a-sign",
        "http://thecolbertreport.cc.com/videos/12d71h/debra-dickerson",
        "http://thecolbertreport.cc.com/videos/ls3y3l/was-it-really-that-bad----salem-witch-trials",
        "http://thecolbertreport.cc.com/videos/m5tx4f/chris-hedges"
      ],
      "guest": "Chris Hedges"
    },
    {
      "date": "2007-02-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sudz5h/intro---2-12-07",
        "http://thecolbertreport.cc.com/videos/cvs0b4/the-word---inappropriate",
        "http://thecolbertreport.cc.com/videos/wetex5/tip-wag---john-howard",
        "http://thecolbertreport.cc.com/videos/ovmu6y/michael-oppenheimer",
        "http://thecolbertreport.cc.com/videos/gbc95s/alpha-dog-of-the-week---amitabh-bachchan"
      ],
      "guest": "Michael Oppenheimer"
    },
    {
      "date": "2007-02-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7zlyvc/the-word---apocalypse-mao--murdered-by-the-orient-s-success---frenemy",
        "http://thecolbertreport.cc.com/videos/dh1nxa/apocalypse-mao--murdered-by-the-orient-s-success---take-the-pulse",
        "http://thecolbertreport.cc.com/videos/cbgmhg/sheryl-wudunn",
        "http://thecolbertreport.cc.com/videos/rewkbj/apocalypse-mao--murdered-by-the-orient-s-success---eight-child-policy"
      ],
      "guest": "Sheryl WuDunn"
    },
    {
      "date": "2007-02-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0unos7/catching-up-with-china",
        "http://thecolbertreport.cc.com/videos/sv6om5/safe-sex-for-senior-citizens",
        "http://thecolbertreport.cc.com/videos/qngp8d/the-word---bad-medicine",
        "http://thecolbertreport.cc.com/videos/e7leqz/stephen-protects-valentine-s-day",
        "http://thecolbertreport.cc.com/videos/npsgvg/sport-report---westminster-kennel-club-dog-show",
        "http://thecolbertreport.cc.com/videos/tv0pg5/lance-armstrong",
        "http://thecolbertreport.cc.com/videos/4zrnjn/intro---2-14-07"
      ],
      "guest": "Lance Armstrong"
    },
    {
      "date": "2007-02-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bemh6r/intro---2-15-07",
        "http://thecolbertreport.cc.com/videos/5h0hc1/the-365-most-influential-cultural-figures-of-2007---j-j--abrams",
        "http://thecolbertreport.cc.com/videos/dv94hn/helen-thomas-s-chair",
        "http://thecolbertreport.cc.com/videos/xsukru/the-365-most-influential-cultural-figures-of-2007---candice-bergen",
        "http://thecolbertreport.cc.com/videos/gxjtk4/better-know-a-district---arkansas--2nd---vic-snyder",
        "http://thecolbertreport.cc.com/videos/htsqly/shashi-tharoor"
      ],
      "guest": "Shashi Tharoor"
    },
    {
      "date": "2007-02-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7kzllg/intro---2-26-07",
        "http://thecolbertreport.cc.com/videos/6q3fey/the-word---success",
        "http://thecolbertreport.cc.com/videos/liy97p/stephen-s-sound-advice---avoiding-humiliation-on-the-campaign-trail",
        "http://thecolbertreport.cc.com/videos/rj64v2/zev-chafets",
        "http://thecolbertreport.cc.com/videos/lto66u/sign-off---the-stupidest-person-in-the-world"
      ],
      "guest": "Zev Chafets"
    },
    {
      "date": "2007-02-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m6llmb/intro---2-27-07",
        "http://thecolbertreport.cc.com/videos/4q8yqr/gore-s-garbage",
        "http://thecolbertreport.cc.com/videos/08vl33/the-word---recoil",
        "http://thecolbertreport.cc.com/videos/kyuvud/dead-to-me---raptors",
        "http://thecolbertreport.cc.com/videos/a5eovz/tip-wag---bilk",
        "http://thecolbertreport.cc.com/videos/xtu2o9/craig-venter"
      ],
      "guest": "Dr. Craig Venter"
    },
    {
      "date": "2007-02-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/k64d0x/intro---2-28-07",
        "http://thecolbertreport.cc.com/videos/94efgl/david-geffen-the-intern-",
        "http://thecolbertreport.cc.com/videos/ax1yhn/obama-vs--colbert",
        "http://thecolbertreport.cc.com/videos/2j1fug/profiles-in-quitters---tom-vilsack",
        "http://thecolbertreport.cc.com/videos/2w1ttr/problems-without-solutions--stay-at-home-dads",
        "http://thecolbertreport.cc.com/videos/rjcwpq/nina-jablonski"
      ],
      "guest": "Nina Jablonski"
    },
    {
      "date": "2007-03-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uvhlbh/intro---3-1-07",
        "http://thecolbertreport.cc.com/videos/dnoicn/jesus--1-",
        "http://thecolbertreport.cc.com/videos/09pfnw/the-word---bury-the-lead",
        "http://thecolbertreport.cc.com/videos/xp8ghf/better-know-a-district---tennessee-s-9th---steve-cohen",
        "http://thecolbertreport.cc.com/videos/hdb72u/larry-king",
        "http://thecolbertreport.cc.com/videos/din9ey/sign-off---all-the-time"
      ],
      "guest": "Larry King"
    },
    {
      "date": "2007-03-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s5zpws/intro---3-5-07",
        "http://thecolbertreport.cc.com/videos/f0veng/stop-the-war-in-congress",
        "http://thecolbertreport.cc.com/videos/9rmkm6/ben-and-jerry---introducing-americone-dream",
        "http://thecolbertreport.cc.com/videos/erco0p/bears---balls---bees",
        "http://thecolbertreport.cc.com/videos/w9i285/mara-vanderslice",
        "http://thecolbertreport.cc.com/videos/u5x46t/sign-off---you-get-a-pint-"
      ],
      "guest": "Mara Vanderslice, Ben and Jerry"
    },
    {
      "date": "2007-03-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jokvk3/intro---3-6-07",
        "http://thecolbertreport.cc.com/videos/987dug/stephen-wins-the-lottery",
        "http://thecolbertreport.cc.com/videos/5xpqn0/libby-verdict",
        "http://thecolbertreport.cc.com/videos/yjwisn/the-word---wwjd",
        "http://thecolbertreport.cc.com/videos/ryt5zt/threatdown---cheney-s-clot",
        "http://thecolbertreport.cc.com/videos/d9k0w9/mark-frauenfelder"
      ],
      "guest": "Mark Frauenfelder"
    },
    {
      "date": "2007-03-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t3l2qk/intro---3-7-07",
        "http://thecolbertreport.cc.com/videos/o5rj01/mega-millions",
        "http://thecolbertreport.cc.com/videos/f4wilr/the-word---don-t",
        "http://thecolbertreport.cc.com/videos/mw47n3/easter-under-attack---bunny",
        "http://thecolbertreport.cc.com/videos/k8n6ln/michael-spector",
        "http://thecolbertreport.cc.com/videos/eu60l7/sign-off---colbert-savings-time"
      ],
      "guest": "Michael Specter"
    },
    {
      "date": "2007-03-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hdanpb/exclusive---better-know-a-district---kentucky-s-3rd---john-yarmuth-pt--1",
        "http://thecolbertreport.cc.com/videos/1fsr4r/exclusive---better-know-a-district---kentucky-s-3rd---john-yarmuth-pt--2",
        "http://thecolbertreport.cc.com/videos/v9pxbp/intro---3-8-07",
        "http://thecolbertreport.cc.com/videos/fkezkh/jesus-libby",
        "http://thecolbertreport.cc.com/videos/kf01z4/the-word---comic-justice",
        "http://thecolbertreport.cc.com/videos/gfi7dr/better-know-a-district---kentucky-s-3rd---john-yarmuth",
        "http://thecolbertreport.cc.com/videos/na2cwe/ted-koppel"
      ],
      "guest": "Ted Koppel"
    },
    {
      "date": "2007-03-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eoubiy/intro---3-12-07",
        "http://thecolbertreport.cc.com/videos/cxle7m/newt-gingrich-s-extramarital-affair",
        "http://thecolbertreport.cc.com/videos/qs3d07/the-word---home-field-advantage",
        "http://thecolbertreport.cc.com/videos/rp8fy7/tip-wag---u-s--mint",
        "http://thecolbertreport.cc.com/videos/0z68wk/nicholas-kristof",
        "http://thecolbertreport.cc.com/videos/paedah/sign-off---captain-america-shield"
      ],
      "guest": "Nicholas D. Kristof"
    },
    {
      "date": "2007-03-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3gv9du/intro---3-13-07",
        "http://thecolbertreport.cc.com/videos/n1695w/time-travel",
        "http://thecolbertreport.cc.com/videos/o93g04/willie-nelson-s-cobbler",
        "http://thecolbertreport.cc.com/videos/aln9gt/donald-shields",
        "http://thecolbertreport.cc.com/videos/nebseq/four-horsemen-of-the-a-pop-calypse---300",
        "http://thecolbertreport.cc.com/videos/pajwaw/michael-eric-dyson",
        "http://thecolbertreport.cc.com/videos/goeagu/the-word---goodnight"
      ],
      "guest": "Michael Eric Dyson"
    },
    {
      "date": "2007-03-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gjg322/intro---3-14-07",
        "http://thecolbertreport.cc.com/videos/mi3odp/when-ancestors-attack---barack-obama",
        "http://thecolbertreport.cc.com/videos/jdieqt/the-word---high-fidelity",
        "http://thecolbertreport.cc.com/videos/6t5ydk/rocky-mountain-high",
        "http://thecolbertreport.cc.com/videos/xy5mon/sport-report---ncaa",
        "http://thecolbertreport.cc.com/videos/3w6h8k/ed-viesturs",
        "http://thecolbertreport.cc.com/videos/x40idi/sign-off---united-we-lick"
      ],
      "guest": "Ed Viesturs"
    },
    {
      "date": "2007-03-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3yjwcu/exclusive---better-know-a-district---illinois--17th---phil-hare-pt--1",
        "http://thecolbertreport.cc.com/videos/l2j89r/exclusive---better-know-a-district---illinois--17th---phil-hare-pt--2",
        "http://thecolbertreport.cc.com/videos/gjg322/intro---3-14-07",
        "http://thecolbertreport.cc.com/videos/mi3odp/when-ancestors-attack---barack-obama",
        "http://thecolbertreport.cc.com/videos/jdieqt/the-word---high-fidelity",
        "http://thecolbertreport.cc.com/videos/6t5ydk/rocky-mountain-high",
        "http://thecolbertreport.cc.com/videos/xy5mon/sport-report---ncaa",
        "http://thecolbertreport.cc.com/videos/3w6h8k/ed-viesturs",
        "http://thecolbertreport.cc.com/videos/x40idi/sign-off---united-we-lick"
      ],
      "guest": "Ayaan Hirsi Ali"
    },
    {
      "date": "2007-03-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/in8gsh/intro---3-15-07",
        "http://thecolbertreport.cc.com/videos/ojcmho/st--patrick-s-day",
        "http://thecolbertreport.cc.com/videos/9wsh6f/better-know-a-district---illinois--17th---phil-hare",
        "http://thecolbertreport.cc.com/videos/pvxlng/ayaan-hirsi-ali",
        "http://thecolbertreport.cc.com/videos/nfjx5l/sign-off---candy"
      ],
      "guest": "Ayaan Hirsi Ali"
    },
    {
      "date": "2007-03-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/akdm39/intro---3-19-07",
        "http://thecolbertreport.cc.com/videos/zfhuml/emanuel-attacks-stephen",
        "http://thecolbertreport.cc.com/videos/ichd6m/the-word---pound-of-flesh",
        "http://thecolbertreport.cc.com/videos/ovsoy3/willie-nelson-tomorrow",
        "http://thecolbertreport.cc.com/videos/i34oa7/threatdown---seniors",
        "http://thecolbertreport.cc.com/videos/nby1fe/jerome-groopman",
        "http://thecolbertreport.cc.com/videos/woj3kf/alpha-dog-of-the-week---pennies"
      ],
      "guest": "Jerome Groopman"
    },
    {
      "date": "2007-03-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nepea4/intro---3-20-07",
        "http://thecolbertreport.cc.com/videos/p3nkju/willie-recall",
        "http://thecolbertreport.cc.com/videos/8w2rhi/the-word---supernatural",
        "http://thecolbertreport.cc.com/videos/4fyygp/threatdown---polar-bear-cub",
        "http://thecolbertreport.cc.com/videos/rn79kl/stephen-colbert-day---honor",
        "http://thecolbertreport.cc.com/videos/fxdmt0/willie-nelson"
      ],
      "guest": "Willie Nelson"
    },
    {
      "date": "2007-03-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b4r6li/intro---3-21-07",
        "http://thecolbertreport.cc.com/videos/r7dj9j/stephen-s-stoned-friend",
        "http://thecolbertreport.cc.com/videos/wyig4v/impeach-bush",
        "http://thecolbertreport.cc.com/videos/js464k/the-word---sex",
        "http://thecolbertreport.cc.com/videos/6b13mn/better-know-a-district---new-york-s-22nd---maurice-hinchey",
        "http://thecolbertreport.cc.com/videos/4jygnv/benjamin-barber",
        "http://thecolbertreport.cc.com/videos/psro3f/sign-off---goodnights"
      ],
      "guest": "Benjamin Barber"
    },
    {
      "date": "2007-03-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rf90w7/intro---3-22-07",
        "http://thecolbertreport.cc.com/videos/yic3o0/infomosexual-graphics",
        "http://thecolbertreport.cc.com/videos/ez9npn/eleanor-holmes-norton",
        "http://thecolbertreport.cc.com/videos/xgjo8q/face-reading-expert",
        "http://thecolbertreport.cc.com/videos/pd3hdf/sport-report---ncaa-final-four",
        "http://thecolbertreport.cc.com/videos/i2wwym/katie-couric",
        "http://thecolbertreport.cc.com/videos/k6m8na/sign-off---future"
      ],
      "guest": "Katie Couric"
    },
    {
      "date": "2007-03-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/k1iiew/intro---3-26-07",
        "http://thecolbertreport.cc.com/videos/t9n8i2/mummy",
        "http://thecolbertreport.cc.com/videos/t7x0xg/torture-gonzales",
        "http://thecolbertreport.cc.com/videos/hc58hq/for-your-editing-pleasure",
        "http://thecolbertreport.cc.com/videos/r6ez6r/stephen-colbert-day",
        "http://thecolbertreport.cc.com/videos/a19udk/john-perry-barlow",
        "http://thecolbertreport.cc.com/videos/dc5qfy/sign-off---photo-op"
      ],
      "guest": "John Perry Barlow"
    },
    {
      "date": "2007-03-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9hzwxa/intro---3-2707",
        "http://thecolbertreport.cc.com/videos/ct77qc/sean-penn-unleashes-on-president-bush",
        "http://thecolbertreport.cc.com/videos/y05sqg/madeleine-albright",
        "http://thecolbertreport.cc.com/videos/ac6sto/tip-wag---drug-dealers",
        "http://thecolbertreport.cc.com/videos/z3a4ow/james-fallows"
      ],
      "guest": "Madeleine Albright, James Fallows"
    },
    {
      "date": "2007-03-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c3lbed/intro---3-28-07",
        "http://thecolbertreport.cc.com/videos/8b58j1/dancing-with-the-stars",
        "http://thecolbertreport.cc.com/videos/eoe8d4/claim-to-the-arctic",
        "http://thecolbertreport.cc.com/videos/e6rbbg/the-word---monkey-business",
        "http://thecolbertreport.cc.com/videos/7t7l7y/the-axis-of-evil-of-the-week",
        "http://thecolbertreport.cc.com/videos/oval1w/jabari-asim",
        "http://thecolbertreport.cc.com/videos/tffkup/sign-off---going-to-bed-angry"
      ],
      "guest": "Jabari Asim"
    },
    {
      "date": "2007-03-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/82ki4g/intro---3-29-07",
        "http://thecolbertreport.cc.com/videos/yp03mv/equal-rights",
        "http://thecolbertreport.cc.com/videos/bwtu8b/strolling-in-baghdad",
        "http://thecolbertreport.cc.com/videos/m1iokb/the-word---lemon-raid",
        "http://thecolbertreport.cc.com/videos/rmylpg/alpha-dog-of-the-week---toby",
        "http://thecolbertreport.cc.com/videos/dune0v/nightgown-novel-model",
        "http://thecolbertreport.cc.com/videos/gp6vcm/clive-james",
        "http://thecolbertreport.cc.com/videos/cnmwu7/sign-off---it-s-been-real"
      ],
      "guest": "Clive James"
    },
    {
      "date": "2007-04-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2secqi/intro---4-9-07",
        "http://thecolbertreport.cc.com/videos/c2ss4c/end-of-lent",
        "http://thecolbertreport.cc.com/videos/jdh0qr/colin-beavan",
        "http://thecolbertreport.cc.com/videos/p1vkhv/ethnic-slurs",
        "http://thecolbertreport.cc.com/videos/uyodpo/formula-401k",
        "http://thecolbertreport.cc.com/videos/d7vjve/katrina-vanden-heuvel",
        "http://thecolbertreport.cc.com/videos/vx3kr4/sign-off---goodnight--ladies"
      ],
      "guest": "Colin Beavan, Katrina vanden Heuvel"
    },
    {
      "date": "2007-04-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gqey9e/intro---4-10-07",
        "http://thecolbertreport.cc.com/videos/t52s2y/stiff-upper-lip",
        "http://thecolbertreport.cc.com/videos/7xhdfc/the-word---hip-replacement",
        "http://thecolbertreport.cc.com/videos/a6j19l/stephen-s-racial-slurs",
        "http://thecolbertreport.cc.com/videos/mmtey6/bears---balls---home",
        "http://thecolbertreport.cc.com/videos/niryzs/jeannette-walls",
        "http://thecolbertreport.cc.com/videos/tjfkfk/the-apology"
      ],
      "guest": "Jeannette Walls"
    },
    {
      "date": "2007-04-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ikived/intro---4-11-07",
        "http://thecolbertreport.cc.com/videos/rndpay/the-great-turtle-race",
        "http://thecolbertreport.cc.com/videos/o57n2d/the-word---season-pass",
        "http://thecolbertreport.cc.com/videos/y3z7pz/anna-nicole-s-baby-daddy",
        "http://thecolbertreport.cc.com/videos/qk7xuu/sport-report---spirit-loses",
        "http://thecolbertreport.cc.com/videos/6ombuy/vali-nasr",
        "http://thecolbertreport.cc.com/videos/py0zro/sign-off---not-literally"
      ],
      "guest": "Vali Nasr"
    },
    {
      "date": "2007-04-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tvo9j1/intro---4-12-07",
        "http://thecolbertreport.cc.com/videos/44wpo2/the-pope-and-iraq",
        "http://thecolbertreport.cc.com/videos/i2w6da/the-word---body-armor",
        "http://thecolbertreport.cc.com/videos/rp5qr3/a-girl-for-stephen-jr-",
        "http://thecolbertreport.cc.com/videos/szc2kp/dr--richard-land",
        "http://thecolbertreport.cc.com/videos/z4a9cf/sign-off---french-canadian-viewers"
      ],
      "guest": "Dr. Richard Land"
    },
    {
      "date": "2007-04-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/opgo7c/intro---4-16-07",
        "http://thecolbertreport.cc.com/videos/ow68vg/mope-retraction",
        "http://thecolbertreport.cc.com/videos/ndyxmi/the-metaphor-off-is-on",
        "http://thecolbertreport.cc.com/videos/fiwckw/the-word---clean-slate",
        "http://thecolbertreport.cc.com/videos/vsf7vy/paulina-likes-stephen",
        "http://thecolbertreport.cc.com/videos/le9tdo/alpha-dog-of-the-week---paul-wolfowitz",
        "http://thecolbertreport.cc.com/videos/yq2yld/sign-off---fondest-memories",
        "http://thecolbertreport.cc.com/videos/1dnqiw/john-kerry"
      ],
      "guest": "Sen. John Kerry"
    },
    {
      "date": "2007-04-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/35u6vo/metaphor-off-training",
        "http://thecolbertreport.cc.com/videos/ctnp41/turtle-race-update",
        "http://thecolbertreport.cc.com/videos/k0gjix/the-word---plan-b",
        "http://thecolbertreport.cc.com/videos/1ca1nf/tip-wag---fake-sperm",
        "http://thecolbertreport.cc.com/videos/ofyxod/elaine-pagels",
        "http://thecolbertreport.cc.com/videos/ka39h6/sign-off---stephen-s-taxes",
        "http://thecolbertreport.cc.com/videos/28ne1f/intro---4-17-07"
      ],
      "guest": "Elaine Pagels"
    },
    {
      "date": "2007-04-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xjlfa3/intro---4-18-07",
        "http://thecolbertreport.cc.com/videos/z7yfgh/who-s-not-honoring-me-now----pulitzer",
        "http://thecolbertreport.cc.com/videos/y8uyv4/the-word---branding",
        "http://thecolbertreport.cc.com/videos/d5i37n/national-library-week---frank-mccourt",
        "http://thecolbertreport.cc.com/videos/hr8hfi/milk---hormones",
        "http://thecolbertreport.cc.com/videos/edyu8c/national-library-week---sebastian-junger",
        "http://thecolbertreport.cc.com/videos/ebje1q/national-library-week---david-remnick",
        "http://thecolbertreport.cc.com/videos/33tv9j/paulina-porizkova",
        "http://thecolbertreport.cc.com/videos/tn0cbn/sign-off---upcoming-metaphor-off"
      ],
      "guest": "William Cohen"
    },
    {
      "date": "2007-04-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wh0xf2/intro---4-19-07",
        "http://thecolbertreport.cc.com/videos/luoh3l/god-s-pet-chimp",
        "http://thecolbertreport.cc.com/videos/goj3np/the-word----400-haircut",
        "http://thecolbertreport.cc.com/videos/tv447i/sean-penn",
        "http://thecolbertreport.cc.com/videos/iowvf0/meta-free-phor-all--shall-i-nail-thee-to-a-summer-s-day-",
        "http://thecolbertreport.cc.com/videos/nzuytf/hyperbole-off"
      ],
      "guest": "Gov. Mike Huckabee"
    },
    {
      "date": "2007-04-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e9s3wp/intro---4-23-07",
        "http://thecolbertreport.cc.com/videos/tuitvp/gonzales-forgot",
        "http://thecolbertreport.cc.com/videos/xgp7gj/stephanie-s-winning-",
        "http://thecolbertreport.cc.com/videos/bsgdkg/mike-huckabee---running-mate-bid",
        "http://thecolbertreport.cc.com/videos/mksggb/threatdown---myspace",
        "http://thecolbertreport.cc.com/videos/25567u/russell-simmons",
        "http://thecolbertreport.cc.com/videos/75z88c/colbert-nation-online-discussion-group"
      ],
      "guest": "Russell Simmons"
    },
    {
      "date": "2007-04-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6edbk9/intro---4-24-07",
        "http://thecolbertreport.cc.com/videos/9lfdmb/bye-bye-to-boris",
        "http://thecolbertreport.cc.com/videos/zf1m9m/d-c--voting-rights---eleanor-holmes-norton",
        "http://thecolbertreport.cc.com/videos/zebgor/the-word---act-globally",
        "http://thecolbertreport.cc.com/videos/o4vs3o/60--good-news",
        "http://thecolbertreport.cc.com/videos/63paz7/alpha-dog-of-the-week---uncle-ben",
        "http://thecolbertreport.cc.com/videos/i6gv9q/dr--andrew-weil",
        "http://thecolbertreport.cc.com/videos/858p8x/sign-off---captain-lead"
      ],
      "guest": "Dr. Andrew Weil"
    },
    {
      "date": "2007-04-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/939oo7/intro---4-25-07",
        "http://thecolbertreport.cc.com/videos/9cksb2/dead-to-me---long-war",
        "http://thecolbertreport.cc.com/videos/uixydp/the-word---sacrifice",
        "http://thecolbertreport.cc.com/videos/xlgsnw/new-issue-of-gq",
        "http://thecolbertreport.cc.com/videos/vsu32z/four-horsemen-of-the-a-pop-calypse---prayer",
        "http://thecolbertreport.cc.com/videos/877wu4/david-walker",
        "http://thecolbertreport.cc.com/videos/dqbrsh/sign-off---promises"
      ],
      "guest": "David Walker"
    },
    {
      "date": "2007-04-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uxgeoh/exclusive---better-know-a-protectorate---guam---madeleine-bordallo-pt--1",
        "http://thecolbertreport.cc.com/videos/nfu1lw/exclusive---better-know-a-protectorate---guam---madeleine-bordallo-pt--2",
        "http://thecolbertreport.cc.com/videos/tioqro/intro---4-26-07",
        "http://thecolbertreport.cc.com/videos/ph7bwx/stephanie-lost",
        "http://thecolbertreport.cc.com/videos/nn2tor/the-word---mending-wall",
        "http://thecolbertreport.cc.com/videos/7ibt5q/better-know-a-protectorate---guam---madeleine-bordallo",
        "http://thecolbertreport.cc.com/videos/wax9na/tom-wolfe",
        "http://thecolbertreport.cc.com/videos/4y1aqm/sign-off---yuri-kuklachev"
      ],
      "guest": "Tom Wolfe"
    },
    {
      "date": "2007-04-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qiwo3g/intro---4-30-07",
        "http://thecolbertreport.cc.com/videos/hpmi3p/first-democratic-debate-for--08",
        "http://thecolbertreport.cc.com/videos/lv3s81/neil-degrasse-tyson",
        "http://thecolbertreport.cc.com/videos/o5hsha/tip-wag---shrek",
        "http://thecolbertreport.cc.com/videos/iwnuxq/bill-bradley"
      ],
      "guest": "Bill Bradley"
    },
    {
      "date": "2007-05-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qd26kv/intro---5-1-07",
        "http://thecolbertreport.cc.com/videos/scarky/mitt-s-favorite-book",
        "http://thecolbertreport.cc.com/videos/oh320q/npr-correction",
        "http://thecolbertreport.cc.com/videos/q45jin/the-word---who-cares-",
        "http://thecolbertreport.cc.com/videos/cgfptc/stephen-s-horse",
        "http://thecolbertreport.cc.com/videos/m9pls7/malcolm-gladwell",
        "http://thecolbertreport.cc.com/videos/zj4aga/sign-off---lutefisk"
      ],
      "guest": "Malcolm Gladwell"
    },
    {
      "date": "2007-05-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zxhw8e/intro---5-2-07",
        "http://thecolbertreport.cc.com/videos/vvfvju/hr-1591",
        "http://thecolbertreport.cc.com/videos/a3d8vy/the-word---better-safe-than-sorry",
        "http://thecolbertreport.cc.com/videos/oo27ij/mike-gravel",
        "http://thecolbertreport.cc.com/videos/u82od0/gina-kolata"
      ],
      "guest": "Gina Kolata"
    },
    {
      "date": "2007-05-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/33wl1k/exclusive---better-know-a-district---virginia-s-11th---tom-davis",
        "http://thecolbertreport.cc.com/videos/42iy2c/intro---5-3-07",
        "http://thecolbertreport.cc.com/videos/wsiuq8/battle-of-the-surfaces",
        "http://thecolbertreport.cc.com/videos/0wtt0d/the-word---the-unquisition",
        "http://thecolbertreport.cc.com/videos/2iymfl/better-know-a-district---virginia-s-11th---tom-davis",
        "http://thecolbertreport.cc.com/videos/6azbk5/conn-iggulden",
        "http://thecolbertreport.cc.com/videos/dblp9v/sign-off---impatiens"
      ],
      "guest": "Conn Iggulden"
    },
    {
      "date": "2007-05-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/re08sm/intro---5-7-07",
        "http://thecolbertreport.cc.com/videos/5ra6xp/bonjour--mon-frere",
        "http://thecolbertreport.cc.com/videos/o0gs8q/republican-debate---diversity",
        "http://thecolbertreport.cc.com/videos/ojz8he/the-word---the-intolerant",
        "http://thecolbertreport.cc.com/videos/x5zaaj/cheating-death---vaxadrin",
        "http://thecolbertreport.cc.com/videos/1i1xa2/richard-preston"
      ],
      "guest": "Richard Preston"
    },
    {
      "date": "2007-05-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ah3swk/intro---5-8-07",
        "http://thecolbertreport.cc.com/videos/4vb9ha/shout-out----uss-rhode-island",
        "http://thecolbertreport.cc.com/videos/v2jrqr/the-word---rendered-moot",
        "http://thecolbertreport.cc.com/videos/bkd3bl/threatdown---oprah",
        "http://thecolbertreport.cc.com/videos/296em4/nassim-nicholas-taleb"
      ],
      "guest": "Nassim Nicholas Taleb"
    },
    {
      "date": "2007-05-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bbia54/intro---5-9-07",
        "http://thecolbertreport.cc.com/videos/hs4hrn/mother-s-day",
        "http://thecolbertreport.cc.com/videos/01nwrp/formal-request",
        "http://thecolbertreport.cc.com/videos/ijt89t/salman-rushdie",
        "http://thecolbertreport.cc.com/videos/y81ejs/kiss-the-host",
        "http://thecolbertreport.cc.com/videos/4mwns0/thompson-fuss",
        "http://thecolbertreport.cc.com/videos/8ixf7m/jane-fonda",
        "http://thecolbertreport.cc.com/videos/bhwtjj/sign-off---bedtime-recipe"
      ],
      "guest": "Salman Rushdie, Jane Fonda"
    },
    {
      "date": "2007-05-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h5fw40/intro---5-10-07",
        "http://thecolbertreport.cc.com/videos/5mohm3/the-word---illusion",
        "http://thecolbertreport.cc.com/videos/6mm58j/hometown-hero-town---naperville--il",
        "http://thecolbertreport.cc.com/videos/1yenb5/the-in-box---doctor-colbert",
        "http://thecolbertreport.cc.com/videos/ya8jd7/jann-wenner",
        "http://thecolbertreport.cc.com/videos/tbehsa/sign-off---time-capsule",
        "http://thecolbertreport.cc.com/videos/59lqle/he-s-singing-in-korean"
      ],
      "guest": "Jann Wenner"
    },
    {
      "date": "2007-05-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q3z8ca/intro---5-14-07",
        "http://thecolbertreport.cc.com/videos/2wmvq0/ferrari-list",
        "http://thecolbertreport.cc.com/videos/ji8vnp/the-word---supporting-role",
        "http://thecolbertreport.cc.com/videos/62strl/tip-wag---mitt-romney",
        "http://thecolbertreport.cc.com/videos/324045/william-langewiesche",
        "http://thecolbertreport.cc.com/videos/70la8y/stealing-lincoln-s-body"
      ],
      "guest": "William Langewiesche"
    },
    {
      "date": "2007-05-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/458uob/intro---5-15-07",
        "http://thecolbertreport.cc.com/videos/0oyxpf/mcnulty-guilty",
        "http://thecolbertreport.cc.com/videos/c0yfoq/pasadena--india",
        "http://thecolbertreport.cc.com/videos/lda912/the-word---heated-debate",
        "http://thecolbertreport.cc.com/videos/7heoq8/bonus-wag---bush-graphic",
        "http://thecolbertreport.cc.com/videos/yqaslk/alpha-dog-of-the-week---michael-wiley",
        "http://thecolbertreport.cc.com/videos/q5o3oe/walter-isaacson",
        "http://thecolbertreport.cc.com/videos/3mglju/r-i-p--ted-maiman"
      ],
      "guest": "Walter Isaacson"
    },
    {
      "date": "2007-05-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l9r090/intro---5-16-07",
        "http://thecolbertreport.cc.com/videos/9nd4g1/second-republican-debate",
        "http://thecolbertreport.cc.com/videos/lqz6xp/the-word---level-playing-field",
        "http://thecolbertreport.cc.com/videos/vb25tk/formidable-opponent---peanuts",
        "http://thecolbertreport.cc.com/videos/vd7dcd/howard-dean",
        "http://thecolbertreport.cc.com/videos/west8f/sign-off---name-of-city-here"
      ],
      "guest": "Howard Dean"
    },
    {
      "date": "2007-05-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j0njxq/intro---5-17-07",
        "http://thecolbertreport.cc.com/videos/xbgufk/the-hammer-is-here-",
        "http://thecolbertreport.cc.com/videos/g57yti/baby-gun-permit",
        "http://thecolbertreport.cc.com/videos/wqfqxb/tom-delay",
        "http://thecolbertreport.cc.com/videos/nfhqh3/randy-kearse",
        "http://thecolbertreport.cc.com/videos/vz0202/sign-off---rafters"
      ],
      "guest": "Randy Kearse, Rep. Tom DeLay"
    },
    {
      "date": "2007-05-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/43r84a/intro---5-21-07",
        "http://thecolbertreport.cc.com/videos/j7bshe/god-loves-a-big-screen-tv",
        "http://thecolbertreport.cc.com/videos/s5odvt/presidential-fraternity",
        "http://thecolbertreport.cc.com/videos/w89fii/the-word---his-way",
        "http://thecolbertreport.cc.com/videos/zg6n7b/cheating-death---internal-decapitation",
        "http://thecolbertreport.cc.com/videos/zhetqf/jared-diamond"
      ],
      "guest": "Jared Diamond"
    },
    {
      "date": "2007-05-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vn2u9p/intro---5-22-07",
        "http://thecolbertreport.cc.com/videos/pp3dmv/popularity-contest",
        "http://thecolbertreport.cc.com/videos/szr9pb/barack-s-a-liar",
        "http://thecolbertreport.cc.com/videos/4wuift/the-word---party-of-change",
        "http://thecolbertreport.cc.com/videos/7bglee/threatdown---environmentalists",
        "http://thecolbertreport.cc.com/videos/661huh/john-amaechi",
        "http://thecolbertreport.cc.com/videos/ivskf6/sign-off---lesson-forgotten"
      ],
      "guest": "John Amaechi"
    },
    {
      "date": "2007-05-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pwwndq/intro---5-23-07",
        "http://thecolbertreport.cc.com/videos/ac7obb/bush-is-back-",
        "http://thecolbertreport.cc.com/videos/2t0qn4/illegal-immigration---bay-buchanan",
        "http://thecolbertreport.cc.com/videos/m6d100/threatdown---pellicano-",
        "http://thecolbertreport.cc.com/videos/0v2e97/bob-deans",
        "http://thecolbertreport.cc.com/videos/1kaqcp/sign-off---hi-def"
      ],
      "guest": "Bay Buchanan, Bob Deans"
    },
    {
      "date": "2007-05-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fc4ao7/intro---5-24-07",
        "http://thecolbertreport.cc.com/videos/ihom0u/fleet-week",
        "http://thecolbertreport.cc.com/videos/5d38de/big-loud-flag",
        "http://thecolbertreport.cc.com/videos/oxz2g4/up-in-smoke",
        "http://thecolbertreport.cc.com/videos/brpu8j/better-know-a-district---arizona-s-7th---raul-grijalva",
        "http://thecolbertreport.cc.com/videos/vylxk3/jimmy-wales",
        "http://thecolbertreport.cc.com/videos/xj2s00/speaking-fee"
      ],
      "guest": "Jimmy Wales"
    },
    {
      "date": "2007-06-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/38wiug/intro---6-4-07",
        "http://thecolbertreport.cc.com/videos/oujnzk/uneventful-vacation",
        "http://thecolbertreport.cc.com/videos/5475j4/democratic-presidential-debate---venue",
        "http://thecolbertreport.cc.com/videos/3bhuju/jan-schakowsky",
        "http://thecolbertreport.cc.com/videos/svome1/better-know-a-district---illinois--9th---jan-schakowsky",
        "http://thecolbertreport.cc.com/videos/o9kyh0/leon-botstein",
        "http://thecolbertreport.cc.com/videos/kaun5v/sign-off---mardi-gras-mask"
      ],
      "guest": "Rep. Jan Schakowsky, Leon Botstein"
    },
    {
      "date": "2007-06-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7sdcg5/intro---6-5-07",
        "http://thecolbertreport.cc.com/videos/cvm31h/you-ve-been-scootered-",
        "http://thecolbertreport.cc.com/videos/j3ieeu/yahoo-korea---rain",
        "http://thecolbertreport.cc.com/videos/8226p8/the-word---mission-control",
        "http://thecolbertreport.cc.com/videos/n0lk8c/the-god-machine-",
        "http://thecolbertreport.cc.com/videos/l7y8g1/when-animals-attack-our-morals---flamingos",
        "http://thecolbertreport.cc.com/videos/rsex2i/jessica-valenti"
      ],
      "guest": "Jessica Valenti"
    },
    {
      "date": "2007-06-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jorp7o/intro---6-6-07",
        "http://thecolbertreport.cc.com/videos/h69756/sinner-edwards",
        "http://thecolbertreport.cc.com/videos/5mthf9/the-word---airogance",
        "http://thecolbertreport.cc.com/videos/cujedg/tip-wag---deep-purple",
        "http://thecolbertreport.cc.com/videos/ngt9bf/carl-bernstein",
        "http://thecolbertreport.cc.com/videos/xd82es/craziest-f--king-thing-i-ve-ever-heard---octopi"
      ],
      "guest": "Carl Bernstein"
    },
    {
      "date": "2007-06-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b0xqmj/intro---6-7-07",
        "http://thecolbertreport.cc.com/videos/w1jmjp/pope-jump",
        "http://thecolbertreport.cc.com/videos/ovs97y/the-word---rodham",
        "http://thecolbertreport.cc.com/videos/tl388o/better-know-a-district---washington-s-9th---adam-smith",
        "http://thecolbertreport.cc.com/videos/ty2mfm/cullen-murphy",
        "http://thecolbertreport.cc.com/videos/sitbn5/sign-off---vomitorium"
      ],
      "guest": "Cullen Murphy"
    },
    {
      "date": "2007-06-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1yiwr5/intro---6-11-07",
        "http://thecolbertreport.cc.com/videos/dufa3e/commencement-speeches",
        "http://thecolbertreport.cc.com/videos/2k0q1b/the-word---easy-a",
        "http://thecolbertreport.cc.com/videos/kd0cks/revenge-on-knox-college",
        "http://thecolbertreport.cc.com/videos/qrkfud/albania-greets-president-bush",
        "http://thecolbertreport.cc.com/videos/zpjdcg/michael-gershon"
      ],
      "guest": "Dr. Michael D. Gershon"
    },
    {
      "date": "2007-06-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b08r7k/intro---6-12-07",
        "http://thecolbertreport.cc.com/videos/8dqxf0/bush-s-missing-watch",
        "http://thecolbertreport.cc.com/videos/sse01t/mr--dyachenko--tear-down-this-wall",
        "http://thecolbertreport.cc.com/videos/lhl8km/tommy-chong--commentator",
        "http://thecolbertreport.cc.com/videos/ey1hjm/mr--dyachenko--tear-down-this-watermelon",
        "http://thecolbertreport.cc.com/videos/2krcmy/colbert-platinum---butler-shortage",
        "http://thecolbertreport.cc.com/videos/gdyajn/josh-wolf",
        "http://thecolbertreport.cc.com/videos/r2b64h/mr--dyachenko--tear-me-off-a-piece-of-this-cake"
      ],
      "guest": "Josh Wolf"
    },
    {
      "date": "2007-06-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/onm1u4/intro---6-13-07",
        "http://thecolbertreport.cc.com/videos/fytk75/ruined-anniversary",
        "http://thecolbertreport.cc.com/videos/6nklj9/freezing-cold-case-files--otzi",
        "http://thecolbertreport.cc.com/videos/tnydpx/the-word---pathophysiology",
        "http://thecolbertreport.cc.com/videos/2bu2sn/threatdown---robots",
        "http://thecolbertreport.cc.com/videos/o2ywub/ron-paul",
        "http://thecolbertreport.cc.com/videos/cakp5s/sign-off---crispy-deliciousness"
      ],
      "guest": "Rep. Ron Paul"
    },
    {
      "date": "2007-06-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oa9gd7/intro---6-14-07",
        "http://thecolbertreport.cc.com/videos/6uc0h1/fred-thompson-on-fire",
        "http://thecolbertreport.cc.com/videos/g52jco/stephen-benjamin",
        "http://thecolbertreport.cc.com/videos/0agktt/bears---balls---summer-vacation-edition",
        "http://thecolbertreport.cc.com/videos/a0p792/daniel-b--smith",
        "http://thecolbertreport.cc.com/videos/llk3nk/sign-off---the-land-of-nod"
      ],
      "guest": "Daniel B. Smith"
    },
    {
      "date": "2007-06-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rwup1e/intro---6-18-07",
        "http://thecolbertreport.cc.com/videos/k3t99j/papal-encounter",
        "http://thecolbertreport.cc.com/videos/rbx9fh/the-price-is-right",
        "http://thecolbertreport.cc.com/videos/w0pe9q/the-word---mcconaughey",
        "http://thecolbertreport.cc.com/videos/yfclcj/stephen-on-itunes",
        "http://thecolbertreport.cc.com/videos/7jalja/tip-wag---arnold-schwarzenegger",
        "http://thecolbertreport.cc.com/videos/ozfwje/toby-keith"
      ],
      "guest": "Toby Keith"
    },
    {
      "date": "2007-06-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ndbsf6/intro---6-19-07",
        "http://thecolbertreport.cc.com/videos/qxyadz/secret-clapton-concert",
        "http://thecolbertreport.cc.com/videos/0y4kih/marybeth-garrigan",
        "http://thecolbertreport.cc.com/videos/mzxikb/countdown-to-armageddon",
        "http://thecolbertreport.cc.com/videos/ij3mgr/alpha-dog-of-the-week---robert-bork",
        "http://thecolbertreport.cc.com/videos/u1dk1e/anne-marie-slaughter",
        "http://thecolbertreport.cc.com/videos/kxk02d/sign-off---manifesto"
      ],
      "guest": "Harriet the Eagle with handler, Anne-Marie Slaughter"
    },
    {
      "date": "2007-06-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jbdbyq/intro---6-20-07",
        "http://thecolbertreport.cc.com/videos/beccdu/bloomberg-for-president",
        "http://thecolbertreport.cc.com/videos/xe5j30/the-word---justice",
        "http://thecolbertreport.cc.com/videos/4yziuf/cheating-death---colgate",
        "http://thecolbertreport.cc.com/videos/7m9bgr/will-schwalbe",
        "http://thecolbertreport.cc.com/videos/glo9c6/sign-off---job-well-done"
      ],
      "guest": "Will Schwalbe"
    },
    {
      "date": "2007-06-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/um7qsm/intro---6-21-07",
        "http://thecolbertreport.cc.com/videos/psamg7/ron-paul-s-colbert-bump",
        "http://thecolbertreport.cc.com/videos/38xzef/difference-makers---tim-donnelly",
        "http://thecolbertreport.cc.com/videos/2oyfu8/vincent-bugliosi",
        "http://thecolbertreport.cc.com/videos/dlqbr6/sign-off---goodbye-to-mr--wizard",
        "http://thecolbertreport.cc.com/videos/35278z/the-word---porking"
      ],
      "guest": "Vincent Bugliosi"
    },
    {
      "date": "2007-06-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wvrrio/intro---6-25-07",
        "http://thecolbertreport.cc.com/videos/xvrdq7/the-freegans",
        "http://thecolbertreport.cc.com/videos/dqezp0/the-word---fourth-branch",
        "http://thecolbertreport.cc.com/videos/oldt6o/threatdown---coral-reefs",
        "http://thecolbertreport.cc.com/videos/mhjtgw/tom-hayden",
        "http://thecolbertreport.cc.com/videos/5zivhy/sign-off---contract"
      ],
      "guest": "Tom Hayden"
    },
    {
      "date": "2007-06-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2dxfpk/intro---6-26-07",
        "http://thecolbertreport.cc.com/videos/id2z8d/christmas-in-june",
        "http://thecolbertreport.cc.com/videos/eelu64/tony-blair-s-conversion",
        "http://thecolbertreport.cc.com/videos/tpff57/the-word---elsewhere",
        "http://thecolbertreport.cc.com/videos/0t819z/christmas-presents",
        "http://thecolbertreport.cc.com/videos/5awnum/alpha-dog-of-the-week---fred-thompson",
        "http://thecolbertreport.cc.com/videos/1uvv46/david-france",
        "http://thecolbertreport.cc.com/videos/96ew1f/sign-off---visions-of-sugarplums"
      ],
      "guest": "David France"
    },
    {
      "date": "2007-06-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/47zhcv/intro---6-27-07",
        "http://thecolbertreport.cc.com/videos/y34h2c/give-stephen-an-iphone",
        "http://thecolbertreport.cc.com/videos/wepdgq/tom-blanton",
        "http://thecolbertreport.cc.com/videos/f6in26/four-horsemen-of-the-a-pop-calypse---shaq",
        "http://thecolbertreport.cc.com/videos/msuhoe/daniel-gilbert"
      ],
      "guest": "Tom Blanton, Daniel Gilbert"
    },
    {
      "date": "2007-06-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ftc2tr/intro---6-28-07",
        "http://thecolbertreport.cc.com/videos/2o9nj2/spot-the-difference",
        "http://thecolbertreport.cc.com/videos/kb8br0/civil-unrest-in-iran",
        "http://thecolbertreport.cc.com/videos/0lfyqf/the-word---profiles-in-timing",
        "http://thecolbertreport.cc.com/videos/owh6vd/colbert-platinum---luxury-car-wrecks",
        "http://thecolbertreport.cc.com/videos/f9y6wb/doug-bailey",
        "http://thecolbertreport.cc.com/videos/oxeeoj/sign-off---going-on-vacation"
      ],
      "guest": "Doug Bailey"
    },
    {
      "date": "2007-07-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rsv8g9/intro---7-16-07",
        "http://thecolbertreport.cc.com/videos/bwablo/tunneling-to-free-scooter-libby",
        "http://thecolbertreport.cc.com/videos/lnroz7/richard-florida",
        "http://thecolbertreport.cc.com/videos/scrz03/difference-makers---johnna-mink",
        "http://thecolbertreport.cc.com/videos/r0qxf5/ben-nelson",
        "http://thecolbertreport.cc.com/videos/zabqma/sign-off---take-five"
      ],
      "guest": "Richard Florida, Sen. Ben Nelson"
    },
    {
      "date": "2007-07-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cliw91/intro---7-17-07",
        "http://thecolbertreport.cc.com/videos/zl176l/all-night-senate-session",
        "http://thecolbertreport.cc.com/videos/depupc/the-word---victimcrite",
        "http://thecolbertreport.cc.com/videos/hdn59k/1-428-minutes-to-go",
        "http://thecolbertreport.cc.com/videos/gafa5t/tip-wag---michael-chertoff-s-gut-o-meter",
        "http://thecolbertreport.cc.com/videos/ev6dp9/mark-moffett",
        "http://thecolbertreport.cc.com/videos/1jb3qq/threatdown---500-threat-marathon"
      ],
      "guest": "Mark Moffett"
    },
    {
      "date": "2007-07-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uf8wpk/intro---7-18-07",
        "http://thecolbertreport.cc.com/videos/gn1bt7/2007-filibustacular",
        "http://thecolbertreport.cc.com/videos/hqa77b/the-word---smiley-face",
        "http://thecolbertreport.cc.com/videos/ysfdjx/pope-goes-green",
        "http://thecolbertreport.cc.com/videos/artj1e/alpha-dog-of-the-week---david-beckham",
        "http://thecolbertreport.cc.com/videos/ga3vsc/john-mellencamp"
      ],
      "guest": "John Mellencamp"
    },
    {
      "date": "2007-07-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/19mw0q/intro---7-19-07",
        "http://thecolbertreport.cc.com/videos/1esv0i/republican-candidates--suffering",
        "http://thecolbertreport.cc.com/videos/a9zoea/michael-moore",
        "http://thecolbertreport.cc.com/videos/bn2nox/march-to-enslavement---stephen-gets-an-iphone",
        "http://thecolbertreport.cc.com/videos/9p0lhk/frank-sulloway",
        "http://thecolbertreport.cc.com/videos/qhp9z3/sign-off---length-of-the-show-contest"
      ],
      "guest": "Frank Sulloway"
    },
    {
      "date": "2007-07-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nc8xh3/intro---7-23-07",
        "http://thecolbertreport.cc.com/videos/fkxqbr/stephen-s-fountain-of-youth",
        "http://thecolbertreport.cc.com/videos/4rqgp5/the-word---premium-package",
        "http://thecolbertreport.cc.com/videos/l0ig1p/colbert-platinum---private-submarines",
        "http://thecolbertreport.cc.com/videos/6e6gd1/simon-schama",
        "http://thecolbertreport.cc.com/videos/vfxa7p/sign-off---just-about-out-of-time"
      ],
      "guest": "Simon Schama"
    },
    {
      "date": "2007-07-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/15l5ov/intro---7-24-07",
        "http://thecolbertreport.cc.com/videos/d9v0fp/bush-s-butt",
        "http://thecolbertreport.cc.com/videos/nvdygh/the-word---modest-porpoisal",
        "http://thecolbertreport.cc.com/videos/e5420t/movies-that-are-destroying-america--chuck-and-larry",
        "http://thecolbertreport.cc.com/videos/yqgj2h/anthony-romero",
        "http://thecolbertreport.cc.com/videos/alsjeo/joining-the-illuminati"
      ],
      "guest": "Anthony D. Romero"
    },
    {
      "date": "2007-07-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/shyero/intro---7-25-07",
        "http://thecolbertreport.cc.com/videos/4md3eg/daily-kos",
        "http://thecolbertreport.cc.com/videos/ikcdyi/the-word---no-regrets",
        "http://thecolbertreport.cc.com/videos/bdjzxb/thompson-campaign",
        "http://thecolbertreport.cc.com/videos/bc0mf3/hometown-hero-town---bryce-canyon-city",
        "http://thecolbertreport.cc.com/videos/2f2r58/charles-kaiser"
      ],
      "guest": "Charles Kaiser"
    },
    {
      "date": "2007-07-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wth3ve/intro---7-26-07",
        "http://thecolbertreport.cc.com/videos/3or3gc/how-did-stephen-break-his-wrist-",
        "http://thecolbertreport.cc.com/videos/if6h6s/industrial-hemp---medical-marijuana---aaron-houston",
        "http://thecolbertreport.cc.com/videos/8p2na8/advice-to-the-gods---nepalese-pre-teen-goddesses",
        "http://thecolbertreport.cc.com/videos/kcb6kk/bob-shrum"
      ],
      "guest": "Robert Shrum"
    },
    {
      "date": "2007-07-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8m5y0f/intro---7-30-07",
        "http://thecolbertreport.cc.com/videos/tyo2os/wrist-violence---glorification",
        "http://thecolbertreport.cc.com/videos/9e0vz0/pollution-immigration",
        "http://thecolbertreport.cc.com/videos/brdooe/the-word---solidarity",
        "http://thecolbertreport.cc.com/videos/ii5xvp/threatdown---scottish-surgeons",
        "http://thecolbertreport.cc.com/videos/o55kxd/evan-osnos"
      ],
      "guest": "Evan Osnos"
    },
    {
      "date": "2007-07-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/01xv20/intro---7-31-07",
        "http://thecolbertreport.cc.com/videos/bgyn76/wrist-violence-epidemic",
        "http://thecolbertreport.cc.com/videos/aryder/smokin--pole---arc--who-goes-there-",
        "http://thecolbertreport.cc.com/videos/tg3umi/the-word---special-prosecutor",
        "http://thecolbertreport.cc.com/videos/egvqvt/rupert-murdoch-purchases-the-wall-street-journal",
        "http://thecolbertreport.cc.com/videos/i9cr44/sport-report---barry-bonds",
        "http://thecolbertreport.cc.com/videos/3tom79/kathleen-kennedy-townsend"
      ],
      "guest": "Kathleen Kennedy Townsend"
    },
    {
      "date": "2007-08-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jtpqex/intro---8-1-07",
        "http://thecolbertreport.cc.com/videos/b8kbe8/dr--jerry-vizzone",
        "http://thecolbertreport.cc.com/videos/zd2nvn/the-word---college-credit",
        "http://thecolbertreport.cc.com/videos/nlqwhc/when-animals-attack-our-morals---hollywood-pigeons",
        "http://thecolbertreport.cc.com/videos/agisiu/michael-beschloss",
        "http://thecolbertreport.cc.com/videos/a0yv9l/30-minute-anniversary"
      ],
      "guest": "Michael Beschloss"
    },
    {
      "date": "2007-08-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qjky5n/farewell-ingmar-bergman",
        "http://thecolbertreport.cc.com/videos/jtpqex/intro---8-1-07",
        "http://thecolbertreport.cc.com/videos/b8kbe8/dr--jerry-vizzone",
        "http://thecolbertreport.cc.com/videos/zd2nvn/the-word---college-credit",
        "http://thecolbertreport.cc.com/videos/nlqwhc/when-animals-attack-our-morals---hollywood-pigeons",
        "http://thecolbertreport.cc.com/videos/agisiu/michael-beschloss",
        "http://thecolbertreport.cc.com/videos/a0yv9l/30-minute-anniversary"
      ],
      "guest": "Michael J. Behe"
    },
    {
      "date": "2007-08-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tqb1ek/intro---8-2-07",
        "http://thecolbertreport.cc.com/videos/4fa4lg/superhighway",
        "http://thecolbertreport.cc.com/videos/sg9xg3/rick-macarthur",
        "http://thecolbertreport.cc.com/videos/vc3b3c/thighmasters-for-the-troops",
        "http://thecolbertreport.cc.com/videos/ptvqa7/sport-report---barry-smash",
        "http://thecolbertreport.cc.com/videos/z81ulz/michael-behe"
      ],
      "guest": "Michael J. Behe"
    },
    {
      "date": "2007-08-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7r677j/intro---8-7-07",
        "http://thecolbertreport.cc.com/videos/4kw9z4/yearly-kos-convention",
        "http://thecolbertreport.cc.com/videos/f3w2rh/the-word---the-dark-side",
        "http://thecolbertreport.cc.com/videos/zwnri3/better-know-a-protectorate---american-samoa---eni-faleomavaega",
        "http://thecolbertreport.cc.com/videos/d21xmf/ian-bogost",
        "http://thecolbertreport.cc.com/videos/kzlukl/sign-off---colbert-commonsensicals"
      ],
      "guest": "Ian Bogost"
    },
    {
      "date": "2007-08-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4f7upv/intro---8-8-07",
        "http://thecolbertreport.cc.com/videos/oxms8d/wrist-watch---fighting-back",
        "http://thecolbertreport.cc.com/videos/jtqjr6/jim-cramer",
        "http://thecolbertreport.cc.com/videos/nveh3o/bears---balls---bootlegging",
        "http://thecolbertreport.cc.com/videos/7zavlx/tina-brown"
      ],
      "guest": "Jim Cramer, Tina Brown"
    },
    {
      "date": "2007-08-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hutdl7/intro---8-9-07",
        "http://thecolbertreport.cc.com/videos/3abho5/the-word---clarity",
        "http://thecolbertreport.cc.com/videos/qp6xha/tip-wag---bloomberg",
        "http://thecolbertreport.cc.com/videos/h9y997/judd-apatow",
        "http://thecolbertreport.cc.com/videos/161mvg/sign-off---toenails"
      ],
      "guest": "Judd Apatow"
    },
    {
      "date": "2007-08-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1833p0/intro---8-13-07",
        "http://thecolbertreport.cc.com/videos/gavjew/rove-resigns",
        "http://thecolbertreport.cc.com/videos/qu995y/the-word---white-guy",
        "http://thecolbertreport.cc.com/videos/bruhc9/threatdown---bats",
        "http://thecolbertreport.cc.com/videos/fk3k31/michael-jacobson",
        "http://thecolbertreport.cc.com/videos/dnjitq/sign-off---americone-dream"
      ],
      "guest": "Michael Jacobson"
    },
    {
      "date": "2007-08-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0imzs4/dna--could-it-happen-to-you----jackknife",
        "http://thecolbertreport.cc.com/videos/n35y17/jerry-miller",
        "http://thecolbertreport.cc.com/videos/5o7ie1/dr--spencer-wells",
        "http://thecolbertreport.cc.com/videos/x03vyw/dna--could-it-happen-to-you----incrimination"
      ],
      "guest": "Jerry Miller, Spencer Wells"
    },
    {
      "date": "2007-08-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6o4ihx/intro---8-15-07",
        "http://thecolbertreport.cc.com/videos/rv9k9s/jewish-colbert-ancestry",
        "http://thecolbertreport.cc.com/videos/3zlayh/markos-moulitsas",
        "http://thecolbertreport.cc.com/videos/6mvd9x/monkey-on-the-lam---oliver",
        "http://thecolbertreport.cc.com/videos/zp4iw7/the-word---potential",
        "http://thecolbertreport.cc.com/videos/734nxn/michael-wallis",
        "http://thecolbertreport.cc.com/videos/z4d4y4/sign-off---doctor-s-orders"
      ],
      "guest": "Michael Wallis"
    },
    {
      "date": "2007-08-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ns0g26/intro---8-16-07",
        "http://thecolbertreport.cc.com/videos/14jprr/colbert-branson-trainwreck",
        "http://thecolbertreport.cc.com/videos/kgguey/mike-huckabee",
        "http://thecolbertreport.cc.com/videos/fnrvrc/cheating-death---gene-therapy",
        "http://thecolbertreport.cc.com/videos/u8nc37/andrew-keen"
      ],
      "guest": "Andrew Keen"
    },
    {
      "date": "2007-08-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tfnhsy/intro---8-20-07",
        "http://thecolbertreport.cc.com/videos/xo98yh/wriststrong-bracelets",
        "http://thecolbertreport.cc.com/videos/us6itk/the-word---made-in-iraq",
        "http://thecolbertreport.cc.com/videos/9a8i9h/nailed--em---northern-border",
        "http://thecolbertreport.cc.com/videos/o9ho2y/nathan-sawaya"
      ],
      "guest": "Nathan Sawaya"
    },
    {
      "date": "2007-08-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2gjr3w/intro---8-21-07",
        "http://thecolbertreport.cc.com/videos/bcfeni/smokin--pole---global-warming",
        "http://thecolbertreport.cc.com/videos/7gfsui/the-word---self-determination",
        "http://thecolbertreport.cc.com/videos/v4twhy/formidable-opponent---terrorism",
        "http://thecolbertreport.cc.com/videos/4o129i/michael-shermer"
      ],
      "guest": "Michael Shermer"
    },
    {
      "date": "2007-08-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v8cwuz/intro---8-22-07",
        "http://thecolbertreport.cc.com/videos/k7oqos/foreshadowing",
        "http://thecolbertreport.cc.com/videos/9snnh5/the-word---november-surprise",
        "http://thecolbertreport.cc.com/videos/ymi1da/where-in-the-world-is-matt-lauer-s-wriststrong-bracelet-",
        "http://thecolbertreport.cc.com/videos/r18bn4/colbert-platinum---san-tropez",
        "http://thecolbertreport.cc.com/videos/xxwsh0/richard-branson",
        "http://thecolbertreport.cc.com/videos/eb410v/doused"
      ],
      "guest": "Richard Branson"
    },
    {
      "date": "2007-08-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/w3z5w0/intro---8-23-07",
        "http://thecolbertreport.cc.com/videos/uc4umy/cheney-s-pre-emptive-strike",
        "http://thecolbertreport.cc.com/videos/en1mx1/thomas-ricks",
        "http://thecolbertreport.cc.com/videos/xjgukn/fractured-freedom",
        "http://thecolbertreport.cc.com/videos/0arcqm/wrist-cast-signatories",
        "http://thecolbertreport.cc.com/videos/3xfbbo/free-at-last",
        "http://thecolbertreport.cc.com/videos/qta5f5/the-auction-begins-"
      ],
      "guest": "Thomas Ricks"
    },
    {
      "date": "2007-09-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/844a7k/intro---9-10-07",
        "http://thecolbertreport.cc.com/videos/vdvpmz/kicking-the-habit",
        "http://thecolbertreport.cc.com/videos/p14g3t/the-word---honor-bound",
        "http://thecolbertreport.cc.com/videos/2qi5qf/cast-auction",
        "http://thecolbertreport.cc.com/videos/u1yamr/bjorn-lomborg"
      ],
      "guest": "Bjorn Lomborg"
    },
    {
      "date": "2007-09-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hy8je4/intro---9-11-07",
        "http://thecolbertreport.cc.com/videos/3l7k3j/general-betray-us",
        "http://thecolbertreport.cc.com/videos/5yaj4x/indecision-2008--don-t-f--k-this-up-america---the-kickoff",
        "http://thecolbertreport.cc.com/videos/mjzhz2/the-word---southsourcing",
        "http://thecolbertreport.cc.com/videos/5z4esb/katie-bruggeman---exclusive",
        "http://thecolbertreport.cc.com/videos/o07u14/garrison-keillor"
      ],
      "guest": "Garrison Keillor"
    },
    {
      "date": "2007-09-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h5njj1/intro---9-12-07",
        "http://thecolbertreport.cc.com/videos/8lpy3i/1-888-mops-key",
        "http://thecolbertreport.cc.com/videos/7hc8lx/the-word---re-run",
        "http://thecolbertreport.cc.com/videos/r6x2pm/michael-bloomberg",
        "http://thecolbertreport.cc.com/videos/3rano7/tek-jansen---beginning-s-first-dawn--episode-one",
        "http://thecolbertreport.cc.com/videos/n46uq9/joel-klein",
        "http://thecolbertreport.cc.com/videos/pc4v8w/klein-s-penance"
      ],
      "guest": "Joel Klein"
    },
    {
      "date": "2007-09-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tduyob/intro---9-13-07",
        "http://thecolbertreport.cc.com/videos/rvio16/the-emmys",
        "http://thecolbertreport.cc.com/videos/g1gps7/father-james-martin",
        "http://thecolbertreport.cc.com/videos/9unkmu/wriststrong",
        "http://thecolbertreport.cc.com/videos/5c8kig/ed-begley-jr-",
        "http://thecolbertreport.cc.com/videos/9mwknn/stephen-for-president---answering-the-call"
      ],
      "guest": "Ed Begley Jr."
    },
    {
      "date": "2007-09-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tr81w4/intro---9-18-07",
        "http://thecolbertreport.cc.com/videos/6l9i7j/the-word---let-my-people-go",
        "http://thecolbertreport.cc.com/videos/6we8r4/difference-makers---nitro-girl",
        "http://thecolbertreport.cc.com/videos/jx6a68/susan-sarandon"
      ],
      "guest": "Susan Sarandon"
    },
    {
      "date": "2007-09-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lv4fuw/intro---9-19-07",
        "http://thecolbertreport.cc.com/videos/zeoen2/ed-asner-dials-the-atone-phone",
        "http://thecolbertreport.cc.com/videos/0aau1u/the-word---solitarity",
        "http://thecolbertreport.cc.com/videos/7ooxuh/colbert-platinum---green-edition",
        "http://thecolbertreport.cc.com/videos/nnhbey/naomi-wolf"
      ],
      "guest": "Naomi Wolf"
    },
    {
      "date": "2007-09-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fojlm8/intro---9-20-07",
        "http://thecolbertreport.cc.com/videos/0ek76n/rabbi-fish",
        "http://thecolbertreport.cc.com/videos/2h18lo/blistering-rebuttal",
        "http://thecolbertreport.cc.com/videos/z6i9oa/the-word---market-forces",
        "http://thecolbertreport.cc.com/videos/b5qfpk/threatdown---us",
        "http://thecolbertreport.cc.com/videos/wthvm9/jeffrey-toobin",
        "http://thecolbertreport.cc.com/videos/1pktzf/craziest-f--king-thing-i-ve-ever-heard---mayo-kitchen"
      ],
      "guest": "Jeffrey Toobin"
    },
    {
      "date": "2007-09-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tgxkym/intro---9-24-07",
        "http://thecolbertreport.cc.com/videos/kwfydk/the-word---na-na-na-na-na-na",
        "http://thecolbertreport.cc.com/videos/zztck4/alpha-dog-of-the-week---honniball",
        "http://thecolbertreport.cc.com/videos/l00qbc/the-metric-system",
        "http://thecolbertreport.cc.com/videos/pkz7i5/thomas-l--friedman",
        "http://thecolbertreport.cc.com/videos/emtni3/sign-off---stephen-accepts-your-apologies"
      ],
      "guest": "Thomas Friedman"
    },
    {
      "date": "2007-09-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yrize5/intro---9-25-07",
        "http://thecolbertreport.cc.com/videos/cminr7/no-nuclear-iran",
        "http://thecolbertreport.cc.com/videos/2g01er/indecision-2008--don-t-f--k-this-up-america---giuliani",
        "http://thecolbertreport.cc.com/videos/bjhu7f/k--david-harrison",
        "http://thecolbertreport.cc.com/videos/b5cc0e/tip-wag---muslim-hipsters",
        "http://thecolbertreport.cc.com/videos/5ny4ja/john-grisham"
      ],
      "guest": "John Grisham"
    },
    {
      "date": "2007-09-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ups73z/intro---9-26-07",
        "http://thecolbertreport.cc.com/videos/rn3hke/forgiving-bennett",
        "http://thecolbertreport.cc.com/videos/agyblq/canadian-dollar",
        "http://thecolbertreport.cc.com/videos/nj93xu/the-word---a-word-from-our-sponsors",
        "http://thecolbertreport.cc.com/videos/0iswbv/sam-waterston",
        "http://thecolbertreport.cc.com/videos/79m504/tony-bennett"
      ],
      "guest": "Tony Bennett"
    },
    {
      "date": "2007-09-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i67egh/intro---9-27-07",
        "http://thecolbertreport.cc.com/videos/o502gv/king-tut",
        "http://thecolbertreport.cc.com/videos/mhmga5/democratic-presidential-debate---the-clintons",
        "http://thecolbertreport.cc.com/videos/th2rny/the-word---early-immunization",
        "http://thecolbertreport.cc.com/videos/ev9qqd/david-schwartz",
        "http://thecolbertreport.cc.com/videos/q0vng8/sign-off---bear-in-the-woods"
      ],
      "guest": "David Schwartz"
    },
    {
      "date": "2007-10-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4vmpg2/intro---10-1-07",
        "http://thecolbertreport.cc.com/videos/s3koea/on-notice---dennis-kucinich",
        "http://thecolbertreport.cc.com/videos/e5dl9b/the-word---evitable",
        "http://thecolbertreport.cc.com/videos/7s7h6l/cheating-death---sleep",
        "http://thecolbertreport.cc.com/videos/5wkeol/charlie-savage",
        "http://thecolbertreport.cc.com/videos/g86mf6/sign-off---all-night-date"
      ],
      "guest": "Charlie Savage"
    },
    {
      "date": "2007-10-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5ycsxc/intro---10-2-07",
        "http://thecolbertreport.cc.com/videos/ws1a9l/end-of-the-universe",
        "http://thecolbertreport.cc.com/videos/boxkhr/the-real-showdown",
        "http://thecolbertreport.cc.com/videos/f1ovth/the-word---troops-out-now",
        "http://thecolbertreport.cc.com/videos/berne3/nailed--em---cyberrorists",
        "http://thecolbertreport.cc.com/videos/non4mf/john-mearsheimer",
        "http://thecolbertreport.cc.com/videos/yxngw7/what-number-is-stephen-thinking-of----between-one-and-ten"
      ],
      "guest": "John Mearsheimer"
    },
    {
      "date": "2007-10-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/77zwpl/intro---10-3-07",
        "http://thecolbertreport.cc.com/videos/rsugzz/krugman-correction",
        "http://thecolbertreport.cc.com/videos/ujxs1h/gay-roundup---dan-savage",
        "http://thecolbertreport.cc.com/videos/ttvyxm/alpha-dog-of-the-week---president-bush",
        "http://thecolbertreport.cc.com/videos/bohex1/monkey-on-the-lam---missouri",
        "http://thecolbertreport.cc.com/videos/1scf3a/jim-lovell"
      ],
      "guest": "Jim Lovell"
    },
    {
      "date": "2007-10-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6takag/intro---10-4-07",
        "http://thecolbertreport.cc.com/videos/9ie5cp/fred-thompson-s-lackluster-candidacy",
        "http://thecolbertreport.cc.com/videos/t9j9vd/the-word---catastrophe",
        "http://thecolbertreport.cc.com/videos/ze1fvk/threatdown---science-and-technology-edition",
        "http://thecolbertreport.cc.com/videos/i58e8l/john-kao",
        "http://thecolbertreport.cc.com/videos/jy5aw2/an--i-am-america--and-so-can-you----success-story"
      ],
      "guest": "John Kao"
    },
    {
      "date": "2007-10-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zjbyqa/intro---10-8-07",
        "http://thecolbertreport.cc.com/videos/pw4m4c/doggie-co-author",
        "http://thecolbertreport.cc.com/videos/xkdwvy/the-word---medium-matters",
        "http://thecolbertreport.cc.com/videos/56gzq7/balls-for-kidz---schip",
        "http://thecolbertreport.cc.com/videos/og377e/george-saunders",
        "http://thecolbertreport.cc.com/videos/p6057q/sign-off---i-am-america--and-so-can-you---day"
      ],
      "guest": "George Saunders"
    },
    {
      "date": "2007-10-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q3jijk/intro---10-9-07",
        "http://thecolbertreport.cc.com/videos/plzp6y/i-am-america-on-sale-now-",
        "http://thecolbertreport.cc.com/videos/ubbze1/new-reagan-coin",
        "http://thecolbertreport.cc.com/videos/597azm/the-word---mighty-duck",
        "http://thecolbertreport.cc.com/videos/1znjlb/obama-s-lapel",
        "http://thecolbertreport.cc.com/videos/x1wzb3/the-stephen-colbert-interview",
        "http://thecolbertreport.cc.com/videos/r0xdzt/sign-off---lead-free-ink"
      ],
      "guest": "Stephen Colbert"
    },
    {
      "date": "2007-10-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vsm7hv/intro---10-10-07",
        "http://thecolbertreport.cc.com/videos/4ht7gm/dead-to-me---pocketmaster",
        "http://thecolbertreport.cc.com/videos/79ara8/the-word---americon-dream",
        "http://thecolbertreport.cc.com/videos/dzvdm0/tip-wag---bruce-springsteen",
        "http://thecolbertreport.cc.com/videos/97z30b/wesley-clark"
      ],
      "guest": "Gen. Wesley Clark"
    },
    {
      "date": "2007-10-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sprkvb/intro---10-11-07",
        "http://thecolbertreport.cc.com/videos/a27soa/black-haired-guy-who-isn-t-steve-doocy",
        "http://thecolbertreport.cc.com/videos/o6xiyi/frank-gaffney",
        "http://thecolbertreport.cc.com/videos/zipx3v/colbert-platinum---kidz-edition",
        "http://thecolbertreport.cc.com/videos/zv1po1/chris-jordan"
      ],
      "guest": "Chris Jordan"
    },
    {
      "date": "2007-10-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/56sadv/intro---10-15-07",
        "http://thecolbertreport.cc.com/videos/9esznw/who-s-honoring-me-now----marie-claire",
        "http://thecolbertreport.cc.com/videos/oogvcb/the-word---enviro-medal-disaster",
        "http://thecolbertreport.cc.com/videos/cmpb1d/kucinich-s-pockets",
        "http://thecolbertreport.cc.com/videos/biff8k/paul-glastris"
      ],
      "guest": "Dennis Kucinich, Paul Glastris"
    },
    {
      "date": "2007-10-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6k009y/intro---10-16-07",
        "http://thecolbertreport.cc.com/videos/0pl61p/planet-in-peril",
        "http://thecolbertreport.cc.com/videos/f97ynd/indecision-2008--don-t-f--k-this-up-america---presidential-bid",
        "http://thecolbertreport.cc.com/videos/9phoww/jeff-greenfield",
        "http://thecolbertreport.cc.com/videos/9j5u2v/bob-drogin"
      ],
      "guest": "Bob Drogin, Jeff Greenfield"
    },
    {
      "date": "2007-10-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e6jgx6/intro---10-17-07",
        "http://thecolbertreport.cc.com/videos/el4ceo/the-big-news",
        "http://thecolbertreport.cc.com/videos/ps9172/hail-to-the-cheese---filing-papers",
        "http://thecolbertreport.cc.com/videos/duz61o/threatdown---anniversary",
        "http://thecolbertreport.cc.com/videos/dvoers/garry-kasparov",
        "http://thecolbertreport.cc.com/videos/e0223g/sign-off---revenge-is-sweet"
      ],
      "guest": "Garry Kasparov"
    },
    {
      "date": "2007-10-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i4a6fg/intro---10-18-07",
        "http://thecolbertreport.cc.com/videos/z3kzwl/pumpkin-shortage",
        "http://thecolbertreport.cc.com/videos/6o9coa/global-scrunching---anderson-cooper",
        "http://thecolbertreport.cc.com/videos/p1wo65/hail-to-the-cheese---campaign-coverage-finance",
        "http://thecolbertreport.cc.com/videos/rcmqef/craig-newmark",
        "http://thecolbertreport.cc.com/videos/i2rw4t/sign-off---portrait-unveiled"
      ],
      "guest": "Craig Newmark, Anderson Cooper"
    },
    {
      "date": "2007-10-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3xfeo5/intro---10-29-07",
        "http://thecolbertreport.cc.com/videos/oqlp6f/the-last-infographic",
        "http://thecolbertreport.cc.com/videos/2hfe9b/hail-to-the-cheese---branded-killings",
        "http://thecolbertreport.cc.com/videos/wli1tg/the-word---absinthetinence",
        "http://thecolbertreport.cc.com/videos/49my1v/tip-wag---sleep-deprivation",
        "http://thecolbertreport.cc.com/videos/pmtsjp/richard-berman",
        "http://thecolbertreport.cc.com/videos/1yeaa0/sign-off---rocktober"
      ],
      "guest": "Richard Berman"
    },
    {
      "date": "2007-10-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6130g5/intro---10-30-07",
        "http://thecolbertreport.cc.com/videos/f3dddn/massie-ritsch",
        "http://thecolbertreport.cc.com/videos/rrhz2o/earth-attacks---georgia-drought",
        "http://thecolbertreport.cc.com/videos/czdur4/j--craig-venter"
      ],
      "guest": "Massie Ritsch, Craig Venter"
    },
    {
      "date": "2007-10-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fjrl1d/intro---10-31-07",
        "http://thecolbertreport.cc.com/videos/iwuly8/hallo-weening",
        "http://thecolbertreport.cc.com/videos/lshob0/democra-see--democra-do---elections",
        "http://thecolbertreport.cc.com/videos/pcplr6/the-word---job-description",
        "http://thecolbertreport.cc.com/videos/hpr411/obama-s-grit-off-challenge",
        "http://thecolbertreport.cc.com/videos/s7cadq/monkey-on-the-lam---lobster-edition",
        "http://thecolbertreport.cc.com/videos/4uxxf3/lawrence-wilkerson"
      ],
      "guest": "Col. Lawrence Wilkerson"
    },
    {
      "date": "2007-11-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/we8h5v/intro---11-1-07",
        "http://thecolbertreport.cc.com/videos/dzscg7/hail-to-the-cheese---ballot-issues",
        "http://thecolbertreport.cc.com/videos/9d4e78/hail-to-the-cheese---democratic-executive-council",
        "http://thecolbertreport.cc.com/videos/tcxqui/walter-kirn",
        "http://thecolbertreport.cc.com/videos/zymn63/hail-to-the-cheese---donors-choose"
      ],
      "guest": "Walter Kirn"
    }
  ],
  "2008": [
    {
      "date": "2008-01-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3q3gby/intro---1-7-08",
        "http://thecolbertreport.cc.com/videos/cva2to/applause",
        "http://thecolbertreport.cc.com/videos/mdmdd0/nothing-in-the-prompters",
        "http://thecolbertreport.cc.com/videos/lp7qsd/2008-election",
        "http://thecolbertreport.cc.com/videos/ku5oni/the-word--------",
        "http://thecolbertreport.cc.com/videos/mbip8q/democratic-change---andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/v60qiq/richard-freeman",
        "http://thecolbertreport.cc.com/videos/ckwp47/first-wrap-up"
      ],
      "guest": "Andrew Sullivan, Richard Freeman"
    },
    {
      "date": "2008-01-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8ws9bh/self-driving-car",
        "http://thecolbertreport.cc.com/videos/2785cy/bush-absolutely-optimistic",
        "http://thecolbertreport.cc.com/videos/2hhoxp/meteorite-market",
        "http://thecolbertreport.cc.com/videos/ljxmh2/chris-beam",
        "http://thecolbertreport.cc.com/videos/tl8ofm/gary-rosen",
        "http://thecolbertreport.cc.com/videos/m7kpci/note-to-strikers"
      ],
      "guest": "Chris Beam, Gary Rosen"
    },
    {
      "date": "2008-01-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/33bwbo/she-won-",
        "http://thecolbertreport.cc.com/videos/fu1w6p/new-hampshire-wrap-up",
        "http://thecolbertreport.cc.com/videos/weeodm/mike-huckabee",
        "http://thecolbertreport.cc.com/videos/d0g8tk/matt-taibbi",
        "http://thecolbertreport.cc.com/videos/je02b9/studio-on-fire"
      ],
      "guest": "Gov. Mike Huckabee, Matt Taibbi"
    },
    {
      "date": "2008-01-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/613lgd/un-american-news---primaries",
        "http://thecolbertreport.cc.com/videos/s269t4/norman-ornstein",
        "http://thecolbertreport.cc.com/videos/y7lisr/national-treasure-pt--1",
        "http://thecolbertreport.cc.com/videos/x10j2p/muhammad-yunus",
        "http://thecolbertreport.cc.com/videos/ypiss3/to-the-writers"
      ],
      "guest": "Norman Ornstein, Muhammad Yunus"
    },
    {
      "date": "2008-01-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pm5v1p/papa-bear-takes-note",
        "http://thecolbertreport.cc.com/videos/1vwzy6/around-the-world-in-11-6-seconds---lo-mein",
        "http://thecolbertreport.cc.com/videos/7k6fkq/indecision-2008--don-t-f--k-this-up-america---trustworthy-manner",
        "http://thecolbertreport.cc.com/videos/dytre7/national-treasure-pt--2",
        "http://thecolbertreport.cc.com/videos/xgsf42/neil-shubin",
        "http://thecolbertreport.cc.com/videos/tmke9w/digesting-lo-mein"
      ],
      "guest": "Neil Shubin"
    },
    {
      "date": "2008-01-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4wimo2/who-s-riding-my-coattails-now----vince-vaughn",
        "http://thecolbertreport.cc.com/videos/hrzpve/peter-hopkins",
        "http://thecolbertreport.cc.com/videos/1m3t4h/national-treasure-pt--3",
        "http://thecolbertreport.cc.com/videos/b0e6w3/jared-cohen",
        "http://thecolbertreport.cc.com/videos/4f2fw9/parting-shot"
      ],
      "guest": "Peter Hopkins, Jared Cohen"
    },
    {
      "date": "2008-01-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6mjra2/primary-update",
        "http://thecolbertreport.cc.com/videos/ng3cbb/political-roulette-pt--1",
        "http://thecolbertreport.cc.com/videos/v0glj4/back-off-mike-huckabee",
        "http://thecolbertreport.cc.com/videos/zlpayq/deborah-tannen"
      ],
      "guest": "Deborah Tannen"
    },
    {
      "date": "2008-01-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0tl5ul/push-polling",
        "http://thecolbertreport.cc.com/videos/phko2g/political-roulette-pt--2",
        "http://thecolbertreport.cc.com/videos/xj86rv/lou-dobbs",
        "http://thecolbertreport.cc.com/videos/ykpl7i/david-levy"
      ],
      "guest": "Lou Dobbs, David Levy"
    },
    {
      "date": "2008-01-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3xkco0/nevada-caucus",
        "http://thecolbertreport.cc.com/videos/qznknb/huckabee-s-message",
        "http://thecolbertreport.cc.com/videos/i2josd/allan-sloan",
        "http://thecolbertreport.cc.com/videos/wjtmux/better-know-a-governor---mark-sanford",
        "http://thecolbertreport.cc.com/videos/ia8xzl/eric-weiner"
      ],
      "guest": "Allan Sloan, Eric Weiner"
    },
    {
      "date": "2008-01-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8q1hh4/dow-drop",
        "http://thecolbertreport.cc.com/videos/7cp97e/malcolm-gladwell",
        "http://thecolbertreport.cc.com/videos/xw3v9i/andrew-young",
        "http://thecolbertreport.cc.com/videos/5tvl4o/let-my-people-go"
      ],
      "guest": "Malcolm Gladwell, Andrew Young"
    },
    {
      "date": "2008-01-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1vjtzq/fred-thompson-out",
        "http://thecolbertreport.cc.com/videos/1fbgf9/sport-report---tom-brady-s-injury",
        "http://thecolbertreport.cc.com/videos/08lghg/big-check",
        "http://thecolbertreport.cc.com/videos/wmftq8/jeb-corliss",
        "http://thecolbertreport.cc.com/videos/rp759h/andrew-mclean"
      ],
      "guest": "Marie Wood, Jeb Corliss, Andrew McLean"
    },
    {
      "date": "2008-01-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7uwyyh/rudy-in-florida",
        "http://thecolbertreport.cc.com/videos/xoh710/clinton-s-hero",
        "http://thecolbertreport.cc.com/videos/swzg9r/debra-dickerson",
        "http://thecolbertreport.cc.com/videos/0wz55a/south-carolina-debate",
        "http://thecolbertreport.cc.com/videos/bpcnyw/charles-nesson"
      ],
      "guest": "Debra Dickerson, Charles Nesson"
    },
    {
      "date": "2008-01-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/na6amv/obama-just-like-jfk",
        "http://thecolbertreport.cc.com/videos/zvtkxx/gordon-b--hinckley-died",
        "http://thecolbertreport.cc.com/videos/07hrs5/marjane-satrapi",
        "http://thecolbertreport.cc.com/videos/wrdlsf/south-carolina---what-could-have-been-",
        "http://thecolbertreport.cc.com/videos/l1477t/rick-warren"
      ],
      "guest": "Marjane Satrapi, Rick Warren"
    },
    {
      "date": "2008-01-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/aeooxe/googley-eyed-clams",
        "http://thecolbertreport.cc.com/videos/laposi/joe-quesada",
        "http://thecolbertreport.cc.com/videos/xw6ugs/french-clam",
        "http://thecolbertreport.cc.com/videos/38i4eg/alex-ross"
      ],
      "guest": "Joe Quesada, Alex Ross"
    },
    {
      "date": "2008-01-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/akx9de/exclusive---better-know-a-district---south-carolina-s-4th---bob-inglis",
        "http://thecolbertreport.cc.com/videos/t6sflk/florida-primary",
        "http://thecolbertreport.cc.com/videos/vb4t2x/carl-hiaasen",
        "http://thecolbertreport.cc.com/videos/n87g1n/better-know-a-district---south-carolina-s-4th---bob-inglis",
        "http://thecolbertreport.cc.com/videos/m4iax5/frans-de-waal"
      ],
      "guest": "Carl Hiaasen, Frans de Waal"
    },
    {
      "date": "2008-01-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z0raub/timetables",
        "http://thecolbertreport.cc.com/videos/8l0ndt/ron-paul-sounds-alarm",
        "http://thecolbertreport.cc.com/videos/2lwxda/tim-harford",
        "http://thecolbertreport.cc.com/videos/0d4uq9/people-who-are-destroying-america---pick-up-trucks",
        "http://thecolbertreport.cc.com/videos/kgrty6/andrew-napolitano"
      ],
      "guest": "Tim Harford, Andrew Napolitano"
    },
    {
      "date": "2008-02-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pwg4p2/conan-and-jon",
        "http://thecolbertreport.cc.com/videos/y5zzyu/tony-campolo",
        "http://thecolbertreport.cc.com/videos/tmuhtk/jacob-weisberg",
        "http://thecolbertreport.cc.com/videos/7r0nt2/post-show-ass-kicking"
      ],
      "guest": "Tony Campolo, Jacob Weisberg"
    },
    {
      "date": "2008-02-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yvxknz/happy-super-tuesday-",
        "http://thecolbertreport.cc.com/videos/nqwcui/hillary-is-a-target",
        "http://thecolbertreport.cc.com/videos/xonm3y/angelo-falcon",
        "http://thecolbertreport.cc.com/videos/xq9nc4/mukasey-on-torture",
        "http://thecolbertreport.cc.com/videos/gjwjsl/bob-dole"
      ],
      "guest": "Angelo Falcon, Bob Dole"
    },
    {
      "date": "2008-02-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j3dp2u/late-night-fight",
        "http://thecolbertreport.cc.com/videos/gqstf6/clap-clap-point-point",
        "http://thecolbertreport.cc.com/videos/yxx0w5/richard-brookhiser",
        "http://thecolbertreport.cc.com/videos/ammxmv/better-know-a-lobby---human-rights-campaign-pt--1",
        "http://thecolbertreport.cc.com/videos/nhkpwj/tad-devine"
      ],
      "guest": "Tad Devine"
    },
    {
      "date": "2008-02-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ctzo98/stephen-s-ethnic-minute",
        "http://thecolbertreport.cc.com/videos/v43el0/huckabee-s-still-in",
        "http://thecolbertreport.cc.com/videos/negp2q/better-know-a-lobby---human-rights-campaign-pt--2",
        "http://thecolbertreport.cc.com/videos/oxf63b/mark-moffett"
      ],
      "guest": "Mark Moffett"
    },
    {
      "date": "2008-02-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bs8egm/obama-wins-a-grammy",
        "http://thecolbertreport.cc.com/videos/lnkbna/goodbye-mitt",
        "http://thecolbertreport.cc.com/videos/myptag/aubrey-de-grey",
        "http://thecolbertreport.cc.com/videos/in3tg3/portrait-check-in",
        "http://thecolbertreport.cc.com/videos/8sjpoa/philip-zimbardo"
      ],
      "guest": "Aubrey de Grey, Philip Zimbardo"
    },
    {
      "date": "2008-02-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gucgvs/huckabee-s-obligation",
        "http://thecolbertreport.cc.com/videos/6g98j7/eliot-spitzer",
        "http://thecolbertreport.cc.com/videos/udbv19/eleanor-holmes-norton",
        "http://thecolbertreport.cc.com/videos/ekpicq/lisa-randall"
      ],
      "guest": "Gov. Eliot Spitzer, Eleanor Holmes Norton, Lisa Randall"
    },
    {
      "date": "2008-02-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r9rjo5/intro---2-13-08",
        "http://thecolbertreport.cc.com/videos/mvp1nc/the-writers-return-",
        "http://thecolbertreport.cc.com/videos/n3dwin/david-gracer",
        "http://thecolbertreport.cc.com/videos/aebxex/neil-de-grasse-tyson",
        "http://thecolbertreport.cc.com/videos/n39iqt/richard-thompson-ford"
      ],
      "guest": "David Gracer, Richard Thompson Ford"
    },
    {
      "date": "2008-02-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5hf18t/intro---2-14-08",
        "http://thecolbertreport.cc.com/videos/qg63hg/who-s-riding-my-coattails-now----oliver-pocher",
        "http://thecolbertreport.cc.com/videos/slbgcr/clemens-hearing",
        "http://thecolbertreport.cc.com/videos/0i3hg8/john-feinstein",
        "http://thecolbertreport.cc.com/videos/dmxs6z/people-who-are-destroying-america---happy-meal",
        "http://thecolbertreport.cc.com/videos/hxt6mo/leonard-nimoy"
      ],
      "guest": "John Feinstein, Leonard Nimoy"
    },
    {
      "date": "2008-02-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t6xzxc/intro---2-26-08",
        "http://thecolbertreport.cc.com/videos/cexk3g/obama-s-photo",
        "http://thecolbertreport.cc.com/videos/x6h69l/the-word---good-bad-journalism",
        "http://thecolbertreport.cc.com/videos/4s0owa/henry-louis-gates-jr-"
      ],
      "guest": "Henry Louis Gates Jr."
    },
    {
      "date": "2008-02-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3uzan2/exclusive---guitar-heroes",
        "http://thecolbertreport.cc.com/videos/spigs3/intro---2-27-08",
        "http://thecolbertreport.cc.com/videos/fb142a/mccain-rally",
        "http://thecolbertreport.cc.com/videos/717g03/threatdown---air-colbert",
        "http://thecolbertreport.cc.com/videos/ni7mzt/tony-snow"
      ],
      "guest": "Tony Snow"
    },
    {
      "date": "2008-02-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/upjayy/the-music-man",
        "http://thecolbertreport.cc.com/videos/80mnx9/intro---2-28-08",
        "http://thecolbertreport.cc.com/videos/wq9qga/russian-billboard",
        "http://thecolbertreport.cc.com/videos/c64r8o/cold-war-update",
        "http://thecolbertreport.cc.com/videos/zrhp7w/richard-brookhiser",
        "http://thecolbertreport.cc.com/videos/n7g9t0/ingrid-newkirk",
        "http://thecolbertreport.cc.com/videos/zsj0rq/sign-off---shoe-phone"
      ],
      "guest": "Richard Brookhiser, Ingrid Newkirk"
    },
    {
      "date": "2008-03-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/laopsy/intro---3-3-08",
        "http://thecolbertreport.cc.com/videos/1gyoec/the-coveted-colbert-bump",
        "http://thecolbertreport.cc.com/videos/do24ht/das-booty---hitler-s-gold-pt--1",
        "http://thecolbertreport.cc.com/videos/dvfqt3/maestro-lorin-maazel",
        "http://thecolbertreport.cc.com/videos/8llta1/shashi-tharoor",
        "http://thecolbertreport.cc.com/videos/beqjns/leap-day"
      ],
      "guest": "Lorin Maazel, Shashi Tharoor"
    },
    {
      "date": "2008-03-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1d4djp/intro---3-4-08",
        "http://thecolbertreport.cc.com/videos/509s01/william-donohue",
        "http://thecolbertreport.cc.com/videos/myyov6/howard-dean",
        "http://thecolbertreport.cc.com/videos/wvt9ny/nailed--em---graffiti-punk",
        "http://thecolbertreport.cc.com/videos/86yukf/jennifer-8--lee",
        "http://thecolbertreport.cc.com/videos/10okbb/to-howard-dean",
        "http://thecolbertreport.cc.com/videos/q08fbb/the-word---experience"
      ],
      "guest": "William Donohue, Howard Dean, Jennifer 8. Lee"
    },
    {
      "date": "2008-03-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9o2e4d/intro---3-5-08",
        "http://thecolbertreport.cc.com/videos/d60bre/farewell-brett-favre",
        "http://thecolbertreport.cc.com/videos/q038rv/hucka-bye",
        "http://thecolbertreport.cc.com/videos/6296yb/robert-reich",
        "http://thecolbertreport.cc.com/videos/lrlzri/difference-makers---free-implants",
        "http://thecolbertreport.cc.com/videos/z6yixf/gregory-rodriguez",
        "http://thecolbertreport.cc.com/videos/p6i1w8/r-i-p--gary-gygax"
      ],
      "guest": "Robert Reich, Gregory Rodriguez"
    },
    {
      "date": "2008-03-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zoimd4/intro---3-6-08",
        "http://thecolbertreport.cc.com/videos/m9ob1y/hot-dog-with-the-president",
        "http://thecolbertreport.cc.com/videos/i9idne/the-word---at---treason",
        "http://thecolbertreport.cc.com/videos/0ih0ea/cheating-death---surgery",
        "http://thecolbertreport.cc.com/videos/cv6bwa/john-legend"
      ],
      "guest": "John Legend"
    },
    {
      "date": "2008-03-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mahtb2/intro---3-10-08",
        "http://thecolbertreport.cc.com/videos/3a9bum/whores-",
        "http://thecolbertreport.cc.com/videos/8p3t8b/the-word---size-matters",
        "http://thecolbertreport.cc.com/videos/fdo5yd/the--72-democrats",
        "http://thecolbertreport.cc.com/videos/7m46n6/george-mcgovern"
      ],
      "guest": "George McGovern"
    },
    {
      "date": "2008-03-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3ybl08/intro---3-11-08",
        "http://thecolbertreport.cc.com/videos/me89dy/spitzer-greeting-cards",
        "http://thecolbertreport.cc.com/videos/twuo43/the-word---mr--right-now",
        "http://thecolbertreport.cc.com/videos/f7ltv5/colbert-platinum---liechtenstein",
        "http://thecolbertreport.cc.com/videos/gcwzrr/geraldo-rivera",
        "http://thecolbertreport.cc.com/videos/8h6jvx/sign-off---show-s-over--america"
      ],
      "guest": "Geraldo Rivera"
    },
    {
      "date": "2008-03-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tvzv05/intro---3-12-08",
        "http://thecolbertreport.cc.com/videos/ntzxtt/spitzer-sandwich",
        "http://thecolbertreport.cc.com/videos/ippftn/smokin--pole---alaska",
        "http://thecolbertreport.cc.com/videos/50a47x/better-know-a-lobby---drug-policy-alliance",
        "http://thecolbertreport.cc.com/videos/nouiem/howard-kurtz"
      ],
      "guest": "Howard Kurtz"
    },
    {
      "date": "2008-03-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gpd5cu/intro---3-13-08",
        "http://thecolbertreport.cc.com/videos/k8bsjv/airborne-lawsuit",
        "http://thecolbertreport.cc.com/videos/d51tqz/democralypse-now---ferraro",
        "http://thecolbertreport.cc.com/videos/tvjvip/hussein-ibish",
        "http://thecolbertreport.cc.com/videos/oe7yd2/difference-makers---doug-jackson",
        "http://thecolbertreport.cc.com/videos/mzut29/sudhir-venkatesh"
      ],
      "guest": "Hussein Ibish, Sudhir Venkatesh"
    },
    {
      "date": "2008-03-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ck2j7u/exclusive---spitzer",
        "http://thecolbertreport.cc.com/videos/8zfc9q/intro---3-17-08",
        "http://thecolbertreport.cc.com/videos/v28dea/stephen-in-philly",
        "http://thecolbertreport.cc.com/videos/rxdrv8/the-word---the-audacity-of-hopelessness",
        "http://thecolbertreport.cc.com/videos/tw4jo4/people-who-are-destroying-america---st--patrick-s-day",
        "http://thecolbertreport.cc.com/videos/5j8sg4/samantha-power"
      ],
      "guest": "Samantha Power"
    },
    {
      "date": "2008-03-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vgwiie/intro---3-18-08",
        "http://thecolbertreport.cc.com/videos/wsz08m/yes-we-can-",
        "http://thecolbertreport.cc.com/videos/xtwx8p/spicy-sweet-coverage",
        "http://thecolbertreport.cc.com/videos/mogf73/das-booty---hitler-s-gold-pt--2",
        "http://thecolbertreport.cc.com/videos/5boih5/carole-king"
      ],
      "guest": "Carole King"
    },
    {
      "date": "2008-03-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hcafrk/intro---3-19-08",
        "http://thecolbertreport.cc.com/videos/hrjm1z/patterson-affair",
        "http://thecolbertreport.cc.com/videos/scqdwy/the-word---the-gospel-of-john",
        "http://thecolbertreport.cc.com/videos/y6aybj/pennsylvania-primary",
        "http://thecolbertreport.cc.com/videos/037ygf/tip-wag---afghanistan",
        "http://thecolbertreport.cc.com/videos/vk922m/dee-dee-myers"
      ],
      "guest": "Dee Dee Myers"
    },
    {
      "date": "2008-03-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vq76dq/watershift-down--getting-the-sea-monkey-off-america-s-aqua-back",
        "http://thecolbertreport.cc.com/videos/wkdrt1/aqua-colbert",
        "http://thecolbertreport.cc.com/videos/l1sl1c/water-is-life",
        "http://thecolbertreport.cc.com/videos/3mtvfm/dean-kamen",
        "http://thecolbertreport.cc.com/videos/4y9sds/setting-water-on-fire"
      ],
      "guest": "Dean Kamen"
    },
    {
      "date": "2008-03-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f3rbbv/intro---3-31-08",
        "http://thecolbertreport.cc.com/videos/aqkiox/opening-day",
        "http://thecolbertreport.cc.com/videos/0fo1qd/bowling-in-pa",
        "http://thecolbertreport.cc.com/videos/2ii77j/eric-alterman",
        "http://thecolbertreport.cc.com/videos/b149k1/tek-jansen---beginning-s-first-dawn--episode-one-revisited",
        "http://thecolbertreport.cc.com/videos/3p6caw/michael-reynolds"
      ],
      "guest": "Eric Alterman, Michael Reynolds"
    },
    {
      "date": "2008-04-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ayieu5/intro---4-1-08",
        "http://thecolbertreport.cc.com/videos/irlo9m/portrait-update",
        "http://thecolbertreport.cc.com/videos/inwuqm/the-word---pick-sicks",
        "http://thecolbertreport.cc.com/videos/fpyy9k/bears---balls---rat-rakes",
        "http://thecolbertreport.cc.com/videos/700kdb/van-jones",
        "http://thecolbertreport.cc.com/videos/lrepiq/portrait-displayed"
      ],
      "guest": "Van Jones"
    },
    {
      "date": "2008-04-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/46s8py/intro---4-2-08",
        "http://thecolbertreport.cc.com/videos/sbidx5/stephen-wins-a-peabody",
        "http://thecolbertreport.cc.com/videos/3fc86e/threatdown---nipples",
        "http://thecolbertreport.cc.com/videos/n3f5qh/r-e-m-"
      ],
      "guest": "R.E.M."
    },
    {
      "date": "2008-04-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/aj43z8/intro---4-3-08",
        "http://thecolbertreport.cc.com/videos/tyapiy/peabody-credit",
        "http://thecolbertreport.cc.com/videos/xwlefp/the-word---let-the-games-begin",
        "http://thecolbertreport.cc.com/videos/gx1oov/tek-jansen---beginning-s-first-dawn--episode-two",
        "http://thecolbertreport.cc.com/videos/dm9a7h/clay-shirky",
        "http://thecolbertreport.cc.com/videos/jsqez9/tek-jansen---you-are-the-best"
      ],
      "guest": "Clay Shirky"
    },
    {
      "date": "2008-04-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7lye0f/intro---4-7-08",
        "http://thecolbertreport.cc.com/videos/we6e20/r-i-p--charlton-heston",
        "http://thecolbertreport.cc.com/videos/xh2gv1/trevor-paglen",
        "http://thecolbertreport.cc.com/videos/3xlgs3/democralypse-now---3am",
        "http://thecolbertreport.cc.com/videos/82gipv/jesse-ventura"
      ],
      "guest": "Trevor Paglen, Jesse Ventura"
    },
    {
      "date": "2008-04-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/54jfl6/intro---4-8-08",
        "http://thecolbertreport.cc.com/videos/yme30m/pope-coming-to-nyc",
        "http://thecolbertreport.cc.com/videos/g0ke6u/children-s-drawings",
        "http://thecolbertreport.cc.com/videos/0dimmt/wilford-brimley-calls---donation",
        "http://thecolbertreport.cc.com/videos/elawer/madeleine-albright"
      ],
      "guest": "Madeleine Albright"
    },
    {
      "date": "2008-04-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bdme3x/intro---4-9-08",
        "http://thecolbertreport.cc.com/videos/iekisu/olympic-torch",
        "http://thecolbertreport.cc.com/videos/ypse7c/the-word---starter-country",
        "http://thecolbertreport.cc.com/videos/jycq7p/cheating-death---sexual-health",
        "http://thecolbertreport.cc.com/videos/nlvpn4/jeff-gore"
      ],
      "guest": "Jeff Gore"
    },
    {
      "date": "2008-04-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zsmonm/intro---4-10-08",
        "http://thecolbertreport.cc.com/videos/6sdfwa/petraeus-hearings",
        "http://thecolbertreport.cc.com/videos/x8pxwi/more-drawings-from-kids",
        "http://thecolbertreport.cc.com/videos/z2z65o/the-word---black-and-white",
        "http://thecolbertreport.cc.com/videos/v1k50e/tip-wag---rain",
        "http://thecolbertreport.cc.com/videos/torkh7/robin-wright"
      ],
      "guest": "Robin Wright"
    },
    {
      "date": "2008-04-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qfrdo9/from-philadelphia",
        "http://thecolbertreport.cc.com/videos/5phute/pennsylvania-primary-history",
        "http://thecolbertreport.cc.com/videos/1b60fj/chris-matthews"
      ],
      "guest": "Chris Matthews"
    },
    {
      "date": "2008-04-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oj9blc/intro---4-15-08",
        "http://thecolbertreport.cc.com/videos/3aqwqx/nice-roomba",
        "http://thecolbertreport.cc.com/videos/ad5qga/the-word---tradition",
        "http://thecolbertreport.cc.com/videos/7unrts/independence-park",
        "http://thecolbertreport.cc.com/videos/upl7xe/michelle-obama"
      ],
      "guest": "Michelle Obama, The Roots"
    },
    {
      "date": "2008-04-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h0lfw9/intro---4-16-08",
        "http://thecolbertreport.cc.com/videos/pi51oz/jackie-o--amendment",
        "http://thecolbertreport.cc.com/videos/9z3000/democralypse-now---the-boss",
        "http://thecolbertreport.cc.com/videos/9zm7cy/national-constitution-center",
        "http://thecolbertreport.cc.com/videos/51r39w/ed-rendell",
        "http://thecolbertreport.cc.com/videos/1bzrgk/benjamin-franklin-s-news"
      ],
      "guest": "Philadelphia Eagles Cheerleaders, Gov. Ed Rendell"
    },
    {
      "date": "2008-04-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ky7oxg/benjamin-franklin-s-latest-invention",
        "http://thecolbertreport.cc.com/videos/uzusr0/hillary-clinton-takes-on-technical-difficulties",
        "http://thecolbertreport.cc.com/videos/1i62sd/clinton-vs--obama-philadelphia-debate-review",
        "http://thecolbertreport.cc.com/videos/ew5t9y/patrick-murphy",
        "http://thecolbertreport.cc.com/videos/x3zme5/the-ed-words---valued-voter",
        "http://thecolbertreport.cc.com/videos/ol0nn3/on-notice---barack-obama-against-distractions"
      ],
      "guest": "Hillary Clinton, John Edwards, Barack Obama"
    },
    {
      "date": "2008-04-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i6ihlp/intro---4-21-08",
        "http://thecolbertreport.cc.com/videos/foffke/philly-loves-colbert-nation",
        "http://thecolbertreport.cc.com/videos/5jm58y/global-food-shortage",
        "http://thecolbertreport.cc.com/videos/ehgxth/father-james-martin",
        "http://thecolbertreport.cc.com/videos/oo6wpp/bernie-sanders",
        "http://thecolbertreport.cc.com/videos/e7gpah/farewell-to-bobby"
      ],
      "guest": "Fr. James Martin, Sen. Bernie Sanders"
    },
    {
      "date": "2008-04-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ah79bq/intro---4-22-08",
        "http://thecolbertreport.cc.com/videos/tp640v/earth-is-awesome",
        "http://thecolbertreport.cc.com/videos/uyxyc7/obama-copycattery",
        "http://thecolbertreport.cc.com/videos/a2ha6c/indecision-cheesesteaks",
        "http://thecolbertreport.cc.com/videos/0nsiap/better-know-a-district---pennsylvania-s-7th---joe-sestak",
        "http://thecolbertreport.cc.com/videos/5427ng/susan-jacoby",
        "http://thecolbertreport.cc.com/videos/l34czb/exclusive---better-know-a-district---pennsylvania-s-7th---joe-sestak"
      ],
      "guest": "Susan Jacoby"
    },
    {
      "date": "2008-04-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lxpsri/intro---4-23-08",
        "http://thecolbertreport.cc.com/videos/6wperh/rain-rivalry-challenge",
        "http://thecolbertreport.cc.com/videos/hpr26d/the-word---iraq-the-vote",
        "http://thecolbertreport.cc.com/videos/fqo64s/colbert-platinum---cat-pooped-coffee",
        "http://thecolbertreport.cc.com/videos/5azl7m/mitch-albom",
        "http://thecolbertreport.cc.com/videos/qdf6zq/the-lost-o-reilly-tapes-pt--1"
      ],
      "guest": "Mitch Albom"
    },
    {
      "date": "2008-04-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6kux9r/intro---4-24-08",
        "http://thecolbertreport.cc.com/videos/a1qle2/petraeus--promotion",
        "http://thecolbertreport.cc.com/videos/uddwea/threatdown---juicing-bulls",
        "http://thecolbertreport.cc.com/videos/e3l9yt/difference-makers---bumbot",
        "http://thecolbertreport.cc.com/videos/lr9uai/maria-shriver"
      ],
      "guest": "Maria Shriver"
    },
    {
      "date": "2008-04-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3fwic4/intro---4-28-08",
        "http://thecolbertreport.cc.com/videos/244o0l/miley-cyrus-photo-shoot",
        "http://thecolbertreport.cc.com/videos/9v4qwg/electability",
        "http://thecolbertreport.cc.com/videos/ejbmnx/the-word---kernel-of-truth",
        "http://thecolbertreport.cc.com/videos/3osshb/sport-report---timbersports",
        "http://thecolbertreport.cc.com/videos/222rjo/feist"
      ],
      "guest": "Feist"
    },
    {
      "date": "2008-04-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a1muh6/intro---4-29-08",
        "http://thecolbertreport.cc.com/videos/vc3sa7/obama-breaks-with-wright",
        "http://thecolbertreport.cc.com/videos/uk74h6/mccain-s-superstitions",
        "http://thecolbertreport.cc.com/videos/ry65tk/the-word---separation-of-church---plate",
        "http://thecolbertreport.cc.com/videos/cy9dmw/tip-wag---barbie",
        "http://thecolbertreport.cc.com/videos/s3buaq/anne-lamott"
      ],
      "guest": "Anne Lamott"
    },
    {
      "date": "2008-04-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/byoxj1/intro---4-30-08",
        "http://thecolbertreport.cc.com/videos/xju86c/salinger-watch",
        "http://thecolbertreport.cc.com/videos/1rdkem/donna-brazile-on-the-democratic-campaign",
        "http://thecolbertreport.cc.com/videos/4ngs9u/better-know-a-protectorate---guam---madeleine-bordallo-update",
        "http://thecolbertreport.cc.com/videos/vjk2cd/noah-feldman"
      ],
      "guest": "Donna Brazile, Noah Feldman"
    },
    {
      "date": "2008-05-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1zd3gn/intro---5-01-08",
        "http://thecolbertreport.cc.com/videos/clfbo3/jenna-bush-wedding",
        "http://thecolbertreport.cc.com/videos/sctmlw/trailers-destroying-america---summer-movie-edition",
        "http://thecolbertreport.cc.com/videos/aka0f3/formidable-opponent---electability",
        "http://thecolbertreport.cc.com/videos/zck6ux/james-howard-kunstler"
      ],
      "guest": "James Kunstler"
    },
    {
      "date": "2008-05-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nhsr7z/intro---5-05-08",
        "http://thecolbertreport.cc.com/videos/wtbn4l/time-s-2008-top-100-most-influential",
        "http://thecolbertreport.cc.com/videos/x20ttg/the-word---free-gas-",
        "http://thecolbertreport.cc.com/videos/oov14y/speed-racer",
        "http://thecolbertreport.cc.com/videos/91hddq/alpha-dog-of-the-week---911-operator",
        "http://thecolbertreport.cc.com/videos/2uj60r/carl-hiaasen",
        "http://thecolbertreport.cc.com/videos/k44vbf/rain-dance-off"
      ],
      "guest": "Carl Hiaasen"
    },
    {
      "date": "2008-05-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e38w0k/intro---5-06-08",
        "http://thecolbertreport.cc.com/videos/e3fb1q/sexy-voice-study",
        "http://thecolbertreport.cc.com/videos/qy6hoq/the-word---collateral-friendage",
        "http://thecolbertreport.cc.com/videos/byyq8n/stephen-s-sound-advice---karl-s-advice",
        "http://thecolbertreport.cc.com/videos/y777b4/nathan-gunn"
      ],
      "guest": "Nathan Gunn"
    },
    {
      "date": "2008-05-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fk83lx/intro---5-07-08",
        "http://thecolbertreport.cc.com/videos/20qjta/stephen-colbert-s-shockettes",
        "http://thecolbertreport.cc.com/videos/su4v1v/terrorist-nelson-mandela",
        "http://thecolbertreport.cc.com/videos/07p71k/hasan-elahi",
        "http://thecolbertreport.cc.com/videos/bc4u9e/democralypse-now---justin-myers",
        "http://thecolbertreport.cc.com/videos/av0o9p/george-johnson"
      ],
      "guest": "Hasan Elahi, George Johnson"
    },
    {
      "date": "2008-05-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ey98z2/exclusive---stephen-vs--rain",
        "http://thecolbertreport.cc.com/videos/6wn8i5/garrett-reisman",
        "http://thecolbertreport.cc.com/videos/qnk6x8/gas-dollar",
        "http://thecolbertreport.cc.com/videos/txq3hp/arianna-huffington",
        "http://thecolbertreport.cc.com/videos/uafvva/r-i-p--albert-hoffman"
      ],
      "guest": "Arianna Huffington"
    },
    {
      "date": "2008-05-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/da4u0g/intro---5-12-08",
        "http://thecolbertreport.cc.com/videos/tj7sih/big-russ",
        "http://thecolbertreport.cc.com/videos/kdeptj/cold-war-update---russia",
        "http://thecolbertreport.cc.com/videos/k7k3ke/threatdown---cute-bears",
        "http://thecolbertreport.cc.com/videos/3i279j/dr--mehmet-oz"
      ],
      "guest": "Dr. Mehmet Oz"
    },
    {
      "date": "2008-05-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oycul0/exclusive---better-know-a-lobby---brady-campaign-to-prevent-gun-violence",
        "http://thecolbertreport.cc.com/videos/1siped/intro---5-13-08",
        "http://thecolbertreport.cc.com/videos/mpq03a/hillary-drop-out",
        "http://thecolbertreport.cc.com/videos/qxr59r/bill-o-reilly-inside-edition",
        "http://thecolbertreport.cc.com/videos/np2mes/better-know-a-lobby---brady-campaign-to-prevent-gun-violence",
        "http://thecolbertreport.cc.com/videos/24b8xh/jennifer-hooper-mccarty"
      ],
      "guest": "Jennifer Hooper McCarty"
    },
    {
      "date": "2008-05-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/suewpq/intro---5-14-08",
        "http://thecolbertreport.cc.com/videos/fygt2g/edwards-supports-obama",
        "http://thecolbertreport.cc.com/videos/ry9ff3/who-s-not-honoring-me-now----science",
        "http://thecolbertreport.cc.com/videos/xnkjrq/the-word---declaration-of-warming",
        "http://thecolbertreport.cc.com/videos/gxghyw/laura-dern",
        "http://thecolbertreport.cc.com/videos/4tldfc/grover-norquist",
        "http://thecolbertreport.cc.com/videos/zujfq0/the-show-comes-to-an-end"
      ],
      "guest": "Laura Dern, Grover Norquist"
    },
    {
      "date": "2008-05-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nkmoxa/intro---5-15-08",
        "http://thecolbertreport.cc.com/videos/ekfqs4/american-craft-beer-week",
        "http://thecolbertreport.cc.com/videos/wy0c00/edwards-endorses-obama",
        "http://thecolbertreport.cc.com/videos/scm34l/the-word---jail-sweet-jail",
        "http://thecolbertreport.cc.com/videos/ak0o7t/bears---balls---dollar-stores",
        "http://thecolbertreport.cc.com/videos/rarvxz/andrei-cherny"
      ],
      "guest": "Andrei Cherny"
    },
    {
      "date": "2008-05-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v79z0o/intro---5-27-08",
        "http://thecolbertreport.cc.com/videos/k0kiom/fleet-week",
        "http://thecolbertreport.cc.com/videos/xuhumb/mccain-s-preachers",
        "http://thecolbertreport.cc.com/videos/dxmleo/tony-perkins",
        "http://thecolbertreport.cc.com/videos/o5c67w/brian-greene"
      ],
      "guest": "Tony Perkins, Brian Greene"
    },
    {
      "date": "2008-05-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tuxwuw/intro---5-28-08",
        "http://thecolbertreport.cc.com/videos/euhkkf/microbe-beat-",
        "http://thecolbertreport.cc.com/videos/z1nl4c/the-word---brushback-pitch",
        "http://thecolbertreport.cc.com/videos/jhmlmk/cheating-death---liquid-launch",
        "http://thecolbertreport.cc.com/videos/ngaz1d/claire-mccaskill"
      ],
      "guest": "Sen. Claire McCaskill"
    },
    {
      "date": "2008-05-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6wfa6q/intro---5-29-08",
        "http://thecolbertreport.cc.com/videos/79u1cf/shout-out----broken-space-toilet",
        "http://thecolbertreport.cc.com/videos/6735i1/democralypse-now---florida-and-michigan",
        "http://thecolbertreport.cc.com/videos/ug78n1/tad-devine",
        "http://thecolbertreport.cc.com/videos/lhma93/tip-wag---monetary-discrimination",
        "http://thecolbertreport.cc.com/videos/3qprbm/david-sirota",
        "http://thecolbertreport.cc.com/videos/g0kftc/sneak-preview"
      ],
      "guest": "Tad Devine, David Sirota"
    },
    {
      "date": "2008-06-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hrlfp0/intro---6-02-08",
        "http://thecolbertreport.cc.com/videos/dvmsby/obama-s-church",
        "http://thecolbertreport.cc.com/videos/38jpc2/fire-at-universal",
        "http://thecolbertreport.cc.com/videos/jlvsj6/the-word---media-culpa",
        "http://thecolbertreport.cc.com/videos/8cygn0/colbert-platinum---private-jets",
        "http://thecolbertreport.cc.com/videos/p0u6f8/jon-paskowitz",
        "http://thecolbertreport.cc.com/videos/piym7c/final-thought"
      ],
      "guest": "Jon Paskowitz"
    },
    {
      "date": "2008-06-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4vr7xb/intro---6-03-08",
        "http://thecolbertreport.cc.com/videos/o005k6/democratic-primaries-over",
        "http://thecolbertreport.cc.com/videos/viwun3/the-word---unhealthy-competition",
        "http://thecolbertreport.cc.com/videos/po30h9/stephen-s-sound-advice---summer-jobs",
        "http://thecolbertreport.cc.com/videos/xhigi4/george-will"
      ],
      "guest": "George Will"
    },
    {
      "date": "2008-06-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0w2khv/intro---6-04-08",
        "http://thecolbertreport.cc.com/videos/hfq15q/john-mccain-s-green-screen-challenge",
        "http://thecolbertreport.cc.com/videos/wsbc0i/libertarian-party---bob-barr",
        "http://thecolbertreport.cc.com/videos/sn90ui/salman-rushdie",
        "http://thecolbertreport.cc.com/videos/uji4o5/the-lost-o-reilly-tapes-pt--2"
      ],
      "guest": "Rep. Bob Barr, Salman Rushdie"
    },
    {
      "date": "2008-06-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yv02dd/intro---6-05-08",
        "http://thecolbertreport.cc.com/videos/n90wjr/the-andromeda-strain",
        "http://thecolbertreport.cc.com/videos/ugt12v/the-word---oh--the-places-you-ll-stay",
        "http://thecolbertreport.cc.com/videos/6nrkel/sport-report---mike-forrester",
        "http://thecolbertreport.cc.com/videos/ibt0j9/pat-buchanan"
      ],
      "guest": "Pat Buchanan"
    },
    {
      "date": "2008-06-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qowh4f/intro---6-09-08",
        "http://thecolbertreport.cc.com/videos/icuy8o/democralypse-now---hillary-concedes",
        "http://thecolbertreport.cc.com/videos/numnri/the-word---if-at-first-you-don-t-secede",
        "http://thecolbertreport.cc.com/videos/vlab0d/threatdown---secret-negro-presidents",
        "http://thecolbertreport.cc.com/videos/gv27al/philip-weiss"
      ],
      "guest": "Phil Weiss"
    },
    {
      "date": "2008-06-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/705tqw/intro---6-10-08",
        "http://thecolbertreport.cc.com/videos/cbjixz/new-giant-iphone",
        "http://thecolbertreport.cc.com/videos/w5you4/tickling-the-rocks",
        "http://thecolbertreport.cc.com/videos/skw5sl/the-elitist-menace-among-us",
        "http://thecolbertreport.cc.com/videos/qhpj5f/smokin--pole---canada-s-hockey-theme",
        "http://thecolbertreport.cc.com/videos/9bdggo/alan-rabinowitz"
      ],
      "guest": "Alan Rabinowitz"
    },
    {
      "date": "2008-06-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/373j1n/intro---6-11-08",
        "http://thecolbertreport.cc.com/videos/gbgmuk/israel-s-new-bird",
        "http://thecolbertreport.cc.com/videos/twddgu/the-word---u-s--airweighs",
        "http://thecolbertreport.cc.com/videos/pp8c40/un-american-news---u-s--election-edition",
        "http://thecolbertreport.cc.com/videos/zudzs0/david-hajdu",
        "http://thecolbertreport.cc.com/videos/idly59/memorized-script"
      ],
      "guest": "David Hajdu"
    },
    {
      "date": "2008-06-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mpfrre/intro---6-12-08",
        "http://thecolbertreport.cc.com/videos/nsgvgc/stephen-colbert-s-make-mccain-exciting-challenge-",
        "http://thecolbertreport.cc.com/videos/86su5q/winona-laduke",
        "http://thecolbertreport.cc.com/videos/qrbimj/we-the-mediator",
        "http://thecolbertreport.cc.com/videos/t6nh85/dickson-despommier"
      ],
      "guest": "Winona LaDuke, Dixon Despommier"
    },
    {
      "date": "2008-06-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vnwwom/intro---6-16-08",
        "http://thecolbertreport.cc.com/videos/6vk2ye/tim-russert-tribute",
        "http://thecolbertreport.cc.com/videos/mpqoje/the-word---ploy-cott",
        "http://thecolbertreport.cc.com/videos/cqvvlk/the-enemy-within---wizard-teachers",
        "http://thecolbertreport.cc.com/videos/8xg385/kenneth-miller"
      ],
      "guest": "Kenneth R. Miller"
    },
    {
      "date": "2008-06-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jfofbj/intro---6-17-08",
        "http://thecolbertreport.cc.com/videos/kwlu8o/peabody-award",
        "http://thecolbertreport.cc.com/videos/tapfcu/neal-katyal",
        "http://thecolbertreport.cc.com/videos/fuhy6f/sport-report---timbersports-championship",
        "http://thecolbertreport.cc.com/videos/vcz3hv/jonathan-zittrain",
        "http://thecolbertreport.cc.com/videos/ci1ljt/peabody-on-mantel"
      ],
      "guest": "Neal Katyal, Jonathan Zittrain"
    },
    {
      "date": "2008-06-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b2ddmd/intro---6-18-08",
        "http://thecolbertreport.cc.com/videos/prx5o1/the-new-smurfs-movie",
        "http://thecolbertreport.cc.com/videos/ciovvr/the-word---lexicon-artist",
        "http://thecolbertreport.cc.com/videos/vtx5qc/barack-obama-s-church-search---dr--uma-mysorekar",
        "http://thecolbertreport.cc.com/videos/ir7gne/junot-diaz"
      ],
      "guest": "Dr. Uma Mysorekar, Junot Diaz"
    },
    {
      "date": "2008-06-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d6b6nb/intro---6-19-08",
        "http://thecolbertreport.cc.com/videos/6sj17e/shout-out---peabody-awards",
        "http://thecolbertreport.cc.com/videos/mr1053/sean-hannity-loves-america",
        "http://thecolbertreport.cc.com/videos/zcd35g/cookie-monster",
        "http://thecolbertreport.cc.com/videos/aytt4h/make-mccain-exciting-challenge---the-secret-of-mccain-s-brain",
        "http://thecolbertreport.cc.com/videos/m7daav/bishop-n-t--wright",
        "http://thecolbertreport.cc.com/videos/der3el/stephen-s-missing-peabody"
      ],
      "guest": "Bishop N.T. Wright"
    },
    {
      "date": "2008-06-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ua8qbe/intro---6-23-08",
        "http://thecolbertreport.cc.com/videos/a4nt5i/wriststrong-anniversary",
        "http://thecolbertreport.cc.com/videos/kj72hq/the-word---black-and-white",
        "http://thecolbertreport.cc.com/videos/vlidof/tip-wag---barack-obama",
        "http://thecolbertreport.cc.com/videos/ymze92/barbara-ehrenreich",
        "http://thecolbertreport.cc.com/videos/1f40by/sign-off---time-for-stephen-to-watch"
      ],
      "guest": "Barbara Ehrenreich"
    },
    {
      "date": "2008-06-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mhd7wr/intro---6-24-08",
        "http://thecolbertreport.cc.com/videos/n11h6w/hollywood-face-violence",
        "http://thecolbertreport.cc.com/videos/ov4362/oil-crisis",
        "http://thecolbertreport.cc.com/videos/hxtoyj/the-word---bleep",
        "http://thecolbertreport.cc.com/videos/f5yznc/dr--jason-bond",
        "http://thecolbertreport.cc.com/videos/ilejmp/will-smith"
      ],
      "guest": "Jason Bond, Will Smith"
    },
    {
      "date": "2008-06-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mdtg3q/intro---6-25-08",
        "http://thecolbertreport.cc.com/videos/q0qc77/paul-goldberger",
        "http://thecolbertreport.cc.com/videos/ajsxzq/judge--jury---executioner---whales",
        "http://thecolbertreport.cc.com/videos/zucjth/neil-degrasse-tyson",
        "http://thecolbertreport.cc.com/videos/2r47v6/stephen-s-gun"
      ],
      "guest": "Paul Goldberger, Neil deGrasse Tyson"
    },
    {
      "date": "2008-06-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gvc60t/intro---6-26-08",
        "http://thecolbertreport.cc.com/videos/038ej3/stephen-and-sweetness",
        "http://thecolbertreport.cc.com/videos/txteih/the-tank-is-half-full---criminals",
        "http://thecolbertreport.cc.com/videos/hdan1z/difference-makers---steve-pelkey",
        "http://thecolbertreport.cc.com/videos/6vucxh/robert-wexler",
        "http://thecolbertreport.cc.com/videos/s7cul5/stephen-packs-for-his-trip"
      ],
      "guest": "Rep. Robert Wexler"
    },
    {
      "date": "2008-07-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a4vl00/intro---7-14-08",
        "http://thecolbertreport.cc.com/videos/t1ic5h/belgians-buy-budweiser",
        "http://thecolbertreport.cc.com/videos/e8zxmm/the-word---priceless",
        "http://thecolbertreport.cc.com/videos/6fnysv/barack-obama-s-church-search---lama-surya-das",
        "http://thecolbertreport.cc.com/videos/iuafl5/daniel-c--esty",
        "http://thecolbertreport.cc.com/videos/zeelo6/one-last-sip"
      ],
      "guest": "Lama Surya Das, Daniel C. Esty"
    },
    {
      "date": "2008-07-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/btd58c/intro---7-15-08",
        "http://thecolbertreport.cc.com/videos/iojfbw/the-new-yorker-cover",
        "http://thecolbertreport.cc.com/videos/4r3fs4/julia-e--sweig",
        "http://thecolbertreport.cc.com/videos/slbivd/difference-makers---donald-trump",
        "http://thecolbertreport.cc.com/videos/w3v1ei/jason-riley"
      ],
      "guest": "Julia E. Sweig, Jason Riley"
    },
    {
      "date": "2008-07-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/apzepe/intro---7-16-08",
        "http://thecolbertreport.cc.com/videos/nxgrjc/rush-is-here",
        "http://thecolbertreport.cc.com/videos/u9v0kj/the-word---placebo",
        "http://thecolbertreport.cc.com/videos/r6ylvr/alpha-dog-of-the-week---george-w--bush"
      ],
      "guest": "Rush"
    },
    {
      "date": "2008-07-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fv156w/intro---7-17-08",
        "http://thecolbertreport.cc.com/videos/hy6e1y/ofec",
        "http://thecolbertreport.cc.com/videos/fdazma/tip-wag---9-11-billboard",
        "http://thecolbertreport.cc.com/videos/75y9kg/green-screen-challenge---bill-o-reilly-rant",
        "http://thecolbertreport.cc.com/videos/ti6y23/elizabeth-edwards",
        "http://thecolbertreport.cc.com/videos/2i4pii/esquire-cover"
      ],
      "guest": "Elizabeth Edwards"
    },
    {
      "date": "2008-07-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ypasrv/exclusive---better-know-a-lobby---sierra-club",
        "http://thecolbertreport.cc.com/videos/298hev/intro---7-21-08",
        "http://thecolbertreport.cc.com/videos/2uxo91/barack-obama-s-elitist-summer-abroad",
        "http://thecolbertreport.cc.com/videos/ytt7lh/better-know-a-lobby---sierra-club",
        "http://thecolbertreport.cc.com/videos/7zt9o1/jim-webb"
      ],
      "guest": "Sen. Jim Webb"
    },
    {
      "date": "2008-07-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/isgn6o/intro---7-22-08",
        "http://thecolbertreport.cc.com/videos/5us80y/obama-s-trip",
        "http://thecolbertreport.cc.com/videos/twxrmk/the-word---fight-to-the-furnish",
        "http://thecolbertreport.cc.com/videos/g536lz/elton-john-s-new-ice-cream",
        "http://thecolbertreport.cc.com/videos/dqvjy7/south-carolina-is-so-gay",
        "http://thecolbertreport.cc.com/videos/ypbiy1/margaret-spellings"
      ],
      "guest": "Margaret Spellings"
    },
    {
      "date": "2008-07-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ephzov/intro---7-23-08",
        "http://thecolbertreport.cc.com/videos/008wql/starbucks-closings",
        "http://thecolbertreport.cc.com/videos/ckerul/the-word---join-the-european-union",
        "http://thecolbertreport.cc.com/videos/p099m0/colorofchange-org-petition",
        "http://thecolbertreport.cc.com/videos/ef4747/nas-pt--1"
      ],
      "guest": "Nas"
    },
    {
      "date": "2008-07-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9e4ipx/intro---7-24-08",
        "http://thecolbertreport.cc.com/videos/mzk1jw/john-mccain-s-sausage-party",
        "http://thecolbertreport.cc.com/videos/y6db2n/laurie-goodstein",
        "http://thecolbertreport.cc.com/videos/oyh9ck/threatdown---greek-courts",
        "http://thecolbertreport.cc.com/videos/qkxsxv/garrett-reisman",
        "http://thecolbertreport.cc.com/videos/my4p2n/decoder-rings"
      ],
      "guest": "Laurie Goodstein, Garrett Reisman"
    },
    {
      "date": "2008-07-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5mv6ij/intro---7-28-08",
        "http://thecolbertreport.cc.com/videos/ahi7x5/obama-returns",
        "http://thecolbertreport.cc.com/videos/n5o1z2/heroic-refusal-to-discuss-robert-novak",
        "http://thecolbertreport.cc.com/videos/wksh33/trigger-happy---d-c--v--heller",
        "http://thecolbertreport.cc.com/videos/2fxv2r/toby-keith"
      ],
      "guest": "Toby Keith"
    },
    {
      "date": "2008-07-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8y4ush/intro---7-29-08",
        "http://thecolbertreport.cc.com/videos/ft9iza/mccain-s-mustache",
        "http://thecolbertreport.cc.com/videos/je97nz/the-word---honest-belief",
        "http://thecolbertreport.cc.com/videos/079fu3/better-know-a-district---new-york-s-14th---carolyn-maloney",
        "http://thecolbertreport.cc.com/videos/4pok23/eric-roston"
      ],
      "guest": "Eric Roston"
    },
    {
      "date": "2008-07-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/aej937/intro---7-30-08",
        "http://thecolbertreport.cc.com/videos/0igq3j/fat-cat",
        "http://thecolbertreport.cc.com/videos/z8lld1/the-word---save-ferris",
        "http://thecolbertreport.cc.com/videos/77hd54/spiders-for-stephen-",
        "http://thecolbertreport.cc.com/videos/9riu8g/canton-apology",
        "http://thecolbertreport.cc.com/videos/paplnu/crosby--stills---nash-pt--1"
      ],
      "guest": "Crosby, Stills &amp; Nash"
    },
    {
      "date": "2008-07-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2yeaq8/intro---7-31-08",
        "http://thecolbertreport.cc.com/videos/cy7kpu/starbucks-cuts-jobs",
        "http://thecolbertreport.cc.com/videos/evgv9c/brendan-koerner",
        "http://thecolbertreport.cc.com/videos/3pi9ch/cheating-death---swimming-safety",
        "http://thecolbertreport.cc.com/videos/k8sku2/buzz-aldrin",
        "http://thecolbertreport.cc.com/videos/xrkpup/thanks-to-the-guests"
      ],
      "guest": "Brendan I. Koerner, Buzz Aldrin"
    },
    {
      "date": "2008-08-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y56p3h/intro---8-4-08",
        "http://thecolbertreport.cc.com/videos/j7c1ly/democrats--five-week-recess",
        "http://thecolbertreport.cc.com/videos/n4qhgk/the-word---we-the-people",
        "http://thecolbertreport.cc.com/videos/gjy6co/ryan-seacrest-s-shark-attack",
        "http://thecolbertreport.cc.com/videos/j0iwzv/lucas-conley"
      ],
      "guest": "Lucas Conley, The Apples in Stereo"
    },
    {
      "date": "2008-08-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0b9ndt/intro---8-5-08",
        "http://thecolbertreport.cc.com/videos/a60qui/starbucks-promotion",
        "http://thecolbertreport.cc.com/videos/ts3set/obama-s-energy-plan---tire-gauges",
        "http://thecolbertreport.cc.com/videos/c8orpt/the-word---divided-we-win",
        "http://thecolbertreport.cc.com/videos/u7dbu9/canton--kansas-apology",
        "http://thecolbertreport.cc.com/videos/sw0u58/david-carr",
        "http://thecolbertreport.cc.com/videos/zghj54/obsessive-compulsive-checklist"
      ],
      "guest": "David Carr"
    },
    {
      "date": "2008-08-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j12mau/intro---8-6-08",
        "http://thecolbertreport.cc.com/videos/ad4cbz/ignorance-history-month",
        "http://thecolbertreport.cc.com/videos/v2zmtk/spida-of-love---jason-bond",
        "http://thecolbertreport.cc.com/videos/luli3g/colbert-platinum---the-dribble-down-effect",
        "http://thecolbertreport.cc.com/videos/3pe5h3/kevin-costner",
        "http://thecolbertreport.cc.com/videos/ot8cw0/spanish-audio"
      ],
      "guest": "Jason Bond, Kevin Costner"
    },
    {
      "date": "2008-08-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bxoz3a/intro---8-7-08",
        "http://thecolbertreport.cc.com/videos/e6qhsv/osama-bin-laden-s-driver-guilty",
        "http://thecolbertreport.cc.com/videos/f3opxi/sport-report---devin-gordon",
        "http://thecolbertreport.cc.com/videos/6u4m61/tip-wag---exxon-s-record-profits",
        "http://thecolbertreport.cc.com/videos/dmymte/thomas-frank",
        "http://thecolbertreport.cc.com/videos/iwrdpe/reading-newsweek"
      ],
      "guest": "Devin Gordon, Thomas Frank"
    },
    {
      "date": "2008-08-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jk0e27/intro---8-11-08",
        "http://thecolbertreport.cc.com/videos/riwpa4/esteban-loves-jorge-ramos",
        "http://thecolbertreport.cc.com/videos/bfwvvn/the-word---catharsis",
        "http://thecolbertreport.cc.com/videos/txv0gu/nailed--em---medical-marijuana",
        "http://thecolbertreport.cc.com/videos/8j40t0/jorge-ramos",
        "http://thecolbertreport.cc.com/videos/b7houz/stephen-wants-snacks"
      ],
      "guest": "Jorge Ramos"
    },
    {
      "date": "2008-08-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kt49i5/intro---8-12-08",
        "http://thecolbertreport.cc.com/videos/zgupdj/unsubstantiated-rumors",
        "http://thecolbertreport.cc.com/videos/6d57uu/olympic-opening-ceremony",
        "http://thecolbertreport.cc.com/videos/5njkui/joey-cheek",
        "http://thecolbertreport.cc.com/videos/jhg2wn/canton--south-dakota-apology",
        "http://thecolbertreport.cc.com/videos/bv3152/jane-mayer",
        "http://thecolbertreport.cc.com/videos/dwnfyl/reading-the-national-enquirer"
      ],
      "guest": "Joey Cheek, Jane Mayer"
    },
    {
      "date": "2008-08-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/o7nbb7/intro---8-13-08",
        "http://thecolbertreport.cc.com/videos/zewvls/stephen-s-world-record",
        "http://thecolbertreport.cc.com/videos/3ae93q/john-mccain-steals-from-wikipedia",
        "http://thecolbertreport.cc.com/videos/htzkd9/the-word---blame-monica-goodling",
        "http://thecolbertreport.cc.com/videos/1clyqz/formidable-opponent---offshore-drilling",
        "http://thecolbertreport.cc.com/videos/yplzsy/dick-meyer",
        "http://thecolbertreport.cc.com/videos/x9tyb8/goodbye-from-wprg"
      ],
      "guest": "Dick Meyer"
    },
    {
      "date": "2008-08-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/481cqy/intro---8-14-08",
        "http://thecolbertreport.cc.com/videos/0gs1a9/jeopardy-shout-out",
        "http://thecolbertreport.cc.com/videos/s99fxp/threatdown---killer-iphones",
        "http://thecolbertreport.cc.com/videos/9x55ta/the-1952-helsinki-games---the-reindeer-roars",
        "http://thecolbertreport.cc.com/videos/ebnqyp/bing-west",
        "http://thecolbertreport.cc.com/videos/h0yxjt/gold-medals"
      ],
      "guest": "Bing West"
    },
    {
      "date": "2008-08-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r6ivli/intro---8-26-08",
        "http://thecolbertreport.cc.com/videos/zpxtn2/burning-man-festival-confusion",
        "http://thecolbertreport.cc.com/videos/ez5jp1/michelle-obama-s-speech",
        "http://thecolbertreport.cc.com/videos/tojy8p/anniversary-pandering",
        "http://thecolbertreport.cc.com/videos/ax1v4e/bob-barr",
        "http://thecolbertreport.cc.com/videos/f120f5/scott-mcclellan",
        "http://thecolbertreport.cc.com/videos/twqqkj/up-next"
      ],
      "guest": "Rep. Bob Barr, Scott McClellan"
    },
    {
      "date": "2008-08-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mb4pgm/intro---8-27-08",
        "http://thecolbertreport.cc.com/videos/63yvi3/live-from-dynasty",
        "http://thecolbertreport.cc.com/videos/xfzios/hillary-clinton-supports-barack-obama",
        "http://thecolbertreport.cc.com/videos/m1mag5/repo-man",
        "http://thecolbertreport.cc.com/videos/402muh/mike-huckabee",
        "http://thecolbertreport.cc.com/videos/llvqjv/stephanie-tubbs-jones-tribute"
      ],
      "guest": "Gov. Mike Huckabee"
    },
    {
      "date": "2008-08-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ua1ppo/intro---8-28-08",
        "http://thecolbertreport.cc.com/videos/9lke5e/high-altitude-brownies",
        "http://thecolbertreport.cc.com/videos/53s26i/the-word---acid-flashback",
        "http://thecolbertreport.cc.com/videos/kmna3f/dnc-formal-roll-call",
        "http://thecolbertreport.cc.com/videos/eifqog/richard-brookhiser",
        "http://thecolbertreport.cc.com/videos/c42fhd/stephen-s-brownies"
      ],
      "guest": "Rick Brookhiser"
    },
    {
      "date": "2008-08-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7p5vgn/intro---8-29-08",
        "http://thecolbertreport.cc.com/videos/ctsiz5/sarah-palin-for-vp",
        "http://thecolbertreport.cc.com/videos/9os3w0/better-know-a-lobby---secular-coalition-for-america",
        "http://thecolbertreport.cc.com/videos/rufbl6/john-mcwhorter",
        "http://thecolbertreport.cc.com/videos/bzvjxb/revenge-of-the-styrofoam-cups"
      ],
      "guest": "John McWhorter"
    },
    {
      "date": "2008-09-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hp450x/intro---9-2-08",
        "http://thecolbertreport.cc.com/videos/8tw46w/stephen-from-four-years-ago",
        "http://thecolbertreport.cc.com/videos/rf8uos/the-word---that-s-the-ticket",
        "http://thecolbertreport.cc.com/videos/gmnlx9/green-screen-challenge---last-shot",
        "http://thecolbertreport.cc.com/videos/f81p33/laura-d-andrea-tyson",
        "http://thecolbertreport.cc.com/videos/xhysj6/blowing-your-mind"
      ],
      "guest": "Laura D'Andrea Tyson"
    },
    {
      "date": "2008-09-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gujtwh/intro---9-3-08",
        "http://thecolbertreport.cc.com/videos/kepht9/stephen-is-in-new-orleans",
        "http://thecolbertreport.cc.com/videos/sbatmc/rnc-tuesday",
        "http://thecolbertreport.cc.com/videos/awnw4i/susan-eisenhower-endorses-obama",
        "http://thecolbertreport.cc.com/videos/4cdiam/john-mccain--her-story",
        "http://thecolbertreport.cc.com/videos/x8u7qp/doris-kearns-goodwin",
        "http://thecolbertreport.cc.com/videos/rk1eeg/who-wants-beads-"
      ],
      "guest": "Doris Kearns Goodwin"
    },
    {
      "date": "2008-09-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nvj1zq/intro---9-4-08",
        "http://thecolbertreport.cc.com/videos/1cwp12/stuck-in-atlanta-airport",
        "http://thecolbertreport.cc.com/videos/kyo8u3/adam-brickley",
        "http://thecolbertreport.cc.com/videos/c6ux4z/tip-wag---rnc-edition",
        "http://thecolbertreport.cc.com/videos/yywrwl/ron-paul",
        "http://thecolbertreport.cc.com/videos/kwoupb/flight-out-of-atlanta"
      ],
      "guest": "Adam Brickley, Ron Paul"
    },
    {
      "date": "2008-09-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pg1oxm/intro---9-5-08",
        "http://thecolbertreport.cc.com/videos/2rjlbj/stephen-missed-the-convention",
        "http://thecolbertreport.cc.com/videos/njb4bu/green-screen-challenge---john-mccain-s-acceptance-speech",
        "http://thecolbertreport.cc.com/videos/zk7gig/better-know-a-district---georgia-s-8th---lynn-westmoreland-update",
        "http://thecolbertreport.cc.com/videos/xeizbt/david-paterson",
        "http://thecolbertreport.cc.com/videos/u3k61y/green-screen-challenge---go-nuts"
      ],
      "guest": "Gov. David Paterson"
    },
    {
      "date": "2008-09-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jshk87/exclusive---charlene--i-m-right-behind-you----rock-band-2",
        "http://thecolbertreport.cc.com/videos/jfwpwo/intro---9-15-08",
        "http://thecolbertreport.cc.com/videos/7yzozt/colbert-shopping-network",
        "http://thecolbertreport.cc.com/videos/f9h01l/the-word---how-dare-you-",
        "http://thecolbertreport.cc.com/videos/r0u91k/colbert-platinum---supermodel-statue",
        "http://thecolbertreport.cc.com/videos/ihx562/peter-j--gomes",
        "http://thecolbertreport.cc.com/videos/4ebszq/another-episode"
      ],
      "guest": "Rev. Peter J. Gomes"
    },
    {
      "date": "2008-09-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/urn1ti/intro---9-16-08",
        "http://thecolbertreport.cc.com/videos/k0bsca/financial-advice-from-gorlock",
        "http://thecolbertreport.cc.com/videos/mkpl4k/tyson-slocum",
        "http://thecolbertreport.cc.com/videos/75xh2f/threatdown---icebergs-",
        "http://thecolbertreport.cc.com/videos/3tm40j/rick-reilly",
        "http://thecolbertreport.cc.com/videos/vnf5o3/thirty-minutes"
      ],
      "guest": "Tyson Slocum, Rick Reilly"
    },
    {
      "date": "2008-09-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4l5nqm/intro---9-17-08",
        "http://thecolbertreport.cc.com/videos/y012iz/mccain-attacks-obama",
        "http://thecolbertreport.cc.com/videos/kyb0cu/the-word---powerless",
        "http://thecolbertreport.cc.com/videos/n6eo9j/country-first",
        "http://thecolbertreport.cc.com/videos/uwjjvf/bob-lutz",
        "http://thecolbertreport.cc.com/videos/3odd8c/stephen---the-colberts--music-video"
      ],
      "guest": "Bob Lutz"
    },
    {
      "date": "2008-09-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/crbm2j/intro---9-18-08",
        "http://thecolbertreport.cc.com/videos/1jklj8/stephen-wants-an-emmy",
        "http://thecolbertreport.cc.com/videos/j1rb59/smokin--pole---american-arctic-expert",
        "http://thecolbertreport.cc.com/videos/jgr23t/richard-garriott-takes-stephen-to-space",
        "http://thecolbertreport.cc.com/videos/r2z9cm/maria-bartiromo",
        "http://thecolbertreport.cc.com/videos/f0iah5/off-to-the-emmys"
      ],
      "guest": "Maria Bartiromo"
    },
    {
      "date": "2008-09-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s3o9jz/intro---9-23-08",
        "http://thecolbertreport.cc.com/videos/ikji5j/stephen-loses-to-don-rickles",
        "http://thecolbertreport.cc.com/videos/vj8wko/the-word---ohmygodsocietyiscollapsing---",
        "http://thecolbertreport.cc.com/videos/bna75w/peter-grosz-insults",
        "http://thecolbertreport.cc.com/videos/iscpss/john-mccain-s-theme-song",
        "http://thecolbertreport.cc.com/videos/8uwmb0/jackson-browne"
      ],
      "guest": "Jackson Browne"
    },
    {
      "date": "2008-09-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5k16zp/intro---9-24-08",
        "http://thecolbertreport.cc.com/videos/zxun4o/stephen-suspends-the-show",
        "http://thecolbertreport.cc.com/videos/y03i0s/joe-nocera",
        "http://thecolbertreport.cc.com/videos/ug1eaa/alpha-dog-of-the-week---bill-bennett",
        "http://thecolbertreport.cc.com/videos/m77ip1/cornel-west",
        "http://thecolbertreport.cc.com/videos/5lq5u2/colbertnation-com"
      ],
      "guest": "Joe Nocera, Cornel West"
    },
    {
      "date": "2008-09-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c2lklm/intro---9-25-08",
        "http://thecolbertreport.cc.com/videos/n6lmpg/stephen-settles-the-debate---fdr-vs--tr",
        "http://thecolbertreport.cc.com/videos/k6o1ga/now-s-presidential-endorsement---kim-gandy",
        "http://thecolbertreport.cc.com/videos/bqde8h/nicholas-carr",
        "http://thecolbertreport.cc.com/videos/c44c8h/one-more-thing"
      ],
      "guest": "Nicholas Carr"
    },
    {
      "date": "2008-09-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1c54hn/intro---9-29-08",
        "http://thecolbertreport.cc.com/videos/05f4cg/the-first-debate-winner",
        "http://thecolbertreport.cc.com/videos/bweuwc/the-word---ye-of-little-faith",
        "http://thecolbertreport.cc.com/videos/cgij7r/cheating-death---car-bacteria",
        "http://thecolbertreport.cc.com/videos/vp621m/paul-begala",
        "http://thecolbertreport.cc.com/videos/gpa8yw/good-night"
      ],
      "guest": "Paul Begala"
    },
    {
      "date": "2008-09-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y8hkhe/intro---9-30-08",
        "http://thecolbertreport.cc.com/videos/9st6mt/partisanship-kills-the-bailout",
        "http://thecolbertreport.cc.com/videos/f9oh9q/prescott-oil-loves-the-earth",
        "http://thecolbertreport.cc.com/videos/d0zdru/tip-wag---wall-street-jagoffs",
        "http://thecolbertreport.cc.com/videos/j67wur/out-of-time"
      ],
      "guest": "James Taylor"
    },
    {
      "date": "2008-10-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t7tnvd/exclusive---nas-plays-rock-band",
        "http://thecolbertreport.cc.com/videos/y8hkhe/intro---9-30-08",
        "http://thecolbertreport.cc.com/videos/9st6mt/partisanship-kills-the-bailout",
        "http://thecolbertreport.cc.com/videos/f9oh9q/prescott-oil-loves-the-earth",
        "http://thecolbertreport.cc.com/videos/d0zdru/tip-wag---wall-street-jagoffs",
        "http://thecolbertreport.cc.com/videos/j67wur/out-of-time"
      ],
      "guest": "Dave Levin"
    },
    {
      "date": "2008-10-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eqbu4l/intro---10-01-08",
        "http://thecolbertreport.cc.com/videos/ovyu4c/campbell-s-soup-stock",
        "http://thecolbertreport.cc.com/videos/bhfa94/the-word---future-perfect",
        "http://thecolbertreport.cc.com/videos/86s1x0/colbert-teen-talk---voter-abstinence",
        "http://thecolbertreport.cc.com/videos/1v6olb/dave-levin",
        "http://thecolbertreport.cc.com/videos/e5ngk1/you-snooze--you-lose"
      ],
      "guest": "Dave Levin"
    },
    {
      "date": "2008-10-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zc7pti/intro---10-02-08",
        "http://thecolbertreport.cc.com/videos/jwi5c6/stephen-shoots-an-audience-member",
        "http://thecolbertreport.cc.com/videos/nkfn9g/shakespearean-candidates---stephen-greenblatt",
        "http://thecolbertreport.cc.com/videos/9cm5sl/formidable-opponent---business-syphilis",
        "http://thecolbertreport.cc.com/videos/kvfh5w/naomi-klein",
        "http://thecolbertreport.cc.com/videos/xsttzx/that-s-all-she-wrote"
      ],
      "guest": "Stephen Greenblatt, Naomi Klein"
    },
    {
      "date": "2008-10-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xxiviw/intro---10-6-08",
        "http://thecolbertreport.cc.com/videos/1hb3kb/oj-simpson-guilty",
        "http://thecolbertreport.cc.com/videos/qlbk95/the-word---maverick-without-a-cause",
        "http://thecolbertreport.cc.com/videos/qnwvgs/un-american-news---financial-edition",
        "http://thecolbertreport.cc.com/videos/tn9q1r/jim-cramer",
        "http://thecolbertreport.cc.com/videos/gpjjik/life-drawing-lesson"
      ],
      "guest": "Jim Cramer"
    },
    {
      "date": "2008-10-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lr7n1e/intro---10-7-08",
        "http://thecolbertreport.cc.com/videos/ehcjcu/stephen-s-town-hall",
        "http://thecolbertreport.cc.com/videos/yulr8u/threatdown---zombies",
        "http://thecolbertreport.cc.com/videos/e56sfz/the-red-lending-menace",
        "http://thecolbertreport.cc.com/videos/xoy3ny/nate-silver",
        "http://thecolbertreport.cc.com/videos/0t800l/phone-book"
      ],
      "guest": "Nate Silver"
    },
    {
      "date": "2008-10-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wnllod/intro---10-08-08",
        "http://thecolbertreport.cc.com/videos/rb63v8/town-hall-fashion-apology",
        "http://thecolbertreport.cc.com/videos/pmvhoi/the-second-presidential-debate",
        "http://thecolbertreport.cc.com/videos/r8hb9t/atone-phone---gilbert-gottfried",
        "http://thecolbertreport.cc.com/videos/7943ea/joe-scarborough",
        "http://thecolbertreport.cc.com/videos/02dsh7/stephen-s-post-show-routine"
      ],
      "guest": "Joe Scarborough"
    },
    {
      "date": "2008-10-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cbxmlr/intro---10-09-08",
        "http://thecolbertreport.cc.com/videos/l3uq93/dismayed-stockbroker-photos",
        "http://thecolbertreport.cc.com/videos/pqsng6/campaign-personal-attacks---david-gergen",
        "http://thecolbertreport.cc.com/videos/f6283x/who-s-not-honoring-me-now----nepal",
        "http://thecolbertreport.cc.com/videos/ge3feb/oliver-stone",
        "http://thecolbertreport.cc.com/videos/w87c40/bad-news"
      ],
      "guest": "David Gergen, Oliver Stone"
    },
    {
      "date": "2008-10-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5c0f2m/intro---10-13-08",
        "http://thecolbertreport.cc.com/videos/fnytnd/mccain-crossword-clue",
        "http://thecolbertreport.cc.com/videos/1jl5yn/the-computer-menace---bethany-mclean",
        "http://thecolbertreport.cc.com/videos/1goeih/bears---balls---salt-based-economy",
        "http://thecolbertreport.cc.com/videos/gyyaxy/kathleen-parker",
        "http://thecolbertreport.cc.com/videos/6y4q65/happy-birthday"
      ],
      "guest": "Bethany McLean, Kathleen Parker"
    },
    {
      "date": "2008-10-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n5hrc3/intro---10-14-08",
        "http://thecolbertreport.cc.com/videos/7pd7zc/paul-krugman-s-nobel-prize",
        "http://thecolbertreport.cc.com/videos/r0q5ve/the-word---p-o-w-",
        "http://thecolbertreport.cc.com/videos/pfbd0x/tip-wag---palin-s-newsweek-cover",
        "http://thecolbertreport.cc.com/videos/usq8wp/joseph-stiglitz",
        "http://thecolbertreport.cc.com/videos/lvn4rk/good-night"
      ],
      "guest": "Joseph Stiglitz"
    },
    {
      "date": "2008-10-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zwbmit/intro---10-15-08",
        "http://thecolbertreport.cc.com/videos/9308mk/kfc-snacker",
        "http://thecolbertreport.cc.com/videos/l7yb6p/the-word---freaky-three-way-calling",
        "http://thecolbertreport.cc.com/videos/4e7lhp/sport-report---lame-sports-edition",
        "http://thecolbertreport.cc.com/videos/38m5c1/tina-brown",
        "http://thecolbertreport.cc.com/videos/8g4g6k/chest-tivo"
      ],
      "guest": "Tina Brown"
    },
    {
      "date": "2008-10-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wiiett/intro---10-16-08",
        "http://thecolbertreport.cc.com/videos/clx1g3/the-final-debate",
        "http://thecolbertreport.cc.com/videos/irar1b/portrait-accepted---brent-glass",
        "http://thecolbertreport.cc.com/videos/vhpq80/robert-greenwald",
        "http://thecolbertreport.cc.com/videos/dtl1jb/a-new-portrait"
      ],
      "guest": "Brent Glass, Robert Greenwald"
    },
    {
      "date": "2008-10-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/icr62o/intro---10-20-08",
        "http://thecolbertreport.cc.com/videos/hztig3/colin-powell-endorses-barack-obama",
        "http://thecolbertreport.cc.com/videos/m2bwgq/fareed-zakaria",
        "http://thecolbertreport.cc.com/videos/f1sjmz/colbert-aluminum---paris",
        "http://thecolbertreport.cc.com/videos/ihme7b/wynton-marsalis",
        "http://thecolbertreport.cc.com/videos/1zx8mm/good-night"
      ],
      "guest": "Fareed Zakaria, Wynton Marsalis"
    },
    {
      "date": "2008-10-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ipzwmk/intro---10-21-08",
        "http://thecolbertreport.cc.com/videos/1q0lgd/stephen-jr--campaigns-for-mccain",
        "http://thecolbertreport.cc.com/videos/6mt8jf/the-word---fantasyland",
        "http://thecolbertreport.cc.com/videos/yf6nbq/battle-of-the-gods",
        "http://thecolbertreport.cc.com/videos/ajdj8y/atone-phone---the-pony-down",
        "http://thecolbertreport.cc.com/videos/2f3tuj/michael-farris",
        "http://thecolbertreport.cc.com/videos/gsnyc0/another-one-tomorrow"
      ],
      "guest": "Michael Farris"
    },
    {
      "date": "2008-10-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zfo3j9/intro---10-22-08",
        "http://thecolbertreport.cc.com/videos/bnfehb/mccain-loves-the-middle-class",
        "http://thecolbertreport.cc.com/videos/2fhvot/too-much-political-knowledge",
        "http://thecolbertreport.cc.com/videos/l9sa9k/movies-that-are-destroying-america---quantum-of-solace",
        "http://thecolbertreport.cc.com/videos/bfif72/david-frum",
        "http://thecolbertreport.cc.com/videos/zijniy/thanks-to-cedric-the-entertainer"
      ],
      "guest": "David Frum"
    },
    {
      "date": "2008-10-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4fsdf9/intro---10-23-08",
        "http://thecolbertreport.cc.com/videos/mxdemq/the-palins-in-people-magazine",
        "http://thecolbertreport.cc.com/videos/9r8mtw/threatdown---who-s-nailin--paylin",
        "http://thecolbertreport.cc.com/videos/d9d59e/difference-makers---the-national-hummer-club",
        "http://thecolbertreport.cc.com/videos/vu40sp/jonathan-alter",
        "http://thecolbertreport.cc.com/videos/4q4n65/a-short-goodbye"
      ],
      "guest": "Jonathan Alter"
    },
    {
      "date": "2008-10-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/59kvnn/intro---10-27-08",
        "http://thecolbertreport.cc.com/videos/o5x5iu/mccain-guarantees-victory",
        "http://thecolbertreport.cc.com/videos/05r6nq/the-word---it-s-alive-",
        "http://thecolbertreport.cc.com/videos/7g8kx1/alpha-dog-of-the-week---mark-ciptak",
        "http://thecolbertreport.cc.com/videos/fnuvdv/yo-yo-ma"
      ],
      "guest": "Yo-Yo Ma"
    },
    {
      "date": "2008-10-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ghj64m/intro---10-28-08",
        "http://thecolbertreport.cc.com/videos/xk09yu/ted-stevens-is-found-guilty",
        "http://thecolbertreport.cc.com/videos/7j217q/obama-the-socialist",
        "http://thecolbertreport.cc.com/videos/bxzmkn/socialist-candidate-for-president---brian-moore",
        "http://thecolbertreport.cc.com/videos/wz2u1e/canton--ohio",
        "http://thecolbertreport.cc.com/videos/ytg04i/sherman-alexie",
        "http://thecolbertreport.cc.com/videos/jz4m1g/tickets-to-canada"
      ],
      "guest": "Brian Moore, Sherman Alexie"
    },
    {
      "date": "2008-10-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ix1wn7/intro---10-29-08",
        "http://thecolbertreport.cc.com/videos/ks5pt8/john-mccain-s-big-prank",
        "http://thecolbertreport.cc.com/videos/7qwbk4/the-word---i-endorse-barack-obama",
        "http://thecolbertreport.cc.com/videos/k5qv33/was-it-really-that-bad----the-great-depression",
        "http://thecolbertreport.cc.com/videos/cxwcsb/david-simon",
        "http://thecolbertreport.cc.com/videos/prhqai/colbert-completists"
      ],
      "guest": "David Simon"
    },
    {
      "date": "2008-10-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9sqk1r/intro---10-30-08",
        "http://thecolbertreport.cc.com/videos/b7m8ic/obama-infomercial",
        "http://thecolbertreport.cc.com/videos/7mbhhk/tip-wag---apple-computers",
        "http://thecolbertreport.cc.com/videos/tiopht/the-dacolbert-code---the-election",
        "http://thecolbertreport.cc.com/videos/ugfx1s/wilco-interview"
      ],
      "guest": "Wilco"
    },
    {
      "date": "2008-11-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gc439u/intro---11-03-08",
        "http://thecolbertreport.cc.com/videos/jtvn9v/2008-campaign-winners-and-losers",
        "http://thecolbertreport.cc.com/videos/q31c3b/charlie-cook",
        "http://thecolbertreport.cc.com/videos/syw57q/how-to-be-a-maverick",
        "http://thecolbertreport.cc.com/videos/3lix4b/andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/5snsio/election-eve-prayer"
      ],
      "guest": "Charlie Cook, Andrew Sullivan"
    },
    {
      "date": "2008-11-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/deihkn/intro---11-05-08",
        "http://thecolbertreport.cc.com/videos/ek3v6r/president-obama",
        "http://thecolbertreport.cc.com/videos/p698of/the-word---change",
        "http://thecolbertreport.cc.com/videos/b3gurg/threatdown---black-presidents",
        "http://thecolbertreport.cc.com/videos/1bpyxl/andrew-young",
        "http://thecolbertreport.cc.com/videos/wmwkia/note-to-gorlock"
      ],
      "guest": "Ambassador Andrew Young"
    },
    {
      "date": "2008-11-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jvmllx/intro---11-06-08",
        "http://thecolbertreport.cc.com/videos/8cjwkf/obama-s-spider-battle",
        "http://thecolbertreport.cc.com/videos/91wunt/un-american-news---obama-edition",
        "http://thecolbertreport.cc.com/videos/aedolr/fallback-position---peter-earnest-pt--1",
        "http://thecolbertreport.cc.com/videos/tp44lf/rachel-maddow"
      ],
      "guest": "Rachel Maddow"
    },
    {
      "date": "2008-11-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3vbqce/intro---11-11-08",
        "http://thecolbertreport.cc.com/videos/t0o0ln/the-obamas-meet-the-bushes",
        "http://thecolbertreport.cc.com/videos/cf9i7o/proposition-8-protests---dan-savage",
        "http://thecolbertreport.cc.com/videos/a4htau/fallback-position---peter-earnest-pt--2",
        "http://thecolbertreport.cc.com/videos/97cxi9/kevin-johnson",
        "http://thecolbertreport.cc.com/videos/knwq1k/gay-black-violence"
      ],
      "guest": "Dan Savage, Kevin Johnson"
    },
    {
      "date": "2008-11-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jxnavl/intro---11-12-08",
        "http://thecolbertreport.cc.com/videos/hs06sa/formula-4ou1",
        "http://thecolbertreport.cc.com/videos/jdc5wl/the-word---pity-party",
        "http://thecolbertreport.cc.com/videos/vq5z69/cheating-death---women-s-health",
        "http://thecolbertreport.cc.com/videos/h8pdku/bob-woodward",
        "http://thecolbertreport.cc.com/videos/yj3fvl/good-night"
      ],
      "guest": "Bob Woodward"
    },
    {
      "date": "2008-11-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iy78xf/intro---11-13-08",
        "http://thecolbertreport.cc.com/videos/ws4itq/imaginary-gay-black-warfare",
        "http://thecolbertreport.cc.com/videos/54gy81/tip-wag---marvel-comics",
        "http://thecolbertreport.cc.com/videos/9so57k/rahm-emanuel-s-finger",
        "http://thecolbertreport.cc.com/videos/84locu/stephen-moore",
        "http://thecolbertreport.cc.com/videos/kwiam8/obama-spider-man-comic-bribe"
      ],
      "guest": "Stephen Moore"
    },
    {
      "date": "2008-11-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/edyiaw/intro---11-17-08",
        "http://thecolbertreport.cc.com/videos/vfh1d7/stephen-s-gma-appearance",
        "http://thecolbertreport.cc.com/videos/tyr5yf/barack-obama-is-hiring",
        "http://thecolbertreport.cc.com/videos/xubttj/obama-s-cabinet---tom-brokaw",
        "http://thecolbertreport.cc.com/videos/okezd5/soup-war",
        "http://thecolbertreport.cc.com/videos/lu8hmu/malcolm-gladwell",
        "http://thecolbertreport.cc.com/videos/f67l6s/stephen-drinks-soup"
      ],
      "guest": "Tom Brokaw, Malcolm Gladwell"
    },
    {
      "date": "2008-11-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cpar3w/intro---11-18-08",
        "http://thecolbertreport.cc.com/videos/gpyfhe/joe-lieberman-learns-his-fate",
        "http://thecolbertreport.cc.com/videos/tda4m3/the-word---love-lost",
        "http://thecolbertreport.cc.com/videos/rfqomg/stephen-s-vetting-process---cliff-sloan-pt--1"
      ],
      "guest": "Paul Simon"
    },
    {
      "date": "2008-11-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a4gbi9/intro---11-19-08",
        "http://thecolbertreport.cc.com/videos/3ebcnc/the-word---mad-men",
        "http://thecolbertreport.cc.com/videos/hjm6c3/stephen-s-vetting-process---cliff-sloan-pt--2",
        "http://thecolbertreport.cc.com/videos/p1vjk5/michael-lewis",
        "http://thecolbertreport.cc.com/videos/5n2dbq/tearful-apology"
      ],
      "guest": "Michael Lewis"
    },
    {
      "date": "2008-11-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cbvik4/intro---11-20-08",
        "http://thecolbertreport.cc.com/videos/ag7dg1/racism-is-over---cory-booker",
        "http://thecolbertreport.cc.com/videos/2frm4q/metunes---chinese-democracy",
        "http://thecolbertreport.cc.com/videos/c48nk9/thomas-friedman",
        "http://thecolbertreport.cc.com/videos/bd8wju/christmas-special-dvd-warning"
      ],
      "guest": "Cory Booker, Thomas L. Friedman"
    },
    {
      "date": "2008-12-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rpma6e/intro---12-01-08",
        "http://thecolbertreport.cc.com/videos/tq2nxp/operation-humble-kanye",
        "http://thecolbertreport.cc.com/videos/qarmhd/war-in-afghanistan",
        "http://thecolbertreport.cc.com/videos/rven6i/khaled-hosseini",
        "http://thecolbertreport.cc.com/videos/36dgrv/tip-wag---all-wag-christmas-edition",
        "http://thecolbertreport.cc.com/videos/7058uf/roland-fryer",
        "http://thecolbertreport.cc.com/videos/n1in3i/good-night"
      ],
      "guest": "Khaled Hosseini, Roland Fryer"
    },
    {
      "date": "2008-12-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cj7hhg/intro---12-02-08",
        "http://thecolbertreport.cc.com/videos/qvwoip/operation-humble-kanye---buy-stephen-s-album",
        "http://thecolbertreport.cc.com/videos/ztjt9g/the-word---a-man-named-plaxico",
        "http://thecolbertreport.cc.com/videos/fic3d1/colbert-platinum---christmas-edition",
        "http://thecolbertreport.cc.com/videos/bshkcz/jeffrey-goldberg",
        "http://thecolbertreport.cc.com/videos/utntlq/buy-stephen-s-boots-on-ebay"
      ],
      "guest": "Jeffrey Goldberg"
    },
    {
      "date": "2008-12-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/il4wbl/intro---12-03-08",
        "http://thecolbertreport.cc.com/videos/owefww/nasa-spider-escapes",
        "http://thecolbertreport.cc.com/videos/z33t4w/the-word---barack-handed-compliment",
        "http://thecolbertreport.cc.com/videos/mcfi82/nailed--em---radical-knitting",
        "http://thecolbertreport.cc.com/videos/2karre/barbara-walters",
        "http://thecolbertreport.cc.com/videos/r6ufyo/the-end--not-the-beginning"
      ],
      "guest": "Barbara Walters"
    },
    {
      "date": "2008-12-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d118oe/intro---12-04-08",
        "http://thecolbertreport.cc.com/videos/2fjry6/operation-humble-kanye---stephen-beats-kanye",
        "http://thecolbertreport.cc.com/videos/2d2zn0/pakistani-threat---bob-graham",
        "http://thecolbertreport.cc.com/videos/d5jif7/movies-that-are-destroying-america---holiday-movie-edition",
        "http://thecolbertreport.cc.com/videos/n7jvhg/nicholas-wade",
        "http://thecolbertreport.cc.com/videos/sugr09/returning-monday"
      ],
      "guest": "Sen. Bob Graham, Nicholas Wade"
    },
    {
      "date": "2008-12-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7u2bhk/intro---12-08-08",
        "http://thecolbertreport.cc.com/videos/ao9vg7/bush-kisses-streisand",
        "http://thecolbertreport.cc.com/videos/gctknh/the-word---season-of-giving",
        "http://thecolbertreport.cc.com/videos/6153k5/barry---the-stump",
        "http://thecolbertreport.cc.com/videos/hpitea/geoffrey-canada",
        "http://thecolbertreport.cc.com/videos/0r2h5l/stephen-on-conan"
      ],
      "guest": "Geoffrey Canada"
    },
    {
      "date": "2008-12-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4g9cia/intro---12-09-08",
        "http://thecolbertreport.cc.com/videos/onbk9a/rod-blagojevich-is-arrested",
        "http://thecolbertreport.cc.com/videos/600m6s/nixmas-tree-trimming---kevin-bacon",
        "http://thecolbertreport.cc.com/videos/yflimf/tek-jansen---beginning-s-first-dawn--episode-two-revisited",
        "http://thecolbertreport.cc.com/videos/srrck8/charlie-kaufman",
        "http://thecolbertreport.cc.com/videos/zkndmq/nixon-angel"
      ],
      "guest": "Kevin Bacon, Charlie Kaufman"
    },
    {
      "date": "2008-12-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u8ghsg/intro---12-10-08",
        "http://thecolbertreport.cc.com/videos/f9io4y/rod-blagojevich-s-birthday",
        "http://thecolbertreport.cc.com/videos/imth2d/threatdown---happiness",
        "http://thecolbertreport.cc.com/videos/jnn2lb/on-notice---forgiveness",
        "http://thecolbertreport.cc.com/videos/i1wzcc/richard-haass",
        "http://thecolbertreport.cc.com/videos/uw87dl/good-night"
      ],
      "guest": "Richard Haass"
    },
    {
      "date": "2008-12-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y3mqae/intro---12-11-08",
        "http://thecolbertreport.cc.com/videos/djirpd/michael-phelps",
        "http://thecolbertreport.cc.com/videos/j11gba/stephen-eats-ghost-ribs",
        "http://thecolbertreport.cc.com/videos/zc9rq9/the-ghost-of-stage-manager-bobby",
        "http://thecolbertreport.cc.com/videos/1756ia/the-word---the-unbearable-lightness-of-supreme-being"
      ],
      "guest": "Michael Phelps"
    }
  ],
  "2009": [
    {
      "date": "2009-01-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9k2tbm/intro---1-05-09",
        "http://thecolbertreport.cc.com/videos/za98w3/colbert-and-colmes---roland-burris-appointment",
        "http://thecolbertreport.cc.com/videos/hq4p9o/tek-jansen---beginning-s-first-dawn--episode-three",
        "http://thecolbertreport.cc.com/videos/nrlhy0/john-king",
        "http://thecolbertreport.cc.com/videos/5hoaoz/colbert-and-colmes---colmes-gets-fired"
      ],
      "guest": "Riley Crane"
    },
    {
      "date": "2009-01-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sn2rhf/ponzi-schemes",
        "http://thecolbertreport.cc.com/videos/k6j6as/hiding-gold---david-leonhardt",
        "http://thecolbertreport.cc.com/videos/4zhwch/better-know-a-district---utah-s-3rd---jason-chaffetz",
        "http://thecolbertreport.cc.com/videos/g9ppzt/matt-miller",
        "http://thecolbertreport.cc.com/videos/yys5yk/thank-you--stephen"
      ],
      "guest": "Capt. Charles Moore"
    },
    {
      "date": "2009-01-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z8rm3b/intro---01-07-09",
        "http://thecolbertreport.cc.com/videos/92yx1q/che-stadium",
        "http://thecolbertreport.cc.com/videos/d1e1eu/dr--gupta-s-penis-pyramid",
        "http://thecolbertreport.cc.com/videos/nqulkz/the-word---statute-of-liberty",
        "http://thecolbertreport.cc.com/videos/amgd80/tip-wag---cocaine-honey",
        "http://thecolbertreport.cc.com/videos/yau33c/benicio-del-toro"
      ],
      "guest": "James Fowler"
    },
    {
      "date": "2009-01-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/88kvmz/intro---01-08-09",
        "http://thecolbertreport.cc.com/videos/wcgnr1/new-york-times-abandons-dignity",
        "http://thecolbertreport.cc.com/videos/926dzf/yahweh-or-no-way---roland-burris",
        "http://thecolbertreport.cc.com/videos/fk4a9c/leg-wrestling-rematch",
        "http://thecolbertreport.cc.com/videos/gteixg/a-really-good-book",
        "http://thecolbertreport.cc.com/videos/6428p8/pro-commie-epic"
      ],
      "guest": "Lawrence Lessig"
    },
    {
      "date": "2009-01-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kni4vi/intro---01-12-09",
        "http://thecolbertreport.cc.com/videos/9c4f03/bush-s-last-press-conference",
        "http://thecolbertreport.cc.com/videos/bwmns5/the-word---sweet-smell-of-success",
        "http://thecolbertreport.cc.com/videos/0o1xwh/stephen-jr--on-christmas-eve",
        "http://thecolbertreport.cc.com/videos/dkx1ya/anthony-romero",
        "http://thecolbertreport.cc.com/videos/by8gkb/a-lot-more-to-say"
      ],
      "guest": "Anthony Romero"
    },
    {
      "date": "2009-01-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/32ytiz/intro---01-13-09",
        "http://thecolbertreport.cc.com/videos/fmzudp/bush-presidency-aged-us",
        "http://thecolbertreport.cc.com/videos/9et79a/cold-war-update---cuba",
        "http://thecolbertreport.cc.com/videos/m3x3ok/on-notice---limey-squirrel-eaters",
        "http://thecolbertreport.cc.com/videos/k1og3a/niall-ferguson",
        "http://thecolbertreport.cc.com/videos/5px40o/that-s-all-the-time-we-have"
      ],
      "guest": "Niall Ferguson"
    },
    {
      "date": "2009-01-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oyml2f/intro---01-14-09",
        "http://thecolbertreport.cc.com/videos/34mj4v/the-last-bush-effigy",
        "http://thecolbertreport.cc.com/videos/y0f472/p-k--winsome---obama-collectibles",
        "http://thecolbertreport.cc.com/videos/ur3zl1/little-victories---america-s-galaxy-is-big",
        "http://thecolbertreport.cc.com/videos/gizrjk/alan-khazei",
        "http://thecolbertreport.cc.com/videos/9hlcm3/commemorative-plates"
      ],
      "guest": "Alan Khazei"
    },
    {
      "date": "2009-01-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q7vz1i/intro---01-15-09",
        "http://thecolbertreport.cc.com/videos/95lbi6/bush-and-the-press",
        "http://thecolbertreport.cc.com/videos/sy3mow/bush-s-romance-with-the-media---david-gregory",
        "http://thecolbertreport.cc.com/videos/7iuuwa/tip-wag---monkey-on-the-lam",
        "http://thecolbertreport.cc.com/videos/ux2atw/shepard-fairey",
        "http://thecolbertreport.cc.com/videos/wfge8o/spay-and-neuter-your-pets"
      ],
      "guest": "David Gregory, Shepard Fairey"
    },
    {
      "date": "2009-01-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r1uwlh/intro---01-19-09",
        "http://thecolbertreport.cc.com/videos/ul1a7j/mlk-day-mascot",
        "http://thecolbertreport.cc.com/videos/lypf68/the-word---sacrifice",
        "http://thecolbertreport.cc.com/videos/ydvpvb/frank-rich",
        "http://thecolbertreport.cc.com/videos/52s3oy/boiling-frog-metaphor"
      ],
      "guest": "Frank Rich"
    },
    {
      "date": "2009-01-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ymrs37/stephen-s-inauguration-breakdown",
        "http://thecolbertreport.cc.com/videos/301bds/p-k--winsome---inauguration-merchandise",
        "http://thecolbertreport.cc.com/videos/9hjhcy/stephen-s-sound-advice---how-to-be-like-lincoln",
        "http://thecolbertreport.cc.com/videos/mmoodw/jabari-asim",
        "http://thecolbertreport.cc.com/videos/kai9la/stephen-realizes-he-s-black"
      ],
      "guest": "Jabari Asim"
    },
    {
      "date": "2009-01-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dl8i2q/intro---01-21-09",
        "http://thecolbertreport.cc.com/videos/l2d6st/president-yo-yo-ma",
        "http://thecolbertreport.cc.com/videos/axsw46/election-2012---chuck-todd",
        "http://thecolbertreport.cc.com/videos/xkmfex/stephen-s-remix-challenge",
        "http://thecolbertreport.cc.com/videos/8l6srp/elizabeth-alexander",
        "http://thecolbertreport.cc.com/videos/a3p8mj/good-night"
      ],
      "guest": "Elizabeth Alexander"
    },
    {
      "date": "2009-01-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0zgr4t/intro---01-22-09",
        "http://thecolbertreport.cc.com/videos/t6meak/near-president-obama",
        "http://thecolbertreport.cc.com/videos/mtzrkq/un-american-news---president-obama-edition",
        "http://thecolbertreport.cc.com/videos/689o7m/better-know-a-lobby---naacp",
        "http://thecolbertreport.cc.com/videos/8awmoy/jon-meacham",
        "http://thecolbertreport.cc.com/videos/ili9if/refreshing-sierra-mist"
      ],
      "guest": "Jon Meacham"
    },
    {
      "date": "2009-01-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7nxt06/intro---01-26-09",
        "http://thecolbertreport.cc.com/videos/4oz085/stephen-s-secret-prison",
        "http://thecolbertreport.cc.com/videos/cw8n8j/obama-s-new-science-policy---chris-mooney",
        "http://thecolbertreport.cc.com/videos/yxtpn8/tip-wag---john-yarmuth-s-holiday-card",
        "http://thecolbertreport.cc.com/videos/uj76wp/ed-young",
        "http://thecolbertreport.cc.com/videos/49ccbt/1-877-sean-930"
      ],
      "guest": "Chris Mooney, Ed Young"
    },
    {
      "date": "2009-01-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rwx1ie/intro---01-27-09",
        "http://thecolbertreport.cc.com/videos/8ws8hw/al-arabiya-kidnaps-obama",
        "http://thecolbertreport.cc.com/videos/ei15xx/cheating-death---lung-health",
        "http://thecolbertreport.cc.com/videos/yzw1s5/bill-o-reilly-doesn-t-report-rumors",
        "http://thecolbertreport.cc.com/videos/7ljyqd/philippe-petit",
        "http://thecolbertreport.cc.com/videos/qx6mra/omar-returns"
      ],
      "guest": "Philippe Petit"
    },
    {
      "date": "2009-01-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mrairj/exclusive---better-know-a-beatle---paul-mccartney",
        "http://thecolbertreport.cc.com/videos/qfnuqn/intro---01-28-09",
        "http://thecolbertreport.cc.com/videos/4c854b/countdown-to-atomic-disaster---the-wing-ageddon",
        "http://thecolbertreport.cc.com/videos/m2fb3c/denis-dutton",
        "http://thecolbertreport.cc.com/videos/x3yxrz/call-1-877-sean-930"
      ],
      "guest": "Paul McCartney, Denis Dutton"
    },
    {
      "date": "2009-01-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s0jwx0/intro---01-29-09",
        "http://thecolbertreport.cc.com/videos/7k3noc/rod-blagojevich-is-impeached",
        "http://thecolbertreport.cc.com/videos/05hiht/the-word---the-audacity-of-nope",
        "http://thecolbertreport.cc.com/videos/ra6q6v/sport-report---chicken-wing-spokesman-richard-lobb",
        "http://thecolbertreport.cc.com/videos/n7s40p/john-podesta",
        "http://thecolbertreport.cc.com/videos/t92qhf/goodnight-illinois-gov--patrick-quinn"
      ],
      "guest": "John Podesta"
    },
    {
      "date": "2009-02-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2e9hx6/intro---02-02-09",
        "http://thecolbertreport.cc.com/videos/qx0vt7/the-lilly-ledbetter-fair-pay-act",
        "http://thecolbertreport.cc.com/videos/3n4xx4/it-could-be-worse---iceland",
        "http://thecolbertreport.cc.com/videos/9kc6le/nailed--em---amtrak-photographer",
        "http://thecolbertreport.cc.com/videos/1tdafu/dan-zaccagnino",
        "http://thecolbertreport.cc.com/videos/z0ddpw/so-long--farewell"
      ],
      "guest": "Dan Zaccagnino"
    },
    {
      "date": "2009-02-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5d9tuo/intro---02-03-09",
        "http://thecolbertreport.cc.com/videos/cfzmri/tom-daschle-steps-down",
        "http://thecolbertreport.cc.com/videos/b8o45v/the-word---army-of-one",
        "http://thecolbertreport.cc.com/videos/eo7n2c/colbert-platinum---ass-covering-edition",
        "http://thecolbertreport.cc.com/videos/lr21yl/henry-louis-gates--jr-",
        "http://thecolbertreport.cc.com/videos/fz6ra7/all-the-show-we-have-time-for"
      ],
      "guest": "Henry Louis Gates Jr."
    },
    {
      "date": "2009-02-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hm493e/intro---02-04-09",
        "http://thecolbertreport.cc.com/videos/7z1jvo/stephen-verbally-thrashes-steve-martin",
        "http://thecolbertreport.cc.com/videos/1t7nor/yahweh-or-no-way---the-super-bowl",
        "http://thecolbertreport.cc.com/videos/vtzs6d/who-s-not-honoring-me-now----the-newberry-awards",
        "http://thecolbertreport.cc.com/videos/7z3biy/tell-your-friends"
      ],
      "guest": "Steve Martin"
    },
    {
      "date": "2009-02-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oqo6m1/intro---02-05-09",
        "http://thecolbertreport.cc.com/videos/hkvbbb/stelephant-colbert-the-elephant-seal",
        "http://thecolbertreport.cc.com/videos/7v0jg2/economic-stimulus-debate",
        "http://thecolbertreport.cc.com/videos/9xbuuq/economic-stimulus-bill---james-surowiecki",
        "http://thecolbertreport.cc.com/videos/e378n6/alpha-dog-of-the-week---boy-scouts-of-america",
        "http://thecolbertreport.cc.com/videos/avti1a/jonah-lehrer",
        "http://thecolbertreport.cc.com/videos/qj4lmo/keep-your-friends-close"
      ],
      "guest": "James Surowiecki, Jonah Lehrer"
    },
    {
      "date": "2009-02-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vp4fvu/intro---02-09-09",
        "http://thecolbertreport.cc.com/videos/it28fw/the-new-word-czar",
        "http://thecolbertreport.cc.com/videos/13lrs0/threatdown---gay-divorce",
        "http://thecolbertreport.cc.com/videos/hr5hvl/al-gore-steals-stephen-s-grammy"
      ],
      "guest": "TV on the Radio"
    },
    {
      "date": "2009-02-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fv48bo/intro---02-10-09",
        "http://thecolbertreport.cc.com/videos/mj9pcq/the-visa-black-card",
        "http://thecolbertreport.cc.com/videos/l6kty8/the-word---loyal-opposition",
        "http://thecolbertreport.cc.com/videos/nj38bb/shout-out---honey--counterterrorism---an-old-guard-flag",
        "http://thecolbertreport.cc.com/videos/9w33a7/robert-ballard",
        "http://thecolbertreport.cc.com/videos/gissod/you-look-like-stephen"
      ],
      "guest": "Robert Ballard"
    },
    {
      "date": "2009-02-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/smxfup/intro---02-11-09",
        "http://thecolbertreport.cc.com/videos/l5ealo/westminster-dog-show-snub---formula-40-woof",
        "http://thecolbertreport.cc.com/videos/jxgbb9/dc-voting-rights-act---eleanor-holmes-norton",
        "http://thecolbertreport.cc.com/videos/wfrwar/truth-from-the-gut",
        "http://thecolbertreport.cc.com/videos/42vhyq/steven-pinker",
        "http://thecolbertreport.cc.com/videos/tpb22v/good-night----except-for-the-west-coast"
      ],
      "guest": "Eleanor Holmes Norton, Steven Pinker"
    },
    {
      "date": "2009-02-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m1tx5d/exclusive---stephen-s-sexiest-moments",
        "http://thecolbertreport.cc.com/videos/f0688o/obama-poster-debate---david-ross-and-ed-colbert",
        "http://thecolbertreport.cc.com/videos/vgbtpp/the-dacolbert-code---oscar-predictions",
        "http://thecolbertreport.cc.com/videos/tbf4y6/adam-gopnik",
        "http://thecolbertreport.cc.com/videos/okmu84/goodbye--conan-o-brien"
      ],
      "guest": "David Ross, Ed Colbert, Adam Gopnik"
    },
    {
      "date": "2009-02-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9ynh43/intro---02-23-09",
        "http://thecolbertreport.cc.com/videos/xlgfrl/stephen-s-prayer-day",
        "http://thecolbertreport.cc.com/videos/legx6j/stephen-s-moral-dimension",
        "http://thecolbertreport.cc.com/videos/om9959/helen-fisher"
      ],
      "guest": "Father James Martin, Helen Fisher"
    },
    {
      "date": "2009-02-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mngx54/mardi-gras-celebrations",
        "http://thecolbertreport.cc.com/videos/9jcm4g/1997-flashback",
        "http://thecolbertreport.cc.com/videos/pljjhc/nailed--em---buffet-crime",
        "http://thecolbertreport.cc.com/videos/n75sz3/cliff-sloan",
        "http://thecolbertreport.cc.com/videos/yg82dj/happy-mardi-gras",
        "http://thecolbertreport.cc.com/videos/823sva/turning-to-religion---jim-martin",
        "http://thecolbertreport.cc.com/videos/gks8m8/breaded-fish-sticks"
      ],
      "guest": "Cliff Sloan"
    },
    {
      "date": "2009-02-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4v3vka/intro---02-25-09",
        "http://thecolbertreport.cc.com/videos/fbot0q/obama-s-congressional-address---jindal-s-response",
        "http://thecolbertreport.cc.com/videos/o1f5mr/tip-wag---gorilla-crabs-and-gandhi-s-shoes",
        "http://thecolbertreport.cc.com/videos/jyyb0h/john-fetterman",
        "http://thecolbertreport.cc.com/videos/10ufmk/bears---balls---company-bailouts"
      ],
      "guest": "John Fetterman"
    },
    {
      "date": "2009-02-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lvfhs2/intro---02-26-09",
        "http://thecolbertreport.cc.com/videos/1q3zjs/claire-mccaskill-s-twittering",
        "http://thecolbertreport.cc.com/videos/5j9jjo/conservative-rap-battle---stephen-challenges-michael-steele",
        "http://thecolbertreport.cc.com/videos/831wm1/kris-kristofferson",
        "http://thecolbertreport.cc.com/videos/lh0vwj/the-word---ablacknophobia",
        "http://thecolbertreport.cc.com/videos/um02qq/analog-tv"
      ],
      "guest": "Kris Kristofferson"
    },
    {
      "date": "2009-03-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tfciz3/conservative-rap-battle---michael-steele-gets-served",
        "http://thecolbertreport.cc.com/videos/xtntgt/snow-in-the-studio",
        "http://thecolbertreport.cc.com/videos/52t6yh/p-k--winsome---defective-obama-collectibles",
        "http://thecolbertreport.cc.com/videos/j78ngs/david-byrne"
      ],
      "guest": "David Byrne"
    },
    {
      "date": "2009-03-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qs5iv1/beer-pong-herpes-outbreak",
        "http://thecolbertreport.cc.com/videos/0c92nb/guns-for-roses",
        "http://thecolbertreport.cc.com/videos/l9p0ah/space-module--colbert---name-nasa-s-node-3-after-stephen",
        "http://thecolbertreport.cc.com/videos/oayyzq/mark-bittman",
        "http://thecolbertreport.cc.com/videos/tfciz3/conservative-rap-battle---michael-steele-gets-served"
      ],
      "guest": "Mark Bittman"
    },
    {
      "date": "2009-03-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n8kt9r/intro---03-04-09",
        "http://thecolbertreport.cc.com/videos/kob10w/space-module--colbert---scientology-s-new-galactic-overlord",
        "http://thecolbertreport.cc.com/videos/9opkqc/doom-bunker---jack-jacobs-and-stephen-moore",
        "http://thecolbertreport.cc.com/videos/sx98t6/carl-wilson",
        "http://thecolbertreport.cc.com/videos/239tij/goodnight",
        "http://thecolbertreport.cc.com/videos/1kkbbd/intro---03-03-09",
        "http://thecolbertreport.cc.com/videos/00d1sm/the-word---share-the-wealth",
        "http://thecolbertreport.cc.com/videos/nhjls5/the-murderer-was-derek"
      ],
      "guest": "Carl Wilson"
    },
    {
      "date": "2009-03-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ej854l/intro---03-05-09",
        "http://thecolbertreport.cc.com/videos/w194ds/obama-s-swing-set",
        "http://thecolbertreport.cc.com/videos/a7l1re/tip-wag---rush-limbaugh",
        "http://thecolbertreport.cc.com/videos/n8dlml/steven-johnson",
        "http://thecolbertreport.cc.com/videos/nfx4fy/leave-you-wanting-more",
        "http://thecolbertreport.cc.com/videos/1y41q9/doom-bunker---glenn-beck-s--war-room-"
      ],
      "guest": "Steven Johnson"
    },
    {
      "date": "2009-03-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/itgd4m/intro---03-09-09",
        "http://thecolbertreport.cc.com/videos/4bvnlr/new-baby-abraham-carter-grosz",
        "http://thecolbertreport.cc.com/videos/z9c9ak/better-know-a-district---wyoming-s-at-large---cynthia-lummis",
        "http://thecolbertreport.cc.com/videos/54ad8f/lisa-hannigan"
      ],
      "guest": "Lisa Hannigan"
    },
    {
      "date": "2009-03-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1h7cfe/intro---03-10-09",
        "http://thecolbertreport.cc.com/videos/i1w6au/conservative-rap-battle---droppin--science-on-michael-steele",
        "http://thecolbertreport.cc.com/videos/858jnr/coffee-induced-hallucinations",
        "http://thecolbertreport.cc.com/videos/ogsw1c/jay-keasling",
        "http://thecolbertreport.cc.com/videos/ovf9hb/sick-three-way",
        "http://thecolbertreport.cc.com/videos/mtwuig/exclusive---better-know-a-district---wyoming-s-at-large---cynthia-lummis",
        "http://thecolbertreport.cc.com/videos/psylhz/the-word---locked-and-loathed",
        "http://thecolbertreport.cc.com/videos/dw94ms/sleep-tight--abraham"
      ],
      "guest": "William Gerstenmaier, Dr. Jay Keasling"
    },
    {
      "date": "2009-03-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sa3out/intro---03-11-09",
        "http://thecolbertreport.cc.com/videos/4sbc36/earmarks-abuse-ends-tomorrow",
        "http://thecolbertreport.cc.com/videos/7bt4s0/cheating-death---legal--sweat---pre-natal-health",
        "http://thecolbertreport.cc.com/videos/rovggj/howard-fineman",
        "http://thecolbertreport.cc.com/videos/vpswgr/stephen-s-encore",
        "http://thecolbertreport.cc.com/videos/m6st31/space-module--colbert---william-gerstenmaier"
      ],
      "guest": "Howard Fineman"
    },
    {
      "date": "2009-03-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xum4x8/intro---03-12-09",
        "http://thecolbertreport.cc.com/videos/uvfw3m/mahmoud-s-non-consensual-endorsement-deal",
        "http://thecolbertreport.cc.com/videos/p4j2xc/craziest-f--king-thing-i-ve-ever-heard---barreleye-fish",
        "http://thecolbertreport.cc.com/videos/8nmnda/peter-singer",
        "http://thecolbertreport.cc.com/videos/8tqo3i/goodnight",
        "http://thecolbertreport.cc.com/videos/xjpl01/the-word---rand-illusion"
      ],
      "guest": "Simon Johnson, Peter Singer"
    },
    {
      "date": "2009-03-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8zwa7x/intro---03-16-09",
        "http://thecolbertreport.cc.com/videos/yz9sik/stephen-s-angry-mob-will-crush-aig",
        "http://thecolbertreport.cc.com/videos/pe3tou/better-know-a-governor---mark-sanford-update",
        "http://thecolbertreport.cc.com/videos/ck0fd5/neil-gaiman",
        "http://thecolbertreport.cc.com/videos/qxrsxr/stephen-wants-to-hug-you"
      ],
      "guest": "Jonathan Chait, Neil Gaiman"
    },
    {
      "date": "2009-03-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ogmrdd/intro---03-17-09",
        "http://thecolbertreport.cc.com/videos/v1zxe6/shout-out---the-colbert-report-overseas",
        "http://thecolbertreport.cc.com/videos/bsv6p7/world-of-nahlej---shmeat",
        "http://thecolbertreport.cc.com/videos/7byrkj/david-grann",
        "http://thecolbertreport.cc.com/videos/zrpt32/persian-gulf-countdown-clock",
        "http://thecolbertreport.cc.com/videos/59sfdt/the-new-deal---jonathan-chait"
      ],
      "guest": "David Grann"
    },
    {
      "date": "2009-03-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u70zrc/intro---03-18-09",
        "http://thecolbertreport.cc.com/videos/an5849/predator-x-discovery",
        "http://thecolbertreport.cc.com/videos/fnlgez/tip-wag---mississippi--talk-shows---syfy",
        "http://thecolbertreport.cc.com/videos/5hu17z/juan-cole",
        "http://thecolbertreport.cc.com/videos/bokh2r/sam-s-club-time",
        "http://thecolbertreport.cc.com/videos/3i8x9a/colbert-aluminum---cigar-nubs--faux-poor---blixseth"
      ],
      "guest": "Juan Cole"
    },
    {
      "date": "2009-03-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ntnm0v/intro---03-19-09",
        "http://thecolbertreport.cc.com/videos/tkjk8k/bill-posey-alligator-rumors",
        "http://thecolbertreport.cc.com/videos/oi2fxr/when-animals-attack-our-morals---chimps--lizards---spiders",
        "http://thecolbertreport.cc.com/videos/m9oys8/john-mccardell",
        "http://thecolbertreport.cc.com/videos/f189zq/space-module--colbert---vote-now",
        "http://thecolbertreport.cc.com/videos/wa8cs2/the-word---keeping-our-heads"
      ],
      "guest": "John McCardell"
    },
    {
      "date": "2009-03-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hta8xf/intro---03-30-09",
        "http://thecolbertreport.cc.com/videos/04agpr/violence-in-mexico",
        "http://thecolbertreport.cc.com/videos/ttpqpq/me-time---emily-yoffe-on-narcissistic-personality-disorder",
        "http://thecolbertreport.cc.com/videos/y6yflv/space-module--colbert---democracy-in-orbit",
        "http://thecolbertreport.cc.com/videos/yz8bqz/derrick-pitts"
      ],
      "guest": "Derrick Pitts"
    },
    {
      "date": "2009-03-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/prw3dp/intro---03-31-09",
        "http://thecolbertreport.cc.com/videos/ga9h1c/obama-s-epic-dog-quest",
        "http://thecolbertreport.cc.com/videos/19bdth/better-know-a-lobby---newspaper-association-of-america",
        "http://thecolbertreport.cc.com/videos/fkt6tu/david-plotz",
        "http://thecolbertreport.cc.com/videos/ch71k9/sudoku-answers",
        "http://thecolbertreport.cc.com/videos/7l6w83/me-time---american-narcissism",
        "http://thecolbertreport.cc.com/videos/k0knxh/30-minute-applause"
      ],
      "guest": "David Plotz"
    },
    {
      "date": "2009-04-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/du0pk9/intro---04-01-09",
        "http://thecolbertreport.cc.com/videos/1o1nya/french-worker-protests",
        "http://thecolbertreport.cc.com/videos/5t3340/cheating-death---sperm-sale---colonoscopies",
        "http://thecolbertreport.cc.com/videos/wol3qg/dambisa-moyo",
        "http://thecolbertreport.cc.com/videos/vof9z5/hide-and-seek",
        "http://thecolbertreport.cc.com/videos/jt0f3j/the-10-31-project"
      ],
      "guest": "Dambisa Moyo"
    },
    {
      "date": "2009-04-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/scsjxw/intro---04-02-09",
        "http://thecolbertreport.cc.com/videos/78s5oz/cheney-s-secret-assassination-squad",
        "http://thecolbertreport.cc.com/videos/mkb4ls/merriam-webster-s-word-s-worth",
        "http://thecolbertreport.cc.com/videos/4qhn4o/biz-stone",
        "http://thecolbertreport.cc.com/videos/5uxqom/let-your-gps-be-your-guide",
        "http://thecolbertreport.cc.com/videos/idkq46/the-word---fine-line"
      ],
      "guest": "Biz Stone"
    },
    {
      "date": "2009-04-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d5ju1a/colbert-s-easter-parade",
        "http://thecolbertreport.cc.com/videos/v1ybgk/intro---04-06-09",
        "http://thecolbertreport.cc.com/videos/f3bajc/body-loss",
        "http://thecolbertreport.cc.com/videos/y3ocaq/space-module--colbert---urine-recycling-room",
        "http://thecolbertreport.cc.com/videos/2zq8u0/rich-lowry",
        "http://thecolbertreport.cc.com/videos/k9vxpy/make-lemonade"
      ],
      "guest": "Tom Brokaw, Rich Lowry"
    },
    {
      "date": "2009-04-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/168lgg/intro---04-07-09",
        "http://thecolbertreport.cc.com/videos/9kk3jy/queen-noor-s-royal-treatment",
        "http://thecolbertreport.cc.com/videos/6uykwu/better-know-a-district---new-york-s-25th---dan-maffei",
        "http://thecolbertreport.cc.com/videos/31tszu/queen-noor",
        "http://thecolbertreport.cc.com/videos/pqumra/hiccup-free",
        "http://thecolbertreport.cc.com/videos/njp3xz/un-american-news---rest-of-the-world",
        "http://thecolbertreport.cc.com/videos/u5yf3y/obama-s-european-trip---tom-brokaw"
      ],
      "guest": "Queen Noor"
    },
    {
      "date": "2009-04-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f1gjz4/intro---04-08-09",
        "http://thecolbertreport.cc.com/videos/lyeuyj/birkat-hachama---stephen-frees-his-jews",
        "http://thecolbertreport.cc.com/videos/10cwvc/alpha-dog-of-the-week---ted-stevens",
        "http://thecolbertreport.cc.com/videos/eknw52/phil-bronstein",
        "http://thecolbertreport.cc.com/videos/jmb43t/electronic-edition",
        "http://thecolbertreport.cc.com/videos/7jw15b/the-word---morally-bankrupt"
      ],
      "guest": "Phil Bronstein"
    },
    {
      "date": "2009-04-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ly7fhn/workers--comp-temptation",
        "http://thecolbertreport.cc.com/videos/1adwqk/threatdown---robert-gates--dog-seders---obama",
        "http://thecolbertreport.cc.com/videos/lywaay/bart-ehrman",
        "http://thecolbertreport.cc.com/videos/vd2m1k/stephen-s-severed-head",
        "http://thecolbertreport.cc.com/videos/4wgqsm/where-and-when-is-stephen-going-to-the-persian-gulf----bahrain"
      ],
      "guest": "Bart Ehrman"
    },
    {
      "date": "2009-04-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uvnlz3/intro---04-14-09",
        "http://thecolbertreport.cc.com/videos/1tgxfo/clarence-thomas--new-job",
        "http://thecolbertreport.cc.com/videos/bz4xly/space-module--colbert---sunita-williams",
        "http://thecolbertreport.cc.com/videos/gxfl4g/susie-orbach",
        "http://thecolbertreport.cc.com/videos/5m2sci/goodnight--helen"
      ],
      "guest": "Sunita L. Williams, Susie Orbach"
    },
    {
      "date": "2009-04-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2t8bkw/intro---04-15-09",
        "http://thecolbertreport.cc.com/videos/whfbdu/obama-denies-habeas-corpus",
        "http://thecolbertreport.cc.com/videos/xkxq0s/better-know-a-district---illinois--18th---aaron-schock",
        "http://thecolbertreport.cc.com/videos/0ca7u5/jim-lehrer",
        "http://thecolbertreport.cc.com/videos/g6fu2q/homework-assignment",
        "http://thecolbertreport.cc.com/videos/5rzknc/the-word---have-your-cake-and-eat-it--too"
      ],
      "guest": "Jim Lehrer"
    },
    {
      "date": "2009-04-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t8chps/intro---04-16-09",
        "http://thecolbertreport.cc.com/videos/abfalc/teabagging-protests",
        "http://thecolbertreport.cc.com/videos/npq9t7/indian-elections---kanishk-tharoor",
        "http://thecolbertreport.cc.com/videos/btde8y/douglas-kmiec",
        "http://thecolbertreport.cc.com/videos/gu6q0n/goodnight-salute",
        "http://thecolbertreport.cc.com/videos/a8qba2/tax-atax"
      ],
      "guest": "Kanishk Tharoor, Doug Kmiec"
    },
    {
      "date": "2009-04-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b06wzj/intro---04-20-09",
        "http://thecolbertreport.cc.com/videos/3g58oe/castro-death-wish-list",
        "http://thecolbertreport.cc.com/videos/pzg5id/maersk-alabama---ken-quinn",
        "http://thecolbertreport.cc.com/videos/b1hfbd/tip-wag---texas-secession---maca",
        "http://thecolbertreport.cc.com/videos/qi09sh/joe-arpaio"
      ],
      "guest": "Ken Quinn, Sheriff Joe Arpaio"
    },
    {
      "date": "2009-04-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fll3xv/intro---04-21-09",
        "http://thecolbertreport.cc.com/videos/mnalwu/george-will-s-demon-denim",
        "http://thecolbertreport.cc.com/videos/hezs49/who-s-riding-my-coattails-now----blown-away-by-the-usa",
        "http://thecolbertreport.cc.com/videos/7lqvgy/mike-krzyzewski",
        "http://thecolbertreport.cc.com/videos/4dj3xs/special-dvd-commentary",
        "http://thecolbertreport.cc.com/videos/g9ilpe/anger-s-aweigh",
        "http://thecolbertreport.cc.com/videos/h6pabb/stephen-s-only-regrets"
      ],
      "guest": "Coach Mike Kryzewski"
    },
    {
      "date": "2009-04-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/licvuz/intro---04-22-09",
        "http://thecolbertreport.cc.com/videos/g6q0sp/-the-price-is-right--goes-green",
        "http://thecolbertreport.cc.com/videos/7ax5b6/where-and-when-is-stephen-going-to-the-persian-gulf----qatar",
        "http://thecolbertreport.cc.com/videos/ui31iq/ira-glass",
        "http://thecolbertreport.cc.com/videos/77b5v5/never-go-to-bed-angry",
        "http://thecolbertreport.cc.com/videos/zbqudz/the-word---stressed-position"
      ],
      "guest": "Ira Glass"
    },
    {
      "date": "2009-04-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gj1jdr/intro---04-23-09",
        "http://thecolbertreport.cc.com/videos/16z7m7/america-does-not-swear-on-camera",
        "http://thecolbertreport.cc.com/videos/dbshcz/illegitimate-grandson-of-an-alligator",
        "http://thecolbertreport.cc.com/videos/2tn51j/elizabeth-bintliff",
        "http://thecolbertreport.cc.com/videos/ylolny/goodnight--daisy",
        "http://thecolbertreport.cc.com/videos/g1doyw/summit-of-all-fears"
      ],
      "guest": "Elizabeth Bintliff"
    },
    {
      "date": "2009-04-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ak2bbq/intro---04-27-09",
        "http://thecolbertreport.cc.com/videos/u3yqqg/days-of-swine-and-doses",
        "http://thecolbertreport.cc.com/videos/ioe7hh/craziest-f--king-thing-i-ve-ever-heard---fir-tree-lung",
        "http://thecolbertreport.cc.com/videos/6ywn6l/a-rare-correction---stephen-eats-an-ewok",
        "http://thecolbertreport.cc.com/videos/jlx2r1/the-decemberists"
      ],
      "guest": "The Decemberists"
    },
    {
      "date": "2009-04-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5phyy1/intro---04-28-09",
        "http://thecolbertreport.cc.com/videos/pwdiki/arlen-specter-contracts-donkey-flu",
        "http://thecolbertreport.cc.com/videos/14mfow/foreign-reporting---richard-engel",
        "http://thecolbertreport.cc.com/videos/u40xb8/daniel-gross",
        "http://thecolbertreport.cc.com/videos/l8q5cp/shout-out---kids-edition"
      ],
      "guest": "Richard Engel, Daniel Gross"
    },
    {
      "date": "2009-04-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/we8zzj/intro---04-29-09",
        "http://thecolbertreport.cc.com/videos/0gktuh/ahmadinejad-steals-obama-s-slogan",
        "http://thecolbertreport.cc.com/videos/ou4xko/enemy-swine--a-pigcalypse-now",
        "http://thecolbertreport.cc.com/videos/i5hw2i/david-kessler",
        "http://thecolbertreport.cc.com/videos/seesef/feet-teeth",
        "http://thecolbertreport.cc.com/videos/5kllsr/where-and-when-is-stephen-going-to-the-persian-gulf----correspondents",
        "http://thecolbertreport.cc.com/videos/ewzt0z/no-animals-were-harmed"
      ],
      "guest": "David Kessler"
    },
    {
      "date": "2009-04-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4ncl78/intro---04-30-09",
        "http://thecolbertreport.cc.com/videos/hr47fj/president-obama---the-first-14-mondays",
        "http://thecolbertreport.cc.com/videos/zhiu9l/ethan-nadelmann",
        "http://thecolbertreport.cc.com/videos/1e83az/the-after-show",
        "http://thecolbertreport.cc.com/videos/dnh80p/i-s-on-edjukashun---textbooks--americorps---strip-search"
      ],
      "guest": "Jonathan Alter, Ethan Nadelman"
    },
    {
      "date": "2009-05-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ithaxo/code-word---empathy",
        "http://thecolbertreport.cc.com/videos/e4d421/the-prescott-group-bailout",
        "http://thecolbertreport.cc.com/videos/57pcxy/j-j--abrams",
        "http://thecolbertreport.cc.com/videos/3q06z6/sign-off---colbert-nation-home"
      ],
      "guest": "J.J. Abrams"
    },
    {
      "date": "2009-05-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1yb1cp/intro---05-05-09",
        "http://thecolbertreport.cc.com/videos/daeu0o/cinco-de-mayo-precautions",
        "http://thecolbertreport.cc.com/videos/73g8ui/the-word---captain-kangaroo-court",
        "http://thecolbertreport.cc.com/videos/sye42t/paul-rieckhoff",
        "http://thecolbertreport.cc.com/videos/xul98m/sign-off---iteam",
        "http://thecolbertreport.cc.com/videos/0a05it/movies-that-are-destroying-america---summer-movie-edition"
      ],
      "guest": "Cliff Sloan, Paul Rieckhoff"
    },
    {
      "date": "2009-05-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4aqttz/intro---05-06-09",
        "http://thecolbertreport.cc.com/videos/k97z53/colbert-branson-duel",
        "http://thecolbertreport.cc.com/videos/4h8qcx/where-and-when-is-stephen-going-to-the-persian-gulf----saudi-arabia",
        "http://thecolbertreport.cc.com/videos/q7lfqg/laurie-garrett",
        "http://thecolbertreport.cc.com/videos/2y8ihh/hug-your-television",
        "http://thecolbertreport.cc.com/videos/mekuw6/picking-a-new-supreme-court-justice---cliff-sloan"
      ],
      "guest": "Laurie Garrett"
    },
    {
      "date": "2009-05-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nqr22g/intro---05-07-09",
        "http://thecolbertreport.cc.com/videos/40ivqy/sean-hannity-s-liberty-tree",
        "http://thecolbertreport.cc.com/videos/ednx54/smokin--pole---the-fight-for-arctic-riches--inuit-nation",
        "http://thecolbertreport.cc.com/videos/as8qiu/mitchell-joachim",
        "http://thecolbertreport.cc.com/videos/4bas9p/spay-and-neuter-your-pets",
        "http://thecolbertreport.cc.com/videos/686y3f/tip-wag---forced-smoking---grizzly-best-man"
      ],
      "guest": "Mitchell Joachim"
    },
    {
      "date": "2009-05-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/imn21t/intro---05-11-09",
        "http://thecolbertreport.cc.com/videos/cctfpl/stephen-s-fancy-feast",
        "http://thecolbertreport.cc.com/videos/bwc8x1/credit-card-industry-regulation---tamara-draut",
        "http://thecolbertreport.cc.com/videos/cguksk/alpha-dog-of-the-week---erik-slye",
        "http://thecolbertreport.cc.com/videos/3ttm11/jeff-daniels"
      ],
      "guest": "Tamara Draut"
    },
    {
      "date": "2009-05-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wr98c1/intro---05-12-09",
        "http://thecolbertreport.cc.com/videos/zy5zj6/howard-s-end",
        "http://thecolbertreport.cc.com/videos/n89zl7/cuba-us-trade-relations---julia-sweig",
        "http://thecolbertreport.cc.com/videos/hs7gtm/stephen-s-sound-advice---how-to-re-brand-the-gop",
        "http://thecolbertreport.cc.com/videos/a0bgn9/ron-howard",
        "http://thecolbertreport.cc.com/videos/6fx090/credit-check",
        "http://thecolbertreport.cc.com/videos/lzvish/sign-off---unicorn-dealership"
      ],
      "guest": "Ron Howard"
    },
    {
      "date": "2009-05-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yvcq61/intro---05-13-09",
        "http://thecolbertreport.cc.com/videos/g3716f/robert-gibbs-hates-ringing-cell-phones",
        "http://thecolbertreport.cc.com/videos/hp9jyy/colbert-platinum----1-000-dishes",
        "http://thecolbertreport.cc.com/videos/eon7i2/michael-pollan",
        "http://thecolbertreport.cc.com/videos/0it13s/stephen-colbert-is-awesome",
        "http://thecolbertreport.cc.com/videos/5715dt/our-plan-in-havana",
        "http://thecolbertreport.cc.com/videos/g7s21x/you-are-a-dummy"
      ],
      "guest": "Michael Pollan"
    },
    {
      "date": "2009-05-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ph1m2t/intro---05-14-09",
        "http://thecolbertreport.cc.com/videos/priitm/caveman-porn-stash",
        "http://thecolbertreport.cc.com/videos/phfour/donorschoose-org-donations",
        "http://thecolbertreport.cc.com/videos/m82ydm/yusuf",
        "http://thecolbertreport.cc.com/videos/vyychn/stephen-s-coke-party-protest"
      ],
      "guest": "Yusuf"
    },
    {
      "date": "2009-05-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hopfi8/intro---05-18-09",
        "http://thecolbertreport.cc.com/videos/gc17yz/welcome-to-the-real-world--obama",
        "http://thecolbertreport.cc.com/videos/oh4xki/threatdown---charity--casual-jesus---robot-teachers",
        "http://thecolbertreport.cc.com/videos/phv8h6/meghan-mccain",
        "http://thecolbertreport.cc.com/videos/h4dfgj/sign-off---internal-clock"
      ],
      "guest": "Meghan McCain"
    },
    {
      "date": "2009-05-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/k69zx1/intro---05-19-09",
        "http://thecolbertreport.cc.com/videos/um8x6x/rumsfeld-s-cover-letter-bible-quotes",
        "http://thecolbertreport.cc.com/videos/9w54d6/difference-makers---stephen-keith",
        "http://thecolbertreport.cc.com/videos/tn9xuo/walter-kirn",
        "http://thecolbertreport.cc.com/videos/l2dw5z/stephen-s-show",
        "http://thecolbertreport.cc.com/videos/y5v5ns/the-word---tough-cell"
      ],
      "guest": "Walter Kirn"
    },
    {
      "date": "2009-05-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zq89uw/intro---05-20-09",
        "http://thecolbertreport.cc.com/videos/b9eth2/extra--extra--bleed-all-about-it-",
        "http://thecolbertreport.cc.com/videos/e5f1sd/donorschoose-org-classroom-projects",
        "http://thecolbertreport.cc.com/videos/u2rpts/seth-shostak",
        "http://thecolbertreport.cc.com/videos/m63aac/goodnight",
        "http://thecolbertreport.cc.com/videos/i401ml/the-word---i-know-you-are-but-what-am-i-"
      ],
      "guest": "Seth Shostak"
    },
    {
      "date": "2009-05-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sll291/intro---05-21-09",
        "http://thecolbertreport.cc.com/videos/hck7te/47-million-year-old-fossil",
        "http://thecolbertreport.cc.com/videos/4kzrbn/formidable-opponent---pragmatism-or-idealism",
        "http://thecolbertreport.cc.com/videos/ait1y2/green-day",
        "http://thecolbertreport.cc.com/videos/iuaf6k/she-said--cia-said---bob-graham"
      ],
      "guest": "Green Day"
    },
    {
      "date": "2009-06-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kbuqbk/intro---06-01-09",
        "http://thecolbertreport.cc.com/videos/ckumab/guns-in-national-parks",
        "http://thecolbertreport.cc.com/videos/ezeifx/sonia-sotomayor-s-nomination---jeffrey-toobin",
        "http://thecolbertreport.cc.com/videos/2p70rc/where-and-when-is-stephen-going-to-the-persian-gulf----united-arab-emirates",
        "http://thecolbertreport.cc.com/videos/4suoo4/byron-dorgan"
      ],
      "guest": "Jeffrey Toobin, Sen. Byron Dorgan"
    },
    {
      "date": "2009-06-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/poyt56/intro---06-02-09",
        "http://thecolbertreport.cc.com/videos/xahwo7/saudi-arabia-press-restrictions",
        "http://thecolbertreport.cc.com/videos/m4ur7f/jim-moran-vs--viagra",
        "http://thecolbertreport.cc.com/videos/bpwglm/katty-kay",
        "http://thecolbertreport.cc.com/videos/860dm5/best-audience-of-the-night",
        "http://thecolbertreport.cc.com/videos/ch9xnn/supreme-court-press",
        "http://thecolbertreport.cc.com/videos/t28i3d/dance-for-stephen"
      ],
      "guest": "Katty Kay"
    },
    {
      "date": "2009-06-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lte593/intro---06-03-09",
        "http://thecolbertreport.cc.com/videos/1azzsn/we-have-a-death-star-",
        "http://thecolbertreport.cc.com/videos/in49m6/tip-wag---4th-of-july--craig-t--nelson---gm",
        "http://thecolbertreport.cc.com/videos/ughago/eric-schlosser",
        "http://thecolbertreport.cc.com/videos/fw7nrm/sign-off----the-hollow-men-",
        "http://thecolbertreport.cc.com/videos/rfeepg/cheating-death---cheerios--soda-paralysis---oprah-s-crazy-talk"
      ],
      "guest": "Eric Schlosser"
    },
    {
      "date": "2009-06-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rpkl6b/intro---06-04-09",
        "http://thecolbertreport.cc.com/videos/oqx005/wikipedia-bans-scientologists",
        "http://thecolbertreport.cc.com/videos/anuhnx/craziest-f--king-thing-i-ve-ever-heard---external-lungs",
        "http://thecolbertreport.cc.com/videos/obi6e0/dag-soderberg",
        "http://thecolbertreport.cc.com/videos/u226dl/the-word---i-do--you-don-t"
      ],
      "guest": "Dag Soderberg, David Byrne"
    },
    {
      "date": "2009-06-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gbu94e/operation-iraqi-stephen---mysterious-trip",
        "http://thecolbertreport.cc.com/videos/wy7a2l/operation-iraqi-stephen---john-mccain",
        "http://thecolbertreport.cc.com/videos/n4g2vg/stephen-strong---army-of-me---basic-training-pt--1",
        "http://thecolbertreport.cc.com/videos/c4z5y3/obama-orders-stephen-s-haircut---ray-odierno",
        "http://thecolbertreport.cc.com/videos/m6uaot/sign-off---new-haircut"
      ],
      "guest": "Stephen broadcasts from Iraq, Gen. Ray Odierno"
    },
    {
      "date": "2009-06-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xuowp6/operation-iraqi-stephen---s-h-",
        "http://thecolbertreport.cc.com/videos/nlvzz2/operation-iraqi-stephen---bill-clinton---amp-energy",
        "http://thecolbertreport.cc.com/videos/8querl/formidable-opponent---don-t-ask--don-t-tell",
        "http://thecolbertreport.cc.com/videos/xjmvnq/tareq-salha---robin-balcom",
        "http://thecolbertreport.cc.com/videos/bdo17v/sign-off---hi--stephen-s-mom",
        "http://thecolbertreport.cc.com/videos/clgan9/the-word---why-are-you-here-"
      ],
      "guest": "Stephen broadcasts from Iraq (1)"
    },
    {
      "date": "2009-06-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3avxyi/operation-iraqi-stephen---stephen-s-spider-hole",
        "http://thecolbertreport.cc.com/videos/cyrxgp/admiral-crunch",
        "http://thecolbertreport.cc.com/videos/xfobul/lt--gen--charles-h--jacoby-jr-",
        "http://thecolbertreport.cc.com/videos/jk0yi6/sign-off---head-rub",
        "http://thecolbertreport.cc.com/videos/nlng6v/operation-iraqi-stephen---tom-hanks-care-package",
        "http://thecolbertreport.cc.com/videos/xbtx2g/stephen-strong---army-of-me---basic-training-pt--2"
      ],
      "guest": "Stephen broadcasts from Iraq (2)"
    },
    {
      "date": "2009-06-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x1yyko/stephen-gets-his-hair-cut",
        "http://thecolbertreport.cc.com/videos/ithwrz/operation-iraqi-stephen---golf-club---george-w--bush-s-greeting",
        "http://thecolbertreport.cc.com/videos/9p7eto/operation-iraqi-stephen---fallback-position---air-force-thunderbirds",
        "http://thecolbertreport.cc.com/videos/hqcfyh/operation-iraqi-stephen---frank-a--grippe",
        "http://thecolbertreport.cc.com/videos/aa7w7z/operation-iraqi-stephen---sign-off---honey--i-m-coming-home",
        "http://thecolbertreport.cc.com/videos/74tfzb/better-know-a-cradle-of-civilization---barham-saleh"
      ],
      "guest": "Stephen broadcasts from Iraq (3)"
    },
    {
      "date": "2009-06-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7zoy4v/intro---06-15-09",
        "http://thecolbertreport.cc.com/videos/ycfoc7/warm-memories-of-iraq",
        "http://thecolbertreport.cc.com/videos/cgcvlh/car-shout---gm---chrysler",
        "http://thecolbertreport.cc.com/videos/px4jql/austan-goolsbee",
        "http://thecolbertreport.cc.com/videos/22hank/sign-off---driving-for-the-last-10-minutes"
      ],
      "guest": "Austan Goolsbee"
    },
    {
      "date": "2009-06-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6kwzzi/intro---06-16-09",
        "http://thecolbertreport.cc.com/videos/e51xox/croatia-s-biggest-jeans-world-record",
        "http://thecolbertreport.cc.com/videos/86p43v/teh-runoff---karim-sadjadpour",
        "http://thecolbertreport.cc.com/videos/guirtz/balls-for-kidz---carnivals-encore",
        "http://thecolbertreport.cc.com/videos/8g3agb/jim-rogers",
        "http://thecolbertreport.cc.com/videos/1bur1p/stephen-s-sound-advice---how-to-be-a-totalitarian-nutjob"
      ],
      "guest": "Karim Sadjadpour, Jim Rogers"
    },
    {
      "date": "2009-06-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vz7xis/intro---06-17-09",
        "http://thecolbertreport.cc.com/videos/y8n8bj/stephen-s-positive-obama-coverage",
        "http://thecolbertreport.cc.com/videos/v8qfms/the-word---bohemian-grove",
        "http://thecolbertreport.cc.com/videos/fgc5qj/alpha-dog-of-the-week---silvio-berlusconi",
        "http://thecolbertreport.cc.com/videos/6wqhd0/joshua-micah-marshall",
        "http://thecolbertreport.cc.com/videos/1jvq35/teh-runoff",
        "http://thecolbertreport.cc.com/videos/31otgs/goodnight"
      ],
      "guest": "Joshua Micah Marshall"
    },
    {
      "date": "2009-06-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ewcaj5/intro---06-18-09",
        "http://thecolbertreport.cc.com/videos/0qwej8/murder-in-the-white-house---jeff-goldblum",
        "http://thecolbertreport.cc.com/videos/nmpsnk/bears---balls---tobacco--project-natal---graveyard-bids",
        "http://thecolbertreport.cc.com/videos/e8rev9/paul-muldoon",
        "http://thecolbertreport.cc.com/videos/dvld1q/sign-off---law---order-preview",
        "http://thecolbertreport.cc.com/videos/e8h8e5/murder-in-the-white-house---fly-widow-interview",
        "http://thecolbertreport.cc.com/videos/e72lp2/sign-off---aloha--idaho"
      ],
      "guest": "Paul Muldoon"
    },
    {
      "date": "2009-06-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/je4uya/intro---06-22-09",
        "http://thecolbertreport.cc.com/videos/91fk6r/zicam-recall",
        "http://thecolbertreport.cc.com/videos/h9527k/the-enemy-within---cane-fu",
        "http://thecolbertreport.cc.com/videos/he9dc0/simon-schama",
        "http://thecolbertreport.cc.com/videos/k4vrsb/sign-off---stephen-suffers--too"
      ],
      "guest": "Simon Schama"
    },
    {
      "date": "2009-06-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wovkbp/barack-obama-s-response-to-iran",
        "http://thecolbertreport.cc.com/videos/yaknra/america-s-health-plan-demic",
        "http://thecolbertreport.cc.com/videos/xc1sqp/governor-alert---the-search-for-mark-sanford",
        "http://thecolbertreport.cc.com/videos/fmv6yq/david-kilcullen",
        "http://thecolbertreport.cc.com/videos/i99yp3/the-smell-of-freedom---jeff-goldblum"
      ],
      "guest": "Howard Dean, David Kilcullen"
    },
    {
      "date": "2009-06-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rhiizu/intro---06-24-09",
        "http://thecolbertreport.cc.com/videos/5xejpe/mark-sanford-does-something-interesting",
        "http://thecolbertreport.cc.com/videos/neths8/matthew-crawford",
        "http://thecolbertreport.cc.com/videos/i50dum/sign-off---random-gps-coordinate-lottery",
        "http://thecolbertreport.cc.com/videos/jkobj5/america-s-health-plan-demic---howard-dean",
        "http://thecolbertreport.cc.com/videos/411cqv/sign-off---goodnight"
      ],
      "guest": "Matthew Crawford"
    },
    {
      "date": "2009-06-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j1tx3a/intro---06-25-09",
        "http://thecolbertreport.cc.com/videos/g71yl5/gay-demon-on-the-loose",
        "http://thecolbertreport.cc.com/videos/5gki1y/commonsense-health-care-reform-infomercial",
        "http://thecolbertreport.cc.com/videos/ohjhjq/jim-fouratt",
        "http://thecolbertreport.cc.com/videos/l3h2eg/sign-off---one-breath",
        "http://thecolbertreport.cc.com/videos/nw0bxn/sport-report---soccer--tennis---brett-favre"
      ],
      "guest": "Jim Fouratt"
    },
    {
      "date": "2009-06-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ehxpq9/jeff-goldblum-will-be-missed",
        "http://thecolbertreport.cc.com/videos/di8fs8/michael-jackson-s-media-attention",
        "http://thecolbertreport.cc.com/videos/8ouc6a/the-word---noncensus",
        "http://thecolbertreport.cc.com/videos/4zr9io/neil-degrasse-tyson"
      ],
      "guest": "Neil DeGrasse Tyson"
    },
    {
      "date": "2009-06-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/klvpw6/intro---06-30-09",
        "http://thecolbertreport.cc.com/videos/hy9hl7/al-franken-finally-declared-senator",
        "http://thecolbertreport.cc.com/videos/hzd5cg/4th-of-july-under-attack",
        "http://thecolbertreport.cc.com/videos/jzev8y/is-it-time-to-care-about-soccer-",
        "http://thecolbertreport.cc.com/videos/knfvfz/is-it-time-to-care-about-soccer----alexi-lalas",
        "http://thecolbertreport.cc.com/videos/8x5ezx/kevin-mattson",
        "http://thecolbertreport.cc.com/videos/ehxpq9/jeff-goldblum-will-be-missed"
      ],
      "guest": "Alexi Lalas, Kevin Mattson"
    },
    {
      "date": "2009-07-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/umpd2x/intro---07-01-09",
        "http://thecolbertreport.cc.com/videos/opbzv4/the-second-coming-of-ronald-reagan",
        "http://thecolbertreport.cc.com/videos/6wo5t4/the-clinton-curse",
        "http://thecolbertreport.cc.com/videos/heqh3g/judge--jury---executioner---firefighters--gold-waste---strip-search",
        "http://thecolbertreport.cc.com/videos/r9zau8/nicholas-kristof",
        "http://thecolbertreport.cc.com/videos/sldptb/sign-off---farewell--david-souter"
      ],
      "guest": "Nicholas Kristof"
    },
    {
      "date": "2009-07-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f4016f/intro---07-02-09",
        "http://thecolbertreport.cc.com/videos/mc9la4/cnn-finds-bubbles-the-chimp",
        "http://thecolbertreport.cc.com/videos/n31uuy/re-report---lost-treasures-of-babylon",
        "http://thecolbertreport.cc.com/videos/v5trw8/ed-viesturs",
        "http://thecolbertreport.cc.com/videos/zc3q4z/sign-off---see-you-at-the-bar",
        "http://thecolbertreport.cc.com/videos/sedae1/tip-wag---cynthia-davis---fox-news",
        "http://thecolbertreport.cc.com/videos/wyj1b1/sign-off---get-your-illegal-fireworks"
      ],
      "guest": "Ed Viesturs"
    },
    {
      "date": "2009-07-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4zm73s/intro---07-13-09",
        "http://thecolbertreport.cc.com/videos/m8x1rr/va-backlog---paul-rieckhoff",
        "http://thecolbertreport.cc.com/videos/qvijip/paul-krugman",
        "http://thecolbertreport.cc.com/videos/2wjc98/goodnight"
      ],
      "guest": "Paul Rieckhoff, Paul Krugman"
    },
    {
      "date": "2009-07-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/w7y41r/intro---07-14-09",
        "http://thecolbertreport.cc.com/videos/17wwbv/raise-high-the-rage-beams",
        "http://thecolbertreport.cc.com/videos/o7y2te/leymah-gbowee",
        "http://thecolbertreport.cc.com/videos/9nhp7n/sign-off---the-pitcher-in-the-oat",
        "http://thecolbertreport.cc.com/videos/55a0ws/remembering-remembering-michael-jackson",
        "http://thecolbertreport.cc.com/videos/bfjyjy/stephen-s-sound-advice---how-to-bork-a-nominee"
      ],
      "guest": "Leymah Gbowee"
    },
    {
      "date": "2009-07-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/38zw9a/intro---07-15-09",
        "http://thecolbertreport.cc.com/videos/7avxb3/stephen-wants-to-be-the-worst-person-in-the-world",
        "http://thecolbertreport.cc.com/videos/yhsbjx/difference-makers---doug-jackson",
        "http://thecolbertreport.cc.com/videos/jkayfy/douglas-rushkoff",
        "http://thecolbertreport.cc.com/videos/1ikoxj/sign-off---no-man-is-a-failure",
        "http://thecolbertreport.cc.com/videos/9vyt62/senator-wences-questions-sonia-sotomayor",
        "http://thecolbertreport.cc.com/videos/jb4xw4/the-word---guns--credit--and-corn"
      ],
      "guest": "Douglas Rushkoff"
    },
    {
      "date": "2009-07-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n291gl/intro---07-16-09",
        "http://thecolbertreport.cc.com/videos/7pmbq4/the-memy-awards",
        "http://thecolbertreport.cc.com/videos/3ahlmo/cheating-death---diabetes-dogs--chocolate-milk---swearing-in-pain",
        "http://thecolbertreport.cc.com/videos/7hp904/edmund-andrews",
        "http://thecolbertreport.cc.com/videos/1wc2dn/sign-off---stephen-wins",
        "http://thecolbertreport.cc.com/videos/cqz0pq/tip-wag---assassination-squads--biblical-history---gay-penguins"
      ],
      "guest": "Edmund Andrews"
    },
    {
      "date": "2009-07-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z5a6bx/walter-cronkite-remembered",
        "http://thecolbertreport.cc.com/videos/0a6zq6/reverse-racism",
        "http://thecolbertreport.cc.com/videos/wqv2b7/sport-report---jessica-simpson--olympic-brothel---bud-light",
        "http://thecolbertreport.cc.com/videos/bowvin/bob-park",
        "http://thecolbertreport.cc.com/videos/x2ppm1/sign-off---goodnight"
      ],
      "guest": "Geoffrey Canada, Bob Park"
    },
    {
      "date": "2009-07-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/78h601/intro---07-21-09",
        "http://thecolbertreport.cc.com/videos/1egi6s/40th-anniversary-of-the-moon-landing",
        "http://thecolbertreport.cc.com/videos/puckfx/better-know-a-lobby---acorn",
        "http://thecolbertreport.cc.com/videos/gwtxoo/aaron-carroll",
        "http://thecolbertreport.cc.com/videos/o84f1o/sign-off---stephen-s-chip",
        "http://thecolbertreport.cc.com/videos/hmh0yy/reverse-racism---geoffrey-canada"
      ],
      "guest": "Dr. Aaron Carroll"
    },
    {
      "date": "2009-07-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j9y28p/intro---07-22-09",
        "http://thecolbertreport.cc.com/videos/43yfk6/the-longest-solar-eclipse-of-the-century",
        "http://thecolbertreport.cc.com/videos/8st941/sniper-trifle---matthew-waxman",
        "http://thecolbertreport.cc.com/videos/gda2z2/pope-wrist-watch",
        "http://thecolbertreport.cc.com/videos/hlljrv/chris-anderson",
        "http://thecolbertreport.cc.com/videos/tzs7et/the-word---a-perfect-world"
      ],
      "guest": "Matthew Waxman, Chris Anderson"
    },
    {
      "date": "2009-07-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/abmeny/health-care-reform-is-the-matrix",
        "http://thecolbertreport.cc.com/videos/al2ar6/health-care-hell-scare---die-agnosis--mur-dr",
        "http://thecolbertreport.cc.com/videos/lb7ei8/sign-off---tivo",
        "http://thecolbertreport.cc.com/videos/l3lw8t/sniper-trifle",
        "http://thecolbertreport.cc.com/videos/1y6s8z/sign-off---goodnight"
      ],
      "guest": "Zev Chafets"
    },
    {
      "date": "2009-07-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g64g5i/intro---07-27-09",
        "http://thecolbertreport.cc.com/videos/bx3wyo/sarah-palin-will-be-missed",
        "http://thecolbertreport.cc.com/videos/5mjokj/nailed--em---library-crime",
        "http://thecolbertreport.cc.com/videos/c4hocz/movits-"
      ],
      "guest": "Movits"
    },
    {
      "date": "2009-07-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nwsa83/president-obama-s-teachable-moment",
        "http://thecolbertreport.cc.com/videos/574gc1/womb-raiders---the-fight-for-the-truth-behind-obama-s-birth",
        "http://thecolbertreport.cc.com/videos/wg36jw/arianna-huffington",
        "http://thecolbertreport.cc.com/videos/aayh4c/sign-off---devil-s-tricks",
        "http://thecolbertreport.cc.com/videos/g64g5i/intro---07-27-09"
      ],
      "guest": "Arianna Huffington"
    },
    {
      "date": "2009-07-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n0hvmj/intro---07-29-09",
        "http://thecolbertreport.cc.com/videos/em0er2/frank-the-roommate",
        "http://thecolbertreport.cc.com/videos/hw67wd/sport-report---tour-de-france---robotic-baseball",
        "http://thecolbertreport.cc.com/videos/2dvjk4/kevin-baker",
        "http://thecolbertreport.cc.com/videos/h00qyf/sign-off---watch-without-blinking",
        "http://thecolbertreport.cc.com/videos/zafhtu/womb-raiders---orly-taitz"
      ],
      "guest": "Kevin Baker"
    },
    {
      "date": "2009-07-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jdw6pa/intro---07-30-09",
        "http://thecolbertreport.cc.com/videos/uq6k19/white-house-beer-summit",
        "http://thecolbertreport.cc.com/videos/fmie7p/tip-wag---man-words---movits-",
        "http://thecolbertreport.cc.com/videos/g75n20/kathryn-bigelow",
        "http://thecolbertreport.cc.com/videos/2mqpw1/sign-off---taco-bell-spokesdog",
        "http://thecolbertreport.cc.com/videos/10c870/the-word---he-who-smelt-it--dealt-it"
      ],
      "guest": "Kathryn Bigelow"
    },
    {
      "date": "2009-08-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6tkw9s/intro---08-03-09",
        "http://thecolbertreport.cc.com/videos/g2s68c/dominic-philip-s-book-habit",
        "http://thecolbertreport.cc.com/videos/kc14p7/nailed--em---war-on-birth-control",
        "http://thecolbertreport.cc.com/videos/yre45i/tony-zinni",
        "http://thecolbertreport.cc.com/videos/vv0gs6/sign-off---goodnight"
      ],
      "guest": "Gen. Tony Zinni"
    },
    {
      "date": "2009-08-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2qha08/merry-barackmas",
        "http://thecolbertreport.cc.com/videos/wyon84/the-word---hippie-replacement",
        "http://thecolbertreport.cc.com/videos/m1d4yt/kurt-andersen",
        "http://thecolbertreport.cc.com/videos/e8glog/sign-off---love-makes-the-world-go-round",
        "http://thecolbertreport.cc.com/videos/lqp674/bears---balls---how-to-pay-for-health-care"
      ],
      "guest": "Kurt Andersen"
    },
    {
      "date": "2009-08-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dozbxd/bill-clinton-s-personal-appearance",
        "http://thecolbertreport.cc.com/videos/pedumk/2010-midterms---joe-sestak",
        "http://thecolbertreport.cc.com/videos/8s2cpt/kris-kobach",
        "http://thecolbertreport.cc.com/videos/5f7tro/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/7wxgsg/colbert-bump-cocktail---david-wondrich"
      ],
      "guest": "Kris Kobach"
    },
    {
      "date": "2009-08-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vesroc/intro---08-06-09",
        "http://thecolbertreport.cc.com/videos/7qrkub/back-to-school-with-jeremih",
        "http://thecolbertreport.cc.com/videos/04qijm/movies-that-are-destroying-america---summer",
        "http://thecolbertreport.cc.com/videos/zar0yt/meryl-streep",
        "http://thecolbertreport.cc.com/videos/diktol/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/updeyd/human-week"
      ],
      "guest": "Meryl Streep"
    },
    {
      "date": "2009-08-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gaywhl/intro---08-10-09",
        "http://thecolbertreport.cc.com/videos/0aiuqk/death-panels",
        "http://thecolbertreport.cc.com/videos/1d8uxl/better-know-a-district---maine-s-1st---chellie-pingree",
        "http://thecolbertreport.cc.com/videos/klodac/barbara-boxer",
        "http://thecolbertreport.cc.com/videos/9r0u01/sign-off---encore"
      ],
      "guest": "Sen. Barbara Boxer"
    },
    {
      "date": "2009-08-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1qhrzu/intro---08-11-09",
        "http://thecolbertreport.cc.com/videos/tq0ixs/stephen-s-driving-tips-via-twitter-service",
        "http://thecolbertreport.cc.com/videos/kc7xgf/alpha-dog-of-the-week---betty-lichtenstein",
        "http://thecolbertreport.cc.com/videos/0ivmu5/jonathan-cohn",
        "http://thecolbertreport.cc.com/videos/9pu9xl/sign-off---prevent-forest-fires",
        "http://thecolbertreport.cc.com/videos/dra60l/cold-war-update---cuba---topless-putin"
      ],
      "guest": "Jonathan Cohn"
    },
    {
      "date": "2009-08-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9g2evg/intro---08-12-09",
        "http://thecolbertreport.cc.com/videos/cypmfk/americans-sacrifice-their-ipods",
        "http://thecolbertreport.cc.com/videos/5esjcx/formidable-opponent---health-care---burger-king",
        "http://thecolbertreport.cc.com/videos/53n2qf/mark-johnson",
        "http://thecolbertreport.cc.com/videos/j153gh/yes-we-afghan---james-carville"
      ],
      "guest": "Mark Johnson"
    },
    {
      "date": "2009-08-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3rk7mk/intro---08-13-09",
        "http://thecolbertreport.cc.com/videos/d9wypw/sheila-jackson-lee-takes-a-phone-call",
        "http://thecolbertreport.cc.com/videos/1fblyv/cheating-death---blue-m-ms--vitamin-d---hormones",
        "http://thecolbertreport.cc.com/videos/pfw8xc/mark-devlin",
        "http://thecolbertreport.cc.com/videos/xagarl/sign-off---stephen-s-online-information",
        "http://thecolbertreport.cc.com/videos/8bsp4q/who-s-not-honoring-me-now----obama--nra---teen-choice-awards"
      ],
      "guest": "Mark Devlin"
    },
    {
      "date": "2009-08-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eu8yuk/intro---08-17-09",
        "http://thecolbertreport.cc.com/videos/54nh4d/obama-publishes-health-care-op-ed",
        "http://thecolbertreport.cc.com/videos/xe1vuk/even-better-er-know-a-district---colorado-s-2nd---jared-polis",
        "http://thecolbertreport.cc.com/videos/p4m942/bill-mckibben",
        "http://thecolbertreport.cc.com/videos/rasuqa/sign-off---goodnight"
      ],
      "guest": "Bill McKibben"
    },
    {
      "date": "2009-08-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wagj66/intro---08-18-09",
        "http://thecolbertreport.cc.com/videos/wu0pjh/hamid-karzai-endorsement",
        "http://thecolbertreport.cc.com/videos/z3d9c9/tip-wag---german-campaign--russian-dogs---flying-rabbis",
        "http://thecolbertreport.cc.com/videos/xjhfzn/robert-wright",
        "http://thecolbertreport.cc.com/videos/nw5bk3/sign-off--shofar",
        "http://thecolbertreport.cc.com/videos/79rlpw/the-word---must-be-tv"
      ],
      "guest": "Robert Wright"
    },
    {
      "date": "2009-08-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eu5hos/barney-frank-refuses-to-talk-to-a-dining-room-table",
        "http://thecolbertreport.cc.com/videos/f6lol5/sugar-shortage---marion-nestle",
        "http://thecolbertreport.cc.com/videos/ckefur/ang-lee",
        "http://thecolbertreport.cc.com/videos/qwyqmu/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/jrwpha/the-word---arch-enemies"
      ],
      "guest": "Ang Lee"
    },
    {
      "date": "2009-08-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/om1fcy/intro---08-20-09",
        "http://thecolbertreport.cc.com/videos/bgxuqk/france-bans-elephants",
        "http://thecolbertreport.cc.com/videos/ho2y6d/stephen-s-sound-advice---how-to-make-babies",
        "http://thecolbertreport.cc.com/videos/3muzmh/chris-matthews",
        "http://thecolbertreport.cc.com/videos/gv0u6s/sign-off---vacation-begins",
        "http://thecolbertreport.cc.com/videos/k1zrq2/colbert-platinum---urbane-nomads--gigayacht---michael-jackson-diamond"
      ],
      "guest": "Chris Matthews"
    },
    {
      "date": "2009-09-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dq2vzv/intro---09-14-09",
        "http://thecolbertreport.cc.com/videos/npiiku/conservatives-are-back",
        "http://thecolbertreport.cc.com/videos/ehltxr/kanye-west-interrupts-taylor-swift-at-the-vmas",
        "http://thecolbertreport.cc.com/videos/ljbubg/cory-booker",
        "http://thecolbertreport.cc.com/videos/4kq9de/sign-off---goodnight"
      ],
      "guest": "Cory Booker"
    },
    {
      "date": "2009-09-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/drgqxg/world-record-for-mexican-insults",
        "http://thecolbertreport.cc.com/videos/c9v1s6/the-word---let-freedom-ka-ching",
        "http://thecolbertreport.cc.com/videos/qm9oq3/christiane-amanpour",
        "http://thecolbertreport.cc.com/videos/tcjp92/stephen-loses-world-record-to-lou-dobbs",
        "http://thecolbertreport.cc.com/videos/hen1ip/better-know-a-lobby---health-care-for-america-now"
      ],
      "guest": "Christiane Amanpour"
    },
    {
      "date": "2009-09-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ch7xyz/intro---09-16-09",
        "http://thecolbertreport.cc.com/videos/dp3jiw/body-worlds-plans-cadaver-sex-exhibit",
        "http://thecolbertreport.cc.com/videos/p1ugzo/figgy-moonpowder",
        "http://thecolbertreport.cc.com/videos/1642tt/wayne-coyne",
        "http://thecolbertreport.cc.com/videos/pafbhp/citizens-united-v--federal-election-commission---jeffrey-toobin"
      ],
      "guest": "The Flaming Lips"
    },
    {
      "date": "2009-09-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oclyoo/goat-lab",
        "http://thecolbertreport.cc.com/videos/5psdx6/goat-lab---jon-ronson",
        "http://thecolbertreport.cc.com/videos/3zmd8j/frank-bruni",
        "http://thecolbertreport.cc.com/videos/xl4dp2/i-s-on-edjukashun---muslim-textbooks---tony-danza"
      ],
      "guest": "Frank Bruni"
    },
    {
      "date": "2009-09-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fscepw/intro---09-22-09",
        "http://thecolbertreport.cc.com/videos/brwe58/atone-phone---emmy-awards",
        "http://thecolbertreport.cc.com/videos/h3pbsv/atone-phone---jon-stewart-calls-to-apologize",
        "http://thecolbertreport.cc.com/videos/oqiy0y/shai-agassi",
        "http://thecolbertreport.cc.com/videos/zxvw0a/sign-off---shofar-goodnight"
      ],
      "guest": "Shai Agassi"
    },
    {
      "date": "2009-09-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/epco4o/lunatic-dictator-accommodations",
        "http://thecolbertreport.cc.com/videos/xtts8p/capitalism-s-enemy---michael-moore",
        "http://thecolbertreport.cc.com/videos/hwx2pv/aj-jacobs",
        "http://thecolbertreport.cc.com/videos/8ch7no/sign-off---thank-you-for-joining-us",
        "http://thecolbertreport.cc.com/videos/npdo9z/tip-wag---guns-on-amtrak--fake-lesbians---battleship-audition"
      ],
      "guest": "Michael Moore, A.J. Jacobs"
    },
    {
      "date": "2009-09-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/92d7p3/intro---09-24-09",
        "http://thecolbertreport.cc.com/videos/srdbkv/atone-phone---larry-king-calls",
        "http://thecolbertreport.cc.com/videos/f4xrhk/easter-under-attack---peeps-display",
        "http://thecolbertreport.cc.com/videos/xqer72/ken-burns",
        "http://thecolbertreport.cc.com/videos/cqqzqe/sign-off---automated-desk",
        "http://thecolbertreport.cc.com/videos/rh4p4f/tom-delay-dances-with-the-stars"
      ],
      "guest": "Ken Burns"
    },
    {
      "date": "2009-09-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ph4cw3/atone-phone---last-day-of-apologies",
        "http://thecolbertreport.cc.com/videos/89wc6t/do--dump-or-marry",
        "http://thecolbertreport.cc.com/videos/r9at2m/sheryl-wudunn",
        "http://thecolbertreport.cc.com/videos/wsefin/sign-off---goodnight--conan"
      ],
      "guest": "Sheryl WuDunn"
    },
    {
      "date": "2009-09-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8qd7gf/intro---09-29-09",
        "http://thecolbertreport.cc.com/videos/4bcajc/spider-pope",
        "http://thecolbertreport.cc.com/videos/22jcm5/cheating-death---snus---placebo-effect",
        "http://thecolbertreport.cc.com/videos/03ei16/matt-latimer",
        "http://thecolbertreport.cc.com/videos/7bmnxg/sign-off---richard-dawkins-will-be-here-tomorrow",
        "http://thecolbertreport.cc.com/videos/ph4cw3/atone-phone---last-day-of-apologies"
      ],
      "guest": "Matt Latimer"
    },
    {
      "date": "2009-09-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6bhu7e/intro---09-30-09",
        "http://thecolbertreport.cc.com/videos/rrbojv/send-your-medical-bills-to-max-baucus",
        "http://thecolbertreport.cc.com/videos/m2yjay/a-pace-odyssey",
        "http://thecolbertreport.cc.com/videos/jhrv69/richard-dawkins",
        "http://thecolbertreport.cc.com/videos/t5u4g8/sign-off---goodnight--grammy",
        "http://thecolbertreport.cc.com/videos/kf4xf5/the-word---out-of-the-closet"
      ],
      "guest": "Richard Dawkins"
    },
    {
      "date": "2009-10-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wlav1v/najibullah-zazi-threatens-beauty-supplies",
        "http://thecolbertreport.cc.com/videos/6dv0jz/2016-olympics-in-chicago---george-wendt",
        "http://thecolbertreport.cc.com/videos/zxuz0a/francis-collins",
        "http://thecolbertreport.cc.com/videos/q9o9qv/sign-off---new-slang",
        "http://thecolbertreport.cc.com/videos/91s6ka/threatdown---environmentalists--kang-lee---mountain-pine-beetles"
      ],
      "guest": "George Wendt, Dr. Francis Collins"
    },
    {
      "date": "2009-10-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/733czp/intro---10-05-09",
        "http://thecolbertreport.cc.com/videos/7yi77e/americans-for-prosperity-cheer-chicago-s-failure",
        "http://thecolbertreport.cc.com/videos/k8e7bl/eating-the-distance---the-brad-sciullo-story-pt--2",
        "http://thecolbertreport.cc.com/videos/wfl2if/arne-duncan",
        "http://thecolbertreport.cc.com/videos/d1uxmt/sign-off---goodnight"
      ],
      "guest": "Arne Duncan"
    },
    {
      "date": "2009-10-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lomf6q/new-swine-flu-vaccine-drops",
        "http://thecolbertreport.cc.com/videos/7060r2/the-road-ahead-in-afghanistan---lara-logan",
        "http://thecolbertreport.cc.com/videos/yz886x/john-darnielle",
        "http://thecolbertreport.cc.com/videos/58l1kv/the-word---learning-is-fundamental"
      ],
      "guest": "Lara Logan, the Mountain Goats"
    },
    {
      "date": "2009-10-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kt8d60/intro---10-07-09",
        "http://thecolbertreport.cc.com/videos/p6tyac/human-sacrifice-channel",
        "http://thecolbertreport.cc.com/videos/i1e7h0/craziest-f--king-thing-i-ve-ever-heard---eye-tooth",
        "http://thecolbertreport.cc.com/videos/59gyno/alison-gopnik",
        "http://thecolbertreport.cc.com/videos/9ergzb/sign-off---jasper-t--jowls",
        "http://thecolbertreport.cc.com/videos/qm22ls/formula-401--a-star-is-born"
      ],
      "guest": "Alison Gopnik"
    },
    {
      "date": "2009-10-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ac6rq4/intro---10-08-09",
        "http://thecolbertreport.cc.com/videos/u1v1j7/kevin-the-iranian-intern",
        "http://thecolbertreport.cc.com/videos/jigfye/sport-report---rush-limbaugh---ted-williams--frozen-head",
        "http://thecolbertreport.cc.com/videos/ih4ouf/colin-beavan",
        "http://thecolbertreport.cc.com/videos/7t5ve1/sign-off---buddy-system",
        "http://thecolbertreport.cc.com/videos/81wvda/tip-wag---conservapedia--louvre---honda-unicycle"
      ],
      "guest": "Colin Beavan"
    },
    {
      "date": "2009-10-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6s4gb6/intro---10-12-09",
        "http://thecolbertreport.cc.com/videos/xiuiwd/happy-columbus-day",
        "http://thecolbertreport.cc.com/videos/vnmcv0/fallback-position---james-blake",
        "http://thecolbertreport.cc.com/videos/2ko3eq/sanjay-gupta",
        "http://thecolbertreport.cc.com/videos/izp5gd/sign-off---thanks-to-the-guests"
      ],
      "guest": "Shashi Tharoor, Dr. Sanjay Gupta"
    },
    {
      "date": "2009-10-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g87deh/intro---10-13-09",
        "http://thecolbertreport.cc.com/videos/4cco61/jermaine-maine-tweets-miley-cyrus-facts",
        "http://thecolbertreport.cc.com/videos/7jpek6/the-born-supremacy---david-javerbaum",
        "http://thecolbertreport.cc.com/videos/s52xb5/sylvia-earle",
        "http://thecolbertreport.cc.com/videos/obxlza/sign-off---gmail",
        "http://thecolbertreport.cc.com/videos/l4n6tb/war-of-peace---shashi-tharoor"
      ],
      "guest": "David Javerbaum, Sylvia Earle"
    },
    {
      "date": "2009-10-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g6skj6/pat-roberts-warns-against-health-care-box-canyon",
        "http://thecolbertreport.cc.com/videos/3copn0/the-obesity-epidemic---amy-farrell",
        "http://thecolbertreport.cc.com/videos/ljym9p/the-rza",
        "http://thecolbertreport.cc.com/videos/wijvgm/sign-off---should-have-put-a-ring-on-it",
        "http://thecolbertreport.cc.com/videos/m5y3ox/the-word---symbol-minded"
      ],
      "guest": "Amy Farrell, The RZA"
    },
    {
      "date": "2009-10-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0bzt4y/intro---10-15-09",
        "http://thecolbertreport.cc.com/videos/0a133r/the-money-shot",
        "http://thecolbertreport.cc.com/videos/8xmsj4/the-mayo-lution-will-not-be-televised",
        "http://thecolbertreport.cc.com/videos/7s45sd/jerry-mitchell",
        "http://thecolbertreport.cc.com/videos/sgqznj/sign-off---stephen-unveils-a-new-portrait",
        "http://thecolbertreport.cc.com/videos/ubn9ao/yahweh-or-no-way---legislation-prayers---fake-shroud-of-turin"
      ],
      "guest": "Jerry Mitchell"
    },
    {
      "date": "2009-10-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4srpg9/george-will-s-long-tie",
        "http://thecolbertreport.cc.com/videos/gy6tin/the-word---don-t-ask-don-t-tell",
        "http://thecolbertreport.cc.com/videos/xhz2mw/cornel-west",
        "http://thecolbertreport.cc.com/videos/2onypd/sign-off---don-t-move"
      ],
      "guest": "Cornel West"
    },
    {
      "date": "2009-10-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l98jof/intro---10-27-09",
        "http://thecolbertreport.cc.com/videos/3f3ssx/george-w--bush-s-motivational-speech",
        "http://thecolbertreport.cc.com/videos/wtcyjy/colbert-platinum---harvard-billionaires---red-diamond-suv",
        "http://thecolbertreport.cc.com/videos/8c9hx0/gail-collins",
        "http://thecolbertreport.cc.com/videos/plvf84/sign-off---goodnight-",
        "http://thecolbertreport.cc.com/videos/liq1p2/job-recommendation-from-stephen-colbert",
        "http://thecolbertreport.cc.com/videos/dtlk2w/stephen-s-sound-advice---how-to-get-a-job"
      ],
      "guest": "Randall Balmer, Gail Collins"
    },
    {
      "date": "2009-10-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zspzvk/intro---10-28-09",
        "http://thecolbertreport.cc.com/videos/qvcosm/joe-lieberman-is-a-true-independent",
        "http://thecolbertreport.cc.com/videos/1r96o8/big-bang-theory",
        "http://thecolbertreport.cc.com/videos/3r9su2/brian-cox",
        "http://thecolbertreport.cc.com/videos/bzrvnc/sign-off---future-stephen",
        "http://thecolbertreport.cc.com/videos/1va17m/holy-water-under-the-bridge---randall-balmer"
      ],
      "guest": "Brian Cox"
    },
    {
      "date": "2009-10-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bbj9sz/intro---10-29-09",
        "http://thecolbertreport.cc.com/videos/yl6xd1/usa-today-slams-dirigibles",
        "http://thecolbertreport.cc.com/videos/al6ssq/threatdown---halloween-edition",
        "http://thecolbertreport.cc.com/videos/ku01px/bill-simmons",
        "http://thecolbertreport.cc.com/videos/xalyef/sign-off---thanks-to-bill-simmons---rosanne-cash",
        "http://thecolbertreport.cc.com/videos/w56skk/the-word---you-genics"
      ],
      "guest": "Rosanne Cash, Bill Simmons"
    },
    {
      "date": "2009-11-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vfdy5q/intro---11-02-09",
        "http://thecolbertreport.cc.com/videos/uke17x/used-karzai",
        "http://thecolbertreport.cc.com/videos/uxgb9s/alpha-dog-of-the-week---arnold-schwarzenegger",
        "http://thecolbertreport.cc.com/videos/t62cji/nicholas-thompson",
        "http://thecolbertreport.cc.com/videos/7g9pgn/sign-off---donate-to-the-u-s--speedskating-team"
      ],
      "guest": "Nicholas Thompson"
    },
    {
      "date": "2009-11-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hlio3b/intro---11-03-09",
        "http://thecolbertreport.cc.com/videos/zbi6j6/canadian-hackers-sabotage-colbert-nation",
        "http://thecolbertreport.cc.com/videos/olb2ep/nailed--em---mormon-church-trespassing",
        "http://thecolbertreport.cc.com/videos/qdk21v/andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/sqdke8/sign-off---they-call-me-mister-fry",
        "http://thecolbertreport.cc.com/videos/b7il1x/sport-report---nyc-marathon---olympic-speedskating"
      ],
      "guest": "Andrew Sullivan"
    },
    {
      "date": "2009-11-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wm06ja/intro---11-04-09",
        "http://thecolbertreport.cc.com/videos/hzm3ur/-09-off-year-semi-presidential-electferendum",
        "http://thecolbertreport.cc.com/videos/src597/formidable-opponent---global-warming-with-al-gore",
        "http://thecolbertreport.cc.com/videos/lkkq9m/harold-evans",
        "http://thecolbertreport.cc.com/videos/64ucdo/sign-off---poison-gas",
        "http://thecolbertreport.cc.com/videos/ol1mvi/the-word---the-green-mile"
      ],
      "guest": "Harold Evans"
    },
    {
      "date": "2009-11-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ymrkt5/intro---11-05-09",
        "http://thecolbertreport.cc.com/videos/i7dq6q/guy-fawkers",
        "http://thecolbertreport.cc.com/videos/6vac7m/cheating-death---swine-flu-scam-detector---vaxaconda",
        "http://thecolbertreport.cc.com/videos/cj1lqu/william-bratton",
        "http://thecolbertreport.cc.com/videos/6e51a0/sign-off---donate-to-u-s--speedskating",
        "http://thecolbertreport.cc.com/videos/hnu3dh/tip-wag---rush-limbaugh---us-weekly"
      ],
      "guest": "Joey Cheek, Chief William Bratton"
    },
    {
      "date": "2009-11-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/p4del4/intro---11-09-09",
        "http://thecolbertreport.cc.com/videos/zhrahz/trouble--coverage",
        "http://thecolbertreport.cc.com/videos/uaeaom/u-s--speedskating-team-takes-gold",
        "http://thecolbertreport.cc.com/videos/62flai/thomas-campbell",
        "http://thecolbertreport.cc.com/videos/5hgk8f/sign-off---goodnight"
      ],
      "guest": "Thomas Campbell"
    },
    {
      "date": "2009-11-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nwm4io/intro---11-10-09",
        "http://thecolbertreport.cc.com/videos/bpec5m/barney-frank-is-not-a-great-outdoorsman",
        "http://thecolbertreport.cc.com/videos/476wty/maria-shriver",
        "http://thecolbertreport.cc.com/videos/rl73xb/sign-off---you-can-t-take-it-with-you",
        "http://thecolbertreport.cc.com/videos/ocuoqq/exclusive---better-know-a-district---delaware-s-at-large---mike-castle",
        "http://thecolbertreport.cc.com/videos/i4pgl0/better-know-a-district---delaware-s-at-large---mike-castle"
      ],
      "guest": "Maria Shriver"
    },
    {
      "date": "2009-11-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8m4icj/intro---11-11-09",
        "http://thecolbertreport.cc.com/videos/d3hhgz/goldman-sachs-does-god-s-work",
        "http://thecolbertreport.cc.com/videos/1al5v4/tip-wag---san-francisco-chronicle---george-clinton",
        "http://thecolbertreport.cc.com/videos/p4wqld/christopher-caldwell",
        "http://thecolbertreport.cc.com/videos/xp7fig/sign-off---stephen-s-fight-with-christopher-caldwell",
        "http://thecolbertreport.cc.com/videos/2vmljd/iraniversary---karim-sadjadpour"
      ],
      "guest": "Christopher Caldwell"
    },
    {
      "date": "2009-11-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lbfhkm/intro---11-12-09",
        "http://thecolbertreport.cc.com/videos/cnw6wz/miracle-whip-buys-ad-space",
        "http://thecolbertreport.cc.com/videos/ips2v8/the-word---the-money-shot",
        "http://thecolbertreport.cc.com/videos/2k90o4/sport-report---cricket-scandal---letter-writing-campaign",
        "http://thecolbertreport.cc.com/videos/1yilwm/woody-harrelson",
        "http://thecolbertreport.cc.com/videos/l85kiv/grover-the-hill"
      ],
      "guest": "Woody Harrelson"
    },
    {
      "date": "2009-11-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t5pqdy/intro---11-16-09",
        "http://thecolbertreport.cc.com/videos/8ggl86/obama-bows-to-japanese-emperor",
        "http://thecolbertreport.cc.com/videos/xgze85/alpha-dog-of-the-week---joe-perry",
        "http://thecolbertreport.cc.com/videos/6einjp/paul-goldberger",
        "http://thecolbertreport.cc.com/videos/i42i9t/sign-off---good-morning--burma"
      ],
      "guest": "Paul Goldberger"
    },
    {
      "date": "2009-11-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/im99fb/intro---11-17-09",
        "http://thecolbertreport.cc.com/videos/z1cr8v/kid-gloves---marc-kielburger",
        "http://thecolbertreport.cc.com/videos/ij8d04/malcolm-gladwell",
        "http://thecolbertreport.cc.com/videos/w71om6/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/mwjf6e/the-word---skeletons-in-the-closet"
      ],
      "guest": "Malcolm Gladwell"
    },
    {
      "date": "2009-11-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/24jack/intro---11-18-09",
        "http://thecolbertreport.cc.com/videos/odu5xx/eggo-waffles-shortage-alert",
        "http://thecolbertreport.cc.com/videos/cuhtda/threatdown---quetzalcoatl--santa-claus---canadian-groin-kickers",
        "http://thecolbertreport.cc.com/videos/ah5dzo/norah-jones",
        "http://thecolbertreport.cc.com/videos/1vm4fs/exclusive---better-know-a-district---california-s-12th---jackie-speier-pt--1",
        "http://thecolbertreport.cc.com/videos/udd9qu/exclusive---better-know-a-district---california-s-12th---jackie-speier-pt--2",
        "http://thecolbertreport.cc.com/videos/p8c7xo/better-know-a-district---california-s-12th---jackie-speier"
      ],
      "guest": "Norah Jones"
    },
    {
      "date": "2009-11-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6iz54h/stephen-shakes-his-moneymaker",
        "http://thecolbertreport.cc.com/videos/4tmz49/celebrating-the-ak-47---john-pike",
        "http://thecolbertreport.cc.com/videos/zy3jiq/sign-off---thanks--elvis-costello",
        "http://thecolbertreport.cc.com/videos/tf53hs/the-word---grand-old-pity-party"
      ],
      "guest": "John Pike, Elvis Costello"
    },
    {
      "date": "2009-11-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x90ton/intro---11-30-09",
        "http://thecolbertreport.cc.com/videos/qljewq/amateur-hour-at-the-white-house",
        "http://thecolbertreport.cc.com/videos/ahhfo9/better-know-a-lobby---ploughshares-fund",
        "http://thecolbertreport.cc.com/videos/ec0x55/cevin-soling",
        "http://thecolbertreport.cc.com/videos/53k9co/sign-off---goodnight"
      ],
      "guest": "Dan Esty, Cevin Soling"
    },
    {
      "date": "2009-12-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jvjn7h/intro---12-01-09",
        "http://thecolbertreport.cc.com/videos/fj2x2m/u-s--army-chain-of-command",
        "http://thecolbertreport.cc.com/videos/zwjey6/gold--frankincense-and-mars---guy-consolmagno",
        "http://thecolbertreport.cc.com/videos/s6mur0/sherman-alexie",
        "http://thecolbertreport.cc.com/videos/km8wtf/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/bohr52/something-is-melting-in-denmark---dan-esty"
      ],
      "guest": "Guy Consolmagno, Sherman Alexie"
    },
    {
      "date": "2009-12-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lstmf1/intro---12-02-09",
        "http://thecolbertreport.cc.com/videos/yvq647/deployment-figures",
        "http://thecolbertreport.cc.com/videos/et6ksb/craig-watkins",
        "http://thecolbertreport.cc.com/videos/cyylc0/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/ndi826/better-know-a-made-up-district---connecticut-s-42nd"
      ],
      "guest": "Craig Watkins"
    },
    {
      "date": "2009-12-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qrqaja/formidable-opponent---gary-the-tennis-coach",
        "http://thecolbertreport.cc.com/videos/q8vv0p/intro---12-03-09",
        "http://thecolbertreport.cc.com/videos/knxrx6/tiger-s-tale",
        "http://thecolbertreport.cc.com/videos/hw80nv/skate-expectations---skeleton-team-tryouts---zach-lund",
        "http://thecolbertreport.cc.com/videos/heye88/janet-napolitano",
        "http://thecolbertreport.cc.com/videos/dy9y1l/sign-off---welcome-sean-julien",
        "http://thecolbertreport.cc.com/videos/qx8k9b/cheating-death---r-j--reynolds--genzyme---bionic-bottom"
      ],
      "guest": "Sec. Janet Napolitano"
    },
    {
      "date": "2009-12-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/opl0gz/intro---12-07-09",
        "http://thecolbertreport.cc.com/videos/l9wksx/who-s-attacking-me-now----g--edward-deseve",
        "http://thecolbertreport.cc.com/videos/t0b3f4/craziest-f--king-thing-i-ve-ever-heard---tongue-eating-parasite",
        "http://thecolbertreport.cc.com/videos/pgp8y2/bill-t--jones"
      ],
      "guest": "Bill T. Jones, a performance by the cast of \"Fela\""
    },
    {
      "date": "2009-12-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7a6f7k/intro---12-08-09",
        "http://thecolbertreport.cc.com/videos/0y3uce/how-far-good-parents-will-go",
        "http://thecolbertreport.cc.com/videos/gcu1ou/fed-s-dead---bernie-sanders",
        "http://thecolbertreport.cc.com/videos/9o2lyz/andy-schlafly",
        "http://thecolbertreport.cc.com/videos/2v1vhb/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/w4zn3p/tip-wag---jonas-brothers--fox-news---japanese-burger-king"
      ],
      "guest": "Sen. Bernie Sanders, Andy Schlafly"
    },
    {
      "date": "2009-12-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fdjwxb/intro---12-09-09",
        "http://thecolbertreport.cc.com/videos/ckek7p/monkey-threatdown---holes---banana-too-high",
        "http://thecolbertreport.cc.com/videos/h3kb0s/the-blitzkrieg-on-grinchitude---hallmark---krampus",
        "http://thecolbertreport.cc.com/videos/is6uvv/matt-taibbi",
        "http://thecolbertreport.cc.com/videos/mlp3y1/sign-off---goodnight-with-krampus",
        "http://thecolbertreport.cc.com/videos/2l8p98/fed-s-dead"
      ],
      "guest": "Matt Taibbi"
    },
    {
      "date": "2009-12-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/03g0d5/obama-s-nobel-prize-speech---afghandyland",
        "http://thecolbertreport.cc.com/videos/zivscx/skate-expectations---bobsled-team-tryouts",
        "http://thecolbertreport.cc.com/videos/hjnxot/lara-logan",
        "http://thecolbertreport.cc.com/videos/y74r8f/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/2jc7dn/the-word---grand-old-purity"
      ],
      "guest": "Lara Logan"
    },
    {
      "date": "2009-12-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/efg3d5/intro---12-14-09",
        "http://thecolbertreport.cc.com/videos/9wxgc9/president-obama---the-colbert-interview",
        "http://thecolbertreport.cc.com/videos/t1tsns/stephen-challenges-shani-davis---katherine-reutter",
        "http://thecolbertreport.cc.com/videos/vt4qtf/snoop-dogg"
      ],
      "guest": "Katherine Reutter, Snoop Dogg"
    },
    {
      "date": "2009-12-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x6ydfv/intro---12-15-09",
        "http://thecolbertreport.cc.com/videos/3plx6x/for-he-s-a-jowly-good-fellow",
        "http://thecolbertreport.cc.com/videos/10vyk2/the-blitzkrieg-on-grinchitude---treesus---christ-mas-tree",
        "http://thecolbertreport.cc.com/videos/i16cci/alicia-keys",
        "http://thecolbertreport.cc.com/videos/qn15hk/stephen-challenges-shani-davis",
        "http://thecolbertreport.cc.com/videos/u5g55p/exclusive---extended-interview-with-barack-obama"
      ],
      "guest": "Alicia Keys"
    },
    {
      "date": "2009-12-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ozgmuy/accenture-drops-tiger-woods",
        "http://thecolbertreport.cc.com/videos/4jdam2/the-word---spyvate-sector",
        "http://thecolbertreport.cc.com/videos/bjlb37/tom-brokaw",
        "http://thecolbertreport.cc.com/videos/q9eqq1/sign-off---goodbye--2009",
        "http://thecolbertreport.cc.com/videos/ufq6qh/prescott-financial---gold--women---sheep"
      ],
      "guest": "Tom Brokaw"
    }
  ],
  "2010": [
    {
      "date": "2010-01-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a6c63f/intro---goodbye--old-set",
        "http://thecolbertreport.cc.com/videos/qr3067/high-definition-upgrade",
        "http://thecolbertreport.cc.com/videos/ca8z2z/genitalia-bomb-threat",
        "http://thecolbertreport.cc.com/videos/hospuh/skate-expectations---curling-team-tryouts",
        "http://thecolbertreport.cc.com/videos/bqki32/skate-expectations---curling-team-tryouts---colbert-vs--shuster",
        "http://thecolbertreport.cc.com/videos/ytow3n/sign-off---thanks-for-the-new-set"
      ],
      "guest": "Erick Erickson"
    },
    {
      "date": "2010-01-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l0fai0/intro---01-05-10",
        "http://thecolbertreport.cc.com/videos/qomtkk/high-definition-advertising",
        "http://thecolbertreport.cc.com/videos/ywy8j4/night-of-terror---the-crapification-of-the-american-pant-scape",
        "http://thecolbertreport.cc.com/videos/s2n141/the-word---ideal-or-no-deal",
        "http://thecolbertreport.cc.com/videos/t3fpvm/better-know-an-enemy---yemen",
        "http://thecolbertreport.cc.com/videos/r8x6ag/riley-crane",
        "http://thecolbertreport.cc.com/videos/doe1xo/sign-off---stephen-draws-woodstock"
      ],
      "guest": "Riley Crane"
    },
    {
      "date": "2010-01-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rewr4u/intro---01-06-10",
        "http://thecolbertreport.cc.com/videos/u584e6/a-message-to-standard-definition-cable-providers",
        "http://thecolbertreport.cc.com/videos/g2gimh/drag-me-to-health---ezra-klein---linda-douglass",
        "http://thecolbertreport.cc.com/videos/h3mxst/alpha-dog-of-the-week---domino-s-pizza",
        "http://thecolbertreport.cc.com/videos/4cd9bx/charles-moore",
        "http://thecolbertreport.cc.com/videos/elm4s5/sign-off---not-stephen-s-show"
      ],
      "guest": "Capt. Charles Moore"
    },
    {
      "date": "2010-01-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uo3v4r/intro---01-07-10",
        "http://thecolbertreport.cc.com/videos/f2zb2u/failure-to-connect-the-dots",
        "http://thecolbertreport.cc.com/videos/z3kdhi/fatal-subtraction---barry-scheck",
        "http://thecolbertreport.cc.com/videos/wi0ong/tip-wag---burj-dubai--avatar---transgender-appointees",
        "http://thecolbertreport.cc.com/videos/c3suh9/james-fowler",
        "http://thecolbertreport.cc.com/videos/tso1cs/sign-off---goodnight"
      ],
      "guest": "Barry Scheck, James Fowler"
    },
    {
      "date": "2010-01-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xptxw6/harry-reid-s-racial-praise",
        "http://thecolbertreport.cc.com/videos/3s1wqs/move-your-money---eugene-jarecki",
        "http://thecolbertreport.cc.com/videos/y47i8f/colbert-platinum---estate-tax---skull-ballot-box",
        "http://thecolbertreport.cc.com/videos/4q61kj/morgan-freeman",
        "http://thecolbertreport.cc.com/videos/8e60wq/sign-off---stephen-will-be-right-back"
      ],
      "guest": "Eugene Jarecki, Morgan Freeman"
    },
    {
      "date": "2010-01-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qjn9bh/intro---01-12-10",
        "http://thecolbertreport.cc.com/videos/7qig8p/roxxxy-the-sex-robot",
        "http://thecolbertreport.cc.com/videos/8ln9tv/cheating-death---alzheimer-s--jet-lag---female-libido",
        "http://thecolbertreport.cc.com/videos/7jfkm7/raj-patel"
      ],
      "guest": "Raj Patel"
    },
    {
      "date": "2010-01-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/w3lt72/intro---01-13-10",
        "http://thecolbertreport.cc.com/videos/34mknq/game-change-gossip",
        "http://thecolbertreport.cc.com/videos/kwpeqs/sport-report---gilbert-arenas---mark-mcgwire",
        "http://thecolbertreport.cc.com/videos/t39jgx/movies-that-are-destroying-america---avatar-edition",
        "http://thecolbertreport.cc.com/videos/1xyrig/john-heilemann",
        "http://thecolbertreport.cc.com/videos/erf677/sign-off---mark-mcgwire-action-figure"
      ],
      "guest": "John Heilemann"
    },
    {
      "date": "2010-01-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t151qr/intro---01-14-10",
        "http://thecolbertreport.cc.com/videos/dbcboq/watercressgate",
        "http://thecolbertreport.cc.com/videos/et1vio/the-word---honor-bound",
        "http://thecolbertreport.cc.com/videos/7owg19/haiti-disaster-relief-donations---kathleen-sebelius",
        "http://thecolbertreport.cc.com/videos/gqd029/kathleen-sebelius",
        "http://thecolbertreport.cc.com/videos/afqd2o/sign-off---text-for-haiti-disaster-relief"
      ],
      "guest": "Kathleen Sebelius"
    },
    {
      "date": "2010-01-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i2h2wa/intro---01-18-10",
        "http://thecolbertreport.cc.com/videos/uqolbx/massachusetts-special-election",
        "http://thecolbertreport.cc.com/videos/6s93dq/coal-comfort---margaret-palmer",
        "http://thecolbertreport.cc.com/videos/2kgg0x/own-a-piece-of-histor-me---original-interview-table",
        "http://thecolbertreport.cc.com/videos/r6fzoi/emily-pilloton",
        "http://thecolbertreport.cc.com/videos/47fs6h/sign-off---home-barbershop-quartet-game"
      ],
      "guest": "Dr. Margaret Palmer, Emily Pilloton"
    },
    {
      "date": "2010-01-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/w2qqgl/intro---01-19-10",
        "http://thecolbertreport.cc.com/videos/9t5rlw/onward-christian-soldiers",
        "http://thecolbertreport.cc.com/videos/eseeb0/skate-expectations---speedskating-team-training",
        "http://thecolbertreport.cc.com/videos/nw0obk/skate-expectations---speedskating-team-training---tucker-fredricks",
        "http://thecolbertreport.cc.com/videos/wljw31/stephen-bosworth",
        "http://thecolbertreport.cc.com/videos/5zz1m5/sign-off---teleprompter-in-italics"
      ],
      "guest": "Amb. Stephen Bosworth"
    },
    {
      "date": "2010-01-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oarl2s/intro---01-20-10",
        "http://thecolbertreport.cc.com/videos/9fshqm/boston-dream-guy",
        "http://thecolbertreport.cc.com/videos/h7cxuq/skate-expectations---speedskating-race",
        "http://thecolbertreport.cc.com/videos/r0fs08/skate-expectations---speedskating-team-training---colbert-vs--davis",
        "http://thecolbertreport.cc.com/videos/9qoq3s/dick-ebersol",
        "http://thecolbertreport.cc.com/videos/ekjbd1/sign-off---original-interview-table-auction"
      ],
      "guest": "Dick Ebersol"
    },
    {
      "date": "2010-01-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dhnvbi/intro---01-21-10",
        "http://thecolbertreport.cc.com/videos/a891l1/own-a-piece-of-histor-me---legendary-interview-table",
        "http://thecolbertreport.cc.com/videos/3t1wu4/taliban-public-relations",
        "http://thecolbertreport.cc.com/videos/61faxb/the-word---two-faced",
        "http://thecolbertreport.cc.com/videos/fqdy69/threatdown---airport-security-edition",
        "http://thecolbertreport.cc.com/videos/nchr4z/john-farmer",
        "http://thecolbertreport.cc.com/videos/ngpu7c/sign-off---raise-money-for-haiti-relief"
      ],
      "guest": "John Farmer"
    },
    {
      "date": "2010-01-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ucog8c/intro---01-25-10",
        "http://thecolbertreport.cc.com/videos/2i26ye/obama-gets-called-for-jury-duty",
        "http://thecolbertreport.cc.com/videos/iyaiyz/the-word---manifest-density",
        "http://thecolbertreport.cc.com/videos/fgn6yx/alpha-dog-of-the-week---harold-ford-jr-",
        "http://thecolbertreport.cc.com/videos/y99wku/kati-marton",
        "http://thecolbertreport.cc.com/videos/6u56ui/sign-off---50th-anniversary-of-bubble-wrap"
      ],
      "guest": "Kati Marton"
    },
    {
      "date": "2010-01-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8ukd1u/andre-bauer-is-not-against-animals",
        "http://thecolbertreport.cc.com/videos/1qu3mj/democrats-must-fight-back---paul-begala",
        "http://thecolbertreport.cc.com/videos/4cv6sy/tip-wag---creigh-deeds---scarebear-trail-companion",
        "http://thecolbertreport.cc.com/videos/t59ksv/mika-brzezinski",
        "http://thecolbertreport.cc.com/videos/oz7mss/own-a-piece-of-histor-me---original-c-shaped-anchor-desk"
      ],
      "guest": "Paul Begala, Mika Brzezinski"
    },
    {
      "date": "2010-01-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5wqyfx/intro---01-27-10",
        "http://thecolbertreport.cc.com/videos/69904a/hamid-karzai-s-fashionable-hat",
        "http://thecolbertreport.cc.com/videos/99bavp/the-word---prece-don-t",
        "http://thecolbertreport.cc.com/videos/9hb7jh/fox-news-puts-james-o-keefe-into-context",
        "http://thecolbertreport.cc.com/videos/suw63r/arthur-benjamin",
        "http://thecolbertreport.cc.com/videos/iljqkj/sign-off---give-stephen-an-ipad"
      ],
      "guest": "Arthur Benjamin"
    },
    {
      "date": "2010-01-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pg6y12/stephen-s-state-of-the-union-speech",
        "http://thecolbertreport.cc.com/videos/lnaqfo/david-gergen",
        "http://thecolbertreport.cc.com/videos/jsxv0a/sport-report---all-white-basketball---jana-rawlinson",
        "http://thecolbertreport.cc.com/videos/xebsoq/sign-off---bid-on-stephen-s-c-shaped-desk"
      ],
      "guest": "David Gergen"
    },
    {
      "date": "2010-02-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pg94s5/the-word---siren-song",
        "http://thecolbertreport.cc.com/videos/2n1vl2/sport-report---nicole-detling-miller---jessica-smith",
        "http://thecolbertreport.cc.com/videos/k0hjb1/harold-ford-jr-",
        "http://thecolbertreport.cc.com/videos/biwfer/sign-off---u-s-a-"
      ],
      "guest": "Nicole Detling Miller, Jessica Smith, Harold Ford Jr."
    },
    {
      "date": "2010-02-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u6k7x8/intro---02-02-10",
        "http://thecolbertreport.cc.com/videos/idx9j1/the-word---cognoscor-ergo-sum",
        "http://thecolbertreport.cc.com/videos/2ffk5q/bananafish-tale---henry-allen",
        "http://thecolbertreport.cc.com/videos/0xtws0/eliot-spitzer",
        "http://thecolbertreport.cc.com/videos/wfnsyt/sign-off---kentucky-fried-regret"
      ],
      "guest": "Eliot Spitzer"
    },
    {
      "date": "2010-02-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pmvmz3/intro---02-03-10",
        "http://thecolbertreport.cc.com/videos/4nj8ql/be-almost-all-that-you-can-be",
        "http://thecolbertreport.cc.com/videos/5iocp5/job-man-caravan",
        "http://thecolbertreport.cc.com/videos/sysu7h/job-man-caravan---peter-cove",
        "http://thecolbertreport.cc.com/videos/t6rlnb/john-durant",
        "http://thecolbertreport.cc.com/videos/s0494z/sign-off---office-pool"
      ],
      "guest": "Peter Cove, John Durant"
    },
    {
      "date": "2010-02-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zn4dgm/intro---02-04-10",
        "http://thecolbertreport.cc.com/videos/qkvdcs/hermaphrodites-can-t-be-gay",
        "http://thecolbertreport.cc.com/videos/qqtebr/tip-wag---waterboarding---canada-s-history",
        "http://thecolbertreport.cc.com/videos/6a6j6j/formidable-opponent---khalid-sheikh-mohammed-s-trial",
        "http://thecolbertreport.cc.com/videos/sm98y8/henry-louis-gates--jr-",
        "http://thecolbertreport.cc.com/videos/bsgq92/own-a-piece-of-histor-me---fireplace-portrait"
      ],
      "guest": "Henry Louis Gates"
    },
    {
      "date": "2010-02-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ek3awf/exclusive---skate-expectations---bobsled-team-tryouts-pt--1",
        "http://thecolbertreport.cc.com/videos/52kgrq/office-super-bowl-ad-pool",
        "http://thecolbertreport.cc.com/videos/2idiz7/the-word---faux--n--tell",
        "http://thecolbertreport.cc.com/videos/mtoffp/sarah-palin-uses-a-hand-o-prompter",
        "http://thecolbertreport.cc.com/videos/xdafq2/jonathan-safran-foer",
        "http://thecolbertreport.cc.com/videos/r5okcx/sign-off---goodnight"
      ],
      "guest": "Jonathan Safran Foer"
    },
    {
      "date": "2010-02-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/msydxm/exclusive---skate-expectations---bobsled-team-tryouts-pt--2",
        "http://thecolbertreport.cc.com/videos/s5t5z4/celebrate-black-history-month-with-heineken",
        "http://thecolbertreport.cc.com/videos/nwoc1b/corporate-free-speech---chris-dodd",
        "http://thecolbertreport.cc.com/videos/884juj/alpha-dog-of-the-week---markus-bestin",
        "http://thecolbertreport.cc.com/videos/uao9dj/george-stephanopoulos",
        "http://thecolbertreport.cc.com/videos/zcybb6/sign-off---it-s-lonely-at-the-top"
      ],
      "guest": "George Stephanopoulos"
    },
    {
      "date": "2010-02-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ka4dxt/exclusive---skate-expectations---bobsled-team-tryouts-pt--3",
        "http://thecolbertreport.cc.com/videos/l0cv8x/intro---02-10-10",
        "http://thecolbertreport.cc.com/videos/br6hwk/we-re-off-to-see-the-blizzard",
        "http://thecolbertreport.cc.com/videos/cu5mso/better-know-a-district---illinois--5th",
        "http://thecolbertreport.cc.com/videos/3752v8/better-know-a-district---illinois--5th---mike-quigley",
        "http://thecolbertreport.cc.com/videos/34z9mm/claire-danes",
        "http://thecolbertreport.cc.com/videos/f2whru/sign-off---goodnight"
      ],
      "guest": "Claire Danes"
    },
    {
      "date": "2010-02-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eyfb9f/exclusive---skate-expectations---curling-team-tryouts-pt--1",
        "http://thecolbertreport.cc.com/videos/65cpdn/iran-begins-enriching-uranian",
        "http://thecolbertreport.cc.com/videos/n5w4fs/the-word---political-suicide",
        "http://thecolbertreport.cc.com/videos/li6roe/sport-report---global-snow-drive---al-michaels",
        "http://thecolbertreport.cc.com/videos/s9qfmt/david-ross",
        "http://thecolbertreport.cc.com/videos/qbth0f/sign-off---see-you-in-vancouver"
      ],
      "guest": "Al Michaels, David Ross"
    },
    {
      "date": "2010-02-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jvyagn/exclusive---skate-expectations---speedskating-team-training-pt--1",
        "http://thecolbertreport.cc.com/videos/rbcb67/intro---02-22-10",
        "http://thecolbertreport.cc.com/videos/racwcb/vancouverage-2010---ed-colbert",
        "http://thecolbertreport.cc.com/videos/tzovg4/better-know-a-riding---vancouver-s-south",
        "http://thecolbertreport.cc.com/videos/5l4d9t/better-know-a-riding---vancouver-s-south---ujjal-dosanjh",
        "http://thecolbertreport.cc.com/videos/gg3l88/shaun-white",
        "http://thecolbertreport.cc.com/videos/iohppn/sign-off---you-are-not-americans"
      ],
      "guest": "Shaun White"
    },
    {
      "date": "2010-02-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iar6l3/exclusive---skate-expectations---speedskating-team-training-pt--2",
        "http://thecolbertreport.cc.com/videos/us6yyq/america-s-olympic-wins---lindsey-vonn",
        "http://thecolbertreport.cc.com/videos/1ftd3s/olympic-international-houses",
        "http://thecolbertreport.cc.com/videos/yd5amw/bob-costas",
        "http://thecolbertreport.cc.com/videos/4vx1ll/sign-off---bob-costas-rides-the-moose"
      ],
      "guest": "Lindsey Vonn, Bob Costas"
    },
    {
      "date": "2010-02-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j11loy/exclusive---better-know-a-riding---vancouver-s-south---ujjal-dosanjh-pt--1",
        "http://thecolbertreport.cc.com/videos/eom1sq/exclusive---better-know-a-riding---vancouver-s-south---ujjal-dosanjh-pt--2",
        "http://thecolbertreport.cc.com/videos/8olwnj/exclusive---better-know-a-riding---vancouver-s-south---ujjal-dosanjh-pt--3",
        "http://thecolbertreport.cc.com/videos/l0ax8q/exclusive---skate-expectations---speedskating-team-training-pt--3",
        "http://thecolbertreport.cc.com/videos/php8ta/cold-war-update---olympic-edition",
        "http://thecolbertreport.cc.com/videos/mrk7jd/freud-rage---the-iceman-counseleth",
        "http://thecolbertreport.cc.com/videos/7u3h32/ryan-st--onge---jeret-peterson",
        "http://thecolbertreport.cc.com/videos/ampazf/sign-off---as-they-say-in-canada"
      ],
      "guest": "Scott Hamilton, Jeret Peterson, Ryan St. Onge"
    },
    {
      "date": "2010-02-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i93x4n/exclusive---skate-expectations---speedskating-team-training-pt--4",
        "http://thecolbertreport.cc.com/videos/e7hgxz/intro---02-25-10",
        "http://thecolbertreport.cc.com/videos/jy3odd/stephen-distracts-bob-costas",
        "http://thecolbertreport.cc.com/videos/zoz0j2/freud-rage---the-iceman-counseleth---shani-davis",
        "http://thecolbertreport.cc.com/videos/iactcg/off-notice---canadian-iceholes",
        "http://thecolbertreport.cc.com/videos/j2htnd/seth-wescott",
        "http://thecolbertreport.cc.com/videos/2pub5y/sign-off---thank-you--everyone"
      ],
      "guest": "Shani Davis, Seth Wescott"
    },
    {
      "date": "2010-03-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r61kzy/intro---stephen-wins-the-olympics",
        "http://thecolbertreport.cc.com/videos/z9bfu8/president-obama-mentions-stephen",
        "http://thecolbertreport.cc.com/videos/4nmlgo/health-care-marriage-counseling",
        "http://thecolbertreport.cc.com/videos/6qwf52/olympics-wrap-up---michael-buble",
        "http://thecolbertreport.cc.com/videos/ncbadn/don-cheadle",
        "http://thecolbertreport.cc.com/videos/zbx22j/sign-off---goodnight"
      ],
      "guest": "Don Cheadle"
    },
    {
      "date": "2010-03-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mevtpj/intro---03-02-10",
        "http://thecolbertreport.cc.com/videos/wa48j7/president-obama-s-first-physical",
        "http://thecolbertreport.cc.com/videos/u1ymnx/the-word---kid-owe",
        "http://thecolbertreport.cc.com/videos/odsatp/colbert-platinum---necker-nymph---lexus-lfa",
        "http://thecolbertreport.cc.com/videos/cc44qu/david-brooks",
        "http://thecolbertreport.cc.com/videos/ci6g0d/sign-off---goose-that-lays-the-golden-egg"
      ],
      "guest": "David Brooks"
    },
    {
      "date": "2010-03-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/srp7ci/jim-bunning-ends-filibuster",
        "http://thecolbertreport.cc.com/videos/37u7lc/greece-s-economic-downfall---scheherazade-rehman",
        "http://thecolbertreport.cc.com/videos/elhxu1/tip-wag---american-academy-of-pediatrics---starbucks",
        "http://thecolbertreport.cc.com/videos/m631tw/garry-wills",
        "http://thecolbertreport.cc.com/videos/d3nhmb/sign-off---goodnight"
      ],
      "guest": "Scheherazade Rehman, Garry Wills"
    },
    {
      "date": "2010-03-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lfv3jf/health-care-magic",
        "http://thecolbertreport.cc.com/videos/cgobmb/iraqracy",
        "http://thecolbertreport.cc.com/videos/qdumax/tip-wag---james-o-keefe---sean-hannity",
        "http://thecolbertreport.cc.com/videos/vy9si5/barry-schwartz",
        "http://thecolbertreport.cc.com/videos/r3uuup/sign-off---see-you-later--alligator"
      ],
      "guest": "Barry Schwartz"
    },
    {
      "date": "2010-03-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1919hp/exclusive---olympic-international-houses-pt--2",
        "http://thecolbertreport.cc.com/videos/zqfavl/action-center---health-care-bill---ezra-klein",
        "http://thecolbertreport.cc.com/videos/1nrjt6/tom-hanks-pt--1",
        "http://thecolbertreport.cc.com/videos/49pae4/tom-hanks-pt--2",
        "http://thecolbertreport.cc.com/videos/60qghm/sign-off---one-thought",
        "http://thecolbertreport.cc.com/videos/xdowah/exclusive---olympic-international-houses-pt--1"
      ],
      "guest": "Tom Hanks"
    },
    {
      "date": "2010-03-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6zrwd6/consumer-alert---pringles",
        "http://thecolbertreport.cc.com/videos/rokdab/the-word---define---conquer",
        "http://thecolbertreport.cc.com/videos/b670fj/tip-wag---joe-lieberman--the-pope---sharks",
        "http://thecolbertreport.cc.com/videos/evq830/annie-leonard",
        "http://thecolbertreport.cc.com/videos/887xl8/sign-off---goodnight"
      ],
      "guest": "Annie Leonard"
    },
    {
      "date": "2010-03-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rj79bv/intro---03-10-10",
        "http://thecolbertreport.cc.com/videos/ij37tl/non-sexual-groping",
        "http://thecolbertreport.cc.com/videos/94dkr8/health-care-vote-information-nerve-center---charlie-cook",
        "http://thecolbertreport.cc.com/videos/9m4kr7/survival-seed-bank",
        "http://thecolbertreport.cc.com/videos/ski7ov/sean-carroll",
        "http://thecolbertreport.cc.com/videos/4k81na/sign-off---the-colbert-repoll"
      ],
      "guest": "Sean Carroll"
    },
    {
      "date": "2010-03-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nce2ba/karl-rove-s-new-book",
        "http://thecolbertreport.cc.com/videos/8tmwv8/the-colbert-repoll---scott-rasmussen",
        "http://thecolbertreport.cc.com/videos/8r95fc/monkey-on-the-lam---florida",
        "http://thecolbertreport.cc.com/videos/c8f0b1/david-aaronovitch",
        "http://thecolbertreport.cc.com/videos/96nihd/sign-off---thanks--karl-rove"
      ],
      "guest": "David Aaronovitch"
    },
    {
      "date": "2010-03-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mz0yt2/intro---03-15-10",
        "http://thecolbertreport.cc.com/videos/hut7vd/daylight-savings-time",
        "http://thecolbertreport.cc.com/videos/cfbe28/the-word---afghanistan",
        "http://thecolbertreport.cc.com/videos/402t35/i-can-t-believe-it-s-not-buddha---raj-patel",
        "http://thecolbertreport.cc.com/videos/rf3mus/robert-baer",
        "http://thecolbertreport.cc.com/videos/mdf427/sign-off---goodnight-with-balloon"
      ],
      "guest": "Robert Baer"
    },
    {
      "date": "2010-03-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fmjopd/intro---03-16-10",
        "http://thecolbertreport.cc.com/videos/jz5m0e/barack-joe-bama",
        "http://thecolbertreport.cc.com/videos/wuyjzf/i-s-on-edjukashun---texas-school-board",
        "http://thecolbertreport.cc.com/videos/wl96gx/thought-for-food---donna-simpson--le-whif---cat-litter",
        "http://thecolbertreport.cc.com/videos/4h8104/rebecca-skloot",
        "http://thecolbertreport.cc.com/videos/r6jed2/sign-off---remember-to-wear-green"
      ],
      "guest": "Rebecca Skloot"
    },
    {
      "date": "2010-03-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/86ybsq/ireland-s-shamrock-shortage",
        "http://thecolbertreport.cc.com/videos/wpflq2/sport-report---vasectomies--chess-boxing---golf",
        "http://thecolbertreport.cc.com/videos/m84hav/united-states-census-2010",
        "http://thecolbertreport.cc.com/videos/wqbtkw/nell-irvin-painter",
        "http://thecolbertreport.cc.com/videos/vvqhqa/sign-off---goodnight"
      ],
      "guest": "Nell Irvin Painter"
    },
    {
      "date": "2010-03-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9cthmz/middle-eastern-dogs",
        "http://thecolbertreport.cc.com/videos/oymi80/glenn-beck-attacks-social-justice---james-martin",
        "http://thecolbertreport.cc.com/videos/70uuap/cheating-death---clenched-fingers---pill-reminder",
        "http://thecolbertreport.cc.com/videos/42czdy/mary-matalin",
        "http://thecolbertreport.cc.com/videos/xqfew6/sign-off---goodnight"
      ],
      "guest": "Mary Matalin"
    },
    {
      "date": "2010-03-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uolmzb/passover-dinner-with-elijah",
        "http://thecolbertreport.cc.com/videos/ua8bnx/geriatric-breeding-program",
        "http://thecolbertreport.cc.com/videos/ixrazk/the-word---napoleon-blown-apart",
        "http://thecolbertreport.cc.com/videos/m8ik8j/passover-commercialism",
        "http://thecolbertreport.cc.com/videos/yksbdg/claire-mccaskill",
        "http://thecolbertreport.cc.com/videos/s0mkwg/sign-off---friedrich-schiller"
      ],
      "guest": "Sen. Claire McCaskill"
    },
    {
      "date": "2010-03-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/13gooh/intro---03-30-10",
        "http://thecolbertreport.cc.com/videos/fbk80n/ricky-martin-is-gay",
        "http://thecolbertreport.cc.com/videos/fvq7gv/the-word---forgive-and-forget",
        "http://thecolbertreport.cc.com/videos/dx0lyr/thought-for-food---corn-diapers--fatty-foods---jamie-oliver",
        "http://thecolbertreport.cc.com/videos/51a308/simon-johnson",
        "http://thecolbertreport.cc.com/videos/c9ef0m/sign-off---pringles---whipped-cream"
      ],
      "guest": "Simon Johnson"
    },
    {
      "date": "2010-03-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xyd8rc/intro---03-31-10",
        "http://thecolbertreport.cc.com/videos/phkk0m/who-s-not-honoring-me-now----peabody-awards",
        "http://thecolbertreport.cc.com/videos/mnvsrm/tip-wag---hutaree-militia---abc",
        "http://thecolbertreport.cc.com/videos/p9l3um/easter-under-attack---peeps-display-update",
        "http://thecolbertreport.cc.com/videos/wj35p0/craig-mullaney",
        "http://thecolbertreport.cc.com/videos/bnjl9e/sign-off---finger-pointing-award"
      ],
      "guest": "Craig Mullaney"
    },
    {
      "date": "2010-04-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cej48a/intro---04-01-10",
        "http://thecolbertreport.cc.com/videos/iymjih/stephen-gets-a-free-ipad",
        "http://thecolbertreport.cc.com/videos/2nbqob/elephant-graveyard---david-frum",
        "http://thecolbertreport.cc.com/videos/d9x5mh/jell-o-tampering",
        "http://thecolbertreport.cc.com/videos/3z9wwh/judith-shulevitz",
        "http://thecolbertreport.cc.com/videos/vjehbr/sign-off---goodnight-with-an-ipad"
      ],
      "guest": "David Frum, Judith Shulevitz"
    },
    {
      "date": "2010-04-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5ehjj8/intro---04-05-10",
        "http://thecolbertreport.cc.com/videos/9ef1ri/stephen-converts-to-3d",
        "http://thecolbertreport.cc.com/videos/xo27p1/the-word---bait-and-snitch",
        "http://thecolbertreport.cc.com/videos/rp7kua/threatdown---fox--the-obamas---time-traveling-brandy-thieves",
        "http://thecolbertreport.cc.com/videos/672vju/dean-kamen",
        "http://thecolbertreport.cc.com/videos/zv5abl/sign-off---goodnight-in-3d"
      ],
      "guest": "Dean Kamen"
    },
    {
      "date": "2010-04-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l4nkoq/science-catfight---joe-bastardi-vs--brenda-ekwurzel",
        "http://thecolbertreport.cc.com/videos/506dri/scrabble-allows-proper-names",
        "http://thecolbertreport.cc.com/videos/hovkbz/al-sharpton",
        "http://thecolbertreport.cc.com/videos/z3ifg9/sign-off---goodnight"
      ],
      "guest": "Joe Bastardi, Brenda Ekwurzel, Rev. Al Sharpton"
    },
    {
      "date": "2010-04-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/b1trvk/tiki-barber-cheats-on-his-wife",
        "http://thecolbertreport.cc.com/videos/ov8dk6/tip-wag---hello-kitty-wine---pig-s-blood-filters",
        "http://thecolbertreport.cc.com/videos/ds7vyt/nailed--em---fentimans-victorian-lemonade",
        "http://thecolbertreport.cc.com/videos/23bsc5/david-simon",
        "http://thecolbertreport.cc.com/videos/c3sk5b/sign-off---hello-kitty-wine---cigarettes"
      ],
      "guest": "David Simon"
    },
    {
      "date": "2010-04-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x3hnt4/intro---04-08-10",
        "http://thecolbertreport.cc.com/videos/p89oku/tiger-s-nike-commercial",
        "http://thecolbertreport.cc.com/videos/06i9x0/the-word---affirmative-inaction",
        "http://thecolbertreport.cc.com/videos/as4xr9/the-final-final-frontier",
        "http://thecolbertreport.cc.com/videos/kkc8ee/neil-degrasse-tyson",
        "http://thecolbertreport.cc.com/videos/54hsqy/sign-off---no-man-is-a-failure"
      ],
      "guest": "Neil DeGrasse Tyson"
    },
    {
      "date": "2010-04-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5mdm7i/exclusive---julian-assange-extended-interview",
        "http://thecolbertreport.cc.com/videos/vxvlp9/unpaid-internship-crackdown",
        "http://thecolbertreport.cc.com/videos/ag970g/justice-stevens-replacement---jeffrey-toobin",
        "http://thecolbertreport.cc.com/videos/3a0o7p/wikileaks-military-video",
        "http://thecolbertreport.cc.com/videos/q1yz2t/julian-assange",
        "http://thecolbertreport.cc.com/videos/abcefn/sign-off---goodnight"
      ],
      "guest": "Jeffrey Toobin, Julian Assange"
    },
    {
      "date": "2010-04-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z1lfjo/dow-hits-11-000",
        "http://thecolbertreport.cc.com/videos/fzwwcp/the-word---the-lost-cause",
        "http://thecolbertreport.cc.com/videos/l0qwni/thought-for-food---mentally-ill-advertisers---german-cupcakes",
        "http://thecolbertreport.cc.com/videos/aab36z/jon-mooallem",
        "http://thecolbertreport.cc.com/videos/qrdpob/sign-off---cupcake-chicken-sandwich"
      ],
      "guest": "Jon Mooallem"
    },
    {
      "date": "2010-04-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i50gi7/president-obama-bows-again",
        "http://thecolbertreport.cc.com/videos/xhpjb5/sunday-morning-fact-checking---jake-tapper---bill-adair",
        "http://thecolbertreport.cc.com/videos/f941v8/ryanair-charges-for-toilets",
        "http://thecolbertreport.cc.com/videos/ohefue/david-shields",
        "http://thecolbertreport.cc.com/videos/igm53s/sign-off---china-s-central-finance-ministry"
      ],
      "guest": "David Shields"
    },
    {
      "date": "2010-04-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eskkbc/intro---04-15-10",
        "http://thecolbertreport.cc.com/videos/1fannu/stephen-saves-the-space-program",
        "http://thecolbertreport.cc.com/videos/1ymc3v/tip-wag---forbes---hipsters",
        "http://thecolbertreport.cc.com/videos/5gztgb/formula-01-liquid-genetic-material",
        "http://thecolbertreport.cc.com/videos/q2q4mc/aimee-mullins",
        "http://thecolbertreport.cc.com/videos/t03669/sign-off---tax-deadline"
      ],
      "guest": "Aimee Mullins"
    },
    {
      "date": "2010-04-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/o36u2p/marilyn-monroe-s-x-rays",
        "http://thecolbertreport.cc.com/videos/55ox6j/goldman-sachs--fraud-case---andrew-ross-sorkin",
        "http://thecolbertreport.cc.com/videos/cyx4fw/volcano-eyjafjallajokull",
        "http://thecolbertreport.cc.com/videos/ca04kl/george-will",
        "http://thecolbertreport.cc.com/videos/8di6ao/sign-off---too-big-to-fail"
      ],
      "guest": "Andrew Ross Sorkin, George Will"
    },
    {
      "date": "2010-04-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5kfqlg/intro---04-20-10",
        "http://thecolbertreport.cc.com/videos/q0xdhc/robotic-voice-simulator---foreign-accent-syndrome",
        "http://thecolbertreport.cc.com/videos/f5imzl/p-k--winsome---tea-party-consulting",
        "http://thecolbertreport.cc.com/videos/2o8c1s/stephen-refuses-to-celebrate-4-20",
        "http://thecolbertreport.cc.com/videos/n3iff5/jeffrey-katzenberg",
        "http://thecolbertreport.cc.com/videos/kuy0dk/sign-off---as-they-say-in-japan"
      ],
      "guest": "Jeffrey Katzenberg"
    },
    {
      "date": "2010-04-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6z2omj/the-new--100-bill",
        "http://thecolbertreport.cc.com/videos/2nsr1s/the-word---no-problemo",
        "http://thecolbertreport.cc.com/videos/mqfg58/nailed--em---drive-through-rapping",
        "http://thecolbertreport.cc.com/videos/0teg38/craig-robinson",
        "http://thecolbertreport.cc.com/videos/2tayao/sign-off---donate-to-john-legend-s-charity"
      ],
      "guest": "Craig Robinson"
    },
    {
      "date": "2010-04-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/62j0m5/newspapers-celebrate-earth-day",
        "http://thecolbertreport.cc.com/videos/tqucn8/the-word---straight-to-video",
        "http://thecolbertreport.cc.com/videos/g660yb/bonus-word---defamation-of-independents",
        "http://thecolbertreport.cc.com/videos/0le7r3/gorillaz",
        "http://thecolbertreport.cc.com/videos/s79r6n/sign-off---this-is-a-fun-job"
      ],
      "guest": "Gorillaz"
    },
    {
      "date": "2010-04-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i6lszt/intro---04-26-10",
        "http://thecolbertreport.cc.com/videos/exfe65/boobquake-day-causes-earthquake",
        "http://thecolbertreport.cc.com/videos/ddudkb/the-word---docu-drama",
        "http://thecolbertreport.cc.com/videos/4qgs1h/indecision-2010---midterm-elections---sue-lowden",
        "http://thecolbertreport.cc.com/videos/j7hi89/sharon-jones"
      ],
      "guest": "Sharon Jones and the Dap-Kings"
    },
    {
      "date": "2010-04-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5m4fi7/intro---04-27-10",
        "http://thecolbertreport.cc.com/videos/7b23mk/the-real-lloyd-blankfein",
        "http://thecolbertreport.cc.com/videos/ais5bh/stephen-hawking-is-such-an-a-hole---encountering-aliens",
        "http://thecolbertreport.cc.com/videos/rjye16/conn-iggulden",
        "http://thecolbertreport.cc.com/videos/68bzkf/sign-off---six-flags-discount-tickets"
      ],
      "guest": "Conn Iggulden"
    },
    {
      "date": "2010-04-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g493lv/intro---04-28-10",
        "http://thecolbertreport.cc.com/videos/uzkxfc/gulf-of-mexico-oil-spill",
        "http://thecolbertreport.cc.com/videos/tzdwrb/cheating-death---tobacco-mints--breast-milk---hallucinogens",
        "http://thecolbertreport.cc.com/videos/ke79c8/difference-makers---robert-ekas",
        "http://thecolbertreport.cc.com/videos/pj9ppq/gregg-easterbrook",
        "http://thecolbertreport.cc.com/videos/1tu0hz/sign-off---chief-wandering-meadow-s-headdress"
      ],
      "guest": "Gregg Easterbrook"
    },
    {
      "date": "2010-04-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qu7aln/intro---rube-goldberg-machine",
        "http://thecolbertreport.cc.com/videos/dima6g/wind-farm---oil-spill",
        "http://thecolbertreport.cc.com/videos/u1djps/california-s-proposition-14---abel-maldonado",
        "http://thecolbertreport.cc.com/videos/yqd68y/tip-wag---scientists---kfc",
        "http://thecolbertreport.cc.com/videos/byd88g/ok-go"
      ],
      "guest": "Abel Maldonado, OK Go"
    },
    {
      "date": "2010-05-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/caaib9/times-square-terrorism",
        "http://thecolbertreport.cc.com/videos/i2zwg4/fda-salt-regulation---lori-roman---michael-jacobson",
        "http://thecolbertreport.cc.com/videos/bfve2i/bp-s-undersea-dome",
        "http://thecolbertreport.cc.com/videos/6yc052/elizabeth-warren",
        "http://thecolbertreport.cc.com/videos/jj9r4k/sign-off---lady-liberty-souvenirs"
      ],
      "guest": "Elizabeth Warren"
    },
    {
      "date": "2010-05-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dula0l/intro---05-04-10",
        "http://thecolbertreport.cc.com/videos/zfi7tc/boom--doesn-t-go-the-dynamite",
        "http://thecolbertreport.cc.com/videos/dvwpph/the-word---flight-risk",
        "http://thecolbertreport.cc.com/videos/xyjhb7/stephen-hawking-is-such-an-a-hole---time-travel",
        "http://thecolbertreport.cc.com/videos/j2pf36/mark-moffett",
        "http://thecolbertreport.cc.com/videos/d97fmn/sign-off---michael-j--fox-gets-locked-in"
      ],
      "guest": "Michael J. Fox, Mark W. Moffett"
    },
    {
      "date": "2010-05-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nlh1ly/intro---05-05-10",
        "http://thecolbertreport.cc.com/videos/2nfnz7/nashville-flood-wakeboarder",
        "http://thecolbertreport.cc.com/videos/bw8v97/the-enemy-within---backyard-clothesline",
        "http://thecolbertreport.cc.com/videos/2p2tqn/alpha-dog-of-the-week---george-rekers",
        "http://thecolbertreport.cc.com/videos/pnjs6i/dave-isay",
        "http://thecolbertreport.cc.com/videos/xufsxi/sign-off---dancing-with-julian"
      ],
      "guest": "David Isay"
    },
    {
      "date": "2010-05-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pvx1hb/white-people-prayer-gap",
        "http://thecolbertreport.cc.com/videos/97ikxz/british-election-couverage---andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/8a0q0r/movies-that-are-destroying-america---2010-summer-movie-edition",
        "http://thecolbertreport.cc.com/videos/xo7hie/stewart-brand",
        "http://thecolbertreport.cc.com/videos/0txjlv/sign-off---the-usa-today"
      ],
      "guest": "Stewart Brand"
    },
    {
      "date": "2010-05-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8bpcly/intro---05-10-10",
        "http://thecolbertreport.cc.com/videos/0m67h9/house-returns-the-favor",
        "http://thecolbertreport.cc.com/videos/pxkemd/greece-wither-soon---scheherazade-rehman",
        "http://thecolbertreport.cc.com/videos/oejc0z/oil-containment-solution-randomizer",
        "http://thecolbertreport.cc.com/videos/6ikft9/gary-johnson",
        "http://thecolbertreport.cc.com/videos/xeq5yb/sign-off---goodnight"
      ],
      "guest": "Gov. Gary Johnson"
    },
    {
      "date": "2010-05-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n8gkaf/intro---05-11-10",
        "http://thecolbertreport.cc.com/videos/pcdm2a/consumer-alert---best-friends-charm-bracelets",
        "http://thecolbertreport.cc.com/videos/1227nt/kagan-worship---dahlia-lithwick",
        "http://thecolbertreport.cc.com/videos/rp68kf/australian-sperm-shortage",
        "http://thecolbertreport.cc.com/videos/d04me7/hampton-sides",
        "http://thecolbertreport.cc.com/videos/qv4b2o/sign-off---wriststrong-arm"
      ],
      "guest": "Hampton Sides"
    },
    {
      "date": "2010-05-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nyl5ye/intro---05-12-10",
        "http://thecolbertreport.cc.com/videos/rxu3ed/controlled-burn-of-a-natural-gas",
        "http://thecolbertreport.cc.com/videos/zf5e7d/threatdown---military-food-police--jazz-robots---pretty-girls",
        "http://thecolbertreport.cc.com/videos/0mg8t8/stephen-s-sound-advice---how-to-ace-the-sats",
        "http://thecolbertreport.cc.com/videos/jynvz7/deepak-chopra",
        "http://thecolbertreport.cc.com/videos/0mpxm3/sign-off---fire-extinguisher-shooting"
      ],
      "guest": "Deepak Chopra"
    },
    {
      "date": "2010-05-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uic1xz/intro---05-13-10",
        "http://thecolbertreport.cc.com/videos/mp7sng/confirming-elena",
        "http://thecolbertreport.cc.com/videos/o1qad4/the-hold-steady",
        "http://thecolbertreport.cc.com/videos/ugcamu/sign-off---time-traveling-brandy-thief"
      ],
      "guest": "The Hold Steady"
    },
    {
      "date": "2010-06-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1heoo5/intro---6-1-10",
        "http://thecolbertreport.cc.com/videos/395e6g/vodka-eyeballing",
        "http://thecolbertreport.cc.com/videos/6f9c47/up-brit-creek",
        "http://thecolbertreport.cc.com/videos/p943d0/failure-to-launch---atlantis-crew",
        "http://thecolbertreport.cc.com/videos/ngl48j/ayaan-hirsi-ali",
        "http://thecolbertreport.cc.com/videos/jygylj/sign-off---water-eyeballing"
      ],
      "guest": "Ayaan Hirsi Ali"
    },
    {
      "date": "2010-06-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6707v3/intro---6-2-10",
        "http://thecolbertreport.cc.com/videos/gqwbeo/japan-s-special-election---kazuo-myazaki",
        "http://thecolbertreport.cc.com/videos/qrxaw1/tip-wag---foxconn--charles-taylor---naomi-campbell",
        "http://thecolbertreport.cc.com/videos/4dk71f/craziest-f--ing-thing-i-ve-ever-heard---gored-bullfighter",
        "http://thecolbertreport.cc.com/videos/dvcqzb/lisa-miller",
        "http://thecolbertreport.cc.com/videos/a4ztpz/sign-off---parting-gifts-for-kazuo-myazaki"
      ],
      "guest": "Lisa Miller"
    },
    {
      "date": "2010-06-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d81bvl/intro---6-3-10",
        "http://thecolbertreport.cc.com/videos/iy7vo7/crude---unusual",
        "http://thecolbertreport.cc.com/videos/44gj25/who-s-watching-the-watchdog----liam-mccormack",
        "http://thecolbertreport.cc.com/videos/p34tly/who-s-riding-my-coattails-now----ipad-suit-pocket",
        "http://thecolbertreport.cc.com/videos/fo5d9i/vampire-weekend"
      ],
      "guest": "Vampire Weekend"
    },
    {
      "date": "2010-06-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r4arov/intro---6-7-10",
        "http://thecolbertreport.cc.com/videos/y0xgng/charity-begins-at-11-30",
        "http://thecolbertreport.cc.com/videos/lc7nxu/oil-s-well-that-never-ends",
        "http://thecolbertreport.cc.com/videos/c2l6b4/oil-spill-rage---james-carville",
        "http://thecolbertreport.cc.com/videos/30w6f5/jonathan-alter",
        "http://thecolbertreport.cc.com/videos/ow5rnp/sign-off---gulf-of-america-fund"
      ],
      "guest": "James Carville, Jonathan Alter"
    },
    {
      "date": "2010-06-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uj5obr/obama-s-whoomp--there-it-is-controversy",
        "http://thecolbertreport.cc.com/videos/yj9oop/the-word---p-r--mageddon",
        "http://thecolbertreport.cc.com/videos/n3e887/mark-frauenfelder",
        "http://thecolbertreport.cc.com/videos/r1zjxy/sign-off---the-most-useless-machine"
      ],
      "guest": "Mark Frauenfelder"
    },
    {
      "date": "2010-06-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ou7te0/helen-thomas-s-reputation",
        "http://thecolbertreport.cc.com/videos/0eesk5/formidable-opponent---michael-oren",
        "http://thecolbertreport.cc.com/videos/41cjs4/shout-out---7th-eaccs",
        "http://thecolbertreport.cc.com/videos/12z179/sam-nunn",
        "http://thecolbertreport.cc.com/videos/hv8uj4/sign-off---50-hamburgers"
      ],
      "guest": "Amb. Michael Oren, Sen. Sam Nunn"
    },
    {
      "date": "2010-06-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6iz8ha/bp-stock-sinks",
        "http://thecolbertreport.cc.com/videos/e46kh9/sport-report---soccer-debate---marc-fisher---mark-starr",
        "http://thecolbertreport.cc.com/videos/9rht3y/simulated-mars-mission",
        "http://thecolbertreport.cc.com/videos/19ikyl/alan-bean",
        "http://thecolbertreport.cc.com/videos/gewg17/sign-off---chocolate-syrup"
      ],
      "guest": "Alan Bean"
    },
    {
      "date": "2010-06-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7xsbh3/intro---6-14-10",
        "http://thecolbertreport.cc.com/videos/vlk9h9/america-s-strained-relationship-with-england",
        "http://thecolbertreport.cc.com/videos/xhnftx/smokin--pole---the-quest-for-arctic-riches--canada---china",
        "http://thecolbertreport.cc.com/videos/b6bfik/who-s-not-honoring-me-now----tonys---mtv-movie-awards",
        "http://thecolbertreport.cc.com/videos/bd9ero/stephen-prothero",
        "http://thecolbertreport.cc.com/videos/t2lbqh/sign-off---the-new-oxford-american-dictionary"
      ],
      "guest": "Stephen Prothero"
    },
    {
      "date": "2010-06-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ue0g9m/intro---6-15-10",
        "http://thecolbertreport.cc.com/videos/w6pwpk/testoster-ruin---hanna-rosin",
        "http://thecolbertreport.cc.com/videos/o42e2u/tip-wag---marshall-islands---disney-world-fate",
        "http://thecolbertreport.cc.com/videos/zkoqn2/carl-safina",
        "http://thecolbertreport.cc.com/videos/vr28jt/sign-off---hot-boxers"
      ],
      "guest": "Dr. Carl Safina"
    },
    {
      "date": "2010-06-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vtw6mw/intro---6-16-10",
        "http://thecolbertreport.cc.com/videos/atwjd4/obama-s-bp-oil-spill-speech",
        "http://thecolbertreport.cc.com/videos/fq1qpx/the-word----tay-the-cour-e",
        "http://thecolbertreport.cc.com/videos/0occfp/brevity-is-the-soul-of-twit",
        "http://thecolbertreport.cc.com/videos/ak28k2/devo"
      ],
      "guest": "Devo"
    },
    {
      "date": "2010-06-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zp0vlt/exclusive---who-s-watching-the-watchdog-pt--1",
        "http://thecolbertreport.cc.com/videos/mgk9uw/exclusive---who-s-watching-the-watchdog-pt--2",
        "http://thecolbertreport.cc.com/videos/lmlfss/obama-s-simplified-bp-oil-spill-speech",
        "http://thecolbertreport.cc.com/videos/r0x7kl/south-carolina-s-4th-district-primary---bob-inglis",
        "http://thecolbertreport.cc.com/videos/pw3z5k/colbert-platinum---summer-travel-edition",
        "http://thecolbertreport.cc.com/videos/psfs9q/david-mamet",
        "http://thecolbertreport.cc.com/videos/t0bf7h/sign-off---retweet-for-the-gulf-of-america-fund"
      ],
      "guest": "David Mamet"
    },
    {
      "date": "2010-06-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3xh3zp/us-ties-with-slovenia",
        "http://thecolbertreport.cc.com/videos/tsbncg/fallback-position---astronaut-pt--1",
        "http://thecolbertreport.cc.com/videos/lw3o9e/joe-barton-s-misconstrued-misconstruction",
        "http://thecolbertreport.cc.com/videos/6rxgjl/wes-moore",
        "http://thecolbertreport.cc.com/videos/xr56ob/sign-off---spare-cursed-monkey-s-paw"
      ],
      "guest": "Wes Moore"
    },
    {
      "date": "2010-06-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f7v2qo/who-s-riding-my-coattails-now----ipad-suit-pocket",
        "http://thecolbertreport.cc.com/videos/mt3j86/stanley-mcchrystal-talks-to-rolling-stone",
        "http://thecolbertreport.cc.com/videos/dry79y/fallback-position---astronaut-pt--2",
        "http://thecolbertreport.cc.com/videos/eyzb5g/usa-board-of-ophthalmological-freedom",
        "http://thecolbertreport.cc.com/videos/ej23e4/gloria-steinem",
        "http://thecolbertreport.cc.com/videos/jewfph/sign-off---goodnight"
      ],
      "guest": "Gloria Steinem"
    },
    {
      "date": "2010-06-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h4yffi/intro---6-23-10",
        "http://thecolbertreport.cc.com/videos/wcoc11/us-defeats-algeria",
        "http://thecolbertreport.cc.com/videos/licobk/yahweh-or-no-way---the-blues-brothers---glenn-beck",
        "http://thecolbertreport.cc.com/videos/3dk57p/prophet-glenn-beck---father-guido-sarducci",
        "http://thecolbertreport.cc.com/videos/quds8l/tim-westergren",
        "http://thecolbertreport.cc.com/videos/p3f9t8/sign-off---tomorrow-s-fallback-position"
      ],
      "guest": "Tim Westergren"
    },
    {
      "date": "2010-06-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/k3vali/intro---6-24-10",
        "http://thecolbertreport.cc.com/videos/i8ohf4/put-the-cursed-monkey-paw-down",
        "http://thecolbertreport.cc.com/videos/5m2oyq/the-word---weapon-of-mass-construction",
        "http://thecolbertreport.cc.com/videos/6ppo8y/fallback-position---astronaut-pt--3",
        "http://thecolbertreport.cc.com/videos/3td47y/michael-specter",
        "http://thecolbertreport.cc.com/videos/86kjse/sign-off---general-s-cap"
      ],
      "guest": "Michael Specter"
    },
    {
      "date": "2010-06-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cchudg/robert-c--byrd-dies-at-92",
        "http://thecolbertreport.cc.com/videos/t7kbm8/rolling-stone-article-on-mcchrystal---michael-hastings",
        "http://thecolbertreport.cc.com/videos/nxs1np/doomsday-bunkers",
        "http://thecolbertreport.cc.com/videos/kpz62f/john-waters",
        "http://thecolbertreport.cc.com/videos/q1un38/sign-off---goodnight"
      ],
      "guest": "Michael Hastings, John Waters"
    },
    {
      "date": "2010-06-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8w7w4q/intro---6-29-10",
        "http://thecolbertreport.cc.com/videos/5i29xg/supreme-court-justice-sweetness",
        "http://thecolbertreport.cc.com/videos/gxmj8l/basketcase---stephie-s-knicks-hoop-de-doo-pt--1",
        "http://thecolbertreport.cc.com/videos/cxtlq7/lube-job",
        "http://thecolbertreport.cc.com/videos/t7eba8/julian-castro",
        "http://thecolbertreport.cc.com/videos/6s4ag9/sign-off---sweetness"
      ],
      "guest": "Mayor Julian Castro"
    },
    {
      "date": "2010-06-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4nay3b/mysteries-of-the-ancient-unknown---king-tut-s-penis-pt--1",
        "http://thecolbertreport.cc.com/videos/200t0y/cold-war-update---north-korea---russian-spies",
        "http://thecolbertreport.cc.com/videos/85xlkw/nicholas-carr",
        "http://thecolbertreport.cc.com/videos/zz75v5/sign-off---goodnight"
      ],
      "guest": "Nicholas Carr"
    },
    {
      "date": "2010-07-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qkh2oy/intro---7-1-10",
        "http://thecolbertreport.cc.com/videos/p1rz8m/al-qaeda-starts-inspire-magazine",
        "http://thecolbertreport.cc.com/videos/ytd0xh/threatdown---dawn--actual-food---texas-gop",
        "http://thecolbertreport.cc.com/videos/zgf08n/tangelo-american-john-boehner",
        "http://thecolbertreport.cc.com/videos/7p27ga/manny-howard",
        "http://thecolbertreport.cc.com/videos/lruog2/sign-off---obsessive-compulsive-disorder"
      ],
      "guest": "Manny Howard"
    },
    {
      "date": "2010-07-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/88l8y3/stephen-is-sick",
        "http://thecolbertreport.cc.com/videos/yw04k6/electronic-frontier-foundation---cindy-cohn",
        "http://thecolbertreport.cc.com/videos/2vgxvc/unemployment-benefits---paul-krugman",
        "http://thecolbertreport.cc.com/videos/tod2oy/michio-kaku",
        "http://thecolbertreport.cc.com/videos/59nr33/sign-off---the-hot-zone"
      ],
      "guest": "Paul Krugman, Dr. Michio Kaku"
    },
    {
      "date": "2010-07-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jogb92/intro---7-6-10",
        "http://thecolbertreport.cc.com/videos/vh6d9y/latest-soap-opera-news",
        "http://thecolbertreport.cc.com/videos/v4t63q/the-word---the-white-stuff",
        "http://thecolbertreport.cc.com/videos/52xc1z/i-s-on-edjukashun---loyola--texas-textbooks---wal-mart",
        "http://thecolbertreport.cc.com/videos/44dhom/garret-keizer",
        "http://thecolbertreport.cc.com/videos/p9lstk/sign-off---goodnight"
      ],
      "guest": "Garret Keizer"
    },
    {
      "date": "2010-07-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yx0x8s/the-carell-corral",
        "http://thecolbertreport.cc.com/videos/u8pmv7/the-economist-photoshops-obama-s-picture",
        "http://thecolbertreport.cc.com/videos/2vaaww/thought-for-food---kentucky-tuna---grilled-cheese-burger-melt",
        "http://thecolbertreport.cc.com/videos/7ctnwz/formula-401--beauty-from-my-beast",
        "http://thecolbertreport.cc.com/videos/s7mibo/steve-carell",
        "http://thecolbertreport.cc.com/videos/ytvd7r/sign-off---2010-sexy-spermatozoa-calendar"
      ],
      "guest": "Steve Carell"
    },
    {
      "date": "2010-07-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/381yrb/intro---7-8-10",
        "http://thecolbertreport.cc.com/videos/x5lln0/modest-con-2010",
        "http://thecolbertreport.cc.com/videos/zjdl0i/automatics-for-the-people---ilya-shapiro---jackie-hilly",
        "http://thecolbertreport.cc.com/videos/eieifn/emergency-thought-for-food---candwich-setback",
        "http://thecolbertreport.cc.com/videos/nlmfgk/arturo-rodriguez",
        "http://thecolbertreport.cc.com/videos/oc0gsm/sign-off---go-get-a-tan"
      ],
      "guest": "Arturo Rodriguez"
    },
    {
      "date": "2010-07-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xsaeav/intro---7-26-10",
        "http://thecolbertreport.cc.com/videos/snrn4u/stephen-s-eco-vacation",
        "http://thecolbertreport.cc.com/videos/qqashr/racial-pro-firing",
        "http://thecolbertreport.cc.com/videos/1axxh8/nailed--em---polka-piracy",
        "http://thecolbertreport.cc.com/videos/u5kfga/hephzibah-anderson",
        "http://thecolbertreport.cc.com/videos/rcl3ml/sign-off---bud-light-lime"
      ],
      "guest": "Hephzibah Anderson"
    },
    {
      "date": "2010-07-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/aiaw4g/intro---7-27-10",
        "http://thecolbertreport.cc.com/videos/56iw57/bp-s-live-hayward-cam",
        "http://thecolbertreport.cc.com/videos/m571z2/that-s-the-way-i-leak-it---tom-blanton",
        "http://thecolbertreport.cc.com/videos/431v9v/tip-wag---baby-gap--dick-cheney---plants",
        "http://thecolbertreport.cc.com/videos/2afxlp/kevin-kline",
        "http://thecolbertreport.cc.com/videos/y6qd20/sign-off---goodnight"
      ],
      "guest": "Thomas S. Blanton, Kevin Kline"
    },
    {
      "date": "2010-07-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/it4pai/obama-blows-off-the-boy-scouts",
        "http://thecolbertreport.cc.com/videos/ce9wme/the-word---ownership-society",
        "http://thecolbertreport.cc.com/videos/k9y4mw/republican-gubernatorial-primary-battle-watch--010---tennessee",
        "http://thecolbertreport.cc.com/videos/hjiro1/elon-musk",
        "http://thecolbertreport.cc.com/videos/fl5n9q/sign-off---bit-of-advice"
      ],
      "guest": "Elon Musk"
    },
    {
      "date": "2010-07-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cjuayn/intro---7-29-10",
        "http://thecolbertreport.cc.com/videos/dzk032/the-oil-is-missing",
        "http://thecolbertreport.cc.com/videos/i9hga3/thought-for-food---cereal--foot-long-cheeseburger---ecobot-iii",
        "http://thecolbertreport.cc.com/videos/jt67k1/apology-box",
        "http://thecolbertreport.cc.com/videos/sdjfj9/andy-cohen",
        "http://thecolbertreport.cc.com/videos/6hqby7/sign-off---cocktails"
      ],
      "guest": "Andy Cohen"
    },
    {
      "date": "2010-08-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/07zpy3/intro---8-2-10",
        "http://thecolbertreport.cc.com/videos/o9k8cr/stephen-might-be-gay",
        "http://thecolbertreport.cc.com/videos/wx3505/sport-report---london-olympics---illegal-bullfighting",
        "http://thecolbertreport.cc.com/videos/3dwyx0/alpha-dog-of-the-week---david-h--brooks",
        "http://thecolbertreport.cc.com/videos/ln5q1u/jimmy-cliff"
      ],
      "guest": "Jimmy Cliff"
    },
    {
      "date": "2010-08-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s8t2k9/brett-favre-retires-again",
        "http://thecolbertreport.cc.com/videos/noj1lw/consumer-protection-agency---barney-frank",
        "http://thecolbertreport.cc.com/videos/jrpte4/republican-gubernatorial-primary-battle-watch--010---basil-marceaux-com",
        "http://thecolbertreport.cc.com/videos/a5r0r5/laura-ingraham",
        "http://thecolbertreport.cc.com/videos/9838f3/sign-off---credit-card-agreement"
      ],
      "guest": "Laura Ingraham"
    },
    {
      "date": "2010-08-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eirad0/basil-marceaux-com---obama-s-birthday",
        "http://thecolbertreport.cc.com/videos/4mbc26/p-k--winsome---black-viewer-ratings",
        "http://thecolbertreport.cc.com/videos/vhx4eu/threat-standdown---monkey-terrorism",
        "http://thecolbertreport.cc.com/videos/t5nlmh/michael-posner",
        "http://thecolbertreport.cc.com/videos/gc9gia/sign-off---nielsen-mandela"
      ],
      "guest": "Michael Posner"
    },
    {
      "date": "2010-08-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tsl05q/intro---8-5-10",
        "http://thecolbertreport.cc.com/videos/1qu0ts/how-to-ruin-same-sex-marriages",
        "http://thecolbertreport.cc.com/videos/gw1rft/pope-s-baseball-cap---catholictv",
        "http://thecolbertreport.cc.com/videos/bdzvwl/savion-glover",
        "http://thecolbertreport.cc.com/videos/our78a/sign-off---tap-dancing"
      ],
      "guest": "Savion Glover"
    },
    {
      "date": "2010-08-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cfbxpk/intro---8-10-10",
        "http://thecolbertreport.cc.com/videos/40r2zf/honoring-martin-luther-king",
        "http://thecolbertreport.cc.com/videos/jbgt2s/citizenship-down---akhil-amar",
        "http://thecolbertreport.cc.com/videos/v2az23/alpha-dog-of-the-week---steven-slater",
        "http://thecolbertreport.cc.com/videos/uhmewn/dylan-ratigan",
        "http://thecolbertreport.cc.com/videos/p3wgd1/sign-off---goodnight"
      ],
      "guest": "Dylan Ratigan"
    },
    {
      "date": "2010-08-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jwpn0p/moral-compass-5000-action-center",
        "http://thecolbertreport.cc.com/videos/tpcehb/david-finkel",
        "http://thecolbertreport.cc.com/videos/j0nge7/sign-off---goodnight"
      ],
      "guest": "David Finkel"
    },
    {
      "date": "2010-08-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ibivj9/intro---8-12-10",
        "http://thecolbertreport.cc.com/videos/t6cmn9/happy-ramadan",
        "http://thecolbertreport.cc.com/videos/tavgu2/the-word---weapon-of-mass-construction",
        "http://thecolbertreport.cc.com/videos/obv2rl/senior-moment",
        "http://thecolbertreport.cc.com/videos/lx17lm/chuck-close",
        "http://thecolbertreport.cc.com/videos/h6dwnn/sign-off---chuck-close-books"
      ],
      "guest": "Chuck Close"
    },
    {
      "date": "2010-08-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q61axv/growing-intelligence-community---richard-clarke",
        "http://thecolbertreport.cc.com/videos/yh08ag/invasion-of-the-country-snatchers",
        "http://thecolbertreport.cc.com/videos/gr3fyt/john-fetterman",
        "http://thecolbertreport.cc.com/videos/6ksdhb/sign-off---starbucks-latte"
      ],
      "guest": "Richard Clarke, John Fetterman"
    },
    {
      "date": "2010-08-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dlrtyi/intro---8-17-10",
        "http://thecolbertreport.cc.com/videos/c3sn86/newsweek-ranks-the-world-s-best-countries",
        "http://thecolbertreport.cc.com/videos/2hdefm/better-know-a-lobby---american-meat-institute",
        "http://thecolbertreport.cc.com/videos/tno3pg/fox-news-and-republican-party-make-it-official",
        "http://thecolbertreport.cc.com/videos/2kzgs4/barry-levine",
        "http://thecolbertreport.cc.com/videos/xsqp9j/sign-off---newsweek"
      ],
      "guest": "Barry Levine"
    },
    {
      "date": "2010-08-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vby4js/intro---8-18-10",
        "http://thecolbertreport.cc.com/videos/50c2du/brett-favre-returns-to-football",
        "http://thecolbertreport.cc.com/videos/08wn77/the-word---borderline-personality",
        "http://thecolbertreport.cc.com/videos/l06vi1/don-t-shoot-the-schlessinger",
        "http://thecolbertreport.cc.com/videos/389e2m/thomas-french",
        "http://thecolbertreport.cc.com/videos/b2scuj/sign-off---sharpened-broom-handle"
      ],
      "guest": "Thomas French"
    },
    {
      "date": "2010-08-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x0zwn9/intro---8-19-10",
        "http://thecolbertreport.cc.com/videos/m4f5im/the-word---what-if-you-threw-a-peace-and-nobody-came-",
        "http://thecolbertreport.cc.com/videos/2rjk08/all-s-well-that-ends-oil-well---michael-blum",
        "http://thecolbertreport.cc.com/videos/c2uztk/jon-krakauer",
        "http://thecolbertreport.cc.com/videos/g9w04r/sign-off---goodnight"
      ],
      "guest": "Jon Krakauer"
    },
    {
      "date": "2010-08-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zn0m8s/stephen-wins-an-emmy",
        "http://thecolbertreport.cc.com/videos/xa3l6x/the-word---losing-his-religion",
        "http://thecolbertreport.cc.com/videos/8vazj8/aqua-threatdown---oyster-sluts--japanese-hackers---israeli-regulators",
        "http://thecolbertreport.cc.com/videos/jjg6uf/leslie-kean",
        "http://thecolbertreport.cc.com/videos/gbrydj/sign-off---balloon"
      ],
      "guest": "Leslie Kean"
    },
    {
      "date": "2010-08-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8v2r6r/intro---8-24-10",
        "http://thecolbertreport.cc.com/videos/ay7pky/terror-bunker-5200",
        "http://thecolbertreport.cc.com/videos/rxmuip/the-word---control-self-delete",
        "http://thecolbertreport.cc.com/videos/7azwuj/mahmoody-blues",
        "http://thecolbertreport.cc.com/videos/vly30s/jeffrey-goldberg",
        "http://thecolbertreport.cc.com/videos/p0468k/sign-off---sanitized-goodnight"
      ],
      "guest": "Jeffrey Goldberg"
    },
    {
      "date": "2010-08-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ckwof5/john-mccain-s-victorious-defeat",
        "http://thecolbertreport.cc.com/videos/bn16zn/stephen-colbert-university---andrew-hacker",
        "http://thecolbertreport.cc.com/videos/nmp9j3/mysteries-of-the-ancient-unknown---king-tut-s-penis-pt--2",
        "http://thecolbertreport.cc.com/videos/boejnl/heidi-cullen",
        "http://thecolbertreport.cc.com/videos/8mv6il/sign-off---calculator"
      ],
      "guest": "Andrew Hacker, Heidi Cullen"
    },
    {
      "date": "2010-08-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8g8jfw/intro---8-26-10",
        "http://thecolbertreport.cc.com/videos/cg8fb2/fox-news-job-opening",
        "http://thecolbertreport.cc.com/videos/3k8c17/glenn-livid",
        "http://thecolbertreport.cc.com/videos/ozbh2e/you-mosque-be-kidding",
        "http://thecolbertreport.cc.com/videos/idhto6/richard-engel",
        "http://thecolbertreport.cc.com/videos/054o86/sign-off---speaking-fee"
      ],
      "guest": "Richard Engel"
    },
    {
      "date": "2010-09-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/99y0f6/intro---9-7-10",
        "http://thecolbertreport.cc.com/videos/xvxdbg/geese-witherspoon",
        "http://thecolbertreport.cc.com/videos/os39h8/better-know-a-district---delaware-s-at-large---mike-castle-update",
        "http://thecolbertreport.cc.com/videos/ylp5nt/anthony-romero",
        "http://thecolbertreport.cc.com/videos/olfody/sign-off---welcome-home-show"
      ],
      "guest": "Anthony Romero"
    },
    {
      "date": "2010-09-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ynyu8x/intro---9-8-10",
        "http://thecolbertreport.cc.com/videos/kmgrcb/been-there--won-that---joe-biden---yogi-berra",
        "http://thecolbertreport.cc.com/videos/l21o2y/been-there--won-that---ray-odierno",
        "http://thecolbertreport.cc.com/videos/dp7uzb/joe-biden",
        "http://thecolbertreport.cc.com/videos/r1r2jw/sign-off---thanks-to-the-returning-troops"
      ],
      "guest": "Vice President Joe Biden, Gen. Raymond Odierno"
    },
    {
      "date": "2010-09-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/txd70l/been-there--won-that---jim-webb",
        "http://thecolbertreport.cc.com/videos/tvmzxz/been-there--won-that---david-petraeus",
        "http://thecolbertreport.cc.com/videos/9543jt/brent-cummings---josh-bleill"
      ],
      "guest": "Sen. Jim Webb, Lt. Col. Brent Cummings, John Legend"
    },
    {
      "date": "2010-09-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4q0lgz/intro---9-13-10",
        "http://thecolbertreport.cc.com/videos/1x4nj0/microwave-programming",
        "http://thecolbertreport.cc.com/videos/wzt5ev/bears---balls---american-apparel---chocolatey",
        "http://thecolbertreport.cc.com/videos/nwwxfb/stop-sending-live-animals",
        "http://thecolbertreport.cc.com/videos/hr5uxa/lisa-birnbach",
        "http://thecolbertreport.cc.com/videos/w7kfgs/sign-off---goodnight"
      ],
      "guest": "Lisa Birnbach"
    },
    {
      "date": "2010-09-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zipkzm/intro---9-14-10",
        "http://thecolbertreport.cc.com/videos/pet2x5/peta-criticizes-joe-biden",
        "http://thecolbertreport.cc.com/videos/7cbxuw/the-word---mutually-assured-coercion",
        "http://thecolbertreport.cc.com/videos/oh49ge/luther-campbell-opposes-ground-zero-mosque",
        "http://thecolbertreport.cc.com/videos/yevohc/sean-wilentz",
        "http://thecolbertreport.cc.com/videos/fugenz/sign-off---goodnight"
      ],
      "guest": "Sean Wilentz"
    },
    {
      "date": "2010-09-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0hpaxs/intro---9-15-10",
        "http://thecolbertreport.cc.com/videos/f8g0cq/libertea",
        "http://thecolbertreport.cc.com/videos/7v15m5/atone-phone---joan-rivers-calls",
        "http://thecolbertreport.cc.com/videos/n9nk9d/saul-griffith",
        "http://thecolbertreport.cc.com/videos/mjozqh/sign-off---world-changing-announcement"
      ],
      "guest": "Saul Griffith"
    },
    {
      "date": "2010-09-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uj8r4c/march-to-keep-fear-alive-announcement",
        "http://thecolbertreport.cc.com/videos/5klha6/threatdown---bedbugs---environmentalists---jerome-goddard",
        "http://thecolbertreport.cc.com/videos/pck634/lawrence-o-donnell",
        "http://thecolbertreport.cc.com/videos/h5yz8n/sign-off---march-to-keep-fear-alive"
      ],
      "guest": "Lawrence O'Donnell"
    },
    {
      "date": "2010-09-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cahpkw/intro---9-20-10",
        "http://thecolbertreport.cc.com/videos/1fmwjo/christine-o-donnell-witch-test",
        "http://thecolbertreport.cc.com/videos/diatjd/tip-wag---chilean-miners--portland-press-herald---isa-blyth",
        "http://thecolbertreport.cc.com/videos/a4y4ey/march-to-keep-fear-alive-media-coverage",
        "http://thecolbertreport.cc.com/videos/b65ofd/pavement"
      ],
      "guest": "Pavement"
    },
    {
      "date": "2010-09-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yi7cbo/intro---9-21-10",
        "http://thecolbertreport.cc.com/videos/t99up5/in-poor-taste---mark-shriver",
        "http://thecolbertreport.cc.com/videos/2vrsvg/colbertslist",
        "http://thecolbertreport.cc.com/videos/tnb3an/eric-schmidt",
        "http://thecolbertreport.cc.com/videos/kecowj/sign-off---sign-up-for-the-march-to-keep-fear-alive"
      ],
      "guest": "Eric Schmidt"
    },
    {
      "date": "2010-09-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q8xj8c/intro---9-22-10",
        "http://thecolbertreport.cc.com/videos/gcap67/the-christine-o-donnell-clip-predictor-3000",
        "http://thecolbertreport.cc.com/videos/xq0472/the-word---the-more-you-no",
        "http://thecolbertreport.cc.com/videos/xr7q4y/fallback-position---migrant-worker-pt--1",
        "http://thecolbertreport.cc.com/videos/kgnwdf/guillermo-del-toro",
        "http://thecolbertreport.cc.com/videos/lnpblj/sign-off---stephen-won-t-forgive-you"
      ],
      "guest": "Guillermo Del Toro"
    },
    {
      "date": "2010-09-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e9ulyf/intro---9-23-10",
        "http://thecolbertreport.cc.com/videos/puxqvp/fallback-position---migrant-worker-pt--2",
        "http://thecolbertreport.cc.com/videos/imp10g/sanchez-bump",
        "http://thecolbertreport.cc.com/videos/937jzh/oscar-goodman",
        "http://thecolbertreport.cc.com/videos/hitep1/sign-off---american-history-lesson"
      ],
      "guest": "Oscar Goodman"
    },
    {
      "date": "2010-09-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/esvw5v/intro---9-27-10",
        "http://thecolbertreport.cc.com/videos/aychpz/corn-packer-apology",
        "http://thecolbertreport.cc.com/videos/nc19il/the-delawert-report",
        "http://thecolbertreport.cc.com/videos/pcae92/the-word---army-of-mum",
        "http://thecolbertreport.cc.com/videos/kby55r/yahweh-or-no-way---ihop---antonio-federici-ad",
        "http://thecolbertreport.cc.com/videos/y2afey/ken-burns",
        "http://thecolbertreport.cc.com/videos/g2pys1/sign-off---goodnight"
      ],
      "guest": "Ken Burns"
    },
    {
      "date": "2010-09-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s437p7/intro---9-28-10",
        "http://thecolbertreport.cc.com/videos/gspyir/left-behind---paul-begala",
        "http://thecolbertreport.cc.com/videos/57ib6e/terror-a-new-one",
        "http://thecolbertreport.cc.com/videos/ut4vp1/ross-douthat",
        "http://thecolbertreport.cc.com/videos/0pm7c2/sign-off---democratic-grave"
      ],
      "guest": "Paul Begala, Ross Douthat"
    },
    {
      "date": "2010-09-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/umvy3w/march-to-keep-fear-alive-insanity-bus",
        "http://thecolbertreport.cc.com/videos/kup6co/the-word---original-spin",
        "http://thecolbertreport.cc.com/videos/z1c69t/threatdown---record-breaking-gays--koalas---purell",
        "http://thecolbertreport.cc.com/videos/q56zhc/steven-rattner",
        "http://thecolbertreport.cc.com/videos/kn5pkq/sign-off---sign-up-for-the-march-to-keep-fear-alive"
      ],
      "guest": "Steve Rattner"
    },
    {
      "date": "2010-09-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/umgd4n/intro---9-30-10",
        "http://thecolbertreport.cc.com/videos/xic7q8/president-obama-endorses-the-rally-to-restore-sanity",
        "http://thecolbertreport.cc.com/videos/xd5pkh/droid-rage",
        "http://thecolbertreport.cc.com/videos/w8i263/stat-of-the-union",
        "http://thecolbertreport.cc.com/videos/h7gmgz/aaron-sorkin",
        "http://thecolbertreport.cc.com/videos/7zrc6h/sign-off---march-to-keep-fear-alive-costumes"
      ],
      "guest": "Aaron Sorkin"
    },
    {
      "date": "2010-10-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vwiap8/intro---10-4-10",
        "http://thecolbertreport.cc.com/videos/h7fctl/we-world-war-won-it",
        "http://thecolbertreport.cc.com/videos/k8t4ao/the-word---it-s-a-small-minded-world",
        "http://thecolbertreport.cc.com/videos/nbdcz5/tip-wag---tea-party-coloring-book---calm-legislation",
        "http://thecolbertreport.cc.com/videos/pl2b2g/eugene-robinson",
        "http://thecolbertreport.cc.com/videos/3w0ogs/sign-off---matching-donor"
      ],
      "guest": "Eugene Robinson"
    },
    {
      "date": "2010-10-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/72j4yn/intro---10-5-10",
        "http://thecolbertreport.cc.com/videos/9xty22/american-sexual-habits",
        "http://thecolbertreport.cc.com/videos/0xyglo/gang-busters---john-burnett",
        "http://thecolbertreport.cc.com/videos/e4gleb/langur-monkey-security",
        "http://thecolbertreport.cc.com/videos/98qo87/leon-botstein",
        "http://thecolbertreport.cc.com/videos/gi2fk6/sign-off---goodnight"
      ],
      "guest": "Leon Botstein"
    },
    {
      "date": "2010-10-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pg4r1d/intro---10-6-10",
        "http://thecolbertreport.cc.com/videos/gu3bg9/tiny-triumphs---environmentalist-ear-pollution",
        "http://thecolbertreport.cc.com/videos/rex0nc/rawesome-foods-raid",
        "http://thecolbertreport.cc.com/videos/6krvaq/mavis-staples---jeff-tweedy",
        "http://thecolbertreport.cc.com/videos/01gaiu/sign-off---you-are-not-alone"
      ],
      "guest": "Mavis Staples &amp; Jeff Tweedy"
    },
    {
      "date": "2010-10-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/sy1j26/indecision-2010---revenge-of-the-fallen---fearstock-com",
        "http://thecolbertreport.cc.com/videos/5qjigz/proposition-19---joseph-califano---gary-johnson",
        "http://thecolbertreport.cc.com/videos/rzuziw/donorschoose-org-fear-drawings",
        "http://thecolbertreport.cc.com/videos/077dy4/davis-guggenheim",
        "http://thecolbertreport.cc.com/videos/th4oe4/sign-off---don-t-go-to-donorschoose-com"
      ],
      "guest": "Davis Guggenheim"
    },
    {
      "date": "2010-10-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mnxgqn/intro---10-11-10",
        "http://thecolbertreport.cc.com/videos/2buyr8/rich-iott-wears-a-nazi-uniform",
        "http://thecolbertreport.cc.com/videos/f1n1ah/threatdown---muslim-edition",
        "http://thecolbertreport.cc.com/videos/6x3w7h/formula-4-your-eyes-only",
        "http://thecolbertreport.cc.com/videos/l23gil/robert-reich",
        "http://thecolbertreport.cc.com/videos/6314hj/sign-off---stephen-needs-a-place-to-hold-his-march"
      ],
      "guest": "Robert Reich"
    },
    {
      "date": "2010-10-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ksbkyk/intro---10-12-10",
        "http://thecolbertreport.cc.com/videos/que3dz/101-year-old-woman-becomes-a-u-s--citizen",
        "http://thecolbertreport.cc.com/videos/xpawsw/tip-wag---peabody-public-schools--andy-rooney---ground-zero-mosque-design",
        "http://thecolbertreport.cc.com/videos/o656bc/merch-to-keep-fear-alive",
        "http://thecolbertreport.cc.com/videos/bncunr/brendan-steinhauser",
        "http://thecolbertreport.cc.com/videos/4i1iy2/sign-off---apple-filled-with-razor-blades"
      ],
      "guest": "Brendan Steinhauser"
    },
    {
      "date": "2010-10-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nkf1gw/intro---10-13-10",
        "http://thecolbertreport.cc.com/videos/40azz5/america-helps-rescue-chilean-miners",
        "http://thecolbertreport.cc.com/videos/fg5dcw/sport-report---steroids--commonwealth-games---brett-favre-s-sexting",
        "http://thecolbertreport.cc.com/videos/nq3g54/tax-shelter-skelter",
        "http://thecolbertreport.cc.com/videos/ip94pd/austan-goolsbee",
        "http://thecolbertreport.cc.com/videos/7n0fzv/sign-off---tic-tac-toe-with-austan-goolsbee"
      ],
      "guest": "Austan Goolsbee"
    },
    {
      "date": "2010-10-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ke3ug4/transitive-property-of-christine-o-donnell",
        "http://thecolbertreport.cc.com/videos/jvi6id/people-who-are-destroying-america---landscaping-goats",
        "http://thecolbertreport.cc.com/videos/8kgt7i/rally-to-restore-sanity-and-or-fear-chinatown-bus-tickets",
        "http://thecolbertreport.cc.com/videos/wc2nwv/bill-bryson",
        "http://thecolbertreport.cc.com/videos/ns0u0b/sign-off---oprah-is-wonderful"
      ],
      "guest": "Bill Bryson"
    },
    {
      "date": "2010-10-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ou6z90/indecision-2010---revenge-of-the-fallen---sean-bielat---ken-buck",
        "http://thecolbertreport.cc.com/videos/t96zw6/the-word---midterm-erection",
        "http://thecolbertreport.cc.com/videos/r3cpem/who-s-honoring-me-now----colbert-nation-five-years-of-excellence-award",
        "http://thecolbertreport.cc.com/videos/tx8w6w/nicholas-negroponte",
        "http://thecolbertreport.cc.com/videos/hjbcjo/sign-off---fifth-anniversary-portrait"
      ],
      "guest": "Nicholas Negroponte"
    },
    {
      "date": "2010-10-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vtn4dg/intro---10-26-10",
        "http://thecolbertreport.cc.com/videos/upm6ow/stephen-appears-in-the-new-york-times-crossword-puzzle",
        "http://thecolbertreport.cc.com/videos/rh943m/the-word---invisible-inc-",
        "http://thecolbertreport.cc.com/videos/57deny/food-insurance-insurance",
        "http://thecolbertreport.cc.com/videos/9dol4n/garry-wills",
        "http://thecolbertreport.cc.com/videos/ifnetg/sign-off---stream-elvis-costello-s-national-ransom"
      ],
      "guest": "Gary Wills"
    },
    {
      "date": "2010-10-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qjfe6u/exclusive---have-you-seen-the-ghost-of-jon-",
        "http://thecolbertreport.cc.com/videos/iyha0d/intro---10-27-10",
        "http://thecolbertreport.cc.com/videos/a393lf/rand-paul-supporter-stomps-on-liberal-activist-s-head",
        "http://thecolbertreport.cc.com/videos/ah47vl/indecision-2010---revenge-of-the-fallen---tom-perriello",
        "http://thecolbertreport.cc.com/videos/k3z37d/snooki-halloween-costume---spooky-rally-song",
        "http://thecolbertreport.cc.com/videos/tmruw9/apolo-ohno",
        "http://thecolbertreport.cc.com/videos/g0i5r2/sign-off---2010-election-map-from-denny-s"
      ],
      "guest": "Rep. Tom Perriello, Apolo Anton Ohno"
    },
    {
      "date": "2010-10-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ea746g/the-mcrib-is-back",
        "http://thecolbertreport.cc.com/videos/y2nj3n/fear-for-all-pt--1",
        "http://thecolbertreport.cc.com/videos/ttx9jf/fear-for-all-pt--2",
        "http://thecolbertreport.cc.com/videos/el1mv0/maira-kalman",
        "http://thecolbertreport.cc.com/videos/p6c0ah/sign-off---see-you-at-the-rally"
      ],
      "guest": "Maira Kalman"
    },
    {
      "date": "2010-11-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4or1uk/intro---11-1-10",
        "http://thecolbertreport.cc.com/videos/pjth2k/a-fond-look-back-at-the-rally",
        "http://thecolbertreport.cc.com/videos/6y87u2/midterm-senate-races---nevada--alaska---delaware",
        "http://thecolbertreport.cc.com/videos/ghbjcp/hispanic-and-gay-voters-should-stay-at-home",
        "http://thecolbertreport.cc.com/videos/r4udbe/jonathan-alter",
        "http://thecolbertreport.cc.com/videos/h06l8n/sign-off---don-t-forget-to-vote"
      ],
      "guest": "Jonathan Alter"
    },
    {
      "date": "2010-11-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q6wjad/indecision-2010---intro---11-2-10",
        "http://thecolbertreport.cc.com/videos/5y5ul8/indecision-2010---gop-takes-house",
        "http://thecolbertreport.cc.com/videos/yubkdk/indecision-2010---david-frum",
        "http://thecolbertreport.cc.com/videos/ii11zs/indecision-2010---katrina-vanden-heuvel",
        "http://thecolbertreport.cc.com/videos/fpxe9g/indecision-2010---sign-off---election-to-end-all-elections"
      ],
      "guest": "Katrina vanden Heuvel, David Frum"
    },
    {
      "date": "2010-11-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/npkdbl/intro---11-3-10",
        "http://thecolbertreport.cc.com/videos/dnol9b/we-hardly-better-knew-ye",
        "http://thecolbertreport.cc.com/videos/tsa7r8/stephen-colbert-gives-you-props",
        "http://thecolbertreport.cc.com/videos/g1n60y/doris-kearns-goodwin",
        "http://thecolbertreport.cc.com/videos/0ciqy7/sign-off---smiley-face-balloon"
      ],
      "guest": "Doris Kearns Goodwin"
    },
    {
      "date": "2010-11-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ze4pgk/intro---11-4-10",
        "http://thecolbertreport.cc.com/videos/jssup2/spider-man-is-alaska-s-write-in-candidate",
        "http://thecolbertreport.cc.com/videos/59l5bf/tip-wag---tsa--bert---dogs",
        "http://thecolbertreport.cc.com/videos/px319n/elvis-costello"
      ],
      "guest": "Elvis Costello"
    },
    {
      "date": "2010-11-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bf24qu/one-hour-in-the-future",
        "http://thecolbertreport.cc.com/videos/odml1w/the-word---nothingness",
        "http://thecolbertreport.cc.com/videos/450kbl/president-obama-s-expensive-trip-to-india",
        "http://thecolbertreport.cc.com/videos/itfuo6/reza-aslan",
        "http://thecolbertreport.cc.com/videos/flh0gj/sign-off---battleship"
      ],
      "guest": "Reza Aslan"
    },
    {
      "date": "2010-11-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ndicnt/decision-points",
        "http://thecolbertreport.cc.com/videos/t6dluv/house-oversight-committee-hearings---abbe-lowell",
        "http://thecolbertreport.cc.com/videos/2tsnui/craziest-f--king-thing-i-ve-ever-heard---crab-vending-machines",
        "http://thecolbertreport.cc.com/videos/thu56b/cee-lo-green"
      ],
      "guest": "Cee-Lo Green"
    },
    {
      "date": "2010-11-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r8nn6k/michelle-obama-s-embarrassing-handshake",
        "http://thecolbertreport.cc.com/videos/h0bv7g/america-s-job-loss---beri-fox",
        "http://thecolbertreport.cc.com/videos/qra7vl/statue-of-jesus",
        "http://thecolbertreport.cc.com/videos/0cxark/martha-stewart",
        "http://thecolbertreport.cc.com/videos/gd9t0s/sign-off---saltine-hors-d-oeuvres"
      ],
      "guest": "Martha Stewart"
    },
    {
      "date": "2010-11-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vavqn0/colbert-platinum---kanye-west---million-dollar-advent-calendar-segment",
        "http://thecolbertreport.cc.com/videos/6py8bn/intro---11-11-10",
        "http://thecolbertreport.cc.com/videos/6obewf/stephen-absorbs-gene-shalit-s-opinions",
        "http://thecolbertreport.cc.com/videos/pigos8/colbert-platinum---kanye-west---million-dollar-advent-calendar",
        "http://thecolbertreport.cc.com/videos/8zchd5/stephen-trademarks-dated-catchphrases",
        "http://thecolbertreport.cc.com/videos/opi39p/quincy-jones",
        "http://thecolbertreport.cc.com/videos/dlv5sb/sign-off---if-it-walks-like-a-duck"
      ],
      "guest": "Quincy Jones"
    },
    {
      "date": "2010-11-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zwpnzb/finding-mr--goodwrench",
        "http://thecolbertreport.cc.com/videos/dzeed3/tsa-full-body-scanners---jeffrey-goldberg",
        "http://thecolbertreport.cc.com/videos/yi115x/garfield-and-president-obama-s-veterans-day-controversies",
        "http://thecolbertreport.cc.com/videos/zgerlg/david-stern",
        "http://thecolbertreport.cc.com/videos/f5nt0v/sign-off---garfield-loves-veterans"
      ],
      "guest": "David Stern"
    },
    {
      "date": "2010-11-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a6jx8i/intro---11-16-10",
        "http://thecolbertreport.cc.com/videos/r1nlt4/prince-william-proposes-to-kate-middleton",
        "http://thecolbertreport.cc.com/videos/6x0tmp/thought-for-food---c-zurrrre--medal-of-hunger-winner---cheesercize",
        "http://thecolbertreport.cc.com/videos/5n8eoi/stephen-colbert-s-report",
        "http://thecolbertreport.cc.com/videos/brwtip/john-legend"
      ],
      "guest": "John Legend"
    },
    {
      "date": "2010-11-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/13lnab/intro---11-17-10",
        "http://thecolbertreport.cc.com/videos/bzhpi2/charlie-rangel--you-got-mailed",
        "http://thecolbertreport.cc.com/videos/izlih7/old-people-in-space",
        "http://thecolbertreport.cc.com/videos/rhup4k/chair-apparent",
        "http://thecolbertreport.cc.com/videos/x10udl/ian-frazier",
        "http://thecolbertreport.cc.com/videos/iu8jdu/synchronize-watches-to-colbert-time"
      ],
      "guest": "Ian Frazier"
    },
    {
      "date": "2010-11-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rip59b/stephen-pardons-joseph-gobbles",
        "http://thecolbertreport.cc.com/videos/6dqu0c/tip-wag---pope-benedict-xvi--trick-play---joseph-gobbles",
        "http://thecolbertreport.cc.com/videos/fbks4j/joseph-gobbles-shoots-jay-the-intern",
        "http://thecolbertreport.cc.com/videos/9ldbp0/salvatore-giunta",
        "http://thecolbertreport.cc.com/videos/92wwov/sign-off---happy-thanksgiving"
      ],
      "guest": "Staff Sgt. Salvatore Giunta"
    },
    {
      "date": "2010-11-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fyh8jk/intro---11-29-10",
        "http://thecolbertreport.cc.com/videos/5liwl3/black-friday-interpretation",
        "http://thecolbertreport.cc.com/videos/qhebrf/better-business-hero",
        "http://thecolbertreport.cc.com/videos/1fhpey/dan-savage",
        "http://thecolbertreport.cc.com/videos/nilxac/sign-off---goodnight"
      ],
      "guest": "Dan Savage"
    },
    {
      "date": "2010-11-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0th7i0/god-drops-steve-johnson-s-football-pass",
        "http://thecolbertreport.cc.com/videos/rd3bzl/wikileaks-document-dump---james-rubin",
        "http://thecolbertreport.cc.com/videos/t2kayc/soap-opera-product-placement",
        "http://thecolbertreport.cc.com/videos/5qjkay/tom-vilsack",
        "http://thecolbertreport.cc.com/videos/ovt98b/sign-off---chex-mix-product-placement"
      ],
      "guest": "Tom Vilsack"
    },
    {
      "date": "2010-12-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/373wri/return-of-the-estate-tax",
        "http://thecolbertreport.cc.com/videos/hml13u/lame-duck-congress---jake-tapper",
        "http://thecolbertreport.cc.com/videos/df8z4y/cheating-death---calming-meat-goggles---the-ithrone",
        "http://thecolbertreport.cc.com/videos/hbifbv/michelle-rhee",
        "http://thecolbertreport.cc.com/videos/5oq9dq/sign-off---up-on-the-lingo"
      ],
      "guest": "Michelle Rhee"
    },
    {
      "date": "2010-12-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d067b7/intro---12-2-10",
        "http://thecolbertreport.cc.com/videos/y4fa8v/john-thune-looks-presidential",
        "http://thecolbertreport.cc.com/videos/vaqkqk/the-word---the-great-white-wail",
        "http://thecolbertreport.cc.com/videos/efh5u1/the-blitzkrieg-on-grinchitude---atheist-billboard---capitol-christmas-tree",
        "http://thecolbertreport.cc.com/videos/trmu6j/david-stockman",
        "http://thecolbertreport.cc.com/videos/v9n94y/sign-off---chinese-finger-trap"
      ],
      "guest": "David Stockman"
    },
    {
      "date": "2010-12-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/exzvsm/cosmo-is-available-in-mongolia",
        "http://thecolbertreport.cc.com/videos/bwubcy/the-word---unrequited-gov",
        "http://thecolbertreport.cc.com/videos/eoidl7/mysteries-of-the-ancient-unknown---the-pursuit-of-the-pharaoh-s-phallus-pt--1",
        "http://thecolbertreport.cc.com/videos/wdodc8/garry-trudeau",
        "http://thecolbertreport.cc.com/videos/gktluk/sign-off---goodnight"
      ],
      "guest": "Garry Trudeau"
    },
    {
      "date": "2010-12-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ishllr/extension-of-the-bush-tax-cuts",
        "http://thecolbertreport.cc.com/videos/n0u86v/mysteries-of-the-ancient-unknown---the-pursuit-of-the-pharaoh-s-phallus-pt--2",
        "http://thecolbertreport.cc.com/videos/ya6qw9/poll-to-repeal-don-t-ask--don-t-tell",
        "http://thecolbertreport.cc.com/videos/gf8r28/david-eisenhower---julie-nixon-eisenhower",
        "http://thecolbertreport.cc.com/videos/99syt9/sign-off---goodnight"
      ],
      "guest": "Julie Nixon Eisenhower &amp; David Eisenhower"
    },
    {
      "date": "2010-12-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f6likw/exclusive---steve-martin-extended-segment",
        "http://thecolbertreport.cc.com/videos/kml8x8/tip-wag---art-edition---brent-glass",
        "http://thecolbertreport.cc.com/videos/2akwcg/steve-martin-pt--1",
        "http://thecolbertreport.cc.com/videos/yqcbtk/steve-martin-pt--2",
        "http://thecolbertreport.cc.com/videos/ct0ud7/sign-off---steve-martin-mask"
      ],
      "guest": "Steve Martin"
    },
    {
      "date": "2010-12-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/znivka/israel-shark-conspiracy",
        "http://thecolbertreport.cc.com/videos/fi19uy/international-manhunt-for-julian-assange---daniel-ellsberg",
        "http://thecolbertreport.cc.com/videos/fk2pnu/art-stephen-up-challenge---william-wegman",
        "http://thecolbertreport.cc.com/videos/1akto9/julie-taymor",
        "http://thecolbertreport.cc.com/videos/hcd55s/sign-off---christmas-party"
      ],
      "guest": "Julie Taymor"
    },
    {
      "date": "2010-12-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f2kl6o/intro---12-13-10",
        "http://thecolbertreport.cc.com/videos/eolk50/found-goldman-sachs-mastercard",
        "http://thecolbertreport.cc.com/videos/c1yv8b/the-word---swift-payment",
        "http://thecolbertreport.cc.com/videos/btsd4o/blitzkrieg-on-grinchitude---gretchen-carlson---christian-nation-christ-mas-tree",
        "http://thecolbertreport.cc.com/videos/rufuhr/patti-smith",
        "http://thecolbertreport.cc.com/videos/t0590z/sign-off---remembering-richard-holbrooke"
      ],
      "guest": "Patti Smith"
    },
    {
      "date": "2010-12-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ycermm/goldman-sachs-lawyers-want-buckley-t--ratchford-s-card-back",
        "http://thecolbertreport.cc.com/videos/rsdutw/prop-8-challenge---david-boies",
        "http://thecolbertreport.cc.com/videos/4tx5ks/stephen-wins-twitter---biz-stone",
        "http://thecolbertreport.cc.com/videos/ouqrnm/stephen-sondheim",
        "http://thecolbertreport.cc.com/videos/ajg2h0/sign-off---closing-credits"
      ],
      "guest": "David Boies, Stephen Sondheim"
    },
    {
      "date": "2010-12-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9gi4ae/intro---12-15-10",
        "http://thecolbertreport.cc.com/videos/67nfxh/scanner-defying-pancakes",
        "http://thecolbertreport.cc.com/videos/fv3gl9/world-war-3-0---omar-wasow",
        "http://thecolbertreport.cc.com/videos/rr8wvk/tiny-triumphs---lethal-drug-shortage",
        "http://thecolbertreport.cc.com/videos/e05lny/laird-hamilton",
        "http://thecolbertreport.cc.com/videos/nv267b/sign-off---winter-fashion-tip"
      ],
      "guest": "Omar Wasow, Laird Hamilton"
    },
    {
      "date": "2010-12-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cb861t/christmas-holy-week",
        "http://thecolbertreport.cc.com/videos/m38gcf/jesus-is-a-liberal-democrat",
        "http://thecolbertreport.cc.com/videos/tvxon5/amy-sedaris",
        "http://thecolbertreport.cc.com/videos/zejxdk/paul-simon"
      ],
      "guest": "Amy Sedaris, Paul Simon"
    }
  ],
  "2011": [
    {
      "date": "2011-01-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a5rzlq/intro---1-3-11",
        "http://thecolbertreport.cc.com/videos/pgayak/snowpocalypse-2010",
        "http://thecolbertreport.cc.com/videos/7b084t/tip-wag---susan-g--komen-foundation---spider-man-musical",
        "http://thecolbertreport.cc.com/videos/44ybv8/the-enemy-within---caboodle-ranch",
        "http://thecolbertreport.cc.com/videos/vopb2f/ed-rendell",
        "http://thecolbertreport.cc.com/videos/bvg4tu/sign-off---home-improvement-tip"
      ],
      "guest": "Sen. Bernie Sanders"
    },
    {
      "date": "2011-01-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/40y983/intro---1-4-11",
        "http://thecolbertreport.cc.com/videos/tq4xo3/native-american-overlords",
        "http://thecolbertreport.cc.com/videos/kafccc/gold-faithful",
        "http://thecolbertreport.cc.com/videos/0ds0c9/gold-faithful---ron-paul---david-leonhardt",
        "http://thecolbertreport.cc.com/videos/leatvt/geoffrey-canada",
        "http://thecolbertreport.cc.com/videos/h983ts/sign-off---12-dutchmen-answer"
      ],
      "guest": "John Heilemann"
    },
    {
      "date": "2011-01-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/upvgg0/intro---1-5-11",
        "http://thecolbertreport.cc.com/videos/ttqn4k/huckleberry-finn-censorship",
        "http://thecolbertreport.cc.com/videos/4c01zx/what-s-a-reince-priebus-",
        "http://thecolbertreport.cc.com/videos/d2586v/yellowline-international--inc-",
        "http://thecolbertreport.cc.com/videos/1yfs5a/atul-gawande",
        "http://thecolbertreport.cc.com/videos/ta25ww/sign-off---dark-side-of-the-moon"
      ],
      "guest": "Steve Case"
    },
    {
      "date": "2011-01-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gfffz6/shout-out-to-arby-s",
        "http://thecolbertreport.cc.com/videos/g7dtso/john-boehner-s-large-gavel",
        "http://thecolbertreport.cc.com/videos/t27er5/cheating-death---placebo-effect--immortality---wild-lynx",
        "http://thecolbertreport.cc.com/videos/n6wqjn/bill-o-reilly-proves-god-s-existence---neil-degrasse-tyson",
        "http://thecolbertreport.cc.com/videos/i48v1q/ronald-depinho",
        "http://thecolbertreport.cc.com/videos/x8bqqt/sign-off---boris-the-lynx"
      ],
      "guest": "Dr. Ronald DePinho"
    },
    {
      "date": "2011-01-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qi5a0o/intro---1-10-11",
        "http://thecolbertreport.cc.com/videos/xl3r2n/pundits-lay-blame-for-senseless-arizona-attack",
        "http://thecolbertreport.cc.com/videos/6s01yh/bull-sessions",
        "http://thecolbertreport.cc.com/videos/cng4n9/difference-makers---galactic-edition-pt--1",
        "http://thecolbertreport.cc.com/videos/oelxfx/difference-makers---galactic-edition-pt--2",
        "http://thecolbertreport.cc.com/videos/gk32r8/fen-montaigne",
        "http://thecolbertreport.cc.com/videos/oslcyl/sign-off---goodnight"
      ],
      "guest": "Fen Montaigne"
    },
    {
      "date": "2011-01-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/97pzie/intro---1-11-11",
        "http://thecolbertreport.cc.com/videos/q63emf/snowstorm-preparation",
        "http://thecolbertreport.cc.com/videos/rbg8gh/metunes---grammy-vote---dan-auerbach--patrick-carney---ezra-koenig",
        "http://thecolbertreport.cc.com/videos/oqami3/lithuania-perfume",
        "http://thecolbertreport.cc.com/videos/mqh8rb/chris-hughes",
        "http://thecolbertreport.cc.com/videos/8re8oa/sign-off---pringles"
      ],
      "guest": "Chris Hughes"
    },
    {
      "date": "2011-01-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1aza8n/50-cent-makes-money-on-twitter",
        "http://thecolbertreport.cc.com/videos/b4mxvn/the-word---life--liberty-and-the-pursuit-of-angriness",
        "http://thecolbertreport.cc.com/videos/56kjjw/bernard-henri-levy-pt--1",
        "http://thecolbertreport.cc.com/videos/cmxyxs/bernard-henri-levy-pt--2",
        "http://thecolbertreport.cc.com/videos/splrfl/sign-off---goodnight"
      ],
      "guest": "Bernard-Henri Levy"
    },
    {
      "date": "2011-01-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h5qwzv/hitler-s-inspiring-tucson-memorial-speech",
        "http://thecolbertreport.cc.com/videos/nhx7bu/thought-for-food---fruit-pouch--doritos-ad---super-big-gulp",
        "http://thecolbertreport.cc.com/videos/wdqdqn/israeli-vulture-spy",
        "http://thecolbertreport.cc.com/videos/xczq8w/kevin-spacey",
        "http://thecolbertreport.cc.com/videos/iyyhr8/sign-off---new-york-post"
      ],
      "guest": "Kevin Spacey"
    },
    {
      "date": "2011-01-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iuhos5/intro---1-17-11",
        "http://thecolbertreport.cc.com/videos/ztaz7m/martin-luther-king-jr--day-sales",
        "http://thecolbertreport.cc.com/videos/9ycstf/the-word---run-for-your-life",
        "http://thecolbertreport.cc.com/videos/ib4cpu/art-stephen-up-challenge---wade-hampton",
        "http://thecolbertreport.cc.com/videos/kd5rmr/sherry-turkle",
        "http://thecolbertreport.cc.com/videos/tj76rr/sign-off---new-york-post"
      ],
      "guest": "Sherry Turkle"
    },
    {
      "date": "2011-01-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fi5nk7/intro---1-18-11",
        "http://thecolbertreport.cc.com/videos/y6lk8z/mika-brzezinski-experiences-palin-fatigue",
        "http://thecolbertreport.cc.com/videos/1zj4bl/the-word---disintegration",
        "http://thecolbertreport.cc.com/videos/l4vdiw/coma-cozy",
        "http://thecolbertreport.cc.com/videos/zeukt7/cornel-west",
        "http://thecolbertreport.cc.com/videos/njlf77/sign-off---coma-cozy"
      ],
      "guest": "Cornel West"
    },
    {
      "date": "2011-01-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4e1xmn/intro---1-19-11",
        "http://thecolbertreport.cc.com/videos/0s8rfq/black-tie-dinner-for-hu-jintao",
        "http://thecolbertreport.cc.com/videos/nujiex/tip-wag---four-loko---horoscopes",
        "http://thecolbertreport.cc.com/videos/vb8d7c/shout-out---preston-pysh",
        "http://thecolbertreport.cc.com/videos/czmy3b/ron-reagan",
        "http://thecolbertreport.cc.com/videos/0ycmn7/sign-off---i-eat-america--and-so-can-you---recall"
      ],
      "guest": "Ron Reagan Jr."
    },
    {
      "date": "2011-01-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/091ydv/rush-limbaugh-speaks-chinese",
        "http://thecolbertreport.cc.com/videos/bq6mnl/state-budget-shortfalls---christine-todd-whitman",
        "http://thecolbertreport.cc.com/videos/c8u4qm/50th-anniversary-of-jfk-s-inaugural-address",
        "http://thecolbertreport.cc.com/videos/6pfgfg/chris-matthews",
        "http://thecolbertreport.cc.com/videos/jjup5d/sign-off---donald-pellview"
      ],
      "guest": "Chris Matthews"
    },
    {
      "date": "2011-01-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z2h5xs/intro---1-24-11",
        "http://thecolbertreport.cc.com/videos/ry0uh0/stephen-rejects-keith-olbermann-s-power",
        "http://thecolbertreport.cc.com/videos/e7bfej/the-word---coverage-of-denial",
        "http://thecolbertreport.cc.com/videos/mjnoqk/art-stephen-up-challenge---banksy",
        "http://thecolbertreport.cc.com/videos/rsyf0v/charlie-rose",
        "http://thecolbertreport.cc.com/videos/v0sh08/sign-off---keith-olbermug"
      ],
      "guest": "Charlie Rose"
    },
    {
      "date": "2011-01-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1mhey7/intro---1-25-11",
        "http://thecolbertreport.cc.com/videos/d21szi/the--battle-hymn-of-the-tiger-mother--controversy",
        "http://thecolbertreport.cc.com/videos/5198pt/threatdown---radical-muslim-snacks--flying-robot-drones---coked-up-vacuums",
        "http://thecolbertreport.cc.com/videos/ooebba/nazi-ometer",
        "http://thecolbertreport.cc.com/videos/2lr90o/amy-chua",
        "http://thecolbertreport.cc.com/videos/71c1bx/sign-off---stephen-welcomes-cody-price"
      ],
      "guest": "Amy Chua"
    },
    {
      "date": "2011-01-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/99necf/anonymous-insider-author-speculation",
        "http://thecolbertreport.cc.com/videos/d2sy94/obama-s-state-of-the-union-address---michael-waldman",
        "http://thecolbertreport.cc.com/videos/za0351/mr--smith-goes-to-the-state-legislature--then-later-possibly-washington---curtis-oda",
        "http://thecolbertreport.cc.com/videos/wja66h/christine-yvette-lewis",
        "http://thecolbertreport.cc.com/videos/7znx6n/sign-off---man-handler---fork-phone"
      ],
      "guest": "Michael Waldman, Christine Yvette Lewis"
    },
    {
      "date": "2011-01-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fllqqg/intro---1-27-11",
        "http://thecolbertreport.cc.com/videos/959fok/candyquake",
        "http://thecolbertreport.cc.com/videos/bhf8jv/time-traveling-porn---daryl-bem",
        "http://thecolbertreport.cc.com/videos/uffqf8/gordita-supreme-court",
        "http://thecolbertreport.cc.com/videos/zgxlja/brian-greene",
        "http://thecolbertreport.cc.com/videos/nkbrns/sign-off---goodnight"
      ],
      "guest": "Dr. Daryl Bem, Brian Greene"
    },
    {
      "date": "2011-01-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2wwddt/intro---1-31-11",
        "http://thecolbertreport.cc.com/videos/uv1y3k/mubarak--mu-problems",
        "http://thecolbertreport.cc.com/videos/w70tw3/mubarak--mu-problems---samer-shehata",
        "http://thecolbertreport.cc.com/videos/35ink0/paul-offit",
        "http://thecolbertreport.cc.com/videos/ccilnn/sign-off---kim-jong-bear"
      ],
      "guest": "Samer Shehata, Dr. Paul Offit"
    },
    {
      "date": "2011-02-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wk9d57/hosni-mubarak-will-not-run-again",
        "http://thecolbertreport.cc.com/videos/ie8q6j/thought-for-food---nestle-corporation",
        "http://thecolbertreport.cc.com/videos/2ucxw7/thought-for-food---wyngz---wal-mart",
        "http://thecolbertreport.cc.com/videos/odeko3/wal-mart-collaborates-with-obama-administration---leslie-dach",
        "http://thecolbertreport.cc.com/videos/4shxg7/michael-lewis",
        "http://thecolbertreport.cc.com/videos/s7oggh/sign-off---digiorno-pizza---boneless-wyngz"
      ],
      "guest": "Leslie Dach, Michael Lewis"
    },
    {
      "date": "2011-02-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zdhdko/intro---2-2-11",
        "http://thecolbertreport.cc.com/videos/ct2jwf/bing-gets-served",
        "http://thecolbertreport.cc.com/videos/a4bw27/cairo-turns-into-the-jersey-shore",
        "http://thecolbertreport.cc.com/videos/q27618/crisis-in-egypt",
        "http://thecolbertreport.cc.com/videos/yjimo0/tip-wag---british-superman---big-flats-beer",
        "http://thecolbertreport.cc.com/videos/dme3nu/sean-dorrance-kelly",
        "http://thecolbertreport.cc.com/videos/n2upjg/sign-off---christiane-aman-purr---big-flats-beer"
      ],
      "guest": "Sean Kelly"
    },
    {
      "date": "2011-02-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nn8o94/intro---2-3-11",
        "http://thecolbertreport.cc.com/videos/lo20rh/crisis-in-egypt---anderson-cooper---bill-o-reilly",
        "http://thecolbertreport.cc.com/videos/vuogyk/sport-report---super-bowl-edition",
        "http://thecolbertreport.cc.com/videos/91t3tp/affirmative-reaction",
        "http://thecolbertreport.cc.com/videos/i5rwqs/jane-mcgonigal",
        "http://thecolbertreport.cc.com/videos/hffd6m/sign-off---newest-member-of-the-colbert-nation"
      ],
      "guest": "Jane McGonigal"
    },
    {
      "date": "2011-02-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kruhy0/intro---2-14-11",
        "http://thecolbertreport.cc.com/videos/4drnjr/mysteries-of-the-ancient-unknown---egyptian-coincidence",
        "http://thecolbertreport.cc.com/videos/gv0hvh/the-enemy-within---toddler-edition",
        "http://thecolbertreport.cc.com/videos/qtecuk/james-murphy-of-lcd-soundsystem",
        "http://thecolbertreport.cc.com/videos/4qawhf/sign-off---scoops-of-americone-dream"
      ],
      "guest": "LCD Soundsystem"
    },
    {
      "date": "2011-02-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ynf8rd/intro---2-15-11",
        "http://thecolbertreport.cc.com/videos/sjuyr9/italian-bunga-bunga-parties---egyptian-democracy",
        "http://thecolbertreport.cc.com/videos/ara6q6/egyptian-democracy---christiane-amanpour",
        "http://thecolbertreport.cc.com/videos/n9a7wj/mr--smith-goes-to-the-state-legislature--then-later-possibly-washington---ron-gould",
        "http://thecolbertreport.cc.com/videos/uobmig/david-albright",
        "http://thecolbertreport.cc.com/videos/95itm9/sign-off---christiane-aman-purr-s-safari-suit"
      ],
      "guest": "Christiane Amanpour, David Albright"
    },
    {
      "date": "2011-02-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bbqm6g/intro---2-16-11",
        "http://thecolbertreport.cc.com/videos/bojft9/republican-voters-doubt-obama-s-american-citizenship",
        "http://thecolbertreport.cc.com/videos/uk8a3q/tip-wag---colbuffington-re-post--repo-games---whale-fail",
        "http://thecolbertreport.cc.com/videos/8r9j45/murdoch-he-wrote",
        "http://thecolbertreport.cc.com/videos/re8ih2/eric-foner",
        "http://thecolbertreport.cc.com/videos/i84xxd/sign-off---general-butterbean"
      ],
      "guest": "Eric Foner"
    },
    {
      "date": "2011-02-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/62enfw/the-huffington-post-posts-about-the-colbuffington-re-post",
        "http://thecolbertreport.cc.com/videos/yjsn8n/clarence-thomas-s-financial-disclosure-controversy",
        "http://thecolbertreport.cc.com/videos/tvwda6/project-magazine-cover-boy",
        "http://thecolbertreport.cc.com/videos/sjlg3t/jeffrey-leonard",
        "http://thecolbertreport.cc.com/videos/m0qkxm/sign-off---project-magazine-cover"
      ],
      "guest": "Jeffrey Leonard"
    },
    {
      "date": "2011-02-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/86hqgf/turmoil-in-the-middle-east---turmoil-in-the-middle-west",
        "http://thecolbertreport.cc.com/videos/lp0v0e/cheating-death---ablibalify---bing-bongavax",
        "http://thecolbertreport.cc.com/videos/fwkicl/rick-santorum-internet-search",
        "http://thecolbertreport.cc.com/videos/8du0y6/eugene-jarecki",
        "http://thecolbertreport.cc.com/videos/58iq33/sign-off---goodnight"
      ],
      "guest": "Eugene Jarecki"
    },
    {
      "date": "2011-02-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bqnw4a/intro---2-22-11",
        "http://thecolbertreport.cc.com/videos/bm2a1j/a-less-perfect-union",
        "http://thecolbertreport.cc.com/videos/usnwve/a-less-perfect-union---randi-weingarten",
        "http://thecolbertreport.cc.com/videos/f6avpd/wisco-inferno---jon-erpenbach",
        "http://thecolbertreport.cc.com/videos/p92sec/bing-west",
        "http://thecolbertreport.cc.com/videos/2kp9tj/sign-off---democrat-call"
      ],
      "guest": "Randi Weingarten, Bing West"
    },
    {
      "date": "2011-02-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pd1kio/intro---2-23-11",
        "http://thecolbertreport.cc.com/videos/883h13/usa-today-infographic-sells-out",
        "http://thecolbertreport.cc.com/videos/fn2n7y/bust-in-show",
        "http://thecolbertreport.cc.com/videos/tnaq8e/nailed--em---mark-burdett",
        "http://thecolbertreport.cc.com/videos/iap6wk/stephanie-coontz",
        "http://thecolbertreport.cc.com/videos/uyxtz0/sign-off---rebroadcasts"
      ],
      "guest": "Stephanie Coontz"
    },
    {
      "date": "2011-02-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7a9kp1/era-of-american-dental-exceptionalism-is-over",
        "http://thecolbertreport.cc.com/videos/xjtazd/corporate-hacker-tries-to-take-down-wikileaks",
        "http://thecolbertreport.cc.com/videos/8jruu4/corporate-hacker-tries-to-take-down-wikileaks---glenn-greenwald",
        "http://thecolbertreport.cc.com/videos/tyiacl/republicans-flirt-with-presidential-candidacy",
        "http://thecolbertreport.cc.com/videos/hxtqey/mike-huckabee",
        "http://thecolbertreport.cc.com/videos/6ahql2/sign-off---elephant-beat"
      ],
      "guest": "Glenn Greenwald, Mike Huckabee"
    },
    {
      "date": "2011-02-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8jxxuv/intro---2-28-11",
        "http://thecolbertreport.cc.com/videos/8fpe6c/anonymous-hacks-the-colbert-report",
        "http://thecolbertreport.cc.com/videos/ohhby5/tip-wag---joe-reed---levi-s-ex-girlfriend-jeans",
        "http://thecolbertreport.cc.com/videos/lrah7j/art-stephen-up-challenge---phillips-de-pury-auction",
        "http://thecolbertreport.cc.com/videos/4oq5za/michael-scheuer",
        "http://thecolbertreport.cc.com/videos/qg45nm/sign-off---tomorrow-s-goodnight-preview"
      ],
      "guest": "Michael Scheuer"
    },
    {
      "date": "2011-03-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dbc523/intro---3-1-11",
        "http://thecolbertreport.cc.com/videos/hl74h7/muammar-al-gaddafi-competes-with-charlie-sheen",
        "http://thecolbertreport.cc.com/videos/ce6ez1/the-word---new-country-for-old-men",
        "http://thecolbertreport.cc.com/videos/6zdcls/senior-moment---geriatric-porn",
        "http://thecolbertreport.cc.com/videos/zxzpiz/evan-osnos",
        "http://thecolbertreport.cc.com/videos/b6gm2j/sign-off---welcome-zachary-paul-dahm"
      ],
      "guest": "Evan Osnos"
    },
    {
      "date": "2011-03-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/44fqvj/intro---3-2-11",
        "http://thecolbertreport.cc.com/videos/jh2tli/wisconsin-prank-call-bill",
        "http://thecolbertreport.cc.com/videos/i9x3xr/the-word---economic-boom",
        "http://thecolbertreport.cc.com/videos/uz0ktw/eulogy-spot",
        "http://thecolbertreport.cc.com/videos/7lrvtf/harry-connick-jr-",
        "http://thecolbertreport.cc.com/videos/ninj2e/sign-off---demise-of-the-white-pages"
      ],
      "guest": "Harry Connick Jr."
    },
    {
      "date": "2011-03-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nb3zpi/fox-news-suspends-contributors",
        "http://thecolbertreport.cc.com/videos/7vwzpc/ice-cream-fight-with-jimmy-fallon",
        "http://thecolbertreport.cc.com/videos/4oi0dh/ice-cream-hallucination-with-jimmy-fallon",
        "http://thecolbertreport.cc.com/videos/zxu7kb/mark-moffett",
        "http://thecolbertreport.cc.com/videos/2x8ter/sign-off---late-night-snack"
      ],
      "guest": "Mark W. Moffett"
    },
    {
      "date": "2011-03-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/432mwn/intro---3-7-11",
        "http://thecolbertreport.cc.com/videos/dmu7rh/stephen-wants-an-ipad-2",
        "http://thecolbertreport.cc.com/videos/zql2lp/on-notice---mike-huckabee",
        "http://thecolbertreport.cc.com/videos/mrhaui/america-s-next-gop-model",
        "http://thecolbertreport.cc.com/videos/ux0w7b/joshua-foer",
        "http://thecolbertreport.cc.com/videos/un3kdu/art-stephen-up-challenge---bid-on-stephen-s-portrait"
      ],
      "guest": "Joshua Foer"
    },
    {
      "date": "2011-03-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2s9pic/happy-mardi-gras---international-women-s-day",
        "http://thecolbertreport.cc.com/videos/29cv4a/light-bulb-ban",
        "http://thecolbertreport.cc.com/videos/yuo5to/light-bulb-ban---dale-bryk",
        "http://thecolbertreport.cc.com/videos/2nv2ie/charlie-sheen---fake-rahm-emanuel-on-twitter",
        "http://thecolbertreport.cc.com/videos/dqh7vp/dan-sinker",
        "http://thecolbertreport.cc.com/videos/wjd0wx/sign-off---welcome-zoe-simone-sanchez"
      ],
      "guest": "Dan Sinker"
    },
    {
      "date": "2011-03-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oivxm4/intro---3-9-11",
        "http://thecolbertreport.cc.com/videos/durtx6/stephen-gives-up-catholicism-for-lent",
        "http://thecolbertreport.cc.com/videos/c3zm6w/bench-press",
        "http://thecolbertreport.cc.com/videos/qi1r7y/bench-press---anthony-weiner",
        "http://thecolbertreport.cc.com/videos/mbmsxi/david-brooks",
        "http://thecolbertreport.cc.com/videos/bh348l/sign-off---jewish-stephen"
      ],
      "guest": "David Brooks"
    },
    {
      "date": "2011-03-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/au4itm/intro---3-10-11",
        "http://thecolbertreport.cc.com/videos/w8nzdj/newt-gingrich-wants-to-screw-america",
        "http://thecolbertreport.cc.com/videos/hagj8b/colbert-pac-ad",
        "http://thecolbertreport.cc.com/videos/k698u1/peter-king-understands-violent-radicalism",
        "http://thecolbertreport.cc.com/videos/84jg83/reza-aslan",
        "http://thecolbertreport.cc.com/videos/x9iaae/sign-off---enjoy-the-moment"
      ],
      "guest": "Reza Aslan"
    },
    {
      "date": "2011-03-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tkzzdn/intro---3-21-11",
        "http://thecolbertreport.cc.com/videos/btot11/crisis-in-the-middle-everywhere---japan---libya",
        "http://thecolbertreport.cc.com/videos/kvj8rv/raging-art-on---art-1",
        "http://thecolbertreport.cc.com/videos/9m4lpg/sign-off---dueling-banjos"
      ],
      "guest": "Steve Martin and the Steep Canyon Rangers"
    },
    {
      "date": "2011-03-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/67fxmc/intro---3-22-11",
        "http://thecolbertreport.cc.com/videos/4k1vs5/californians-respond-to-japanese-disaster",
        "http://thecolbertreport.cc.com/videos/tadiop/raging-art-on---art-2",
        "http://thecolbertreport.cc.com/videos/7fv2d8/crisis-in-the-middle-everywhere---cnn-and-fox-news-fight-in-libya",
        "http://thecolbertreport.cc.com/videos/iky4d9/ayman-mohyeldin",
        "http://thecolbertreport.cc.com/videos/f8fwxt/sign-off---goodnight"
      ],
      "guest": "Ayman Mohyeldin"
    },
    {
      "date": "2011-03-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m2qxvd/top-news-stories-all-at-once",
        "http://thecolbertreport.cc.com/videos/3rhe0w/raging-art-on---art-3",
        "http://thecolbertreport.cc.com/videos/3ccbj2/the-word---over-reactor",
        "http://thecolbertreport.cc.com/videos/wd1pjd/nathan-myhrvold",
        "http://thecolbertreport.cc.com/videos/l5f2yi/sign-off---pistachio-ice-cream"
      ],
      "guest": "Nathan Myhrvold"
    },
    {
      "date": "2011-03-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/awwa6r/intro---3-24-11",
        "http://thecolbertreport.cc.com/videos/o0idw2/bears---balls---misery-edition",
        "http://thecolbertreport.cc.com/videos/pst3ox/eat--pray-to-eat---laurie-garrett",
        "http://thecolbertreport.cc.com/videos/strtop/channeled-rage",
        "http://thecolbertreport.cc.com/videos/rfce7l/jody-williams",
        "http://thecolbertreport.cc.com/videos/3z7nhm/sign-off---john-oliver-s-new-york-stand-up-show"
      ],
      "guest": "Jody Williams"
    },
    {
      "date": "2011-03-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2u3wdk/intro---3-28-11",
        "http://thecolbertreport.cc.com/videos/vou6it/shout-out-to-cece-lederer",
        "http://thecolbertreport.cc.com/videos/xeu06g/chaos-in-chaonada",
        "http://thecolbertreport.cc.com/videos/s3xgtv/tip-wag---cigarette-tax--abortion-waiting-period---bargain-travelers",
        "http://thecolbertreport.cc.com/videos/c06ht5/maine-squeeze",
        "http://thecolbertreport.cc.com/videos/2p412b/michael-moore",
        "http://thecolbertreport.cc.com/videos/lplrhl/sign-off---movits--streams--out-of-my-head-"
      ],
      "guest": "Michael Moore"
    },
    {
      "date": "2011-03-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xysvku/intro---3-29-11",
        "http://thecolbertreport.cc.com/videos/wtajtw/turd-sandwich-in-libya",
        "http://thecolbertreport.cc.com/videos/fkwv1e/yahweh-or-no-way---christianity-is-fattening",
        "http://thecolbertreport.cc.com/videos/oa9b4m/stephen-s-next-religion---stephen-prothero",
        "http://thecolbertreport.cc.com/videos/730dpm/jimmy-fallon-promises-a-performance-by-stephen",
        "http://thecolbertreport.cc.com/videos/7m3guo/anthony-fauci",
        "http://thecolbertreport.cc.com/videos/ms1yr8/sign-off---do-not-help-jimmy-fallon"
      ],
      "guest": "Dr. Anthony Fauci"
    },
    {
      "date": "2011-03-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6nwkpk/exclusive---reporter-gets-nailed-by-san-francisco-cop",
        "http://thecolbertreport.cc.com/videos/xysvku/intro---3-29-11",
        "http://thecolbertreport.cc.com/videos/wtajtw/turd-sandwich-in-libya",
        "http://thecolbertreport.cc.com/videos/fkwv1e/yahweh-or-no-way---christianity-is-fattening",
        "http://thecolbertreport.cc.com/videos/oa9b4m/stephen-s-next-religion---stephen-prothero",
        "http://thecolbertreport.cc.com/videos/730dpm/jimmy-fallon-promises-a-performance-by-stephen",
        "http://thecolbertreport.cc.com/videos/7m3guo/anthony-fauci",
        "http://thecolbertreport.cc.com/videos/ms1yr8/sign-off---do-not-help-jimmy-fallon"
      ],
      "guest": "Tim Shriver"
    },
    {
      "date": "2011-03-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zxtidm/james-o-keefe-asks-for-donations",
        "http://thecolbertreport.cc.com/videos/8stgre/colbert-pac",
        "http://thecolbertreport.cc.com/videos/dtl1ew/colbert-pac---trevor-potter",
        "http://thecolbertreport.cc.com/videos/i3lpcq/stephen-practices-rebecca-black-s--friday-",
        "http://thecolbertreport.cc.com/videos/wug1p5/tim-shriver",
        "http://thecolbertreport.cc.com/videos/dwx5m0/sign-off---goodnight"
      ],
      "guest": "Tim Shriver"
    },
    {
      "date": "2011-03-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a6ko78/intro---3-31-11",
        "http://thecolbertreport.cc.com/videos/oth30j/congressional-budget-menorah",
        "http://thecolbertreport.cc.com/videos/j56fvd/madison-as-hell",
        "http://thecolbertreport.cc.com/videos/o6su04/piers-gibbon",
        "http://thecolbertreport.cc.com/videos/gq7wfn/sign-off---congressional-budget-menorah-fire"
      ],
      "guest": "Piers Gibbon"
    },
    {
      "date": "2011-04-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nknyci/government-shutdown-menorah",
        "http://thecolbertreport.cc.com/videos/8fsxhp/stephen-shows-off-the-ipad-2",
        "http://thecolbertreport.cc.com/videos/953smc/the-word---that-new-smell-smell",
        "http://thecolbertreport.cc.com/videos/zr09m5/the-glennpocalypse",
        "http://thecolbertreport.cc.com/videos/j7j5ds/andrew-chaikin",
        "http://thecolbertreport.cc.com/videos/9h7n61/sign-off---inescapables"
      ],
      "guest": "Andrew Chaikin"
    },
    {
      "date": "2011-04-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x139me/tim-pawlenty-appeals-to-youth-vote",
        "http://thecolbertreport.cc.com/videos/dq1pyh/renaissance-nemesis---frank-jameso",
        "http://thecolbertreport.cc.com/videos/zw8gjf/james-franco-pt--1",
        "http://thecolbertreport.cc.com/videos/91jml7/james-franco-pt--2",
        "http://thecolbertreport.cc.com/videos/upimil/sign-off---frank-jameso"
      ],
      "guest": "James Franco"
    },
    {
      "date": "2011-04-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1fi1u8/wisconsin-supreme-court-race",
        "http://thecolbertreport.cc.com/videos/vu85n8/my-fair-colbert---hugo-vickers-pt--1",
        "http://thecolbertreport.cc.com/videos/53yz6p/wd-40-1",
        "http://thecolbertreport.cc.com/videos/q5s3lh/sir-david-tang",
        "http://thecolbertreport.cc.com/videos/oqhpiw/sign-off---wd-40-1-cleaner"
      ],
      "guest": "Sir David Tang"
    },
    {
      "date": "2011-04-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x9mvny/exclusive---my-fair-colbert---charming-prince-philip",
        "http://thecolbertreport.cc.com/videos/ruv6gp/exclusive---my-fair-colbert---ghost-of-an-irishman",
        "http://thecolbertreport.cc.com/videos/k0xu9f/intro---4-7-11",
        "http://thecolbertreport.cc.com/videos/a3oo5c/the-koran-s-best-day-ever",
        "http://thecolbertreport.cc.com/videos/uepxed/my-fair-colbert---hugo-vickers-pt--2",
        "http://thecolbertreport.cc.com/videos/4zz0jd/my-fair-colbert---hugo-vickers-pt--3",
        "http://thecolbertreport.cc.com/videos/hv2afg/jeff-greenfield",
        "http://thecolbertreport.cc.com/videos/b9aslx/sign-off---goodnight"
      ],
      "guest": "Jeff Greenfield"
    },
    {
      "date": "2011-04-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5p5wwd/countdown-to-government-shutdown",
        "http://thecolbertreport.cc.com/videos/wueypc/pap-smears-at-walgreens",
        "http://thecolbertreport.cc.com/videos/5o6455/thought-for-food---chocolate-air--denny-s---bacon-cologne",
        "http://thecolbertreport.cc.com/videos/5ej465/jamie-hyneman---adam-savage",
        "http://thecolbertreport.cc.com/videos/sse1uc/sign-off---champagne-flute-of-lead-paint"
      ],
      "guest": "Jamie Hyneman &amp; Adam Savage"
    },
    {
      "date": "2011-04-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hvb9sp/intro---4-12-11",
        "http://thecolbertreport.cc.com/videos/ez4az7/jon-kyl-tweets-not-intended-to-be-factual-statements",
        "http://thecolbertreport.cc.com/videos/xcin15/mitt-happens",
        "http://thecolbertreport.cc.com/videos/l039ce/mitt-happens---rick-brookhiser",
        "http://thecolbertreport.cc.com/videos/pqpkrr/threat-level--rainbow",
        "http://thecolbertreport.cc.com/videos/2gpjkk/ray-kurzweil",
        "http://thecolbertreport.cc.com/videos/ry2cgl/sign-off---goodnight"
      ],
      "guest": "Ray Kurzweil"
    },
    {
      "date": "2011-04-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tjsqfs/tim-pawlenty-declares-candidacy-before-he-s-ready",
        "http://thecolbertreport.cc.com/videos/ha4gop/the-word---buy-and-cellulite",
        "http://thecolbertreport.cc.com/videos/jc9fbz/the-enemy-within---unicyclists",
        "http://thecolbertreport.cc.com/videos/nm38xu/morgan-spurlock",
        "http://thecolbertreport.cc.com/videos/l1ikyh/sign-off---doritos-suit"
      ],
      "guest": "Morgan Spurlock"
    },
    {
      "date": "2011-04-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fziyvf/obama-needs-charts-and-graphs",
        "http://thecolbertreport.cc.com/videos/pfzzi1/viacom-ruins-stephen-s-pac-dream",
        "http://thecolbertreport.cc.com/videos/yzb7q2/colbert-super-pac---trevor-potter",
        "http://thecolbertreport.cc.com/videos/k099cq/easter-under-attack---egg-edition",
        "http://thecolbertreport.cc.com/videos/iybrlk/caroline-kennedy",
        "http://thecolbertreport.cc.com/videos/rjwyn0/sign-off---ipad"
      ],
      "guest": "Caroline Kennedy"
    },
    {
      "date": "2011-04-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/00rg0h/catholic-bender",
        "http://thecolbertreport.cc.com/videos/tml3zz/obama-s-tax-return---road-to-the-trump-house",
        "http://thecolbertreport.cc.com/videos/e943tp/cheating-death---vaxa-international--lap-band-surgery---restless-leg-syndrome",
        "http://thecolbertreport.cc.com/videos/nxhrou/ron-paul",
        "http://thecolbertreport.cc.com/videos/8813vl/sign-off---vacsa-not-masturbating"
      ],
      "guest": "Rep. Ron Paul"
    },
    {
      "date": "2011-04-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hl20qf/intro---4-26-11",
        "http://thecolbertreport.cc.com/videos/zv4zje/mitt-romney-s--peacetime--gaffe",
        "http://thecolbertreport.cc.com/videos/rmltni/charles-manson-believes-in-global-warming",
        "http://thecolbertreport.cc.com/videos/i3gdyb/a-c--grayling",
        "http://thecolbertreport.cc.com/videos/qxdqyc/sign-off---taser"
      ],
      "guest": "A.C. Grayling"
    },
    {
      "date": "2011-04-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d9mieg/intro---4-27-11",
        "http://thecolbertreport.cc.com/videos/cnt2qq/america-needs-to-see-obama-s-report-cards",
        "http://thecolbertreport.cc.com/videos/vog079/tip-wag---faa--casio-watches---postal-service",
        "http://thecolbertreport.cc.com/videos/qu6i2l/anderson-cooper-goes-on-the-absurd-u-chart",
        "http://thecolbertreport.cc.com/videos/okt7ac/ice-t",
        "http://thecolbertreport.cc.com/videos/bi5bau/sign-off---goodnight-in-spanish"
      ],
      "guest": "Ice-T"
    },
    {
      "date": "2011-04-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xcnvxf/intro---4-28-11",
        "http://thecolbertreport.cc.com/videos/6ei496/stephen-waits-for-his-royal-wedding-invitation-in-london",
        "http://thecolbertreport.cc.com/videos/8ureil/progressives-united---russ-feingold",
        "http://thecolbertreport.cc.com/videos/dfmioz/homeland-security-eliminates-color-coded-terror-alert-system",
        "http://thecolbertreport.cc.com/videos/r7zj9a/wade-graham",
        "http://thecolbertreport.cc.com/videos/tsom8o/sign-off---off-to-the-royal-wedding"
      ],
      "guest": "Wade Graham"
    },
    {
      "date": "2011-05-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/792my5/intro---5-2-11",
        "http://thecolbertreport.cc.com/videos/6kw3l1/long-awaited--we-got-bin-laden--party",
        "http://thecolbertreport.cc.com/videos/501cxj/carefree-pre-9-11-world",
        "http://thecolbertreport.cc.com/videos/w147rj/relations-with-pakistan---richard-haass",
        "http://thecolbertreport.cc.com/videos/x03tm5/francis-fukuyama",
        "http://thecolbertreport.cc.com/videos/s3o1z2/sign-off---obama-s-timer-runs-out"
      ],
      "guest": "Francis Fukuyama"
    },
    {
      "date": "2011-05-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v58m27/intro---5-3-11",
        "http://thecolbertreport.cc.com/videos/h9f07a/osama-bin-laden-is-still-dead",
        "http://thecolbertreport.cc.com/videos/5n9zp7/obama-takes-credit-for-bin-laden-s-assassination",
        "http://thecolbertreport.cc.com/videos/h1wdo9/journalistic-grintegrity",
        "http://thecolbertreport.cc.com/videos/u2r1n6/rex-ryan",
        "http://thecolbertreport.cc.com/videos/ukrfvl/sign-off---special-kiss"
      ],
      "guest": "Rex Ryan"
    },
    {
      "date": "2011-05-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/edkk4q/intro---5-4-11",
        "http://thecolbertreport.cc.com/videos/ndiuxr/terrorists--they-re-just-like-us-",
        "http://thecolbertreport.cc.com/videos/kbkvj6/stephen-searches-for-shared-bathroom-key",
        "http://thecolbertreport.cc.com/videos/kt1w5q/movies-that-are-destroying-america---saving-america-edition",
        "http://thecolbertreport.cc.com/videos/50b5cb/amy-farrell",
        "http://thecolbertreport.cc.com/videos/jcmie8/sign-off---goodnight"
      ],
      "guest": "Amy Farrell"
    },
    {
      "date": "2011-05-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lbrn85/stephen-confesses-to-a-distracted-media",
        "http://thecolbertreport.cc.com/videos/avpz0y/threatdown---superman--madden-nfl-12----glee-",
        "http://thecolbertreport.cc.com/videos/g2bhyr/inaugural-republican-presidential-debate---donald-trump-s-wisdom",
        "http://thecolbertreport.cc.com/videos/4neb1g/bill-james",
        "http://thecolbertreport.cc.com/videos/k2or8w/sign-off---dennis-kucinich-heat-vision"
      ],
      "guest": "Bill James"
    },
    {
      "date": "2011-05-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dkbe7y/intro---5-9-11",
        "http://thecolbertreport.cc.com/videos/6rdbxz/hasidic-newspaper-removes-hillary-clinton",
        "http://thecolbertreport.cc.com/videos/mqyr6k/herman-cain-wins-the-first-republican-presidential-debate",
        "http://thecolbertreport.cc.com/videos/38grqn/the-word---autocratic-for-the-people",
        "http://thecolbertreport.cc.com/videos/d8bi6b/lupe-fiasco",
        "http://thecolbertreport.cc.com/videos/vonv0r/sign-off---lupe-fiasco-s--lasers-"
      ],
      "guest": "Lupe Fiasco"
    },
    {
      "date": "2011-05-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r02fac/newt-gingrich---donald-trump-announce-future-announcements",
        "http://thecolbertreport.cc.com/videos/w3lgcs/yahweh-or-no-way---thor---apocalypse-billboard",
        "http://thecolbertreport.cc.com/videos/zu0ju2/difference-makers---donald-trump",
        "http://thecolbertreport.cc.com/videos/i4gyok/geoffrey-rush",
        "http://thecolbertreport.cc.com/videos/wmfolw/sign-off---a-rare-correction"
      ],
      "guest": "Geoffrey Rush"
    },
    {
      "date": "2011-05-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g0js2x/intro---5-11-11",
        "http://thecolbertreport.cc.com/videos/txo75b/herman-cain-claims-the-colbert-bump",
        "http://thecolbertreport.cc.com/videos/1ssaiz/corp-constituency",
        "http://thecolbertreport.cc.com/videos/nfv0i1/corp-constituency---trevor-potter",
        "http://thecolbertreport.cc.com/videos/rqvi06/award-to-the-wise",
        "http://thecolbertreport.cc.com/videos/sjt27k/eric-greitens",
        "http://thecolbertreport.cc.com/videos/q3siyv/sign-off---press-hat"
      ],
      "guest": "Eric Greitens"
    },
    {
      "date": "2011-05-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mp7mrs/intro---5-12-11",
        "http://thecolbertreport.cc.com/videos/zz94qv/obama-s-latino-panderfest",
        "http://thecolbertreport.cc.com/videos/vkp4tr/terror--a-new-one",
        "http://thecolbertreport.cc.com/videos/9o0mt6/terror--a-new-one---lawrence-wright",
        "http://thecolbertreport.cc.com/videos/dqvz13/if-at-first-you-don-t-secede",
        "http://thecolbertreport.cc.com/videos/yx5grt/john-bradshaw",
        "http://thecolbertreport.cc.com/videos/sw8fy6/sign-off---stephen-s-super-pac-needs-support"
      ],
      "guest": "John Bradshaw"
    },
    {
      "date": "2011-05-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9xaxr4/mike-huckabee---donald-trump-drop-out",
        "http://thecolbertreport.cc.com/videos/duon08/fig-newton-gingrich-2012",
        "http://thecolbertreport.cc.com/videos/epwg6t/stephen-files-super-pac-request",
        "http://thecolbertreport.cc.com/videos/g3ep11/alison-klayman",
        "http://thecolbertreport.cc.com/videos/4r7evh/sign-off---goodnight"
      ],
      "guest": "Alison Klayman"
    },
    {
      "date": "2011-05-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ip5tv7/intro---5-17-11",
        "http://thecolbertreport.cc.com/videos/1ugsri/world-s-oldest-panda-dies",
        "http://thecolbertreport.cc.com/videos/l4p5dq/the-word---enhanced-rejustification",
        "http://thecolbertreport.cc.com/videos/pg06l0/arnold-schwarzenegger-s-sex-scandal",
        "http://thecolbertreport.cc.com/videos/58filp/amy-kremer",
        "http://thecolbertreport.cc.com/videos/no1rv9/sign-off---goodnight"
      ],
      "guest": "Amy Kremer"
    },
    {
      "date": "2011-05-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/faf2no/exclusive---austan-goolsbee-extended-interview-pt--1",
        "http://thecolbertreport.cc.com/videos/6pf58s/exclusive---austan-goolsbee-extended-interview-pt--2",
        "http://thecolbertreport.cc.com/videos/bdi4g4/exclusive---austan-goolsbee-extended-interview-pt--3",
        "http://thecolbertreport.cc.com/videos/6khcvr/intro---5-18-11",
        "http://thecolbertreport.cc.com/videos/55ye8a/osama-bin-laden-s-replacement",
        "http://thecolbertreport.cc.com/videos/tohq6g/tip-wag---ohio-legislature---facebook",
        "http://thecolbertreport.cc.com/videos/2cxcrh/breaking-newt",
        "http://thecolbertreport.cc.com/videos/vvu071/austan-goolsbee",
        "http://thecolbertreport.cc.com/videos/sklv51/sign-off---long-austan-goolsbee-interview"
      ],
      "guest": "Austan Goolsbee"
    },
    {
      "date": "2011-05-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7qmvog/john-lithgow-performs-gingrich-press-release",
        "http://thecolbertreport.cc.com/videos/pb82sf/better-know-a-district---illinois--18th---aaron-schock-update",
        "http://thecolbertreport.cc.com/videos/3gd1zf/clergy-matic-ecclesi-action-center-3-16",
        "http://thecolbertreport.cc.com/videos/5ec3r8/kareem-abdul-jabbar",
        "http://thecolbertreport.cc.com/videos/p12tcc/sign-off---history-of-life-on-earth"
      ],
      "guest": "Kareem Abdul-Jabbar"
    },
    {
      "date": "2011-05-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gn9ut5/intro---5-31-11",
        "http://thecolbertreport.cc.com/videos/xxn340/charleston-to-bermuda-yacht-race",
        "http://thecolbertreport.cc.com/videos/fgthom/sarah-palin-s-bus-tour",
        "http://thecolbertreport.cc.com/videos/bmwaxh/fec-questions---trevor-potter",
        "http://thecolbertreport.cc.com/videos/7bl2ga/invisible-judgment",
        "http://thecolbertreport.cc.com/videos/ox3on4/james-stewart",
        "http://thecolbertreport.cc.com/videos/vn091b/sign-off---goodnight"
      ],
      "guest": "James B. Stewart"
    },
    {
      "date": "2011-06-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nos79v/intro---6-1-11",
        "http://thecolbertreport.cc.com/videos/mqb30h/sarah-palin-visits-the-times-square-applebee-s",
        "http://thecolbertreport.cc.com/videos/ul70kx/meat-tweet",
        "http://thecolbertreport.cc.com/videos/jph6sv/harmful-cell-phones",
        "http://thecolbertreport.cc.com/videos/beqc1p/who-s-riding-my-coattails-now----jimmy-fallon",
        "http://thecolbertreport.cc.com/videos/5a4ke7/robert-f--kennedy-jr-",
        "http://thecolbertreport.cc.com/videos/3enqpr/sign-off---iphone"
      ],
      "guest": "Robert Kennedy Jr."
    },
    {
      "date": "2011-06-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7o4l3r/intro---6-2-11",
        "http://thecolbertreport.cc.com/videos/rqi6dy/dancing-on-the-ceiling",
        "http://thecolbertreport.cc.com/videos/1db84y/anthony-weiner-addresses-twitter-scandal",
        "http://thecolbertreport.cc.com/videos/qhexu1/tip-wag---osama-bin-laden---hugh-hefner",
        "http://thecolbertreport.cc.com/videos/8t7m7k/salman-khan",
        "http://thecolbertreport.cc.com/videos/rqa2ar/sign-off---goodnight"
      ],
      "guest": "Salman Khan"
    },
    {
      "date": "2011-06-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bwqzbu/anthony-weiner-s-emergency-press-conference",
        "http://thecolbertreport.cc.com/videos/uvi91o/paul-revere-s-famous-ride",
        "http://thecolbertreport.cc.com/videos/x424g2/stephen-s-twitter-scandal",
        "http://thecolbertreport.cc.com/videos/qyadrw/obama-administration-replaces-food-pyramid",
        "http://thecolbertreport.cc.com/videos/fdolcv/werner-herzog",
        "http://thecolbertreport.cc.com/videos/ed6qec/stephen-s-midnight-ride"
      ],
      "guest": "Werner Herzog"
    },
    {
      "date": "2011-06-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/suzxde/scott-pelley-s-first-cbs-broadcast",
        "http://thecolbertreport.cc.com/videos/1w9fvc/the-word---hear-no-evil",
        "http://thecolbertreport.cc.com/videos/fvvawg/sugar-ray-leonard",
        "http://thecolbertreport.cc.com/videos/b4ot0e/apologies-to-shimshamistan"
      ],
      "guest": "Sugar Ray Leonard"
    },
    {
      "date": "2011-06-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fq1085/herman-cain-wants-small-bills",
        "http://thecolbertreport.cc.com/videos/bmggoz/better-know-a-district---california-s-10th---john-garamendi",
        "http://thecolbertreport.cc.com/videos/ycdgvg/weiner-captures-manscaping-vote",
        "http://thecolbertreport.cc.com/videos/yvz8wj/bre-pettis",
        "http://thecolbertreport.cc.com/videos/ao2r17/sign-off---makerbot-head"
      ],
      "guest": "Bre Pettis"
    },
    {
      "date": "2011-06-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tz9edm/shaquille-o-neal-retires",
        "http://thecolbertreport.cc.com/videos/umrvml/mitt-romney-leads-in-fox-news-poll",
        "http://thecolbertreport.cc.com/videos/qgxogp/the-word---the-business-end",
        "http://thecolbertreport.cc.com/videos/oneftb/andrew-breitbart-reveals-weiner-photo",
        "http://thecolbertreport.cc.com/videos/5f3kap/tom-ridge",
        "http://thecolbertreport.cc.com/videos/vvj5q2/sign-off---goodnight"
      ],
      "guest": "Tom Ridge"
    },
    {
      "date": "2011-06-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0zzkov/anthony-weiner-gym-photos",
        "http://thecolbertreport.cc.com/videos/vgcql3/sport-report---miami-heat--fifa---freestyle-canoe-dancing",
        "http://thecolbertreport.cc.com/videos/vyyl7z/henry-kissinger-pt--1",
        "http://thecolbertreport.cc.com/videos/2j87li/henry-kissinger-pt--2",
        "http://thecolbertreport.cc.com/videos/w5b5l1/sign-off---goodnight"
      ],
      "guest": "Henry Kissinger"
    },
    {
      "date": "2011-06-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lokk6e/intro---6-14-11",
        "http://thecolbertreport.cc.com/videos/egh1n7/elephants-in-the-room",
        "http://thecolbertreport.cc.com/videos/ykt712/close-sesame",
        "http://thecolbertreport.cc.com/videos/s6kp16/janny-scott",
        "http://thecolbertreport.cc.com/videos/j0gylk/sign-off---marshmallows"
      ],
      "guest": "Janny Scott"
    },
    {
      "date": "2011-06-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d8iaxd/intro---6-15-11",
        "http://thecolbertreport.cc.com/videos/zj00ia/iran-bans-necklaces-and-shorts",
        "http://thecolbertreport.cc.com/videos/xbt4w9/kindergarten-gop",
        "http://thecolbertreport.cc.com/videos/ynp682/the-word---shock-the-vote",
        "http://thecolbertreport.cc.com/videos/46tlsv/senior-moment---pot-smoking-seniors",
        "http://thecolbertreport.cc.com/videos/5h6ee5/keith-olbermann",
        "http://thecolbertreport.cc.com/videos/5rh3rg/sign-off---stephen-wears-shorts"
      ],
      "guest": "Keith Olbermann"
    },
    {
      "date": "2011-06-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2374v3/intro---6-20-11",
        "http://thecolbertreport.cc.com/videos/q7b70y/stephest-colbchella--011---rock-you-like-a-thirst-icane",
        "http://thecolbertreport.cc.com/videos/y7lr8u/threatdown---moo-shu-man-milk--centenarians---robo-slackers",
        "http://thecolbertreport.cc.com/videos/gds7n9/justin-vernon",
        "http://thecolbertreport.cc.com/videos/su735n/sign-off---bon-iver-bonus-song"
      ],
      "guest": "Bon Iver"
    },
    {
      "date": "2011-06-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3o3le7/generic-republican-presidential-nominee",
        "http://thecolbertreport.cc.com/videos/ct0au7/stephest-colbchella--011---stephen-revives-his-music-career",
        "http://thecolbertreport.cc.com/videos/v43nph/2011--a-rock-odyssey-featuring-jack-white-pt--1",
        "http://thecolbertreport.cc.com/videos/7e8ifi/florence-welch",
        "http://thecolbertreport.cc.com/videos/ei7r0b/sign-off---talib-kweli-tomorrow"
      ],
      "guest": "Florence and the Machine"
    },
    {
      "date": "2011-06-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f5h9ob/george-w--bush-helps-break-a-world-record",
        "http://thecolbertreport.cc.com/videos/ozlnky/2011--a-rock-odyssey-featuring-jack-white-pt--2",
        "http://thecolbertreport.cc.com/videos/u3bmmq/the-word---the-defining-moment",
        "http://thecolbertreport.cc.com/videos/c7shlp/talib-kweli"
      ],
      "guest": "Talib Kweli"
    },
    {
      "date": "2011-06-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ihqt34/exclusive---2011--a-rock-odyssey-featuring-jack-white---catholic-throwdown",
        "http://thecolbertreport.cc.com/videos/zbc2ok/stephest-colbchella--011---stephen-announces-his-hit-song",
        "http://thecolbertreport.cc.com/videos/1if3ir/nation-building-in-america",
        "http://thecolbertreport.cc.com/videos/4evhq9/2011--a-rock-odyssey-featuring-jack-white-pt--3",
        "http://thecolbertreport.cc.com/videos/39or3g/jack-white"
      ],
      "guest": "The Black Belles"
    },
    {
      "date": "2011-06-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8tiso3/intro---6-27-11",
        "http://thecolbertreport.cc.com/videos/zz1v27/tip-wag---scented-razors---rick-scott-s-approval-rating",
        "http://thecolbertreport.cc.com/videos/7e3kfb/stephen---jonathan-alter-at-gaillard-auditorium",
        "http://thecolbertreport.cc.com/videos/npgonl/good-point-other-point---ted-nugent-vs--millennials",
        "http://thecolbertreport.cc.com/videos/89vjk7/grover-norquist",
        "http://thecolbertreport.cc.com/videos/fe2wnr/sign-off---scented-box-cutter"
      ],
      "guest": "Grover Norquist"
    },
    {
      "date": "2011-06-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gs5b2y/intro---6-28-11",
        "http://thecolbertreport.cc.com/videos/im5by3/michele-bachmann-compares-herself-to-john-wayne",
        "http://thecolbertreport.cc.com/videos/b2dez1/the-word---too-big-to-nail",
        "http://thecolbertreport.cc.com/videos/eztgrx/advertising-to-monkeys",
        "http://thecolbertreport.cc.com/videos/jfztdi/alexandra-pelosi",
        "http://thecolbertreport.cc.com/videos/1it2j9/sign-off---teleprompter-eulogy"
      ],
      "guest": "Alexandra Pelosi"
    },
    {
      "date": "2011-06-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e7dlbc/intro---6-29-11",
        "http://thecolbertreport.cc.com/videos/s3xttd/4th-of-july-under-attack---fireworks-cancelled",
        "http://thecolbertreport.cc.com/videos/7gul1z/colbert-super-pac---irresponsible-advertising",
        "http://thecolbertreport.cc.com/videos/kco7lo/colbert-super-pac---trevor-potter-preps-stephen-for-his-fec-hearing",
        "http://thecolbertreport.cc.com/videos/o7wrgl/hometown-hero-town---lexington--ky",
        "http://thecolbertreport.cc.com/videos/zc23xv/gary-sinise",
        "http://thecolbertreport.cc.com/videos/80a7v2/sign-off---see-you-at-the-fec"
      ],
      "guest": "Gary Sinise"
    },
    {
      "date": "2011-06-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3yk8uf/intro---6-30-11",
        "http://thecolbertreport.cc.com/videos/gffis7/colbert-super-pac---i-can-haz-super-pac-",
        "http://thecolbertreport.cc.com/videos/uf525x/colbert-super-pac---stephen-addresses-colbert-super-nation",
        "http://thecolbertreport.cc.com/videos/owodco/formidable-opponent---pakistan",
        "http://thecolbertreport.cc.com/videos/807lhi/timothy-garton-ash",
        "http://thecolbertreport.cc.com/videos/b2dqnd/sign-off---super-pac-donations"
      ],
      "guest": "Timothy Garton Ash"
    },
    {
      "date": "2011-07-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t8xnmj/intro---7-11-11",
        "http://thecolbertreport.cc.com/videos/sgqex9/colbert-super-pac---pushing-the-limits",
        "http://thecolbertreport.cc.com/videos/m3svek/anti-frack-attacks",
        "http://thecolbertreport.cc.com/videos/2h3oe2/tip-wag---conservative-john-lennon---unfunny-germany",
        "http://thecolbertreport.cc.com/videos/z2r2b0/michael-shermer",
        "http://thecolbertreport.cc.com/videos/g47pr3/sign-off---super-pac-fundraising-goal"
      ],
      "guest": "Michael Shermer"
    },
    {
      "date": "2011-07-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/20gpt7/herman-cain-train",
        "http://thecolbertreport.cc.com/videos/7aive1/the-family-leader-s-controversial-pledge",
        "http://thecolbertreport.cc.com/videos/7sobpk/heterosexual-accountability-buddy",
        "http://thecolbertreport.cc.com/videos/vw4tol/dan-savage",
        "http://thecolbertreport.cc.com/videos/nkuukl/sign-off---fixing-the-boiler"
      ],
      "guest": "Dan Savage"
    },
    {
      "date": "2011-07-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/smsyco/intro---7-13-11",
        "http://thecolbertreport.cc.com/videos/70lgql/flagworth-2012",
        "http://thecolbertreport.cc.com/videos/7gb5kn/republicans-choose-none-of-the-above",
        "http://thecolbertreport.cc.com/videos/palj9t/obama-calls-the-republican-bluff",
        "http://thecolbertreport.cc.com/videos/5ulzg5/david-mccullough",
        "http://thecolbertreport.cc.com/videos/7xngpa/sign-off---pen-toss"
      ],
      "guest": "David McCullough"
    },
    {
      "date": "2011-07-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h2i0g7/intro---7-14-11",
        "http://thecolbertreport.cc.com/videos/8oisqi/carmageddon",
        "http://thecolbertreport.cc.com/videos/uqj8qb/may-the-best-stephen-colbert-win",
        "http://thecolbertreport.cc.com/videos/a29405/murdoch-s-media-empire-might-go-down-the-toilet",
        "http://thecolbertreport.cc.com/videos/1o1flh/improvised-expressive-devices",
        "http://thecolbertreport.cc.com/videos/82ovjs/jose-antonio-vargas",
        "http://thecolbertreport.cc.com/videos/9nwz4n/sign-off---goodnight"
      ],
      "guest": "Jose Antonio Vargas"
    },
    {
      "date": "2011-07-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ureory/intro---7-18-11",
        "http://thecolbertreport.cc.com/videos/ybue54/epic-blockbuster",
        "http://thecolbertreport.cc.com/videos/7t9e81/colbert-super-pac---cash-crawl",
        "http://thecolbertreport.cc.com/videos/73lwqj/colbert-super-pac---campaign-finance",
        "http://thecolbertreport.cc.com/videos/9q309t/blood-in-the-water---rupert-murdoch-s-news-of-the-world-scandal",
        "http://thecolbertreport.cc.com/videos/36812w/john-prendergast",
        "http://thecolbertreport.cc.com/videos/d8rt51/sign-off---prerecorded-episodes"
      ],
      "guest": "John Prendergast"
    },
    {
      "date": "2011-07-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bcunwj/newt-s-white-whale",
        "http://thecolbertreport.cc.com/videos/nhl043/god-calls-rick-perry",
        "http://thecolbertreport.cc.com/videos/6cdpui/debt-ceiling-deadline-conspiracy",
        "http://thecolbertreport.cc.com/videos/maophz/david-carr",
        "http://thecolbertreport.cc.com/videos/50pek1/sign-off---goodnight"
      ],
      "guest": "David Carr"
    },
    {
      "date": "2011-07-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pmh9y8/humanized-by-pie",
        "http://thecolbertreport.cc.com/videos/ozixqy/voter-id-laws",
        "http://thecolbertreport.cc.com/videos/2i29ww/congressional-partisan-rancor",
        "http://thecolbertreport.cc.com/videos/2p2ijk/michael-sandel",
        "http://thecolbertreport.cc.com/videos/tia7kd/sign-off---reading"
      ],
      "guest": "Michael Sandel"
    },
    {
      "date": "2011-07-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/egjics/intro---7-21-11",
        "http://thecolbertreport.cc.com/videos/l3rcr1/death-of-america-s-space-program",
        "http://thecolbertreport.cc.com/videos/vntv81/i-s-on-edjukashun---gay-history---disney-english",
        "http://thecolbertreport.cc.com/videos/6yym31/nbc--no-butt-coverage",
        "http://thecolbertreport.cc.com/videos/9catel/david-eagleman",
        "http://thecolbertreport.cc.com/videos/nn8qoh/sign-off---space-robot"
      ],
      "guest": "David Eagleman"
    },
    {
      "date": "2011-07-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l0wxhe/y2-gay",
        "http://thecolbertreport.cc.com/videos/fbd6kf/norwegian-muslish-gunman-s-islam-esque-atrocity",
        "http://thecolbertreport.cc.com/videos/wznkdz/vaginal-puppeteering-vs--d--k-scrub",
        "http://thecolbertreport.cc.com/videos/z4gfkc/brian-cox",
        "http://thecolbertreport.cc.com/videos/9q5n38/sign-off---the-thinker"
      ],
      "guest": "Brian Cox"
    },
    {
      "date": "2011-07-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bzl0xh/intro---7-26-11",
        "http://thecolbertreport.cc.com/videos/umjv5s/herman-cain-cancels-on-stephen",
        "http://thecolbertreport.cc.com/videos/zq2rpw/-poor--in-america",
        "http://thecolbertreport.cc.com/videos/j2gcnk/-poor--in-america---peter-edelman",
        "http://thecolbertreport.cc.com/videos/a4awyb/america-s-bucket-list",
        "http://thecolbertreport.cc.com/videos/azl59v/brooke-gladstone",
        "http://thecolbertreport.cc.com/videos/ly4qfz/sign-off---america-s-bucket-list"
      ],
      "guest": "Brooke Gladstone"
    },
    {
      "date": "2011-07-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zq1omv/nissan-s--leaf-wave--deadline",
        "http://thecolbertreport.cc.com/videos/x50fvb/difference-makers---patrick-rodgers",
        "http://thecolbertreport.cc.com/videos/3o44r7/helium-runs-out",
        "http://thecolbertreport.cc.com/videos/omkngv/missy-cummings",
        "http://thecolbertreport.cc.com/videos/y4zc9o/sign-off---surveillance-drone-crash"
      ],
      "guest": "Mary \"Missy\" Cummings"
    },
    {
      "date": "2011-07-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8c1oeo/the-republican-ring-of-power",
        "http://thecolbertreport.cc.com/videos/yzmsiz/colbert-super-pac---for-the-children",
        "http://thecolbertreport.cc.com/videos/e4r2vc/colbert-super-pac---matthew-dowd---ham-rove",
        "http://thecolbertreport.cc.com/videos/z6f8m4/buddy-roemer-pt--1",
        "http://thecolbertreport.cc.com/videos/n4ldiq/buddy-roemer-pt--2",
        "http://thecolbertreport.cc.com/videos/tzpdu5/sign-off---cone-of-silence"
      ],
      "guest": "Buddy Roemer"
    },
    {
      "date": "2011-08-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/aqw9op/intro---8-1-11",
        "http://thecolbertreport.cc.com/videos/lrz1ud/-three-billy-goats-gruff--budget-negotiations",
        "http://thecolbertreport.cc.com/videos/mgkqu6/the-word---with-great-power-comes-no-responsibility",
        "http://thecolbertreport.cc.com/videos/6v3oa3/from-ashes-to-bullets",
        "http://thecolbertreport.cc.com/videos/mqbxt0/tony-hsieh",
        "http://thecolbertreport.cc.com/videos/sqd53z/sign-off---sneakers"
      ],
      "guest": "Tony Hsieh"
    },
    {
      "date": "2011-08-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xaqx6o/intro---8-2-11",
        "http://thecolbertreport.cc.com/videos/j862uf/newt-gingrich-s-twitter-scandal",
        "http://thecolbertreport.cc.com/videos/pzfcj1/america-s-credit-grating",
        "http://thecolbertreport.cc.com/videos/y1xqdj/america-s-credit-grating---david-leonhardt",
        "http://thecolbertreport.cc.com/videos/gg2p1r/baby-teeth-economy",
        "http://thecolbertreport.cc.com/videos/id20x6/al-hunt",
        "http://thecolbertreport.cc.com/videos/h26uru/sign-off---goodnight"
      ],
      "guest": "Al Hunt"
    },
    {
      "date": "2011-08-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/br7gdf/intro---8-3-11",
        "http://thecolbertreport.cc.com/videos/3i1326/multiracial-spider-man",
        "http://thecolbertreport.cc.com/videos/f3w320/threatdown---fake-states--sharia-weather---monopoly",
        "http://thecolbertreport.cc.com/videos/cvc16w/women-s-health-nazi-plan",
        "http://thecolbertreport.cc.com/videos/6x0m3y/robert-wittman",
        "http://thecolbertreport.cc.com/videos/utsxoh/sign-off---official-flag-updater"
      ],
      "guest": "Robert Wittman"
    },
    {
      "date": "2011-08-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t3bxny/intro---8-4-11",
        "http://thecolbertreport.cc.com/videos/8tx5s2/barack-obama-s-50th-birthday",
        "http://thecolbertreport.cc.com/videos/7ahjkr/colbert-super-pac---the-heroes-respond",
        "http://thecolbertreport.cc.com/videos/ma6ejy/wisconsin-s-recall-election---americans-for-prosperity-s-absentee-ballot-typos",
        "http://thecolbertreport.cc.com/videos/8q9pe2/sport-report---baseball-s-lowest-records---mlb-s-twitter-feed",
        "http://thecolbertreport.cc.com/videos/d8704f/anthony-bourdain",
        "http://thecolbertreport.cc.com/videos/afj5qe/sign-off---goodnight"
      ],
      "guest": "Anthony Bourdain"
    },
    {
      "date": "2011-08-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/smerqo/america-s-credit-downgrade",
        "http://thecolbertreport.cc.com/videos/y7x3es/colbert-super-pac---rick-perry-for-president",
        "http://thecolbertreport.cc.com/videos/lu1v74/doomsday-bargain-bunkers",
        "http://thecolbertreport.cc.com/videos/wkairk/nassir-ghaemi",
        "http://thecolbertreport.cc.com/videos/4zkkn5/sign-off---stephen-sniffs-a-marker"
      ],
      "guest": "Nassir Ghaemi"
    },
    {
      "date": "2011-08-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tufpnm/intro---8-9-11",
        "http://thecolbertreport.cc.com/videos/pxptx8/heatsteria",
        "http://thecolbertreport.cc.com/videos/rtqznl/the-word---head-in-the-cloud",
        "http://thecolbertreport.cc.com/videos/gj6vb5/ric-ocasek"
      ],
      "guest": "The Cars"
    },
    {
      "date": "2011-08-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mjvryb/intro---8-10-11",
        "http://thecolbertreport.cc.com/videos/1jlwac/hooker-drawer-market",
        "http://thecolbertreport.cc.com/videos/cw4el2/yahweh-or-no-way---mormons---god-s-poll-numbers",
        "http://thecolbertreport.cc.com/videos/uulxb3/god-s-job-performance---jim-martin",
        "http://thecolbertreport.cc.com/videos/15zleh/colbert-super-pac---campaign-donation-addiction",
        "http://thecolbertreport.cc.com/videos/zxka8u/elliot-ackerman",
        "http://thecolbertreport.cc.com/videos/mvgmwy/sign-off---e-mailing-colbert-nation"
      ],
      "guest": "Elliott Ackerman"
    },
    {
      "date": "2011-08-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pi19ix/super-pac-ad---behind-the-green-corn",
        "http://thecolbertreport.cc.com/videos/x1aodj/super-pac-ad---episode-iv--a-new-hope",
        "http://thecolbertreport.cc.com/videos/etbj36/romney-2012----corporations-are-people-",
        "http://thecolbertreport.cc.com/videos/90ptp7/colbert-super-pac---rick-parry-with-an--a--for-america",
        "http://thecolbertreport.cc.com/videos/swbu9s/colbert-super-pac---confused-by-rick-parry-with-an--a--for-america",
        "http://thecolbertreport.cc.com/videos/yu257u/gloria-steinem",
        "http://thecolbertreport.cc.com/videos/7x3ryp/sign-off---stephen-s-emmy-award"
      ],
      "guest": "Gloria Steinem"
    },
    {
      "date": "2011-08-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/40fotx/exclusive---susan-rice-extended-interview-pt--1",
        "http://thecolbertreport.cc.com/videos/vvlrva/exclusive---susan-rice-extended-interview-pt--2",
        "http://thecolbertreport.cc.com/videos/lqjncy/susan-rice-extended-interview-pt--3",
        "http://thecolbertreport.cc.com/videos/0yyo1z/colbert-super-pac---stephen-apologizes-to-woi-in-des-moines",
        "http://thecolbertreport.cc.com/videos/dzchwi/colbert-super-pac---iowa-straw-poll-results",
        "http://thecolbertreport.cc.com/videos/dkh4ps/susan-rice-pt--1",
        "http://thecolbertreport.cc.com/videos/nla0b4/susan-rice-pt--2",
        "http://thecolbertreport.cc.com/videos/1rtsq5/sign-off---full-susan-rice-interview-online"
      ],
      "guest": "Amb. Susan Rice"
    },
    {
      "date": "2011-08-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i0nwuy/exclusive---space-shuttle-atlantis-crew---extended-interview-pt--1",
        "http://thecolbertreport.cc.com/videos/8gjrx4/exclusive---space-shuttle-atlantis-crew---extended-interview-pt--2",
        "http://thecolbertreport.cc.com/videos/rmrfc3/the-etymology-of--obamacare-",
        "http://thecolbertreport.cc.com/videos/cjfda6/colbert-super-pac---persuadulux-6000",
        "http://thecolbertreport.cc.com/videos/m00z1i/colbert-super-pac---frank-luntz-commits-to-the-pac",
        "http://thecolbertreport.cc.com/videos/a8v2gy/nasa-s-greatest-moments-montage",
        "http://thecolbertreport.cc.com/videos/nnfhdg/chris-ferguson--doug-hurley--rex-walheim---sandy-magnus",
        "http://thecolbertreport.cc.com/videos/h83o7v/sign-off---stephen-s-launch-pad-nut"
      ],
      "guest": "STS-135 astronauts"
    },
    {
      "date": "2011-08-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/brmz0s/exclusive---jeff-bridges-for-summer-s-eve",
        "http://thecolbertreport.cc.com/videos/1cvtnm/intro---8-17-11",
        "http://thecolbertreport.cc.com/videos/yk47i3/colbert-super-pac---rick-perry-s-treasurer",
        "http://thecolbertreport.cc.com/videos/uiim37/tip-wag---evangelical-scientists---rick-santorum",
        "http://thecolbertreport.cc.com/videos/4km5oi/jeff-bridges",
        "http://thecolbertreport.cc.com/videos/1bb0sg/sign-off---jeff-bridges--album-cover"
      ],
      "guest": "Jeff Bridges"
    },
    {
      "date": "2011-08-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/237rh7/intro---8-18-11",
        "http://thecolbertreport.cc.com/videos/oqd808/russia-s-james-bonds-vs--america-s-barack-obama",
        "http://thecolbertreport.cc.com/videos/j31bbb/colbert-super-pac---parry-with-an-a-gate----day-6---we-may-have-did-it-",
        "http://thecolbertreport.cc.com/videos/94c0x7/colbert-super-pac---parry-with-an-a-gate----day-6---woi-in-des-moines-reports",
        "http://thecolbertreport.cc.com/videos/ger41z/anderson-cooper-s-kryptonite",
        "http://thecolbertreport.cc.com/videos/1yhudu/kevin-mitnick",
        "http://thecolbertreport.cc.com/videos/5r0lwc/sign-off---woi-in-des-moines"
      ],
      "guest": "Kevin Mitnick"
    },
    {
      "date": "2011-09-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s3kv9p/michele-bachmann-s-natural-disaster-metaphor",
        "http://thecolbertreport.cc.com/videos/fk34r7/the-word---happy-endings",
        "http://thecolbertreport.cc.com/videos/ovw3t4/cheating-death---placebocisers---vaxamalgam",
        "http://thecolbertreport.cc.com/videos/1cua0e/tim-pawlenty",
        "http://thecolbertreport.cc.com/videos/d2roue/sign-off---placebocisers"
      ],
      "guest": "Gov. Tim Pawlenty"
    },
    {
      "date": "2011-09-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1iqy2m/intro---9-7-11",
        "http://thecolbertreport.cc.com/videos/nw0vtw/this-weak-in-national-secowardty",
        "http://thecolbertreport.cc.com/videos/dhg1or/martin-luther-king-jr--memorial-paraphrase",
        "http://thecolbertreport.cc.com/videos/796niz/parry-with-an-a-gate----day-26---update",
        "http://thecolbertreport.cc.com/videos/h8ndj7/robin-wright",
        "http://thecolbertreport.cc.com/videos/we0bnb/sign-off---stephen-uses-his-ipad"
      ],
      "guest": "Robin B. Wright"
    },
    {
      "date": "2011-09-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6ut02o/republican-presidential-debate-media-coverage",
        "http://thecolbertreport.cc.com/videos/0yghln/rick-perry-presents",
        "http://thecolbertreport.cc.com/videos/pf00vn/barack-obama-s-jobs-speech",
        "http://thecolbertreport.cc.com/videos/5x0a3c/tom-brokaw",
        "http://thecolbertreport.cc.com/videos/lwsx3m/sign-off---old-milwaukee-beer"
      ],
      "guest": "Tom Brokaw"
    },
    {
      "date": "2011-09-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3ooncl/tea-party-face-off-preview",
        "http://thecolbertreport.cc.com/videos/4ig8mh/stephen-reports-on-an-old-fashioned-hero",
        "http://thecolbertreport.cc.com/videos/eicjwv/shopping-griefportunities",
        "http://thecolbertreport.cc.com/videos/sxy47f/diane-sawyer",
        "http://thecolbertreport.cc.com/videos/g2jfq9/sign-off---stephen-s-mug"
      ],
      "guest": "Diane Sawyer"
    },
    {
      "date": "2011-09-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bgo24q/intro---9-13-11",
        "http://thecolbertreport.cc.com/videos/6jpgl3/cnn-tea-party-republican-debate",
        "http://thecolbertreport.cc.com/videos/swyrcg/barack-obama-s-american-jobs-act",
        "http://thecolbertreport.cc.com/videos/q1hw3n/barack-obama-s-american-jobs-act---paul-krugman",
        "http://thecolbertreport.cc.com/videos/t7gpb8/ron-paul-2012",
        "http://thecolbertreport.cc.com/videos/2cr39e/al-gore",
        "http://thecolbertreport.cc.com/videos/e1gewo/sign-off----stephen-colbert-"
      ],
      "guest": "Al Gore"
    },
    {
      "date": "2011-09-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/thyhg7/jobs-bill-clipgate",
        "http://thecolbertreport.cc.com/videos/gvt0ij/return-to-sender",
        "http://thecolbertreport.cc.com/videos/3h08e2/return-to-sender---phil-rubio",
        "http://thecolbertreport.cc.com/videos/gz48mn/rick-perry-s-hpv-vaccine-mandate",
        "http://thecolbertreport.cc.com/videos/dx27ks/michael-moore",
        "http://thecolbertreport.cc.com/videos/3rxw2x/sign-off---goodnight"
      ],
      "guest": "Michael Moore"
    },
    {
      "date": "2011-09-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jgxmci/intro---9-15-11",
        "http://thecolbertreport.cc.com/videos/rte3k7/take-a-billion--leave-a-billion",
        "http://thecolbertreport.cc.com/videos/15vhbi/the-other-american-jobs-act",
        "http://thecolbertreport.cc.com/videos/rje3k2/jimmy-fallon---stephen-reminisce",
        "http://thecolbertreport.cc.com/videos/h90n13/fema-s-waffle-house-index",
        "http://thecolbertreport.cc.com/videos/b406bd/david-copperfield",
        "http://thecolbertreport.cc.com/videos/7m5lpn/sign-off---stephen-s-magic-trick"
      ],
      "guest": "David Copperfield"
    },
    {
      "date": "2011-09-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tpoc1g/the-63rd-emmy-awards",
        "http://thecolbertreport.cc.com/videos/whouap/barack-obama-unveils-the--buffett-rule-",
        "http://thecolbertreport.cc.com/videos/pyq49u/the-word---death-and-taxes",
        "http://thecolbertreport.cc.com/videos/3q875w/the-gayest-penetration",
        "http://thecolbertreport.cc.com/videos/xnvm51/jeffrey-kluger",
        "http://thecolbertreport.cc.com/videos/t0vjb4/sign-off---colbert-nation-s-newest-members"
      ],
      "guest": "Jeffrey Kluger"
    },
    {
      "date": "2011-09-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hc8ova/intro---9-21-11",
        "http://thecolbertreport.cc.com/videos/negwpt/coming-soon---hour-long-radiohead-special",
        "http://thecolbertreport.cc.com/videos/kyxdz3/european-union-collapse---war-fueled-recovery",
        "http://thecolbertreport.cc.com/videos/t51ow7/european-union-collapse---war-fueled-recovery---chrystia-freeland",
        "http://thecolbertreport.cc.com/videos/wvyk91/wall-street-under-siege",
        "http://thecolbertreport.cc.com/videos/z0celp/daniel-yergin",
        "http://thecolbertreport.cc.com/videos/y9o1cm/sign-off---cigar"
      ],
      "guest": "Daniel Yergin"
    },
    {
      "date": "2011-09-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9dc7h4/defunct-satellite-hurtles-toward-earth",
        "http://thecolbertreport.cc.com/videos/szcqls/tip-wag---marine-corps---department-of-homeland-security",
        "http://thecolbertreport.cc.com/videos/6uyhy5/obama-s-u-n--gaffes---rick-perry-s-support-for-israel",
        "http://thecolbertreport.cc.com/videos/ncny69/jeremy-ben-ami",
        "http://thecolbertreport.cc.com/videos/akoxfi/sign-off---the-beloved-dog-lives-on"
      ],
      "guest": "Jeremy Ben-Ami"
    },
    {
      "date": "2011-09-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1w32i4/intro---9-26-11",
        "http://thecolbertreport.cc.com/videos/p9c0ds/dr-pepper-presents-stephen-colbert-s-rocktember-with-radiohead",
        "http://thecolbertreport.cc.com/videos/u4qbft/the-word---i-think--therefore-i-brand",
        "http://thecolbertreport.cc.com/videos/grlcgn/radiohead",
        "http://thecolbertreport.cc.com/videos/xqeu3w/ignoring-global-warming",
        "http://thecolbertreport.cc.com/videos/wwvu7o/ignoring-global-warming---thom-yorke---ed-o-brien"
      ],
      "guest": "Radiohead"
    },
    {
      "date": "2011-09-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9qb4vy/stephen---melinda-gates-foundation---donorschoose-org",
        "http://thecolbertreport.cc.com/videos/tsm4sg/rick-perry-s-debate-gaffe---arizona-s-primary-date",
        "http://thecolbertreport.cc.com/videos/5mvmay/sport-report---nascar-s-green-initiatives---nfl-pat-downs",
        "http://thecolbertreport.cc.com/videos/ptxagr/melinda-gates",
        "http://thecolbertreport.cc.com/videos/zlthc8/sign-off---beer-from-the-beerkenstocks"
      ],
      "guest": "Melinda Gates"
    },
    {
      "date": "2011-09-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3qibl4/intro---9-28-11",
        "http://thecolbertreport.cc.com/videos/udzuyb/george-clooney-s-villa-parties",
        "http://thecolbertreport.cc.com/videos/tbuq71/the-word---labor-chains",
        "http://thecolbertreport.cc.com/videos/3qmkez/atone-phone---john-lithgow-calls",
        "http://thecolbertreport.cc.com/videos/ndmtp9/ken-burns",
        "http://thecolbertreport.cc.com/videos/osmia6/sign-off---reading---shofar-playing"
      ],
      "guest": "Ken Burns"
    },
    {
      "date": "2011-09-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0agwtq/mark-cuban-dances",
        "http://thecolbertreport.cc.com/videos/ivvzeu/colbert-super-pac---ham-rove-s-secrets",
        "http://thecolbertreport.cc.com/videos/3yzu4u/colbert-super-pac---trevor-potter---stephen-s-shell-corporation",
        "http://thecolbertreport.cc.com/videos/ujyuht/colbert-super-pac-shh----the-donating-game",
        "http://thecolbertreport.cc.com/videos/qiwg3k/mark-cuban",
        "http://thecolbertreport.cc.com/videos/8ekdsc/sign-off---last-heroe--crawl"
      ],
      "guest": "Mark Cuban"
    },
    {
      "date": "2011-10-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fehwjq/rick-perry-s-questionably-named-hunting-camp",
        "http://thecolbertreport.cc.com/videos/m272fc/supreme-courting-season",
        "http://thecolbertreport.cc.com/videos/v2njjc/supreme-courting-season---jeffrey-toobin",
        "http://thecolbertreport.cc.com/videos/25ffk2/threatdown---bears-in-rehab--bear-terminators---sanctimonious-enviro-bears",
        "http://thecolbertreport.cc.com/videos/wmazj5/jerome-groopman",
        "http://thecolbertreport.cc.com/videos/kp6658/sign-off---stephen-s-water-bottle"
      ],
      "guest": "Jerome Groopman"
    },
    {
      "date": "2011-10-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wy82eg/intro---10-4-11",
        "http://thecolbertreport.cc.com/videos/3wq74s/chris-christie-2012",
        "http://thecolbertreport.cc.com/videos/3dpzet/chris-christie-2012---rick-davis",
        "http://thecolbertreport.cc.com/videos/cwuy2m/bocephus-s-eternal-question",
        "http://thecolbertreport.cc.com/videos/xhc68w/john-lithgow",
        "http://thecolbertreport.cc.com/videos/n16lxn/sign-off---formula-401-rumors"
      ],
      "guest": "John Lithgow"
    },
    {
      "date": "2011-10-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0vn7mh/intro---10-5-11",
        "http://thecolbertreport.cc.com/videos/xnxfq5/herman-cain-2012",
        "http://thecolbertreport.cc.com/videos/dbbjic/herman-cain-2012---gay-choice",
        "http://thecolbertreport.cc.com/videos/6kkk93/tip-wag---mexico-city-marriage-licenses---modern-warfare-3-s-xp-promotion",
        "http://thecolbertreport.cc.com/videos/ifegp7/talib-kweli---yasiin-bey--a-k-a--mos-def-",
        "http://thecolbertreport.cc.com/videos/7edjef/sign-off---iphone-goodnight"
      ],
      "guest": "Mos Def &amp; Talib Kweli"
    },
    {
      "date": "2011-10-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0qyxlz/colbert-super-pac-ad---foul-balls",
        "http://thecolbertreport.cc.com/videos/fri8e1/intro---10-6-11",
        "http://thecolbertreport.cc.com/videos/z103m6/sarah-palin-s-sad-news",
        "http://thecolbertreport.cc.com/videos/yarfv2/colbert-super-pac-shh----apology-to-ham-rove",
        "http://thecolbertreport.cc.com/videos/fottda/tribute-to-steve-jobs",
        "http://thecolbertreport.cc.com/videos/98xl59/jason-amerine",
        "http://thecolbertreport.cc.com/videos/oy1k9u/sign-off---goodnight"
      ],
      "guest": "Jason Amerine"
    },
    {
      "date": "2011-10-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nng5h7/exclusive---harry-belafonte-extended-interview",
        "http://thecolbertreport.cc.com/videos/gj3y6l/occupy-wall-street-spreads",
        "http://thecolbertreport.cc.com/videos/z27tp0/the-word---look-out-for-the-little-guy",
        "http://thecolbertreport.cc.com/videos/6vl2zq/sport-report---nba-lockout---colbert-super-pac-ad",
        "http://thecolbertreport.cc.com/videos/01fxlb/harry-belafonte",
        "http://thecolbertreport.cc.com/videos/s0qu24/sign-off---goodnight"
      ],
      "guest": "Harry Belafonte"
    },
    {
      "date": "2011-10-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h40j2n/talking-iphone-4s",
        "http://thecolbertreport.cc.com/videos/ta7e7u/herman-cain-s-electrified-fence",
        "http://thecolbertreport.cc.com/videos/cbwqbb/thought-for-food---school-potato-guidelines---fast-food-stamps",
        "http://thecolbertreport.cc.com/videos/3h8h2l/steven-pinker",
        "http://thecolbertreport.cc.com/videos/9c1bsf/sign-off---sixth-anniversary-portrait"
      ],
      "guest": "Steven Pinker"
    },
    {
      "date": "2011-10-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iirczx/intro---10-19-11",
        "http://thecolbertreport.cc.com/videos/gghhza/herman-cain-canes-the-unemployed",
        "http://thecolbertreport.cc.com/videos/ubi151/job-killing-epa",
        "http://thecolbertreport.cc.com/videos/zi48pt/job-killing-epa---carol-browner",
        "http://thecolbertreport.cc.com/videos/f49qpp/rush-limbaugh-s-l-r-a--research",
        "http://thecolbertreport.cc.com/videos/fztuzs/ali-soufan",
        "http://thecolbertreport.cc.com/videos/kodm5a/sign-off---laptop-music"
      ],
      "guest": "Ali Soufan"
    },
    {
      "date": "2011-10-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n73wq4/intro---10-20-11",
        "http://thecolbertreport.cc.com/videos/5p2a33/goodbye--muammar-al-gaddafi",
        "http://thecolbertreport.cc.com/videos/5xgc3k/tip-wag---tea-party-nation-pledge---spirit-airlines--ad-revenue",
        "http://thecolbertreport.cc.com/videos/ql433h/bill-o-reilly-s--pinheads---patriots-",
        "http://thecolbertreport.cc.com/videos/qw2pao/chris-martin"
      ],
      "guest": "Coldplay"
    },
    {
      "date": "2011-10-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x027jm/exclusive---colbert-super-pac---frank-luntz---stephen-knows-his-classic-rock",
        "http://thecolbertreport.cc.com/videos/f8t1zf/america-s-top-mormons---jon-huntsman",
        "http://thecolbertreport.cc.com/videos/45wqla/colbert-super-pac----corporations-are-people-",
        "http://thecolbertreport.cc.com/videos/6s8sdq/colbert-super-pac----corporations-are-people----frank-luntz",
        "http://thecolbertreport.cc.com/videos/5jjhhv/colbert-super-pac----corporations-are-people----frank-luntz-s-focus-group",
        "http://thecolbertreport.cc.com/videos/541ucf/jon-huntsman",
        "http://thecolbertreport.cc.com/videos/53t2yg/sign-off---goodnight"
      ],
      "guest": "Jon Huntsman"
    },
    {
      "date": "2011-10-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s25oo4/intro---10-25-11",
        "http://thecolbertreport.cc.com/videos/darfes/steve-jobs--biography",
        "http://thecolbertreport.cc.com/videos/3uz7qn/herman-cain-s-campaign-ad",
        "http://thecolbertreport.cc.com/videos/n2dzu0/flogging-the-americone-dream",
        "http://thecolbertreport.cc.com/videos/wsqtx0/susan-saladoff",
        "http://thecolbertreport.cc.com/videos/89ebii/sign-off---enjoying-americone-dream"
      ],
      "guest": "Susan Saladoff"
    },
    {
      "date": "2011-10-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lj5z4k/colbert-super-pac-ad---ball-gag",
        "http://thecolbertreport.cc.com/videos/xlwljf/exclusive---hey--remember-this--alabama-",
        "http://thecolbertreport.cc.com/videos/fa0w0c/intro---10-26-11",
        "http://thecolbertreport.cc.com/videos/zwe40u/whales-aren-t-people",
        "http://thecolbertreport.cc.com/videos/7rtf6k/alabama-s-migrant-workers",
        "http://thecolbertreport.cc.com/videos/dcq3ky/war-on-halloween---costume-swapping---jesus-ween",
        "http://thecolbertreport.cc.com/videos/sqeewv/taylor-branch",
        "http://thecolbertreport.cc.com/videos/6twlww/sign-off---don-t-buy-these-books"
      ],
      "guest": "Taylor Branch"
    },
    {
      "date": "2011-10-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hfaq0j/intro---10-27-11",
        "http://thecolbertreport.cc.com/videos/gmesd4/shockupy-wall-street-fad",
        "http://thecolbertreport.cc.com/videos/xhn542/sport-report---nfl-fines---colbert-super-pac-s-second-nba-lockout-ad",
        "http://thecolbertreport.cc.com/videos/s2ax4o/toby-keith"
      ],
      "guest": "Toby Keith"
    },
    {
      "date": "2011-10-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l7lj84/sexy-costume-discrimination",
        "http://thecolbertreport.cc.com/videos/0svkvx/colbert-super-pac---occupy-wall-street-co-optportunity",
        "http://thecolbertreport.cc.com/videos/d4hmi3/colbert-super-pac---stephen-colbert-occupies-occupy-wall-street-pt--1",
        "http://thecolbertreport.cc.com/videos/4tqlz9/tip-wag---gun-freedom---healthcare-bartering",
        "http://thecolbertreport.cc.com/videos/n0jrmj/neil-macgregor",
        "http://thecolbertreport.cc.com/videos/tyvfoe/sign-off---goodnight"
      ],
      "guest": "Neil MacGregor"
    },
    {
      "date": "2011-11-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9346zn/intro---11-1-11",
        "http://thecolbertreport.cc.com/videos/ysh9bq/herman-cain-under-attack",
        "http://thecolbertreport.cc.com/videos/hqjgoz/colbert-super-pac---stephen-colbert-occupies-occupy-wall-street-pt--2",
        "http://thecolbertreport.cc.com/videos/yo2avl/yo-yo-ma--stuart-duncan--edgar-meyer---chris-thile",
        "http://thecolbertreport.cc.com/videos/pez22q/sign-off---goodnight"
      ],
      "guest": "Yo-Yo Ma"
    },
    {
      "date": "2011-11-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/394xx1/intro---11-2-11",
        "http://thecolbertreport.cc.com/videos/n3ifbc/herman-cain-s-international-affairs",
        "http://thecolbertreport.cc.com/videos/icx1x6/the-word---bite-the-hand-that-feeds-you",
        "http://thecolbertreport.cc.com/videos/6dlo6v/muffingate",
        "http://thecolbertreport.cc.com/videos/6jv4ha/michael-pollan",
        "http://thecolbertreport.cc.com/videos/c8yk04/sign-off---white-castle---beer"
      ],
      "guest": "Michael Pollan"
    },
    {
      "date": "2011-11-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/db8sp6/intro---11-3-11",
        "http://thecolbertreport.cc.com/videos/tvwydl/ghost-sex",
        "http://thecolbertreport.cc.com/videos/gxg7x0/european-investment-prospectus",
        "http://thecolbertreport.cc.com/videos/2nhcbh/colbert-super-pac---herman-cain-s-fundraising---rush-limbaugh-s-stereotypes",
        "http://thecolbertreport.cc.com/videos/rwwdgv/nathan-wolfe",
        "http://thecolbertreport.cc.com/videos/g7b66l/sign-off---purell"
      ],
      "guest": "Nathan Wolfe"
    },
    {
      "date": "2011-11-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/px6doe/colbert-super-pac---issue-ads",
        "http://thecolbertreport.cc.com/videos/otywae/colbert-super-pac---issue-ads---trevor-potter",
        "http://thecolbertreport.cc.com/videos/6nuhjw/blood-in-the-water---larry-taylor-s-anti-semitic-slur",
        "http://thecolbertreport.cc.com/videos/xisem8/niall-ferguson",
        "http://thecolbertreport.cc.com/videos/e9gc1y/sign-off---goodnight"
      ],
      "guest": "Niall Ferguson"
    },
    {
      "date": "2011-11-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m4n0nh/herman-cain-won-t-be-stopped",
        "http://thecolbertreport.cc.com/videos/yk540u/colbert-platinum---wealth-under-siege",
        "http://thecolbertreport.cc.com/videos/3krrxg/the-blitzkrieg-on-grinchitude---fired-santa-claus---colbert-super-pac-christmas",
        "http://thecolbertreport.cc.com/videos/s4sqap/seth-meyers",
        "http://thecolbertreport.cc.com/videos/fz9les/sign-off---custom-escape-yacht"
      ],
      "guest": "Seth Meyers"
    },
    {
      "date": "2011-11-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qc00ca/intro---11-9-11",
        "http://thecolbertreport.cc.com/videos/gs7ppt/herman-cain-s-democrat-conspiracy",
        "http://thecolbertreport.cc.com/videos/e94bhi/the-word---bully-pulpit",
        "http://thecolbertreport.cc.com/videos/v1f4n3/americone-dream-of-the-future",
        "http://thecolbertreport.cc.com/videos/3k5pcf/james-martin",
        "http://thecolbertreport.cc.com/videos/9mrd4k/sign-off---feeding-jimmy-fallon-s-portrait"
      ],
      "guest": "Father Jim Martin"
    },
    {
      "date": "2011-11-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qfc9xd/shock---aussie",
        "http://thecolbertreport.cc.com/videos/pg0q9t/rick-perry-s-sorry--oops",
        "http://thecolbertreport.cc.com/videos/g1tcu5/occupy-u-c--berkeley",
        "http://thecolbertreport.cc.com/videos/4vt0hx/brian-eno"
      ],
      "guest": "Brian Eno"
    },
    {
      "date": "2011-11-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ufww4s/intro---11-14-11",
        "http://thecolbertreport.cc.com/videos/3zodum/cbs-snubs-michele-bachmann",
        "http://thecolbertreport.cc.com/videos/5vb30b/keystone-xl-oil-pipeline---bill-mckibben",
        "http://thecolbertreport.cc.com/videos/hu2y6t/vodka-tampons",
        "http://thecolbertreport.cc.com/videos/uoo5c0/thomas-thwaites",
        "http://thecolbertreport.cc.com/videos/9x16t1/sign-off---leaf-blower"
      ],
      "guest": "Thomas Thwaites"
    },
    {
      "date": "2011-11-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c73ioe/occupy-wall-street-decamped",
        "http://thecolbertreport.cc.com/videos/qzjgvi/difference-makers---jimmy-justice",
        "http://thecolbertreport.cc.com/videos/ufsd5o/bears---balls---celebrity-relics---gooooooold-",
        "http://thecolbertreport.cc.com/videos/f1tu06/elijah-wood",
        "http://thecolbertreport.cc.com/videos/0vuu1j/sign-off---one-ring"
      ],
      "guest": "Elijah Wood"
    },
    {
      "date": "2011-11-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/znljdd/intro---11-16-11",
        "http://thecolbertreport.cc.com/videos/ukaw6z/newt-gingrich-s-greek-cruise",
        "http://thecolbertreport.cc.com/videos/6dwdiy/tip-wag---pin-ups-for-ron-paul--movie-torture-tactics---offensive-merchandise",
        "http://thecolbertreport.cc.com/videos/z9qeks/elderly-occupier-pepper-sprayed",
        "http://thecolbertreport.cc.com/videos/94gywl/chris-matthews",
        "http://thecolbertreport.cc.com/videos/aekw8v/colbert-report-bedtime-stories---dragon---wizard"
      ],
      "guest": "Chris Matthews"
    },
    {
      "date": "2011-11-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hnwps8/intro---11-17-11",
        "http://thecolbertreport.cc.com/videos/41apq9/people-magazine-s-sexiest-man-alive-2011",
        "http://thecolbertreport.cc.com/videos/wdsxo5/the-word---the-1-",
        "http://thecolbertreport.cc.com/videos/h76098/thought-for-food---pushy-pops",
        "http://thecolbertreport.cc.com/videos/y88hzi/susan-orlean",
        "http://thecolbertreport.cc.com/videos/8d1q2a/sign-off---shout-out-to-the-black-belles"
      ],
      "guest": "Susan Orlean"
    },
    {
      "date": "2011-11-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/no4xhk/intro---11-28-11",
        "http://thecolbertreport.cc.com/videos/58ikdq/violent-black-friday",
        "http://thecolbertreport.cc.com/videos/h84vbf/tip-wag---barack-obama-s-omission--mitt-romney-s-ad---lululemon-s-tagline",
        "http://thecolbertreport.cc.com/videos/qggo98/stephen-colbert-s-mereporters",
        "http://thecolbertreport.cc.com/videos/ut1g77/siddhartha-mukherjee",
        "http://thecolbertreport.cc.com/videos/np8x21/sign-off---macbook"
      ],
      "guest": "Siddhartha Mukherjee"
    },
    {
      "date": "2011-11-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/92ekqe/intro---11-29-11",
        "http://thecolbertreport.cc.com/videos/fafzt9/he-said--she-said--she-said--she-said--she-said--she-was-paid-not-to-say",
        "http://thecolbertreport.cc.com/videos/r8p3nn/yahweh-or-no-way---altered-catholic-mass--papal-seat-belt---offensive-vodka-ad",
        "http://thecolbertreport.cc.com/videos/4dohxr/tinariwen-with-kyp-malone---tunde-adebimpe",
        "http://thecolbertreport.cc.com/videos/9nbfru/sign-off---tinariwen--album"
      ],
      "guest": "Tinariwen"
    },
    {
      "date": "2011-11-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fc3loc/newt-gingrich-denies-lobbying",
        "http://thecolbertreport.cc.com/videos/akure9/barney-frank-s-retirement",
        "http://thecolbertreport.cc.com/videos/d0x6zg/better-know-a-district---massachusetts--4th---barney-frank-update",
        "http://thecolbertreport.cc.com/videos/j1oeb0/conservative-siri",
        "http://thecolbertreport.cc.com/videos/okgz78/stephen-sondheim",
        "http://thecolbertreport.cc.com/videos/ga76kd/sign-off---goodnight"
      ],
      "guest": "Stephen Sondheim"
    },
    {
      "date": "2011-12-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eclhxy/in-herman-cain-s-defense",
        "http://thecolbertreport.cc.com/videos/70sj7m/stop-online-piracy-act",
        "http://thecolbertreport.cc.com/videos/nmrgz9/stop-online-piracy-act---danny-goldberg---jonathan-zittrain",
        "http://thecolbertreport.cc.com/videos/pzi69s/mitt-romney-gets-testy",
        "http://thecolbertreport.cc.com/videos/pmypbg/richard-branson",
        "http://thecolbertreport.cc.com/videos/rhwqc7/sign-off---fire-extinguishing-powder"
      ],
      "guest": "Richard Branson"
    },
    {
      "date": "2011-12-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yy5x27/2011-kennedy-center-honors",
        "http://thecolbertreport.cc.com/videos/xn3r3g/mysteries-of-the-ancient-unknown---2012-end-of-times",
        "http://thecolbertreport.cc.com/videos/f2zdhx/herman-cain-drops-out",
        "http://thecolbertreport.cc.com/videos/dt8216/jimmie-johnson",
        "http://thecolbertreport.cc.com/videos/0ewfq6/sign-off---slow-motion-race-replay"
      ],
      "guest": "Jimmie Johnson"
    },
    {
      "date": "2011-12-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1o3huj/american-drone-in-iran",
        "http://thecolbertreport.cc.com/videos/fcu2h2/donald-s-trumptacular---stephen-s-south-carolina-serious--classy-republican-debate",
        "http://thecolbertreport.cc.com/videos/dphj6u/the-black-keys",
        "http://thecolbertreport.cc.com/videos/4t05a5/sign-off---glenn-eichler-s-graphic-novel"
      ],
      "guest": "The Black Keys"
    },
    {
      "date": "2011-12-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5kfnqe/stephen-colbert-s-south-carolina-serious--classy-republican-debate---save-the-date",
        "http://thecolbertreport.cc.com/videos/h7qfup/colbert-super-pac---stephen-s-south-carolina-referendum",
        "http://thecolbertreport.cc.com/videos/6dds1t/colbert-super-pac---stephen-s-south-carolina-referendum---dick-harpootlian",
        "http://thecolbertreport.cc.com/videos/c66w64/jon-huntsman-sr--s-ad-buy",
        "http://thecolbertreport.cc.com/videos/pueyvf/david-hallberg"
      ],
      "guest": "David Hallberg"
    },
    {
      "date": "2011-12-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/08g4y6/intro---12-8-11",
        "http://thecolbertreport.cc.com/videos/sd4lua/michigan-s-snow-cone-machines",
        "http://thecolbertreport.cc.com/videos/lbdchz/cheating-death---chicken-pox-lollipops---fecal-transplants",
        "http://thecolbertreport.cc.com/videos/3d10i3/rick-perry-s-pro-christmas-ad",
        "http://thecolbertreport.cc.com/videos/ovws10/jack-abramoff",
        "http://thecolbertreport.cc.com/videos/gt2hau/sign-off---goodnight"
      ],
      "guest": "Jack Abramoff"
    },
    {
      "date": "2011-12-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iu3gnx/intro---12-12-11",
        "http://thecolbertreport.cc.com/videos/52a05g/christmas-cram",
        "http://thecolbertreport.cc.com/videos/zuufyt/tip-wag---liberal-dictionary---newt-gingrich-alert",
        "http://thecolbertreport.cc.com/videos/qv9fb0/norway-s-butter-shortage",
        "http://thecolbertreport.cc.com/videos/kx2u80/samuel-l--jackson",
        "http://thecolbertreport.cc.com/videos/v6sdfa/sign-off---merry-christmas"
      ],
      "guest": "Samuel L. Jackson"
    },
    {
      "date": "2011-12-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rwb03h/intro---12-13-11",
        "http://thecolbertreport.cc.com/videos/7zgxss/trump-s-cancellation---stephen-s-south-carolina-serious--classy-re-announcement",
        "http://thecolbertreport.cc.com/videos/frhjj0/the-word---let-them-buy-cake",
        "http://thecolbertreport.cc.com/videos/flxy99/anderson-cooper-s-phallus-party-accusation",
        "http://thecolbertreport.cc.com/videos/sn7cpj/mark-whitaker",
        "http://thecolbertreport.cc.com/videos/eswjdg/sign-off---goodnight"
      ],
      "guest": "Mark Whitaker"
    },
    {
      "date": "2011-12-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/18wgz1/stephen-colbert-s-south-carolina-serious--classy-debate---nat-geo-wild-s-response",
        "http://thecolbertreport.cc.com/videos/khf3hx/christine-o-donnell-s-endorsement",
        "http://thecolbertreport.cc.com/videos/vg9vdy/stephen-colbert-s-big-gay-roundup---military-bestiality---homosexual-penguins",
        "http://thecolbertreport.cc.com/videos/qvom30/tv-hat",
        "http://thecolbertreport.cc.com/videos/lqslc3/ray-odierno"
      ],
      "guest": "Gen. Raymond Odierno"
    },
    {
      "date": "2011-12-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8900sr/stephen-colbert-s-south-carolina-serious--classy-republican-debate---network-battle",
        "http://thecolbertreport.cc.com/videos/dwccb9/the-blitzkrieg-on-grinchitude---department-store-cutbacks---gun-filled-christmas",
        "http://thecolbertreport.cc.com/videos/9ugow2/fox-news--mitt-romney-photo-flub",
        "http://thecolbertreport.cc.com/videos/iqj0p8/daniel-craig",
        "http://thecolbertreport.cc.com/videos/tri39n/2011-goodbye"
      ],
      "guest": "Daniel Craig"
    }
  ],
  "2012": [
    {
      "date": "2012-01-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9u9qx6/iowa-caucus-2012",
        "http://thecolbertreport.cc.com/videos/yx6r23/iowa-caucus---caucus-goer-s-choice",
        "http://thecolbertreport.cc.com/videos/5mqn59/iowa-caucus---megyn-shelly-s-prediction",
        "http://thecolbertreport.cc.com/videos/qx2w8n/kim-jong-il---in-memoriam",
        "http://thecolbertreport.cc.com/videos/ioguwl/bernie-sanders",
        "http://thecolbertreport.cc.com/videos/4ob0g2/sign-off---megyn-shelly"
      ],
      "guest": "Sen. Bernie Sanders"
    },
    {
      "date": "2012-01-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s8am6m/iowa-caucus---mitt-romney-s-victory-speech---rick-santorum-s-coup",
        "http://thecolbertreport.cc.com/videos/m762nz/iowa-caucus---not-mitt-romney-s-super-pac",
        "http://thecolbertreport.cc.com/videos/x195wh/iowa-caucus---cable-news-coverage",
        "http://thecolbertreport.cc.com/videos/61k2nf/iowa-caucus---woi-in-des-moines-reports",
        "http://thecolbertreport.cc.com/videos/1ja4vs/john-heilemann",
        "http://thecolbertreport.cc.com/videos/xyq4st/sign-off---erin-burnett-pong"
      ],
      "guest": "John Heilemann"
    },
    {
      "date": "2012-01-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8t37qs/intro---1-5-12",
        "http://thecolbertreport.cc.com/videos/js72my/fun-rick-santorum",
        "http://thecolbertreport.cc.com/videos/5xw4yi/the-word---catch-2012",
        "http://thecolbertreport.cc.com/videos/sjbolu/god-s-message-to-pat-robertson",
        "http://thecolbertreport.cc.com/videos/lgtesz/steve-case",
        "http://thecolbertreport.cc.com/videos/o6dbzj/sign-off---mayan-headwear---sacrificial-chicken"
      ],
      "guest": "Steve Case"
    },
    {
      "date": "2012-01-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y3wl1i/intro---1-9-12",
        "http://thecolbertreport.cc.com/videos/3m6txc/new-hampshire-gop-debates",
        "http://thecolbertreport.cc.com/videos/l08ywe/new-hampshire-gop-debates---moderate-extremes",
        "http://thecolbertreport.cc.com/videos/75c0w9/rick-santorum-on-gay-parents---bla-people",
        "http://thecolbertreport.cc.com/videos/e3zsob/melissa-harris-perry",
        "http://thecolbertreport.cc.com/videos/j2sskk/sign-off---jack-daniels"
      ],
      "guest": "Neil Shubin"
    },
    {
      "date": "2012-01-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9llvcg/new-hampshire-primary---mitt-romney-s-gaffe",
        "http://thecolbertreport.cc.com/videos/m98f4t/tip-wag---irresponsible-dead-people---insensitive-papa-john-s",
        "http://thecolbertreport.cc.com/videos/wwvi39/malice-in-blunderland",
        "http://thecolbertreport.cc.com/videos/fqk2fh/bill-moyers",
        "http://thecolbertreport.cc.com/videos/wdmkv8/sign-off---turntable"
      ],
      "guest": "Ben Gibbard"
    },
    {
      "date": "2012-01-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bxzp6z/intro---1-11-12",
        "http://thecolbertreport.cc.com/videos/f8j0ng/commitment-to-mitt-romney",
        "http://thecolbertreport.cc.com/videos/7t7ct3/south-carolina-s-fresh-face",
        "http://thecolbertreport.cc.com/videos/73ux63/stephen-colbert-s-end-of-the-world-of-the-week---phobos-grunt",
        "http://thecolbertreport.cc.com/videos/wx04iy/george-stephanopoulos",
        "http://thecolbertreport.cc.com/videos/vjhrm3/sign-off---decision-of-a-lifetime"
      ],
      "guest": "George Stephanopoulos"
    },
    {
      "date": "2012-01-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hrwtsb/colbert-super-pac---coordination-problem",
        "http://thecolbertreport.cc.com/videos/av6bvx/colbert-super-pac---coordination-resolution-with-jon-stewart",
        "http://thecolbertreport.cc.com/videos/5otlsk/mike-d-s-hip-hop-semantics",
        "http://thecolbertreport.cc.com/videos/ui35sv/mike-allen",
        "http://thecolbertreport.cc.com/videos/mnp9up/sign-off---ipad-ebook"
      ],
      "guest": "Mike Allen"
    },
    {
      "date": "2012-01-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dyktip/colbert-super-pac-ad---not-abel",
        "http://thecolbertreport.cc.com/videos/lec1ln/intro---1-16-12",
        "http://thecolbertreport.cc.com/videos/ke9tkw/jon-huntsman-out--rick-santorum-in",
        "http://thecolbertreport.cc.com/videos/buf78z/colbert-super-pac---mitt-romney-attack-ad",
        "http://thecolbertreport.cc.com/videos/uh4wcy/the-word---raise-cain",
        "http://thecolbertreport.cc.com/videos/cgtb89/scott-douglas",
        "http://thecolbertreport.cc.com/videos/td091t/sign-off----this-is-herman-cain--"
      ],
      "guest": "Rev. Scott Douglas"
    },
    {
      "date": "2012-01-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/knvkbe/colbert-super-pac-ad---double-negative",
        "http://thecolbertreport.cc.com/videos/fe4nep/intro---1-17-12",
        "http://thecolbertreport.cc.com/videos/ufvy9m/colbert-super-pac---gop-attack-ads---herman-cain-ad",
        "http://thecolbertreport.cc.com/videos/qil57h/yahweh-or-no-way---online-christian-dating---seven-days-of-sex",
        "http://thecolbertreport.cc.com/videos/0alvjc/jennifer-granholm",
        "http://thecolbertreport.cc.com/videos/mbnjnn/sign-off---vote-for-herman-cain"
      ],
      "guest": "Jennifer Granholm"
    },
    {
      "date": "2012-01-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bpbhtr/colbert-super-pac-ad---modern-stage-combat",
        "http://thecolbertreport.cc.com/videos/2f7upq/intro---1-18-12",
        "http://thecolbertreport.cc.com/videos/q6xocp/newt-gingrich-s-performance---mitt-romney-s-tax-returns",
        "http://thecolbertreport.cc.com/videos/fx3xum/stephen-s-approval-rating",
        "http://thecolbertreport.cc.com/videos/zvmmfs/colbert-super-pac---civility-ad---stephen-s-south-carolina-rally",
        "http://thecolbertreport.cc.com/videos/orzoc4/sopa---pipa",
        "http://thecolbertreport.cc.com/videos/i8qam3/david-frum",
        "http://thecolbertreport.cc.com/videos/3mfkme/sign-off---south-carolina-rally-with-herman-cain"
      ],
      "guest": "David Frum"
    },
    {
      "date": "2012-01-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pebyno/troubled-gop-waters---stephen-under-attack",
        "http://thecolbertreport.cc.com/videos/7qvxgu/colbert-super-pac---john-paul-stevens",
        "http://thecolbertreport.cc.com/videos/k3pbui/carrie-rebora-barratt",
        "http://thecolbertreport.cc.com/videos/nno4x3/sign-off---flight-to-charleston--sc"
      ],
      "guest": "Carrie Rebora Barratt"
    },
    {
      "date": "2012-01-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kachyg/intro---1-23-12",
        "http://thecolbertreport.cc.com/videos/iql42n/newt-gingrich-s-south-carolina-kill",
        "http://thecolbertreport.cc.com/videos/50z46i/herman-cain-s-bittersweet-south-carolina-victory",
        "http://thecolbertreport.cc.com/videos/e3y9nd/rock-me-like-a-herman-cain-south-cain-olina-primary-rally---cain-elot-revisited",
        "http://thecolbertreport.cc.com/videos/vim94y/bruce-bueno-de-mesquita",
        "http://thecolbertreport.cc.com/videos/gu52h0/sign-off---sniffing-a-marker"
      ],
      "guest": "Bruce Bueno De Mesquita"
    },
    {
      "date": "2012-01-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n2rnnr/exclusive---rock-me-like-a-herman-cain-south-cain-olina-primary-rally-pt--1",
        "http://thecolbertreport.cc.com/videos/jc76hc/exclusive---rock-me-like-a-herman-cain-south-cain-olina-primary-rally-pt--2",
        "http://thecolbertreport.cc.com/videos/jog4lt/intro---1-24-12",
        "http://thecolbertreport.cc.com/videos/q3ro37/colbert-super-pac---hostage-crisis---day-2",
        "http://thecolbertreport.cc.com/videos/zop8mz/18th-gop-debate",
        "http://thecolbertreport.cc.com/videos/gzi3ec/grim-colberty-tales-with-maurice-sendak-pt--1",
        "http://thecolbertreport.cc.com/videos/kg7hw1/rick-santorum-s-senior-pandering",
        "http://thecolbertreport.cc.com/videos/381zai/andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/14903e/sign-off---reading--bumble-ardy-"
      ],
      "guest": "Andrew Sullivan"
    },
    {
      "date": "2012-01-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9f0foj/2012-state-of-the-union-address---gop-rebuttals",
        "http://thecolbertreport.cc.com/videos/2uwi0i/grim-colberty-tales-with-maurice-sendak-pt--2",
        "http://thecolbertreport.cc.com/videos/3un4zv/un-american-news---china-edition",
        "http://thecolbertreport.cc.com/videos/kwuhk6/terry-gross",
        "http://thecolbertreport.cc.com/videos/r2j6o1/sign-off---colonel-tuxedo-s-cat-food"
      ],
      "guest": "Terry Gross"
    },
    {
      "date": "2012-01-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/05qh1w/colbert-super-pac---hostage-crisis---day-4",
        "http://thecolbertreport.cc.com/videos/5gcr8j/mitt-romney---newt-gingrich-in-florida",
        "http://thecolbertreport.cc.com/videos/pudtpb/sean-hannity-s--the-great-american-panel-",
        "http://thecolbertreport.cc.com/videos/y191mp/the-great-available-panel",
        "http://thecolbertreport.cc.com/videos/sg6jkh/drew-barrymore",
        "http://thecolbertreport.cc.com/videos/kk56ka/sign-off---football-throwing"
      ],
      "guest": "Drew Barrymore"
    },
    {
      "date": "2012-01-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rcm539/colbert-super-pac---the-great-chase",
        "http://thecolbertreport.cc.com/videos/1ws9v2/colbert-super-pac---return-of-the-pac",
        "http://thecolbertreport.cc.com/videos/n3pkmh/threatdown---barack-obama--fundamentalist-flippers---coked-up-diplomats",
        "http://thecolbertreport.cc.com/videos/tlfrhi/gop---the-hispanic-vote",
        "http://thecolbertreport.cc.com/videos/amck6x/laurence-tribe",
        "http://thecolbertreport.cc.com/videos/v9f5m2/sign-off---shouting-goodnight"
      ],
      "guest": "Laurence H. Tribe"
    },
    {
      "date": "2012-01-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/62pas5/intro---1-31-12",
        "http://thecolbertreport.cc.com/videos/f44hch/newt-gingrich-s-supporters",
        "http://thecolbertreport.cc.com/videos/udnnzi/the-word---american-history-x-d",
        "http://thecolbertreport.cc.com/videos/qs311n/bjork",
        "http://thecolbertreport.cc.com/videos/u7u9lh/sign-off----biophilia-"
      ],
      "guest": "Bjork"
    },
    {
      "date": "2012-02-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yk5cpe/intro---2-1-12",
        "http://thecolbertreport.cc.com/videos/o3p6c2/black-history-celebration-moment",
        "http://thecolbertreport.cc.com/videos/3nohh2/mitt-romney-s-florida-victory",
        "http://thecolbertreport.cc.com/videos/uswa0x/colbert-super-pac---americone-dream-super-pack",
        "http://thecolbertreport.cc.com/videos/kqctrf/ameena-matthews",
        "http://thecolbertreport.cc.com/videos/5m98im/sign-off---americone-dream-super-pack"
      ],
      "guest": "Ameena Matthews"
    },
    {
      "date": "2012-02-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4dia59/intro---2-2-12",
        "http://thecolbertreport.cc.com/videos/uu5zmj/the-meaning-of-groundhog-day",
        "http://thecolbertreport.cc.com/videos/bwbr2v/america-s-biggest-super-pac-donors",
        "http://thecolbertreport.cc.com/videos/lh3kq3/colbert-super-pac---thank-you",
        "http://thecolbertreport.cc.com/videos/04ottd/survivor-sues-newt-gingrich---dave-bickler",
        "http://thecolbertreport.cc.com/videos/a7r0zs/christiane-amanpour",
        "http://thecolbertreport.cc.com/videos/uzu0lz/sign-off---goodnight"
      ],
      "guest": "Christiane Amanpour"
    },
    {
      "date": "2012-02-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hhq4en/intro---2-13-12",
        "http://thecolbertreport.cc.com/videos/2kynbu/linsanity-",
        "http://thecolbertreport.cc.com/videos/hgxqxc/people-who-are-destroying-america---sawstop",
        "http://thecolbertreport.cc.com/videos/ju995r/stephen-colbert-s-free-americone-dream-day",
        "http://thecolbertreport.cc.com/videos/eks7za/bill-mckibben",
        "http://thecolbertreport.cc.com/videos/k6qadu/sign-off---colbert-nation-newborn"
      ],
      "guest": "Bill McKibben"
    },
    {
      "date": "2012-02-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u5h2yo/intro---2-14-12",
        "http://thecolbertreport.cc.com/videos/3rk6lv/westminster-kennel-club-dog-show-2012",
        "http://thecolbertreport.cc.com/videos/jx9ojl/contraception-crusade",
        "http://thecolbertreport.cc.com/videos/lyzukj/tip-wag---gay-building-marriage---transportation-safety-board-cell-phone-ban",
        "http://thecolbertreport.cc.com/videos/ej01p5/william-broad",
        "http://thecolbertreport.cc.com/videos/mhuyjx/sign-off---stephen-s-friend-lou-dog"
      ],
      "guest": "William Broad"
    },
    {
      "date": "2012-02-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f1ta15/intro---2-20-12",
        "http://thecolbertreport.cc.com/videos/7ghzcu/mitt-romney---donald-trump-in-michigan",
        "http://thecolbertreport.cc.com/videos/lydem1/rick-santorum-s-energy-war-alarm",
        "http://thecolbertreport.cc.com/videos/tqad40/ann-patchett",
        "http://thecolbertreport.cc.com/videos/qgsly5/sign-off---caught-looking"
      ],
      "guest": "Ann Patchett"
    },
    {
      "date": "2012-02-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vdtnp9/intro---2-21-12",
        "http://thecolbertreport.cc.com/videos/dgnc7d/douchebag-showdown",
        "http://thecolbertreport.cc.com/videos/mnahgd/colbert-super-pac---nancy-pelosi-s-ad---barack-obama-s-super-pac",
        "http://thecolbertreport.cc.com/videos/s0vtdx/robert-kagan",
        "http://thecolbertreport.cc.com/videos/x36uyb/sign-off---dark-lord-of-the-sith"
      ],
      "guest": "Robert Kagan"
    },
    {
      "date": "2012-02-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n05gam/intro---2-22-12",
        "http://thecolbertreport.cc.com/videos/krghr1/stephen-s-lenten-sacrifice",
        "http://thecolbertreport.cc.com/videos/dv9iqc/the-word---surrender-to-a-buyer-power",
        "http://thecolbertreport.cc.com/videos/w2qw1t/better-know-a-district---california-s-8th",
        "http://thecolbertreport.cc.com/videos/d6raxz/nancy-pelosi",
        "http://thecolbertreport.cc.com/videos/9mdx7s/sign-off---conquistador-sacrifice"
      ],
      "guest": "Rep. Nancy Pelosi"
    },
    {
      "date": "2012-02-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g3b2me/arizona-gop-debate",
        "http://thecolbertreport.cc.com/videos/6wnf2j/posthumous-mormon-baptism",
        "http://thecolbertreport.cc.com/videos/zzgfft/wheat-thins-sponsortunity",
        "http://thecolbertreport.cc.com/videos/jshg47/placido-domingo"
      ],
      "guest": "Placido Domingo"
    },
    {
      "date": "2012-02-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6llqzw/mitt-romney-s---rick-santorum-s-michigan-campaigns",
        "http://thecolbertreport.cc.com/videos/45yrtw/peggielene-bartels",
        "http://thecolbertreport.cc.com/videos/xr2dmf/sign-off---goodnight"
      ],
      "guest": "Peggielene Bartels"
    },
    {
      "date": "2012-02-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l484x8/intro---2-28-12",
        "http://thecolbertreport.cc.com/videos/b44eo3/the-colbert-report-s-1000th-show",
        "http://thecolbertreport.cc.com/videos/hsyhov/rising-oil-prices---john-kilduff",
        "http://thecolbertreport.cc.com/videos/gqa08a/mr--smith-goes-to-the-state-legislature--then-later-possibly-washington---bob-morris---kyle-jones",
        "http://thecolbertreport.cc.com/videos/0xatad/ross-eisenbrey",
        "http://thecolbertreport.cc.com/videos/8ebxgr/stephen-s-1000th-ticket"
      ],
      "guest": "Ross Eisenbrey"
    },
    {
      "date": "2012-02-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ueosv6/intro---2-29-12",
        "http://thecolbertreport.cc.com/videos/y0ejfo/countdown-to-loving-mitt",
        "http://thecolbertreport.cc.com/videos/3dllp7/the-word---change-we-can-believe-in",
        "http://thecolbertreport.cc.com/videos/3adb3i/tip-wag---kansas--male-birth-control-pill---new-york-s-babyccino",
        "http://thecolbertreport.cc.com/videos/puth71/william-shatner",
        "http://thecolbertreport.cc.com/videos/dhcxcx/sign-off---goodnight"
      ],
      "guest": "William Shatner"
    },
    {
      "date": "2012-03-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ueosv6/intro---2-29-12",
        "http://thecolbertreport.cc.com/videos/y0ejfo/countdown-to-loving-mitt",
        "http://thecolbertreport.cc.com/videos/3dllp7/the-word---change-we-can-believe-in",
        "http://thecolbertreport.cc.com/videos/3adb3i/tip-wag---kansas--male-birth-control-pill---new-york-s-babyccino",
        "http://thecolbertreport.cc.com/videos/puth71/william-shatner",
        "http://thecolbertreport.cc.com/videos/dhcxcx/sign-off---goodnight"
      ],
      "guest": "Claire Danes"
    },
    {
      "date": "2012-03-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eolisf/countdown-to-loving-mitt---jeb-bush",
        "http://thecolbertreport.cc.com/videos/bf1ekb/people-who-are-destroying-america---teachers",
        "http://thecolbertreport.cc.com/videos/ncu1ti/mysteries-of-the-ancient-unknown---yo-mama-jokes",
        "http://thecolbertreport.cc.com/videos/tw0ear/claire-danes",
        "http://thecolbertreport.cc.com/videos/4gz8ak/sign-off---jeb-bush-s-portrait"
      ],
      "guest": "Claire Danes"
    },
    {
      "date": "2012-03-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xceapv/countdown-to-loving-mitt---super-tuesday",
        "http://thecolbertreport.cc.com/videos/29dn96/rush-limbaugh-apologizes-to-sandra-fluke",
        "http://thecolbertreport.cc.com/videos/pww7ru/sport-report---pete-weber--danica-patrick---the-new-orleans-saints",
        "http://thecolbertreport.cc.com/videos/nwk5lf/audra-mcdonald"
      ],
      "guest": "Audra McDonald"
    },
    {
      "date": "2012-03-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4yvx5w/super-tuesday-party--putin-s-win---india-s-state-assembly",
        "http://thecolbertreport.cc.com/videos/nzr8wl/the-word---due-or-die",
        "http://thecolbertreport.cc.com/videos/rxyz0z/thought-for-food---responsible-snacking---second-breakfast",
        "http://thecolbertreport.cc.com/videos/h24vfx/jonathan-safran-foer",
        "http://thecolbertreport.cc.com/videos/em4ksp/sign-off---good-catch"
      ],
      "guest": "Jonathan Safran Foer"
    },
    {
      "date": "2012-03-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i93vkc/intro---3-7-12",
        "http://thecolbertreport.cc.com/videos/3df60s/higgs-boson-humor",
        "http://thecolbertreport.cc.com/videos/y5rjly/countdown-to-loving-mitt---super-tuesday-results",
        "http://thecolbertreport.cc.com/videos/7v4ikl/cyber-republican-convention",
        "http://thecolbertreport.cc.com/videos/ciyqhs/iranian-irony-threat",
        "http://thecolbertreport.cc.com/videos/060vqq/willem-dafoe",
        "http://thecolbertreport.cc.com/videos/c0qp1t/sign-off---goodnight"
      ],
      "guest": "Willem Dafoe"
    },
    {
      "date": "2012-03-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3nl0qx/eric-bolling-s-secret-gas-prices-plan",
        "http://thecolbertreport.cc.com/videos/fig5ri/herman-cain-s-avant-garde-pac-ad"
      ],
      "guest": "Don Fleming, Elvis Costello, Emmylou Harris"
    },
    {
      "date": "2012-03-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c4fdt8/daylight-savings-socialism",
        "http://thecolbertreport.cc.com/videos/2v3qmo/republicans--southern-strategy",
        "http://thecolbertreport.cc.com/videos/lo9wk9/republicans--southern-strategy---dave--mudcat--saunders",
        "http://thecolbertreport.cc.com/videos/16w3vh/cheating-death---bacon-cure-for-nosebleeds---sound-wave-sterility",
        "http://thecolbertreport.cc.com/videos/nmtsxp/katherine-boo",
        "http://thecolbertreport.cc.com/videos/owkzk2/sign-off---goodnight-with-a-smile"
      ],
      "guest": "Katherine Boo"
    },
    {
      "date": "2012-03-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bz7jdm/who-s-not-honoring-me-now----seattle-s-pop-conference",
        "http://thecolbertreport.cc.com/videos/qn0q26/threatdown---stoned-pat-robertson--muslim-american-reality-tv---pampered-bears",
        "http://thecolbertreport.cc.com/videos/h98570/republican-southern-primary---simplified-speeches",
        "http://thecolbertreport.cc.com/videos/msz5qh/andrew-bird"
      ],
      "guest": "Andrew Bird"
    },
    {
      "date": "2012-03-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m77cwc/greg-smith-s-goldman-sachs-op-ed",
        "http://thecolbertreport.cc.com/videos/rwxeui/republican-southern-primary---rick-santorum-against-teleprompters",
        "http://thecolbertreport.cc.com/videos/yeczkv/republican-southern-primary---kermit-the-frog",
        "http://thecolbertreport.cc.com/videos/7n8gsd/monkey-on-the-lam---alabama",
        "http://thecolbertreport.cc.com/videos/zkum1o/mark-mckinnon",
        "http://thecolbertreport.cc.com/videos/d8t6uu/sign-off---goodnight"
      ],
      "guest": "Mark McKinnon"
    },
    {
      "date": "2012-03-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eq8308/airport-security-for-senior-citizens",
        "http://thecolbertreport.cc.com/videos/zjy3q9/rush-limbaugh-loses-more-sponsors",
        "http://thecolbertreport.cc.com/videos/krx9gw/rick-santorum-visits-puerto-rico-and-speaks-from-his-heart",
        "http://thecolbertreport.cc.com/videos/vh5p5b/ireland-s-imported-sperm---ethnically-accurate-headgear",
        "http://thecolbertreport.cc.com/videos/8o29gb/dexter-filkins",
        "http://thecolbertreport.cc.com/videos/e66q9g/sign-off---goodnight"
      ],
      "guest": "Dexter Filkins"
    },
    {
      "date": "2012-03-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/no5p1a/exclusive---david-page-extended-interview",
        "http://thecolbertreport.cc.com/videos/a8lnqt/intro---3-26-12",
        "http://thecolbertreport.cc.com/videos/3ejcul/stephen-s-spring-break",
        "http://thecolbertreport.cc.com/videos/008ndt/the-word---dressed-to-kill",
        "http://thecolbertreport.cc.com/videos/7faawr/mitt-romney-etch-a-sketch-comparison",
        "http://thecolbertreport.cc.com/videos/rc1xqe/david-page",
        "http://thecolbertreport.cc.com/videos/20xgt7/sign-off---goodnight"
      ],
      "guest": "Dr. David Page"
    },
    {
      "date": "2012-03-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rk3w4e/intro---3-27-12",
        "http://thecolbertreport.cc.com/videos/cua8o6/barack-obama-gun-control-conspiracy",
        "http://thecolbertreport.cc.com/videos/ykhpki/tip-wag---anti-prejudice-drug---dick-cheney-s-heart",
        "http://thecolbertreport.cc.com/videos/53yh09/thought-for-food---tacocopter",
        "http://thecolbertreport.cc.com/videos/ghn5jt/charles-murray",
        "http://thecolbertreport.cc.com/videos/y9plha/sign-off---goodnight"
      ],
      "guest": "Charles Murray"
    },
    {
      "date": "2012-03-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lg7nrp/the-supreme-court-weighs-in-on-obamacare",
        "http://thecolbertreport.cc.com/videos/svf90k/the-supreme-court-weighs-in-on-obamacare---emily-bazelon",
        "http://thecolbertreport.cc.com/videos/tnvz1z/the-conservative-teen",
        "http://thecolbertreport.cc.com/videos/bmkpwj/mark-ruffalo",
        "http://thecolbertreport.cc.com/videos/jjebsm/sign-off---goodnight-snack"
      ],
      "guest": "Mark Ruffalo"
    },
    {
      "date": "2012-03-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7erwuh/stephen-offers-colbert-super-pac-super-fun-pack",
        "http://thecolbertreport.cc.com/videos/9bgxui/intro---3-29-12",
        "http://thecolbertreport.cc.com/videos/nuvo4m/the-mega-millions-lottery",
        "http://thecolbertreport.cc.com/videos/7qagdx/colbert-super-pac---texan-supporters---super-fun-pack",
        "http://thecolbertreport.cc.com/videos/2m6prp/mitt-romney-tells-a-funny-story",
        "http://thecolbertreport.cc.com/videos/7dpy0t/peter-beinart",
        "http://thecolbertreport.cc.com/videos/r5oifs/sign-off---colbert-super-pac-super-fun-pack"
      ],
      "guest": "Peter Beinart"
    },
    {
      "date": "2012-04-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8f8tya/intro---4-2-12",
        "http://thecolbertreport.cc.com/videos/1nq1ce/colbert-super-pac---super-fun-pack-treasure-hunt",
        "http://thecolbertreport.cc.com/videos/1bsxs9/the-beefstate-governors",
        "http://thecolbertreport.cc.com/videos/fmif88/yahweh-or-no-way---christian-card-counters--pope-benedict-on-marxism---pope-cologne",
        "http://thecolbertreport.cc.com/videos/5yl006/gary-johnson",
        "http://thecolbertreport.cc.com/videos/77h3h1/sign-off---goodnight"
      ],
      "guest": "Gov. Gary Johnson"
    },
    {
      "date": "2012-04-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/33j3ar/lftb-colbology",
        "http://thecolbertreport.cc.com/videos/z52jo4/colbert-super-pac---super-fun-pack-not-legal-advice---certificate-of-presidenthood",
        "http://thecolbertreport.cc.com/videos/v3p6ss/colbert-super-pac-shh----501c4-disclosure",
        "http://thecolbertreport.cc.com/videos/ag45p1/colbert-super-pac-shh----501c4-disclosure---trevor-potter",
        "http://thecolbertreport.cc.com/videos/y4berw/rick-santorum-speaks-from-his-heart---california-colleges",
        "http://thecolbertreport.cc.com/videos/1b9vpb/nikki-haley",
        "http://thecolbertreport.cc.com/videos/asl5su/sign-off---helmeted-ham-rove"
      ],
      "guest": "Gov. Nikki Haley"
    },
    {
      "date": "2012-04-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2ihe55/intro---4-4-12",
        "http://thecolbertreport.cc.com/videos/6y1ct4/peabody-award-for-colbert-super-pac",
        "http://thecolbertreport.cc.com/videos/4io3p9/settling-for-mitt-romney",
        "http://thecolbertreport.cc.com/videos/x8e4ps/colbert-super-pac---republicans---the-latino-vote",
        "http://thecolbertreport.cc.com/videos/6ml3sk/wilford-brimley-calls---quaker-oats-makeover",
        "http://thecolbertreport.cc.com/videos/plj4a3/robert-ballard",
        "http://thecolbertreport.cc.com/videos/qyyf0b/sign-off---second-peabody-award"
      ],
      "guest": "Robert D. Ballard"
    },
    {
      "date": "2012-04-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/om9vmg/bad-news-about-good-unemployment-news",
        "http://thecolbertreport.cc.com/videos/lnmh56/colbert-s-very-wanted---manatee-mailbox",
        "http://thecolbertreport.cc.com/videos/0u9fik/dirt-bike-badass-in-the-lincoln-tunnel",
        "http://thecolbertreport.cc.com/videos/ji5xxu/anne-rice",
        "http://thecolbertreport.cc.com/videos/si0xcn/sign-off---lincoln-tunnel"
      ],
      "guest": "Anne Rice"
    },
    {
      "date": "2012-04-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8ziziz/easter-under-attack---bunny-vs--bilby",
        "http://thecolbertreport.cc.com/videos/oyaen8/searching-for-mr--right---mitt-romney---iowa-s-steve-king",
        "http://thecolbertreport.cc.com/videos/csp74m/stephen-colbert-s-shame-spiral---senior-citizen-gymnasts",
        "http://thecolbertreport.cc.com/videos/kruk2j/bob-lutz",
        "http://thecolbertreport.cc.com/videos/9wc34u/sign-off---remembering-mike-wallace"
      ],
      "guest": "Bob Lutz"
    },
    {
      "date": "2012-04-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2n6qw1/intro---4-10-12",
        "http://thecolbertreport.cc.com/videos/82ub2z/rick-santorum-leaves-presidential-race",
        "http://thecolbertreport.cc.com/videos/qu7492/i-got-the-tweets-like-grassley",
        "http://thecolbertreport.cc.com/videos/3la5nh/tip-wag---coal-industry-crackdown---box-spring-bunker",
        "http://thecolbertreport.cc.com/videos/mfxyfn/stephen-colbert-s-lady-heroes---glen-grothman",
        "http://thecolbertreport.cc.com/videos/o4ah40/richard-hersh",
        "http://thecolbertreport.cc.com/videos/es5mrc/sign-off---goodnight"
      ],
      "guest": "Richard Hersh"
    },
    {
      "date": "2012-04-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3ygjj0/amped-up-for-michelle-obama",
        "http://thecolbertreport.cc.com/videos/bc3gqm/the-word---whuh-how-",
        "http://thecolbertreport.cc.com/videos/ingur1/employing-a-veteran---sergeant-bryan-escobedo",
        "http://thecolbertreport.cc.com/videos/f8r4k5/michelle-obama-pt--1",
        "http://thecolbertreport.cc.com/videos/v3wlgc/michelle-obama-pt--2",
        "http://thecolbertreport.cc.com/videos/u0cci1/sign-off---goodnight"
      ],
      "guest": "Michelle Obama"
    },
    {
      "date": "2012-04-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pzrkzg/intro---4-12-12",
        "http://thecolbertreport.cc.com/videos/m5gmsh/the-other-war-on-women",
        "http://thecolbertreport.cc.com/videos/v73czf/stephen-colbert-s-end-of-the-world-of-the-week---survivalist-singles---tsunami-food",
        "http://thecolbertreport.cc.com/videos/s55d89/cold-war-update---alleged-congressional-communists",
        "http://thecolbertreport.cc.com/videos/x9epzo/james-cameron",
        "http://thecolbertreport.cc.com/videos/avonwu/sign-off---goodnight"
      ],
      "guest": "James Cameron"
    },
    {
      "date": "2012-04-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z2fjas/a-beautiful-war-for-women-segment",
        "http://thecolbertreport.cc.com/videos/2ixpov/secret-service-sex-scandal",
        "http://thecolbertreport.cc.com/videos/ilt6wv/a-beautiful-war-for-women",
        "http://thecolbertreport.cc.com/videos/44j8wl/newt-gingrich---gun-rights",
        "http://thecolbertreport.cc.com/videos/ru5vnr/bonnie-raitt"
      ],
      "guest": "Bonnie Raitt"
    },
    {
      "date": "2012-04-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wpng4g/intro---4-17-12",
        "http://thecolbertreport.cc.com/videos/gxlf9b/mitt-romney-s-dinner-table-pranks",
        "http://thecolbertreport.cc.com/videos/sfsf06/thought-for-food---bug-food-coloring--hot-dog-stuffed-crust---drugged-poultry",
        "http://thecolbertreport.cc.com/videos/vklngm/gsa-spending-scandal",
        "http://thecolbertreport.cc.com/videos/6fhp9q/jonah-lehrer",
        "http://thecolbertreport.cc.com/videos/culsks/sign-off---goodnight"
      ],
      "guest": "Jonah Lehrer"
    },
    {
      "date": "2012-04-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q3i7x8/intro---4-18-12",
        "http://thecolbertreport.cc.com/videos/ddq41n/searching-for-mr--right---mitt-romney---ohio-s-rob-portman",
        "http://thecolbertreport.cc.com/videos/er0kn7/the-word---gateway-hug",
        "http://thecolbertreport.cc.com/videos/vw1qdm/stephen-colbert-s-end-of-the-world-of-the-week---doomsday-preppers",
        "http://thecolbertreport.cc.com/videos/xzzk73/arianna-huffington",
        "http://thecolbertreport.cc.com/videos/tttdob/sign-off---goodnight-kiss"
      ],
      "guest": "Arianna Huffington"
    },
    {
      "date": "2012-04-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hrfl05/intro---4-19-12",
        "http://thecolbertreport.cc.com/videos/a9n2pr/stephen-s-4-20-message",
        "http://thecolbertreport.cc.com/videos/zdgaqc/alpha-dog-of-the-week---cory-booker",
        "http://thecolbertreport.cc.com/videos/nb2ksl/the-enemy-within---bologna-border-bust",
        "http://thecolbertreport.cc.com/videos/uio9bo/time-s-2012-top-100-most-influential",
        "http://thecolbertreport.cc.com/videos/h2p67e/tavis-smiley---cornel-west",
        "http://thecolbertreport.cc.com/videos/g291q8/sign-off---time-s-top-100"
      ],
      "guest": "Tavis Smiley &amp; Cornel West"
    },
    {
      "date": "2012-04-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4wypj5/intro---4-23-12",
        "http://thecolbertreport.cc.com/videos/m8blpo/steve-doocy-s-silver-spoon-subtext-reporting",
        "http://thecolbertreport.cc.com/videos/2gwl1y/tip-wag--pheromone-parties---arizona-s--pre-life--laws",
        "http://thecolbertreport.cc.com/videos/v2y3wl/mitt-romney-s-picnic-gaffe",
        "http://thecolbertreport.cc.com/videos/14wyxm/don-mcleroy",
        "http://thecolbertreport.cc.com/videos/l9d2q6/sign-off---goodnight"
      ],
      "guest": "Don McLeroy"
    },
    {
      "date": "2012-04-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ly3so2/super-tuesday-ii--election-boogaloo---death-match-in-hellaware",
        "http://thecolbertreport.cc.com/videos/xmivrq/-i-am-a-pole--and-so-can-you---",
        "http://thecolbertreport.cc.com/videos/i4eh7r/canada-s-currency-coup",
        "http://thecolbertreport.cc.com/videos/ycnifi/magnus-carlsen",
        "http://thecolbertreport.cc.com/videos/cfkek7/sign-off---ipad"
      ],
      "guest": "Magnus Carlsen"
    },
    {
      "date": "2012-04-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/et0kro/intro---4-25-12",
        "http://thecolbertreport.cc.com/videos/or4jr5/nasa-retires-discovery---drops-spacebook",
        "http://thecolbertreport.cc.com/videos/6xkuod/the-word---united-we-can-t-stand-them",
        "http://thecolbertreport.cc.com/videos/gi36k3/cheating-death---crash-diet-feeding-tubes---scrotum-gel-injections",
        "http://thecolbertreport.cc.com/videos/88pieq/michael-sandel",
        "http://thecolbertreport.cc.com/videos/wduflz/sign-off---goodnight"
      ],
      "guest": "Michael Sandel"
    },
    {
      "date": "2012-04-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xrzvpm/intro---4-26-12",
        "http://thecolbertreport.cc.com/videos/9rs6oa/barack-obama-s-slow-jam-backlash",
        "http://thecolbertreport.cc.com/videos/2w9amu/colbert-super-pac---super-fun-pack-1st-treasure-hunt-clue",
        "http://thecolbertreport.cc.com/videos/1ytfce/jack-white",
        "http://thecolbertreport.cc.com/videos/kymj2z/sign-off---montclair-film-festival"
      ],
      "guest": "Jack White"
    },
    {
      "date": "2012-04-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l8r5un/intro---4-30-12",
        "http://thecolbertreport.cc.com/videos/u2x3gk/delicate-advice-for-chen-guangcheng",
        "http://thecolbertreport.cc.com/videos/g6gv3q/the-word---don-t-ask--don-t-show---tell",
        "http://thecolbertreport.cc.com/videos/z2rpip/concealing-weapons-in-style",
        "http://thecolbertreport.cc.com/videos/csg3jo/diane-keaton",
        "http://thecolbertreport.cc.com/videos/tly3vi/sign-off---stephen-s-fashionable-firearm"
      ],
      "guest": "Diane Keaton"
    },
    {
      "date": "2012-05-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8gt820/intro---5-1-12",
        "http://thecolbertreport.cc.com/videos/pktymf/barack-obama---the-anniversary-of-bin-laden-s-assassination",
        "http://thecolbertreport.cc.com/videos/0zj7f4/paul-ryan-s-christian-budget-cuts",
        "http://thecolbertreport.cc.com/videos/7af7jl/paul-ryan-s-christian-budget-cuts---thomas-reese",
        "http://thecolbertreport.cc.com/videos/cpb2np/carne-ross",
        "http://thecolbertreport.cc.com/videos/a9ioqx/sign-off---goodnight"
      ],
      "guest": "Carne Ross"
    },
    {
      "date": "2012-05-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jciyto/intro---5-2-12",
        "http://thecolbertreport.cc.com/videos/n232ru/richard-branson-shaped-ice-cubes",
        "http://thecolbertreport.cc.com/videos/goj2h9/the-word---debt-panels",
        "http://thecolbertreport.cc.com/videos/sv3iag/kermit-the-frog-s-german-tv-offense---hans-beinholtz",
        "http://thecolbertreport.cc.com/videos/luw0ia/jonathan-haidt",
        "http://thecolbertreport.cc.com/videos/k7vmo6/sign-off---stephen-colbert-s-6000k-norway-norwalkathon"
      ],
      "guest": "Jonathan Haidt"
    },
    {
      "date": "2012-05-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/msaxn6/newt-gingrich---mitt-romney-alliance-analogies",
        "http://thecolbertreport.cc.com/videos/eki0dc/colbert-super-pac---in-search-of-mr--larose",
        "http://thecolbertreport.cc.com/videos/2v2ixr/who-s-honoring-me-now----national-space-society---buzz-aldrin",
        "http://thecolbertreport.cc.com/videos/z3ac6o/lena-dunham",
        "http://thecolbertreport.cc.com/videos/1iw8uv/sign-off---2012-space-pioneer-award-for-mass-media"
      ],
      "guest": "Lena Dunham"
    },
    {
      "date": "2012-05-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1jhhu2/uncensored---maurice-sendak-tribute----i-am-a-pole--and-so-can-you----release",
        "http://thecolbertreport.cc.com/videos/feswk7/intro---5-7-12",
        "http://thecolbertreport.cc.com/videos/d6nh6o/hand-disinfectant-drunk-teens",
        "http://thecolbertreport.cc.com/videos/d69ur0/joe-biden-s-same-sex-marriage-gaffe",
        "http://thecolbertreport.cc.com/videos/fplvtb/-pussy-hound--with-eric-mccormack",
        "http://thecolbertreport.cc.com/videos/jrnml0/threatdown---newscasting-bears",
        "http://thecolbertreport.cc.com/videos/u65qci/andy-cohen",
        "http://thecolbertreport.cc.com/videos/xh5269/sign-off---sound-effects-box"
      ],
      "guest": "Andy Cohen"
    },
    {
      "date": "2012-05-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/p05t1b/colbert-super-pac-shh----corporate-campaign-players---super-secret--spooky-pacs-",
        "http://thecolbertreport.cc.com/videos/b2tfg8/anonymous-attack-ads---claire-mccaskill",
        "http://thecolbertreport.cc.com/videos/ad10bn/michelle-alexander",
        "http://thecolbertreport.cc.com/videos/dsprai/sign-off----i-am-a-pole--and-so-can-you---"
      ],
      "guest": "Michelle Alexander"
    },
    {
      "date": "2012-05-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v1k3ci/mexico-s-debate-playmate",
        "http://thecolbertreport.cc.com/videos/b6tiga/barack-obama-vs--north-carolina-on-gay-marriage",
        "http://thecolbertreport.cc.com/videos/t3omhb/jon-mcnaughton-s--nation-under-socialism--artwork",
        "http://thecolbertreport.cc.com/videos/o2c49w/anna-wintour",
        "http://thecolbertreport.cc.com/videos/bogip6/sign-off----i-am-a-pole--and-so-can-you----audiobook"
      ],
      "guest": "Anna Wintour"
    },
    {
      "date": "2012-05-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6cwgo2/intro---5-10-12",
        "http://thecolbertreport.cc.com/videos/7lnqh4/mother-s-day-shout-out",
        "http://thecolbertreport.cc.com/videos/n27g4x/barack-obama-s-gay-blasphemy",
        "http://thecolbertreport.cc.com/videos/b9m4e5/threatdown---interdimensional-black-people--gay-strokes---manipulative-sicko-monkeys",
        "http://thecolbertreport.cc.com/videos/ytlc6i/wisconsin-s-fake-democrats",
        "http://thecolbertreport.cc.com/videos/v6gyoh/francis-collins",
        "http://thecolbertreport.cc.com/videos/vbl44w/sign-off---two-weeks-off---dry-roasted-peanuts"
      ],
      "guest": "Dr. Francis Collins"
    },
    {
      "date": "2012-05-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hx8ph7/intro---5-29-12",
        "http://thecolbertreport.cc.com/videos/cpgg7x/who-s-honoring-me-now----peabody-awards---maxim-s-hot-100",
        "http://thecolbertreport.cc.com/videos/oo0mhd/donald-trump-s-creative-truth---mitt-romney-s-poll-numbers",
        "http://thecolbertreport.cc.com/videos/cw4fxf/un-american-news---egypt-s-presidential-elections",
        "http://thecolbertreport.cc.com/videos/32y78g/charlize-theron",
        "http://thecolbertreport.cc.com/videos/gr0i67/sign-off---goodnight"
      ],
      "guest": "Charlize Theron"
    },
    {
      "date": "2012-05-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u7h1f8/intro---5-30-12",
        "http://thecolbertreport.cc.com/videos/kydmtj/mexico-s-drug---potato-chip-wars",
        "http://thecolbertreport.cc.com/videos/s73hgy/robert-mugabe-s-u-n--tourism-tribute",
        "http://thecolbertreport.cc.com/videos/dfm2k1/alan-alda",
        "http://thecolbertreport.cc.com/videos/b6lw83/sign-off---stephen-s-matchbox"
      ],
      "guest": "Alan Alda"
    },
    {
      "date": "2012-05-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y3bfh6/buy-best-selling--i-am-a-pole--and-so-can-you---",
        "http://thecolbertreport.cc.com/videos/sib2qy/barack-obama-s-righteous-drone-strikes",
        "http://thecolbertreport.cc.com/videos/s3t2y6/the-word---two-birds-with-one-drone",
        "http://thecolbertreport.cc.com/videos/pufh72/michael-bloomberg-s-super-sized-soda-scheme",
        "http://thecolbertreport.cc.com/videos/pz3adl/jack-hitt",
        "http://thecolbertreport.cc.com/videos/e9e1b2/sign-off---welcome-baby-gwinn-"
      ],
      "guest": "Jack Hitt"
    },
    {
      "date": "2012-06-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nhsal8/juvenile-speeches-from-congress---president-sparkle-talk",
        "http://thecolbertreport.cc.com/videos/w6itwj/the-word---sink-or-swim",
        "http://thecolbertreport.cc.com/videos/r7x6me/better-know-a-district---represent-o-map-6000---georgia-s-5th",
        "http://thecolbertreport.cc.com/videos/cx6fmy/john-lewis",
        "http://thecolbertreport.cc.com/videos/5u46bt/sign-off---goodnight"
      ],
      "guest": "Rep. John Lewis"
    },
    {
      "date": "2012-06-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lg5ugg/intro---6-5-12",
        "http://thecolbertreport.cc.com/videos/xt64qc/cdc-zombie-apocalypse-statement",
        "http://thecolbertreport.cc.com/videos/w4utag/tip-wag---japanese-diet-goggles--u-s--sperm-exports---taxidermied-toys",
        "http://thecolbertreport.cc.com/videos/kkce78/self-marriage-problems",
        "http://thecolbertreport.cc.com/videos/90ifev/jill-biden",
        "http://thecolbertreport.cc.com/videos/hhgz9k/sign-off---goodnight"
      ],
      "guest": "Jill Biden"
    },
    {
      "date": "2012-06-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ta5d10/transit-of-venus---mars-reality-show-pitch",
        "http://thecolbertreport.cc.com/videos/y1zpiy/wisconsin-s-recall-results",
        "http://thecolbertreport.cc.com/videos/0vve8r/difference-makers---larry-johnson",
        "http://thecolbertreport.cc.com/videos/pqv8yf/neil-patrick-harris",
        "http://thecolbertreport.cc.com/videos/1n5kn0/sign-off---ray-bradbury-tribute"
      ],
      "guest": "Neil Patrick Harris"
    },
    {
      "date": "2012-06-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2l9h7f/intro---6-7-12",
        "http://thecolbertreport.cc.com/videos/n107py/corruption-on-pakistan-s--sesame-street-",
        "http://thecolbertreport.cc.com/videos/5zzgas/the-new-york-times--hit-job-on-mitt-romney",
        "http://thecolbertreport.cc.com/videos/mlqu18/a-teacup-pig---partisan-politics",
        "http://thecolbertreport.cc.com/videos/gfpnqx/regina-spektor",
        "http://thecolbertreport.cc.com/videos/8x9qre/colbert-super-pac---super-fun-pack-treasure-hunt-clue"
      ],
      "guest": "Regina Spektor"
    },
    {
      "date": "2012-06-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8zxgdh/neil-degrasse-tyson-on--prometheus--gaffe",
        "http://thecolbertreport.cc.com/videos/4dkvt6/radical-feminist-nuns",
        "http://thecolbertreport.cc.com/videos/u1f5qa/radical-feminist-nuns---simone-campbell",
        "http://thecolbertreport.cc.com/videos/beuiqq/-banana-bunker--tutorial",
        "http://thecolbertreport.cc.com/videos/0lbz7s/martin-sheen",
        "http://thecolbertreport.cc.com/videos/h1jqol/sign-off---wooden-ruler"
      ],
      "guest": "Martin Sheen"
    },
    {
      "date": "2012-06-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/syl8av/intro---6-12-12",
        "http://thecolbertreport.cc.com/videos/4p817x/mitt-romney-s-blue-collar-equestrian-pastime",
        "http://thecolbertreport.cc.com/videos/nu56lh/barack-obama-s-anti-terror-leaks",
        "http://thecolbertreport.cc.com/videos/dfjz7v/barack-obama-s-jobs-gaffe---mitt-romney-s-courageous-comeback",
        "http://thecolbertreport.cc.com/videos/e4m68b/operation-artificial-swedener",
        "http://thecolbertreport.cc.com/videos/eici19/will-allen",
        "http://thecolbertreport.cc.com/videos/uaovz2/sign-off---stephen-s-equestrian-display"
      ],
      "guest": "Will Allen"
    },
    {
      "date": "2012-06-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/f93cwg/high-wire-walk-over-niagara-falls",
        "http://thecolbertreport.cc.com/videos/e61ypw/the-word---free-lunch",
        "http://thecolbertreport.cc.com/videos/clm6h7/the-enemy-within---apes-armed-with-ipads",
        "http://thecolbertreport.cc.com/videos/0nbwzv/gregg-allman",
        "http://thecolbertreport.cc.com/videos/0bcb4l/sign-off---goodnight"
      ],
      "guest": "Gregg Allman"
    },
    {
      "date": "2012-06-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wdhef3/marijuana-legalization-as-election-hot-button-issue",
        "http://thecolbertreport.cc.com/videos/zy2va1/super-pac-super-cash---24-hour-political-ad-channels",
        "http://thecolbertreport.cc.com/videos/a5uuwa/cheating-death---penis-curvature-cures---single-women-sleep-aids",
        "http://thecolbertreport.cc.com/videos/jylspq/steve-coll",
        "http://thecolbertreport.cc.com/videos/nw9c2r/sign-off---bon-voyage--peter-gwinn"
      ],
      "guest": "Steve Coll"
    },
    {
      "date": "2012-06-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/34ngb2/intro---6-18-12",
        "http://thecolbertreport.cc.com/videos/c3nu3d/barack-obama-s-immigration-policy-change",
        "http://thecolbertreport.cc.com/videos/z9bjae/press-interruption-at-barack-obama-s-immigration-address",
        "http://thecolbertreport.cc.com/videos/f3coxy/operation-artificial-swedener---sweden-s-response",
        "http://thecolbertreport.cc.com/videos/x4uwku/paul-krugman",
        "http://thecolbertreport.cc.com/videos/fdw0ht/sign-off---goodnight"
      ],
      "guest": "Paul Krugman"
    },
    {
      "date": "2012-06-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0r91gj/john-kerry-as-mitt-romney-in-debate-prep",
        "http://thecolbertreport.cc.com/videos/zxypkl/mitt-romney-s-champion-horse---dressage-tribute",
        "http://thecolbertreport.cc.com/videos/ugscr4/unscooped-dog-poop-crimes",
        "http://thecolbertreport.cc.com/videos/xdevam/olivia-wilde",
        "http://thecolbertreport.cc.com/videos/kada0a/sign-off---stephen-s-dressage-dance"
      ],
      "guest": "Olivia Wilde"
    },
    {
      "date": "2012-06-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6q5qvo/intro---6-20-12",
        "http://thecolbertreport.cc.com/videos/w6vibi/asian-immigration-threat",
        "http://thecolbertreport.cc.com/videos/95tn0n/unraveling-the-operation-fast---furious-scandal",
        "http://thecolbertreport.cc.com/videos/b65og2/joe-the-plumber-s-controversial-gun-control-ad",
        "http://thecolbertreport.cc.com/videos/4h0l60/thought-for-food---doritos-tacos---flavorlopes",
        "http://thecolbertreport.cc.com/videos/lwb6am/daniel-klaidman",
        "http://thecolbertreport.cc.com/videos/31ptzz/sign-off---goodnight"
      ],
      "guest": "Daniel Klaidman"
    },
    {
      "date": "2012-06-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7r29kf/egypt-s-presidential-election---hosni-mubarak-s-health",
        "http://thecolbertreport.cc.com/videos/zdprqc/threatdown---sicko-penguins--stoner-babies---terrorist-furniture",
        "http://thecolbertreport.cc.com/videos/5yjil8/operation-artificial-swedener---c-mon-sweden--take-a-chance-on-stephen",
        "http://thecolbertreport.cc.com/videos/e6ik9l/lawrence-krauss",
        "http://thecolbertreport.cc.com/videos/e8ivor/sign-off----a-universe-from-nothing-"
      ],
      "guest": "Lawrence Krauss"
    },
    {
      "date": "2012-06-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ylc1ta/intro---6-25-12",
        "http://thecolbertreport.cc.com/videos/cbsvdk/colbert-news-alert---obamacare-supreme-court-ruling",
        "http://thecolbertreport.cc.com/videos/wn3vzl/colbert-news-alert---obamacare-supreme-court-ruling---richard-mourdock-s-responses",
        "http://thecolbertreport.cc.com/videos/1nhpf3/the-word---silver-maligning",
        "http://thecolbertreport.cc.com/videos/0u5f3i/i-s-on-edjukashun---study-drugs",
        "http://thecolbertreport.cc.com/videos/2q2di6/frank-deford",
        "http://thecolbertreport.cc.com/videos/wri423/sign-off---five-finger-fillet"
      ],
      "guest": "Frank Deford"
    },
    {
      "date": "2012-06-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ifbnsf/intro---6-26-12",
        "http://thecolbertreport.cc.com/videos/8wlx7c/supreme-court-ruling-on-arizona-immigration-policy",
        "http://thecolbertreport.cc.com/videos/06bwvh/tip-wag---pixar-s-gay-agenda--america-s-obesity---adidas-shackle-sneakers",
        "http://thecolbertreport.cc.com/videos/ohfzqq/dish-network-s-autohop-service",
        "http://thecolbertreport.cc.com/videos/r8iy26/richard-ford",
        "http://thecolbertreport.cc.com/videos/ybvbi1/sign-off---goodnight"
      ],
      "guest": "Richard Ford"
    },
    {
      "date": "2012-06-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g8onr9/colbert-super-pac-treasure-hunt-solution",
        "http://thecolbertreport.cc.com/videos/gl54n8/mitt-romney-s-victory-retreat---democrats--convention-deficit",
        "http://thecolbertreport.cc.com/videos/t2x64z/national-geographic-poll-on-alien-invasion-management",
        "http://thecolbertreport.cc.com/videos/td6pu4/blood-in-the-water---mike-turzai-s-voter-id-remarks",
        "http://thecolbertreport.cc.com/videos/5em8r3/rainbow-stuffed-gay-pride-oreo",
        "http://thecolbertreport.cc.com/videos/aj465n/melinda-gates",
        "http://thecolbertreport.cc.com/videos/bxvxkj/sign-off---oreo-cookie-plate"
      ],
      "guest": "Melinda Gates"
    },
    {
      "date": "2012-06-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/coii6k/cable-news-gaffe-on-obamacare-supreme-court-ruling",
        "http://thecolbertreport.cc.com/videos/p7wwtp/john-roberts--obamacare-swing-vote",
        "http://thecolbertreport.cc.com/videos/n5b9bc/obamacare---the-broccoli-argument",
        "http://thecolbertreport.cc.com/videos/xqmuun/obamacare---the-broccoli-argument---emily-bazelon",
        "http://thecolbertreport.cc.com/videos/843q05/aaron-sorkin",
        "http://thecolbertreport.cc.com/videos/hdpyh9/colbert-super-pac---super-fun-pack-treasure-finder"
      ],
      "guest": "Aaron Sorkin"
    },
    {
      "date": "2012-07-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rkamql/intro---7-16-12",
        "http://thecolbertreport.cc.com/videos/nw0ci8/tomkat-s-divorce---anderson-cooper-s-sexual-orientation",
        "http://thecolbertreport.cc.com/videos/xmrkal/mitt-romney-s-retroactive-retirement-from-bain-capital",
        "http://thecolbertreport.cc.com/videos/hs3epw/thought-for-food---caffeine-edition---funeral-home-starbucks---car-coffee-makers",
        "http://thecolbertreport.cc.com/videos/gxb8p4/anne-marie-slaughter",
        "http://thecolbertreport.cc.com/videos/nj5kky/sign-off---smiles-or-whatever"
      ],
      "guest": "Anne-Marie Slaughter"
    },
    {
      "date": "2012-07-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5r1yvx/nevada-s--none-of-the-above--is-fearsome-foe-for-gop",
        "http://thecolbertreport.cc.com/videos/577ry9/the-word---on-the-straight---narrow-minded",
        "http://thecolbertreport.cc.com/videos/xrrg9u/who-s-honoring-me-now----philadelphia-s-rosenbach-museum-and-library",
        "http://thecolbertreport.cc.com/videos/8qe1km/nas"
      ],
      "guest": "Nas"
    },
    {
      "date": "2012-07-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xiottz/intro---7-18-12",
        "http://thecolbertreport.cc.com/videos/jhpgom/-struggling--waiters---waitresses-at-mitt-romney-s-fundraiser",
        "http://thecolbertreport.cc.com/videos/40x15i/tip-wag---christian-tablet-computer---rock-paper-scissors-robot",
        "http://thecolbertreport.cc.com/videos/5qgquz/stephen-colbert-s-metunes---def-leppard-s--forgeries--of-old-hits",
        "http://thecolbertreport.cc.com/videos/67w2nh/annise-parker",
        "http://thecolbertreport.cc.com/videos/2wz88p/sign-off---goodnight"
      ],
      "guest": "Mayor Annise D. Parker"
    },
    {
      "date": "2012-07-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/h8wtk8/fred-willard-arrested-for-lewd-conduct",
        "http://thecolbertreport.cc.com/videos/64cfhk/libor-interest-rate-scandal",
        "http://thecolbertreport.cc.com/videos/7dpxne/libor-interest-rate-scandal---dave-leonhardt",
        "http://thecolbertreport.cc.com/videos/uknspr/canada-s-economic-growth-despite-melting-currency",
        "http://thecolbertreport.cc.com/videos/xfd2bp/lisa-jackson",
        "http://thecolbertreport.cc.com/videos/iw4bs9/sign-off---goodnight"
      ],
      "guest": "Lisa Jackson"
    },
    {
      "date": "2012-07-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/imdi3o/intro---7-23-12",
        "http://thecolbertreport.cc.com/videos/0xmom4/interview-no-show--mike-tyson",
        "http://thecolbertreport.cc.com/videos/v7f1z0/shepard-smith-s-personal-reporting-style",
        "http://thecolbertreport.cc.com/videos/p2oill/partisan-speculation-over-colorado-shooter",
        "http://thecolbertreport.cc.com/videos/3cxwny/vikram-gandhi",
        "http://thecolbertreport.cc.com/videos/rwkf73/sign-off---goodnight"
      ],
      "guest": "Vikram Gandhi"
    },
    {
      "date": "2012-07-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/knsr5h/intro---7-24-12",
        "http://thecolbertreport.cc.com/videos/h74nmb/hamster-study-links-late-night-tv-with-depression",
        "http://thecolbertreport.cc.com/videos/zxif76/u-s--agriculture---drought-disaster",
        "http://thecolbertreport.cc.com/videos/x2crx4/u-s--agriculture---drought-disaster---bruce-babcock",
        "http://thecolbertreport.cc.com/videos/bov9or/james-fallows",
        "http://thecolbertreport.cc.com/videos/lpy9h0/sign-off---goodnight"
      ],
      "guest": "James Fallows"
    },
    {
      "date": "2012-07-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0mcg76/mitt-romney-s-anglo-saxon-connection",
        "http://thecolbertreport.cc.com/videos/w5w9pn/mitt-romney-vs--barack-obama-on-small-business-owners",
        "http://thecolbertreport.cc.com/videos/x14yw9/the-word---1-man-show",
        "http://thecolbertreport.cc.com/videos/f7r40e/bibles-swapped-for--fifty-shades-of-grey-",
        "http://thecolbertreport.cc.com/videos/4414pc/dan-gross",
        "http://thecolbertreport.cc.com/videos/e1brl1/sign-off---goodnight"
      ],
      "guest": "Dan Gross"
    },
    {
      "date": "2012-07-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vqlxb2/intro---7-26-12",
        "http://thecolbertreport.cc.com/videos/4fk2ow/sport-report---stephen-colbefrajilympic-expealacoverage-",
        "http://thecolbertreport.cc.com/videos/kycpil/mitt-romney-s-london-olympics-blunder",
        "http://thecolbertreport.cc.com/videos/lra5ae/chick-fil-a-s-anti-gay-marriage-announcement",
        "http://thecolbertreport.cc.com/videos/4nngh8/peter-westmacott",
        "http://thecolbertreport.cc.com/videos/ccwpvt/sign-off---colbert-nation-twins"
      ],
      "guest": "Amb. Peter Westmacott"
    },
    {
      "date": "2012-07-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/70ka18/mitt-romney-s-disinterest-in-dressage",
        "http://thecolbertreport.cc.com/videos/lav3uh/stephen-s-dressage-training-pt--1",
        "http://thecolbertreport.cc.com/videos/zdpacy/tony-robbins--signature-firewalk",
        "http://thecolbertreport.cc.com/videos/554xm8/joan-rivers",
        "http://thecolbertreport.cc.com/videos/d69lls/sign-off----i-hate-everyone----starting-with-me-"
      ],
      "guest": "Joan Rivers"
    },
    {
      "date": "2012-07-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d1pkf4/intro---7-31-12",
        "http://thecolbertreport.cc.com/videos/sbevip/rick-gorka-s-press-outburst-in-poland",
        "http://thecolbertreport.cc.com/videos/8qmv9k/rafalca-s-impact-on-mitt-romney-s-vp-pick",
        "http://thecolbertreport.cc.com/videos/f5vsty/stephen-s-dressage-training-pt--2",
        "http://thecolbertreport.cc.com/videos/lfsrga/stephest-colbchella--012---rocktaugustfest",
        "http://thecolbertreport.cc.com/videos/p9ejfs/jeff-koons",
        "http://thecolbertreport.cc.com/videos/e0ikf9/sign-off---goodnight"
      ],
      "guest": "Jeff Koons"
    },
    {
      "date": "2012-08-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fjidln/obama-administration-s-birth-control-mandate",
        "http://thecolbertreport.cc.com/videos/llkyw5/the--fiscal-cliff--conundrum---grover-norquist-s-tax-pledge",
        "http://thecolbertreport.cc.com/videos/u1lf6f/sport-report---stephen-colbefrajilympic-expealacoverage----gymnastics---swimming",
        "http://thecolbertreport.cc.com/videos/gayfdj/john-grunsfeld",
        "http://thecolbertreport.cc.com/videos/gwa2y4/sign-off---totem"
      ],
      "guest": "John Grunsfeld"
    },
    {
      "date": "2012-08-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x1we2u/exclusive---better-know-a-district---missouri-s-3rd-or-1st---russ-carnahan",
        "http://thecolbertreport.cc.com/videos/3wx6bt/rafalca-s-first-day-of-dressage",
        "http://thecolbertreport.cc.com/videos/ql0bqa/nancy-pelosi-s-bkad-pact---the-disclose-act-filibuster",
        "http://thecolbertreport.cc.com/videos/tdj576/better-know-a-district---missouri-s-3rd-or-1st---russ-carnahan",
        "http://thecolbertreport.cc.com/videos/t85slm/thought-for-food---usda-meatless-mondays---plant-communication-research",
        "http://thecolbertreport.cc.com/videos/fyzakp/chris-hayes",
        "http://thecolbertreport.cc.com/videos/m1idm3/sign-off---carrot-nibble"
      ],
      "guest": "Chris Hayes"
    },
    {
      "date": "2012-08-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kz6vda/intro---8-6-12",
        "http://thecolbertreport.cc.com/videos/h9qt0r/mars-rover-landing",
        "http://thecolbertreport.cc.com/videos/w2s6c0/chick-fil-a-appreciation-day",
        "http://thecolbertreport.cc.com/videos/x7yc4w/pete-seeger",
        "http://thecolbertreport.cc.com/videos/aj407y/sign-off----pete-seeger--in-his-own-words-"
      ],
      "guest": "Pete Seeger"
    },
    {
      "date": "2012-08-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1vt8t5/sport-report---stephen-colbefrajilympic-expealacoverage----soft-anti-americanism",
        "http://thecolbertreport.cc.com/videos/k4260i/mitt-romney-s-protective-press-pool---running-mate-clues",
        "http://thecolbertreport.cc.com/videos/q82dz5/steve-king-s-dogfighting-defense",
        "http://thecolbertreport.cc.com/videos/nlroaz/mark-shriver",
        "http://thecolbertreport.cc.com/videos/jx7y7x/sign-off---goodnight"
      ],
      "guest": "Mark Shriver"
    },
    {
      "date": "2012-08-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/23mkh8/intro---8-8-12",
        "http://thecolbertreport.cc.com/videos/4fqxvr/obamacare---pizza-costs",
        "http://thecolbertreport.cc.com/videos/h3tu8s/cheating-death---sensor-enabled-pills---facelift-bungee-cords",
        "http://thecolbertreport.cc.com/videos/zgmish/liza-mundy",
        "http://thecolbertreport.cc.com/videos/d5p8ok/sign-off---vacsa-strap"
      ],
      "guest": "Liza Mundy"
    },
    {
      "date": "2012-08-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8gpwtc/anti-muslim-attack-on-hillary-clinton-aide",
        "http://thecolbertreport.cc.com/videos/sr618c/better-know-a-district---minnesota-s-5th---keith-ellison",
        "http://thecolbertreport.cc.com/videos/zzeqj6/who-s-honoring-me-now----psychonomic-bulletin---review",
        "http://thecolbertreport.cc.com/videos/i891sf/woody-harrelson",
        "http://thecolbertreport.cc.com/videos/nynu71/sign-off---goodnight"
      ],
      "guest": "Woody Harrelson"
    },
    {
      "date": "2012-08-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d4650t/stephest-colbchella--012---welcome-to-rocktaugustfest",
        "http://thecolbertreport.cc.com/videos/6jv3cb/mitt-romney-s-bold-running-mate-pick",
        "http://thecolbertreport.cc.com/videos/wk9zh3/stephest-colbchella--012---fun-",
        "http://thecolbertreport.cc.com/videos/r9jxwl/sign-off---stephest-colbchella--012---t-mobile-goodnight"
      ],
      "guest": "Fun."
    },
    {
      "date": "2012-08-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9sxdgp/stephest-colbchella--012---rocktaugustfest-night-two",
        "http://thecolbertreport.cc.com/videos/ovgwtm/mitt-romney-s---paul-ryan-s-foreign-policy-credentials",
        "http://thecolbertreport.cc.com/videos/ajslu2/-stars-earn-stripes--reality-series",
        "http://thecolbertreport.cc.com/videos/4uk1xx/stephest-colbchella--012---grizzly-bear",
        "http://thecolbertreport.cc.com/videos/1eoihc/sign-off---stephest-colbchella--012---t-mobile-goodnight-auditions"
      ],
      "guest": "Grizzly Bear"
    },
    {
      "date": "2012-08-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jus7dh/exclusive---stephest-colbchella--012---concert-setup-timelapse",
        "http://thecolbertreport.cc.com/videos/lkqb8i/stephest-colbchella--012---rocktaugustfest-night-three",
        "http://thecolbertreport.cc.com/videos/iwgkv9/fierce-five-interns",
        "http://thecolbertreport.cc.com/videos/tzk5xz/stephest-colbchella--012---intrepid-sea--air---space-museum",
        "http://thecolbertreport.cc.com/videos/buxzdm/stephest-colbchella--012---santigold",
        "http://thecolbertreport.cc.com/videos/891lvk/sign-off---stephest-colbchella--012---t-mobile-goodnight-with-grandmaster-flash"
      ],
      "guest": "The U.S. Women's Olympic Gymnastics team, Santigold"
    },
    {
      "date": "2012-08-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bx6qnh/stephest-colbchella--012---rocktaugustfest-night-four",
        "http://thecolbertreport.cc.com/videos/tgqk3o/mitt-romney---paul-ryan---the-dynam-ish-duo",
        "http://thecolbertreport.cc.com/videos/ymbqe6/17th-amendment-under-attack",
        "http://thecolbertreport.cc.com/videos/x5cie8/stephest-colbchella--012---wayne-coyne",
        "http://thecolbertreport.cc.com/videos/ez1hov/sign-off---stephest-colbchella--012---t-mobile-goodnight-in-a-bubble"
      ],
      "guest": "The Flaming Lips"
    },
    {
      "date": "2012-08-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/z0q2d6/hurricane-isaac-at-gop-convention",
        "http://thecolbertreport.cc.com/videos/2a1lg4/colbert-super-pac---hurricane-isaac---stephen-s-money-convention",
        "http://thecolbertreport.cc.com/videos/kcyg86/todd-akin-s-abortion-gaffe",
        "http://thecolbertreport.cc.com/videos/2f1kwv/andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/qomrph/sign-off---goodnight"
      ],
      "guest": "Andrew Sullivan"
    },
    {
      "date": "2012-08-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ane28t/america-strikes-back---episode-ii---return-of-the-america-strikes-back--again",
        "http://thecolbertreport.cc.com/videos/std0vn/the-mitt-romney-story",
        "http://thecolbertreport.cc.com/videos/3teieb/the-mitt-romney-story---ann-romney-s-gop-convention-speech",
        "http://thecolbertreport.cc.com/videos/w1ej3a/mitt-romney-s-role-model",
        "http://thecolbertreport.cc.com/videos/n7yuw7/ayn-rand---paul-ryan",
        "http://thecolbertreport.cc.com/videos/v0fegj/jennifer-burns",
        "http://thecolbertreport.cc.com/videos/gxzmx3/sign-off---goodnight"
      ],
      "guest": "Jennifer Burns"
    },
    {
      "date": "2012-08-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0pjdyn/america-strikes-back---episode-iii---the-phantom-money",
        "http://thecolbertreport.cc.com/videos/7543m5/the-gop-convention---mitt-romney-s-minority-appeal",
        "http://thecolbertreport.cc.com/videos/vo7txi/paul-ryan-s-misleading-gop-convention-speech",
        "http://thecolbertreport.cc.com/videos/ghjrfh/jon-huntsman-pt--1",
        "http://thecolbertreport.cc.com/videos/93jjo7/jon-huntsman-pt--2",
        "http://thecolbertreport.cc.com/videos/vi4rti/sign-off---goodnight"
      ],
      "guest": "Jon Huntsman"
    },
    {
      "date": "2012-08-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/x9yoif/america-strikes-back---episode-iv---a-new-ish-hope",
        "http://thecolbertreport.cc.com/videos/9czru3/mitt-romney-s--solid--gop-convention-speech",
        "http://thecolbertreport.cc.com/videos/spqhue/the-gop-convention-s-mystery-speaker",
        "http://thecolbertreport.cc.com/videos/qrijg7/the-gop-convention-s-mystery-speaker---clint-eastwood-s-chair",
        "http://thecolbertreport.cc.com/videos/cx5s7v/neil-armstrong-tribute",
        "http://thecolbertreport.cc.com/videos/n0qmbf/james-carville",
        "http://thecolbertreport.cc.com/videos/2cv31s/sign-off---goodnight"
      ],
      "guest": "James Carville"
    },
    {
      "date": "2012-09-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r83jxh/exclusive---better-know-a-district---new-york-s-9th---yvette-clarke",
        "http://thecolbertreport.cc.com/videos/mxucyy/the-2012-people-s-party-congress-of-charlotte",
        "http://thecolbertreport.cc.com/videos/bg56qn/better-know-a-district---new-york-s-9th---yvette-clarke",
        "http://thecolbertreport.cc.com/videos/cy97ce/paul-ryan-s-marathon-time-gaffe",
        "http://thecolbertreport.cc.com/videos/stj7xj/reihan-salam",
        "http://thecolbertreport.cc.com/videos/awwi1z/sign-off---goodnight"
      ],
      "guest": "Reihan Salam"
    },
    {
      "date": "2012-09-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4axjsp/the-2012-people-s-party-congress-of-charlotte---sound-system",
        "http://thecolbertreport.cc.com/videos/lnxbm7/the-2012-people-s-party-congress-of-charlotte---michelle-obama---tammy-duckworth",
        "http://thecolbertreport.cc.com/videos/zp0jy0/the-2012-people-s-party-congress-of-charlotte---michelle-obama-s-speech-tweets",
        "http://thecolbertreport.cc.com/videos/75ubcv/sport-report---nfl-referee-lockout",
        "http://thecolbertreport.cc.com/videos/fjhhan/michael-grunwald",
        "http://thecolbertreport.cc.com/videos/05j0ux/sign-off---goodnight"
      ],
      "guest": "Michael Grunwald"
    },
    {
      "date": "2012-09-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vf84g8/the-2012-people-s-party-congress-of-charlotte---avoiding-water-gate--day-1",
        "http://thecolbertreport.cc.com/videos/qfodha/the-2012-people-s-party-congress-of-charlotte---bill-clinton---hill-poll",
        "http://thecolbertreport.cc.com/videos/p7kw6y/the-2012-people-s-party-congress-of-charlotte---god---jerusalem",
        "http://thecolbertreport.cc.com/videos/epwrup/bill-richardson",
        "http://thecolbertreport.cc.com/videos/8ivg8l/sign-off---taco-plate"
      ],
      "guest": "Bill Richardson"
    },
    {
      "date": "2012-09-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9wdqkq/the-2012-people-s-party-congress-of-charlotte---youth-vote",
        "http://thecolbertreport.cc.com/videos/cr72mv/the-2012-people-s-party-congress-of-charlotte---tom-brokaw---barack-obama",
        "http://thecolbertreport.cc.com/videos/l9ys9b/rnc-convention-vs--dnc-convention",
        "http://thecolbertreport.cc.com/videos/6oqr0u/the-2012-people-s-party-congress-of-charlotte---colbert-bump",
        "http://thecolbertreport.cc.com/videos/oq50sl/ed-rendell",
        "http://thecolbertreport.cc.com/videos/fbd0do/sign-off---goodnight"
      ],
      "guest": "Ed Rendell"
    },
    {
      "date": "2012-09-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ohliey/intro---9-17-12",
        "http://thecolbertreport.cc.com/videos/q2ib3a/values-voter-summit-gaffe",
        "http://thecolbertreport.cc.com/videos/kelspo/mitt-romney-s-libya-comments",
        "http://thecolbertreport.cc.com/videos/liknzb/atone-phone---ira-glass-calls",
        "http://thecolbertreport.cc.com/videos/454q6n/drew-faust",
        "http://thecolbertreport.cc.com/videos/lh4d2v/sign-off---shofar"
      ],
      "guest": "Drew Faust"
    },
    {
      "date": "2012-09-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v7w7w3/intro---9-18-12",
        "http://thecolbertreport.cc.com/videos/53lqfp/logo-makeover-for-usa-today",
        "http://thecolbertreport.cc.com/videos/dsvsbf/mitt-romney-s-secret-video",
        "http://thecolbertreport.cc.com/videos/m021ol/tip-wag---apple-samsung-lawsuit---tabloid-clash",
        "http://thecolbertreport.cc.com/videos/ni1t1w/jeffrey-toobin",
        "http://thecolbertreport.cc.com/videos/qteu69/sign-off---shrimp-toss"
      ],
      "guest": "Jeffrey Toobin"
    },
    {
      "date": "2012-09-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8pu5um/intro---9-19-12",
        "http://thecolbertreport.cc.com/videos/yf80jg/mitt-romney-s---barack-obama-s-secret-videos",
        "http://thecolbertreport.cc.com/videos/rdsd7t/the-word---ask-not",
        "http://thecolbertreport.cc.com/videos/4yfsux/wife-of-jesus",
        "http://thecolbertreport.cc.com/videos/3vyhzj/itzhak-perlman"
      ],
      "guest": "Itzhak Perlman"
    },
    {
      "date": "2012-09-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8f3t3h/vladimir-putin-s-crane-flight",
        "http://thecolbertreport.cc.com/videos/asy3gz/mitt-romney-s-hispanic-outreach",
        "http://thecolbertreport.cc.com/videos/3f13ot/mitt-romney-s-hispanic-outreach---esteban-colberto",
        "http://thecolbertreport.cc.com/videos/2ufg9n/alpha-dog-of-the-week---cecilia-gimenez",
        "http://thecolbertreport.cc.com/videos/nxad9d/errol-morris",
        "http://thecolbertreport.cc.com/videos/sbgok9/sign-off---ask-o-matic"
      ],
      "guest": "Errol Morris"
    },
    {
      "date": "2012-09-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kke43t/intro---9-25-12",
        "http://thecolbertreport.cc.com/videos/ahsdxc/mitt-romney-s-airplane-window-gaffe",
        "http://thecolbertreport.cc.com/videos/495xja/national-journal-poll",
        "http://thecolbertreport.cc.com/videos/9vebvz/-rolling-calamity--campaign----america-again--preview",
        "http://thecolbertreport.cc.com/videos/vk8jsq/sport-report---nfl-referee-lockout---replacement-refs---ratings",
        "http://thecolbertreport.cc.com/videos/1my2a8/claressa-shields",
        "http://thecolbertreport.cc.com/videos/n6n3t7/sign-off----america-again-"
      ],
      "guest": "Claressa Shields"
    },
    {
      "date": "2012-09-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dfrukr/intro---9-26-12",
        "http://thecolbertreport.cc.com/videos/diooyo/yom-kippur---aporkalypse",
        "http://thecolbertreport.cc.com/videos/pnhcq0/obama-s-ottoman-empire",
        "http://thecolbertreport.cc.com/videos/kzi40s/40-days-to-save-america",
        "http://thecolbertreport.cc.com/videos/lsl385/jim-holt",
        "http://thecolbertreport.cc.com/videos/jwctvx/sign-off---turkish-delight"
      ],
      "guest": "Jim Holt"
    },
    {
      "date": "2012-09-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/373l0t/-america-again--re-becoming-the-greatness-we-never-weren-t-",
        "http://thecolbertreport.cc.com/videos/s9359o/mitt-romney-s-sliding-poll-numbers",
        "http://thecolbertreport.cc.com/videos/zpnkfm/-skewed--presidential-polls",
        "http://thecolbertreport.cc.com/videos/7tmsil/vince-gilligan-pt--1",
        "http://thecolbertreport.cc.com/videos/e6j3e4/vince-gilligan-pt--2",
        "http://thecolbertreport.cc.com/videos/xrnkns/sign-off----america-again-"
      ],
      "guest": "Vince Gilligan"
    },
    {
      "date": "2012-10-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/21ytsa/mitt-romney-s-tax-plan-math",
        "http://thecolbertreport.cc.com/videos/v5694x/the-word---supply-chained",
        "http://thecolbertreport.cc.com/videos/h64sbo/mahmoud-ahmadinejad-s-un-entourage",
        "http://thecolbertreport.cc.com/videos/k9q5kh/ben-folds-five"
      ],
      "guest": "Ben Folds Five"
    },
    {
      "date": "2012-10-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5ujlwr/intro---10-2-12",
        "http://thecolbertreport.cc.com/videos/yeek7a/-america-again--release",
        "http://thecolbertreport.cc.com/videos/cy7c9f/pulpit-freedom-sunday",
        "http://thecolbertreport.cc.com/videos/x5r0se/pulpit-freedom-sunday---jim-garlow",
        "http://thecolbertreport.cc.com/videos/oe7wh2/debate-hype---mitt-s-strategy",
        "http://thecolbertreport.cc.com/videos/78yg26/jorge-ramos",
        "http://thecolbertreport.cc.com/videos/dictxb/sign-off----america-again--release"
      ],
      "guest": "Jorge Ramos"
    },
    {
      "date": "2012-10-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ef28hc/intro---10-3-12",
        "http://thecolbertreport.cc.com/videos/05md2w/presidential-debates---mitt-romney-s-re-introduction",
        "http://thecolbertreport.cc.com/videos/2cmp66/george-will-s-political-post-racial-journalism",
        "http://thecolbertreport.cc.com/videos/idoutl/cheating-death---low-t",
        "http://thecolbertreport.cc.com/videos/nw3yhm/kenny-rogers",
        "http://thecolbertreport.cc.com/videos/rt3hz7/sign-off---banana-phone"
      ],
      "guest": "Kenny Rogers"
    },
    {
      "date": "2012-10-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5uncqq/obama-s-debate-apathy---pbs",
        "http://thecolbertreport.cc.com/videos/cl08kb/chris-matthews-s-impotent-rage",
        "http://thecolbertreport.cc.com/videos/inrj8y/mitt-s-socialist-rhetoric---body-language",
        "http://thecolbertreport.cc.com/videos/mw7xqx/mitt-s--etch-a-sketch--behavior",
        "http://thecolbertreport.cc.com/videos/nvjrik/voter-fraud-alert---halloween---pennsylvania",
        "http://thecolbertreport.cc.com/videos/fkt99i/george-church",
        "http://thecolbertreport.cc.com/videos/8vqy9e/sign-off---rabbit-food"
      ],
      "guest": "Dr. George Church"
    },
    {
      "date": "2012-10-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ohtrd9/intro---10-8-12",
        "http://thecolbertreport.cc.com/videos/53brnc/unemployment-below-eight-percent",
        "http://thecolbertreport.cc.com/videos/uey9b0/the-word---it-s-not-easy-having-green",
        "http://thecolbertreport.cc.com/videos/s8mn29/koch-brothers---orc-senate-candidate",
        "http://thecolbertreport.cc.com/videos/43khod/mark-kelly",
        "http://thecolbertreport.cc.com/videos/sq2eio/sign-off---welcome-baby-brumm-"
      ],
      "guest": "Mark Kelly"
    },
    {
      "date": "2012-10-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/htdpl2/intro---10-9-12",
        "http://thecolbertreport.cc.com/videos/69kfag/president-obama-s-obsessiveness-plea",
        "http://thecolbertreport.cc.com/videos/0g0ihq/smokin--pole---the-quest-for-arctic-riches---china---russia",
        "http://thecolbertreport.cc.com/videos/fu9mpp/mitt-romney-s-vague--long-winded-foreign-threats",
        "http://thecolbertreport.cc.com/videos/fgftvy/morrissey"
      ],
      "guest": "Morrissey"
    },
    {
      "date": "2012-10-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4jb3d3/intro---10-10-12",
        "http://thecolbertreport.cc.com/videos/ejqp1v/beverage-based-polling---pizza-toppings-town-hall",
        "http://thecolbertreport.cc.com/videos/jur0u9/the-word---meducation",
        "http://thecolbertreport.cc.com/videos/t1y0rc/threatdown---apple-fan-bears--drunk-cars---bears",
        "http://thecolbertreport.cc.com/videos/plccwf/naomi-wolf",
        "http://thecolbertreport.cc.com/videos/od1her/sign-off----vagina--a-new-biography-"
      ],
      "guest": "Naomi Wolf"
    },
    {
      "date": "2012-10-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6smkkc/intro---10-11-12",
        "http://thecolbertreport.cc.com/videos/kiyawb/the-vice-presidential-debate",
        "http://thecolbertreport.cc.com/videos/s190yi/this-changes-everything---obama-s-martian-gayness",
        "http://thecolbertreport.cc.com/videos/2ksunf/formidable-opponent---mitt-romney",
        "http://thecolbertreport.cc.com/videos/xhdwfk/chrystia-freeland",
        "http://thecolbertreport.cc.com/videos/zr1go5/sign-off---goodnight"
      ],
      "guest": "Chrystia Freeland"
    },
    {
      "date": "2012-10-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fuzsdf/intro---10-15-12",
        "http://thecolbertreport.cc.com/videos/0bmyur/supersonic-space-jump",
        "http://thecolbertreport.cc.com/videos/iudpa7/tip-wag---norway---american-family-association",
        "http://thecolbertreport.cc.com/videos/0q2emr/monkey-on-the-lam---florida---monkey-on-the-gram",
        "http://thecolbertreport.cc.com/videos/zj6xib/evan-thomas",
        "http://thecolbertreport.cc.com/videos/n0kt18/sign-off---goodnight"
      ],
      "guest": "Evan Thomas"
    },
    {
      "date": "2012-10-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/keo9r0/the-wealth-edge----cool--debate-technology",
        "http://thecolbertreport.cc.com/videos/4aqbh6/affirmative-action-supreme-court-case",
        "http://thecolbertreport.cc.com/videos/y46z6y/affirmative-action-supreme-court-case---emily-bazelon",
        "http://thecolbertreport.cc.com/videos/4uld4g/paul-ryan-s-phony-campaign-photo",
        "http://thecolbertreport.cc.com/videos/4c7frp/cory-booker",
        "http://thecolbertreport.cc.com/videos/juen77/sign-off---iphone"
      ],
      "guest": "Cory Booker"
    },
    {
      "date": "2012-10-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wd584x/second-presidential-debate-showdown",
        "http://thecolbertreport.cc.com/videos/rjvmac/libya-gate-scandal",
        "http://thecolbertreport.cc.com/videos/j531em/stupid-town-hall-topics",
        "http://thecolbertreport.cc.com/videos/jr7tf6/mitt-s-greatest-debate-triumph",
        "http://thecolbertreport.cc.com/videos/hhxtxg/alpha-dog-of-the-week---scott-desjarlais",
        "http://thecolbertreport.cc.com/videos/f4jil4/tyler-perry",
        "http://thecolbertreport.cc.com/videos/namywp/sign-off---loose-teeth"
      ],
      "guest": "Tyler Perry"
    },
    {
      "date": "2012-10-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1dfeya/celebrity-campaign-endorsements",
        "http://thecolbertreport.cc.com/videos/rgzljg/mitt-s-first-day",
        "http://thecolbertreport.cc.com/videos/2q39xi/junk-food-feed",
        "http://thecolbertreport.cc.com/videos/xttei6/special-report---a-shucking-disaster---nightmare-at-the-mitchell-corn-palace",
        "http://thecolbertreport.cc.com/videos/t8vgd4/the-killers",
        "http://thecolbertreport.cc.com/videos/ieuitc/sign-off----battle-born-"
      ],
      "guest": "The Killers"
    },
    {
      "date": "2012-10-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0t7wmw/virginia-s-voter-fraud-fighter",
        "http://thecolbertreport.cc.com/videos/jhyr4v/ceo-blackmail---fec-consent",
        "http://thecolbertreport.cc.com/videos/t1yx0h/governor-magorium-s-ganja-emporium",
        "http://thecolbertreport.cc.com/videos/8uddyg/donald-sadoway",
        "http://thecolbertreport.cc.com/videos/czceut/sign-off---goodnight"
      ],
      "guest": "Donald Sadoway"
    },
    {
      "date": "2012-10-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nept6x/stephen-colbert-s-debate-2012-coverage",
        "http://thecolbertreport.cc.com/videos/wowfoq/elusive--mysterious--undecided-voters",
        "http://thecolbertreport.cc.com/videos/twexhe/lance-armstrong-s-doping-scandal",
        "http://thecolbertreport.cc.com/videos/hrawp4/john-grisham",
        "http://thecolbertreport.cc.com/videos/rxk7z1/sign-off---manischewitz"
      ],
      "guest": "John Grisham"
    },
    {
      "date": "2012-10-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3gbfdl/intro---10-24-12",
        "http://thecolbertreport.cc.com/videos/ifrr4g/donald-trump-s-october-surprise",
        "http://thecolbertreport.cc.com/videos/n9028e/nonstop-libya-gate-questions",
        "http://thecolbertreport.cc.com/videos/gzidte/richard-mourdock-s-rape-comment",
        "http://thecolbertreport.cc.com/videos/swkt4w/anthony-everitt",
        "http://thecolbertreport.cc.com/videos/ug2zqb/sign-off---gop-rape-mention-tally"
      ],
      "guest": "Anthony Everitt"
    },
    {
      "date": "2012-10-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7k4pkh/intro---10-25-12",
        "http://thecolbertreport.cc.com/videos/a0h9on/voting---hormones",
        "http://thecolbertreport.cc.com/videos/zu00re/stephen-ghoulbert-s-spooky-time-halloween-fun-guide---tom-hanks",
        "http://thecolbertreport.cc.com/videos/pb058e/mitch-daniels-pt--1",
        "http://thecolbertreport.cc.com/videos/9tzl4i/mitch-daniels-pt--2",
        "http://thecolbertreport.cc.com/videos/pstvp6/sign-off---murderer-skull-model"
      ],
      "guest": "Gov. Mitch Daniels"
    },
    {
      "date": "2012-10-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rky5ab/hurricane-sandy-s-aftermath",
        "http://thecolbertreport.cc.com/videos/ey2jqz/hurricane-sandy---election-day",
        "http://thecolbertreport.cc.com/videos/lk60fg/flamboyant-sandy---federal-relief-debate",
        "http://thecolbertreport.cc.com/videos/5vx4ad/donald-trump-s-october-surprise-extension",
        "http://thecolbertreport.cc.com/videos/x89ju7/lilly-ledbetter",
        "http://thecolbertreport.cc.com/videos/jqfgo3/sign-off---american-red-cross---hurricane-sandy"
      ],
      "guest": "Lilly Ledbetter"
    },
    {
      "date": "2012-11-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hk2ox4/intro---11-1-12",
        "http://thecolbertreport.cc.com/videos/mtuxrh/hurricane-sandy-traffic-ordeal",
        "http://thecolbertreport.cc.com/videos/pdmw4z/tip-wag---constant-documentation---billy-graham",
        "http://thecolbertreport.cc.com/videos/rmzkbz/david-byrne---st--vincent",
        "http://thecolbertreport.cc.com/videos/w4v4gd/sign-off---american-red-cross---hurricane-sandy"
      ],
      "guest": "David Byrne &amp; St. Vincent"
    },
    {
      "date": "2012-11-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mm7c7b/colbert-super-pac---severe-candidate-warning",
        "http://thecolbertreport.cc.com/videos/h3qcht/shame-based-campaigning",
        "http://thecolbertreport.cc.com/videos/ga4hky/shame-based-campaigning---sasha-issenberg",
        "http://thecolbertreport.cc.com/videos/ef460s/-razor-tight--presidential-election",
        "http://thecolbertreport.cc.com/videos/tl7vb4/nate-silver",
        "http://thecolbertreport.cc.com/videos/i1cdch/sign-off---go-vote-"
      ],
      "guest": "Nate Silver"
    },
    {
      "date": "2012-11-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2wfr8k/the-colbert-report-election-2012---who-will-replace-obama---012",
        "http://thecolbertreport.cc.com/videos/ydqq2x/the-colbert-report-election-2012---too-close-to-call",
        "http://thecolbertreport.cc.com/videos/b9hvj6/andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/vghwne/senate-races---state-referenda",
        "http://thecolbertreport.cc.com/videos/cao81i/sign-off---election-reflections"
      ],
      "guest": "Andrew Sullivan"
    },
    {
      "date": "2012-11-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d96ihg/intro---11-7-12",
        "http://thecolbertreport.cc.com/videos/zviz5s/four-more-years-of-hopey-change",
        "http://thecolbertreport.cc.com/videos/hbkurh/nontraditional-non-white-america",
        "http://thecolbertreport.cc.com/videos/btqtta/polling-irregularities---vote-by-phone-scam",
        "http://thecolbertreport.cc.com/videos/wjevw3/wind-power-s-health-hazards",
        "http://thecolbertreport.cc.com/videos/xs8d72/doris-kearns-goodwin",
        "http://thecolbertreport.cc.com/videos/6iwo2a/sign-off---solace-in-a-bottle"
      ],
      "guest": "Doris Kearns Goodwin"
    },
    {
      "date": "2012-11-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lttdhm/intro---11-8-12",
        "http://thecolbertreport.cc.com/videos/op51y2/nor-easter---mitt-romney",
        "http://thecolbertreport.cc.com/videos/ryj0jw/difference-makers---stephen-dick-jr-",
        "http://thecolbertreport.cc.com/videos/25lwb9/the-plight-of-platonic-relationships",
        "http://thecolbertreport.cc.com/videos/doygtf/rachel-maddow",
        "http://thecolbertreport.cc.com/videos/jzxfgf/sign-off---goodnight"
      ],
      "guest": "Rachel Maddow"
    },
    {
      "date": "2012-11-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3szdub/david-petraeus-s--all-in--affair",
        "http://thecolbertreport.cc.com/videos/kj1cs9/colbert-super-pac-shh----karl-rove---jon-stewart",
        "http://thecolbertreport.cc.com/videos/66y7dx/colbert-super-pac-shh----secret-second-501c4---trevor-potter",
        "http://thecolbertreport.cc.com/videos/tl4uce/blitzkrieg-on-grinchitude---santa-s-pipe",
        "http://thecolbertreport.cc.com/videos/6vpcf3/ken-burns",
        "http://thecolbertreport.cc.com/videos/3w1i4s/sign-off---goodbye-colbert-super-pac"
      ],
      "guest": "Ken Burns"
    },
    {
      "date": "2012-11-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/i9yvhl/intro---11-13-12",
        "http://thecolbertreport.cc.com/videos/uml8yd/2072--race-to-the-white-orb",
        "http://thecolbertreport.cc.com/videos/s5vmrx/tip-wag---pranab-mukherjee--brazilian-scientists--sonia-sotomayor",
        "http://thecolbertreport.cc.com/videos/icmpvx/newt-gingrich-pt--1",
        "http://thecolbertreport.cc.com/videos/61deqz/newt-gingrich-pt--2",
        "http://thecolbertreport.cc.com/videos/ujlf67/sign-off---goodnight"
      ],
      "guest": "Newt Gingrich"
    },
    {
      "date": "2012-11-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e0pxrk/intro---11-14-12",
        "http://thecolbertreport.cc.com/videos/3zu15f/who-s-attacking-me-now----canadian-broadcasting-corporation",
        "http://thecolbertreport.cc.com/videos/kvs6wn/high-frequency-trading",
        "http://thecolbertreport.cc.com/videos/ba8i6j/high-frequency-trading---christopher-steiner",
        "http://thecolbertreport.cc.com/videos/wvf1nd/tony-kushner-pt--1",
        "http://thecolbertreport.cc.com/videos/ezygjv/tony-kushner-pt--2",
        "http://thecolbertreport.cc.com/videos/cz0sty/sign-off---goodnight"
      ],
      "guest": "Tony Kushner"
    },
    {
      "date": "2012-11-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cazbp6/intro---11-15-12",
        "http://thecolbertreport.cc.com/videos/regxdh/millennial-generation-soup-campaign",
        "http://thecolbertreport.cc.com/videos/jy83mg/general-s-hospital",
        "http://thecolbertreport.cc.com/videos/xve006/cheating-death---flu-fighting-meth",
        "http://thecolbertreport.cc.com/videos/we1zlp/chris-stringer",
        "http://thecolbertreport.cc.com/videos/f23a7f/sign-off---the-colbert-report-s-seventh-anniversary"
      ],
      "guest": "Chris Stringer"
    },
    {
      "date": "2012-11-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9ex0kp/intro---11-26-12",
        "http://thecolbertreport.cc.com/videos/i4lmrj/stephen-s-thanksgiving---holy-black-friday",
        "http://thecolbertreport.cc.com/videos/242ato/judge--jury---executioner---copyright-law",
        "http://thecolbertreport.cc.com/videos/ob3lcn/blitzkrieg-on-grinchitude---pope-benedict-xvi",
        "http://thecolbertreport.cc.com/videos/std5aq/jake-tapper",
        "http://thecolbertreport.cc.com/videos/o2lec3/sign-off---goodnight"
      ],
      "guest": "Jake Tapper"
    },
    {
      "date": "2012-11-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oh9w4r/canada-s-grinch",
        "http://thecolbertreport.cc.com/videos/7imsna/the-fiscal-cliff-compromise",
        "http://thecolbertreport.cc.com/videos/72sdt0/the-fiscal-cliff-compromise---reihan-salam",
        "http://thecolbertreport.cc.com/videos/1fuekz/dolly-parton",
        "http://thecolbertreport.cc.com/videos/nqrlrq/sign-off---country-chords"
      ],
      "guest": "Dolly Parton"
    },
    {
      "date": "2012-11-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ui3lan/intro---11-28-12",
        "http://thecolbertreport.cc.com/videos/omvkv3/record-powerball-jackpot",
        "http://thecolbertreport.cc.com/videos/tnr1l8/the-word---sisters-are-doing-it-to-themselves",
        "http://thecolbertreport.cc.com/videos/xpxkwl/filibuster-reform",
        "http://thecolbertreport.cc.com/videos/qc393o/frank-oz",
        "http://thecolbertreport.cc.com/videos/b9jkcc/sign-off---stephen-s-muppet"
      ],
      "guest": "Frank Oz"
    },
    {
      "date": "2012-11-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gnb0gv/intro---11-29-12",
        "http://thecolbertreport.cc.com/videos/cehmsr/moon-shattering-news",
        "http://thecolbertreport.cc.com/videos/9o0ttj/tip-wag---gay-rights-pioneers---gun-dorms",
        "http://thecolbertreport.cc.com/videos/dgy710/top-10-of-2012---operation-killing--killing-kennedy-",
        "http://thecolbertreport.cc.com/videos/qyxymb/sean-carroll",
        "http://thecolbertreport.cc.com/videos/z8pd91/sign-off---acceptance-speech"
      ],
      "guest": "Sean Carroll"
    },
    {
      "date": "2012-12-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c2msxt/the-pundit--or-colbert-and-back-again",
        "http://thecolbertreport.cc.com/videos/i94qww/the-pundit--or-colbert-and-back-again---hobbit-week-lineup",
        "http://thecolbertreport.cc.com/videos/zkpe65/the-word---base-instincts",
        "http://thecolbertreport.cc.com/videos/47ssk7/senior-moment---granny-pods",
        "http://thecolbertreport.cc.com/videos/zm84yu/ian-mckellen",
        "http://thecolbertreport.cc.com/videos/u8z3mx/sign-off---the-pundit--or-colbert-and-back-again---sting"
      ],
      "guest": "Ian McKellen"
    },
    {
      "date": "2012-12-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ri5csw/the-pundit--or-colbert-and-back-again---hobbit-week-night-two",
        "http://thecolbertreport.cc.com/videos/q3aiti/low-t---low-o",
        "http://thecolbertreport.cc.com/videos/n7lg1x/kate-the-great-s-morning-sickness",
        "http://thecolbertreport.cc.com/videos/v8syf8/martin-freeman",
        "http://thecolbertreport.cc.com/videos/rmahy7/sign-off---the-pundit--or-colbert-and-back-again---rivendell"
      ],
      "guest": "Martin Freeman"
    },
    {
      "date": "2012-12-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qtkdcn/the-pundit--or-colbert-and-back-again---hobbit-week-night-three",
        "http://thecolbertreport.cc.com/videos/6x66a7/the-word---hire-learning",
        "http://thecolbertreport.cc.com/videos/9j5qtc/politicos---paranoid-fantasies",
        "http://thecolbertreport.cc.com/videos/m8dp2f/andy-serkis",
        "http://thecolbertreport.cc.com/videos/msip4s/sign-off---the-pundit--or-colbert-and-back-again---one-ring"
      ],
      "guest": "Peter Jackson"
    },
    {
      "date": "2012-12-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/teluzg/the-pundit--or-colbert-and-back-again---hobbit-week-night-four",
        "http://thecolbertreport.cc.com/videos/hhe4hg/jim-demint-s-resignation",
        "http://thecolbertreport.cc.com/videos/d0n0vz/stephen-colbert--wax-on---wax-off-at-madame-tussauds-pt--1",
        "http://thecolbertreport.cc.com/videos/1voj50/stephen-colbert--wax-on---wax-off-at-madame-tussauds-pt--2",
        "http://thecolbertreport.cc.com/videos/0tvck8/peter-jackson",
        "http://thecolbertreport.cc.com/videos/fbqohj/sign-off---the-pundit--or-colbert-and-back-again---hobbit-week-concludes"
      ],
      "guest": "Andy Serkis"
    },
    {
      "date": "2012-12-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0cfmll/stephen-for-u-s--senate",
        "http://thecolbertreport.cc.com/videos/8skoq2/fox-news-s-secret-presidential-recruit",
        "http://thecolbertreport.cc.com/videos/gdygvq/diana-krall"
      ],
      "guest": "Diana Krall, Elvis Costello"
    },
    {
      "date": "2012-12-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t45azb/intro---12-11-12",
        "http://thecolbertreport.cc.com/videos/69xjmc/fiscal-cliff-negotiations",
        "http://thecolbertreport.cc.com/videos/iwvp9d/threatdown---commie-unicorns---foreman-barbie",
        "http://thecolbertreport.cc.com/videos/8is78z/ex-gay-therapy-debate",
        "http://thecolbertreport.cc.com/videos/m3omdi/malcolm-gladwell"
      ],
      "guest": "Malcolm Gladwell, Audra McDonald"
    },
    {
      "date": "2012-12-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hoair6/success-for-operation-killing--killing-kennedy-",
        "http://thecolbertreport.cc.com/videos/8aazot/stephen-s-appointment-with-destiny---jeff-bingaman",
        "http://thecolbertreport.cc.com/videos/yr83zl/ground-zero-mosque-erade",
        "http://thecolbertreport.cc.com/videos/38iv8s/mandy-patinkin"
      ],
      "guest": "Mandy Patinkin, Michael Stipe"
    },
    {
      "date": "2012-12-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ao4d2q/hurricane-sandy-mega-concert",
        "http://thecolbertreport.cc.com/videos/dseos2/uncensored----breaking-abbey-",
        "http://thecolbertreport.cc.com/videos/clpvpj/colbert-super-pac---the-ham-rove-memorial-fund",
        "http://thecolbertreport.cc.com/videos/wozbhp/simone-campbell"
      ],
      "guest": "Sister Simone Campbell, Jeff Tweedy, Mavis Staples, Sean Lennon"
    }
  ],
  "2013": [
    {
      "date": "2013-01-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bgkrwx/intro---1-7-13",
        "http://thecolbertreport.cc.com/videos/83h5da/stephen-s-holiday-break",
        "http://thecolbertreport.cc.com/videos/9nmhtf/fiscal-cliff-deal---disincentives",
        "http://thecolbertreport.cc.com/videos/wq7dip/the-platinum-debt-ceiling-solution",
        "http://thecolbertreport.cc.com/videos/b1uvtc/blood-in-the-water---bill-o-reilly-s-racial-insensitivity",
        "http://thecolbertreport.cc.com/videos/ayoamg/jimmy-wales",
        "http://thecolbertreport.cc.com/videos/a1dzb3/sign-off---goodnight"
      ],
      "guest": "Jimmy Wales"
    },
    {
      "date": "2013-01-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fuxwr9/intro---1-8-13",
        "http://thecolbertreport.cc.com/videos/gdcdgs/postage-price-hike",
        "http://thecolbertreport.cc.com/videos/vcqeg7/cheating-death---rage---blood-transfusions",
        "http://thecolbertreport.cc.com/videos/ps8djx/bin-laden-film-controversy",
        "http://thecolbertreport.cc.com/videos/kq9pp2/chris-kluwe",
        "http://thecolbertreport.cc.com/videos/gcv2eh/sign-off---vacsa-tern"
      ],
      "guest": "Chris Kluwe"
    },
    {
      "date": "2013-01-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kg1znk/intro---1-9-13",
        "http://thecolbertreport.cc.com/videos/ip7ql9/idaho-s-walled---armed-community",
        "http://thecolbertreport.cc.com/videos/tzcfhr/gun-control-backlash",
        "http://thecolbertreport.cc.com/videos/52uula/thought-for-food---wheat-addictions",
        "http://thecolbertreport.cc.com/videos/ysa6lr/neil-shubin",
        "http://thecolbertreport.cc.com/videos/5majke/sign-off---mcgnaw-the-gluten-free-beaver"
      ],
      "guest": "Neil Shubin"
    },
    {
      "date": "2013-01-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uej3ac/roadside-sofa-boning",
        "http://thecolbertreport.cc.com/videos/5n5w35/obama-s-failed-second-term",
        "http://thecolbertreport.cc.com/videos/35sqrd/tip-wag---hapifork---kevin-garnett",
        "http://thecolbertreport.cc.com/videos/ro7hjf/benjamin-gibbard"
      ],
      "guest": "Ben Gibbard"
    },
    {
      "date": "2013-01-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y2ynrh/stephen-colbert-s-double-barrel-blam-o-rama---silver-bullets---video-games",
        "http://thecolbertreport.cc.com/videos/8zsm19/stephen-colbert-s-double-barrel-blam-o-rama---piers-morgan---james-yeager",
        "http://thecolbertreport.cc.com/videos/zftq7q/stephen-colbert-s-double-barrel-blam-o-rama---guns-as-civil-rights-victims",
        "http://thecolbertreport.cc.com/videos/4lcqtx/vitaminwater-advertising-lawsuit",
        "http://thecolbertreport.cc.com/videos/bainem/piers-morgan",
        "http://thecolbertreport.cc.com/videos/hoc2kn/sign-off---pocketbook-constitution"
      ],
      "guest": "Piers Morgan"
    },
    {
      "date": "2013-01-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t6cye7/intro---1-15-13",
        "http://thecolbertreport.cc.com/videos/p5ll7c/lance-armstrong-s-interview-with-oprah",
        "http://thecolbertreport.cc.com/videos/uuduw3/monkey-on-the-lam---macaque-attack---1-381-days-of-simian-terror-in-tampa",
        "http://thecolbertreport.cc.com/videos/r78s3t/catacoffin-catacombo-sound-system",
        "http://thecolbertreport.cc.com/videos/an9lge/jared-diamond",
        "http://thecolbertreport.cc.com/videos/usj2pz/sign-off---goodnight"
      ],
      "guest": "Jared Diamond"
    },
    {
      "date": "2013-01-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j56lbb/intro---1-16-13",
        "http://thecolbertreport.cc.com/videos/s9aj13/healthy-fake-smiles",
        "http://thecolbertreport.cc.com/videos/uhkynp/hsbc-laundering-charges",
        "http://thecolbertreport.cc.com/videos/hbxrk6/hsbc-laundering-charges---matt-taibbi",
        "http://thecolbertreport.cc.com/videos/62nu7n/pat-robertson-s-romance-advice",
        "http://thecolbertreport.cc.com/videos/m7jh2f/tom-brokaw",
        "http://thecolbertreport.cc.com/videos/ib0ftp/sign-off---goodnight"
      ],
      "guest": "Tom Brokaw"
    },
    {
      "date": "2013-01-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r3kb1q/exclusive---colbert-wax-on---wax-off-at-madame-tussauds--outtakes",
        "http://thecolbertreport.cc.com/videos/qqx0s8/corporate-scamwich",
        "http://thecolbertreport.cc.com/videos/df7rup/obama-s-gun-grab",
        "http://thecolbertreport.cc.com/videos/w73nzv/the-word---united-we-standoff",
        "http://thecolbertreport.cc.com/videos/g1jrq5/porn-names---porn-lawsuits",
        "http://thecolbertreport.cc.com/videos/vem33s/akhil-reed-amar",
        "http://thecolbertreport.cc.com/videos/jawwj8/sign-off---goodnight"
      ],
      "guest": "Akhil Reed Amar"
    },
    {
      "date": "2013-01-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zzot6e/intro---1-21-13",
        "http://thecolbertreport.cc.com/videos/xjexam/obama-s-second-inauguration",
        "http://thecolbertreport.cc.com/videos/li25sm/stephen-s-re-inauguration",
        "http://thecolbertreport.cc.com/videos/djvjxw/threatdown---flu--kate-middleton--vomiting-robots--superintelligent-gonorrhea--bears",
        "http://thecolbertreport.cc.com/videos/o7bw1e/ta-nehisi-coates",
        "http://thecolbertreport.cc.com/videos/9hwods/sign-off---hotel-bibles"
      ],
      "guest": "Ta-Nehisi Coates"
    },
    {
      "date": "2013-01-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u2sxvp/exclusive---kathryn-bigelow-extended-interview",
        "http://thecolbertreport.cc.com/videos/4h7ltu/obama-s-inauguration---class-warfare",
        "http://thecolbertreport.cc.com/videos/0f673t/the-word---win--lose--or-redraw",
        "http://thecolbertreport.cc.com/videos/tccphp/dustin-hoffman-s-bad-news",
        "http://thecolbertreport.cc.com/videos/rn0fho/kathryn-bigelow",
        "http://thecolbertreport.cc.com/videos/msaso2/sign-off----zero-dark-thirty-----quartet-"
      ],
      "guest": "Kathryn Bigelow"
    },
    {
      "date": "2013-01-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3reklz/beyonce-s-lip-gate",
        "http://thecolbertreport.cc.com/videos/vw3zie/tip-wag---montpelier-school-district--theatlasphere-com---florida-officials",
        "http://thecolbertreport.cc.com/videos/f3o0qj/alpha-dog-of-the-week---virginia-state-senate-republicans",
        "http://thecolbertreport.cc.com/videos/202a1c/sally-field",
        "http://thecolbertreport.cc.com/videos/hd80sm/sign-off---goodnight"
      ],
      "guest": "Sally Field"
    },
    {
      "date": "2013-01-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xaaxud/france---the-mali-conflict",
        "http://thecolbertreport.cc.com/videos/i1sdq5/france---the-mali-conflict---edward-berenson",
        "http://thecolbertreport.cc.com/videos/vgqq4z/benghazi-attack-hearing",
        "http://thecolbertreport.cc.com/videos/ktiaje/tavi-gevinson",
        "http://thecolbertreport.cc.com/videos/scixor/sign-off---stephen-s-makeover"
      ],
      "guest": "Tavi Gevinson"
    },
    {
      "date": "2013-01-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/q1iuxz/intro---1-28-13",
        "http://thecolbertreport.cc.com/videos/27at9z/rapiscan-scanners",
        "http://thecolbertreport.cc.com/videos/mm5bdz/the-word---the-new-abnormal",
        "http://thecolbertreport.cc.com/videos/0q31iw/the-axis-of-evil-of-the-week---north-korea",
        "http://thecolbertreport.cc.com/videos/qdf7ec/michael-shellenberger",
        "http://thecolbertreport.cc.com/videos/tquuvs/sign-off---goodnight"
      ],
      "guest": "Michael Shellenberger"
    },
    {
      "date": "2013-01-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4ax2hi/intro---1-29-13",
        "http://thecolbertreport.cc.com/videos/81oaln/iran-s-space-monkey---america-s-ape-moratorium",
        "http://thecolbertreport.cc.com/videos/k95k9v/gun-control---state-sovereignty",
        "http://thecolbertreport.cc.com/videos/7c8y4f/gun-control---state-sovereignty---cliff-sloan",
        "http://thecolbertreport.cc.com/videos/gfoq4g/guantanamo-bay-office-closure",
        "http://thecolbertreport.cc.com/videos/jtkgrc/george-saunders",
        "http://thecolbertreport.cc.com/videos/jzuerq/sign-off----tenth-of-december-"
      ],
      "guest": "George Saunders"
    },
    {
      "date": "2013-01-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/omljip/intro---1-30-13",
        "http://thecolbertreport.cc.com/videos/drdd3e/coming-out-benefits---gay-rights",
        "http://thecolbertreport.cc.com/videos/qnfsur/the-word---it-gets-worse",
        "http://thecolbertreport.cc.com/videos/i6hr57/non-racist-kkk",
        "http://thecolbertreport.cc.com/videos/kiwt0s/bill-gates",
        "http://thecolbertreport.cc.com/videos/4wroqd/sign-off---goodnight"
      ],
      "guest": "Bill Gates"
    },
    {
      "date": "2013-01-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/101faw/sport-report---ads-for-ads---deer-antler-spray",
        "http://thecolbertreport.cc.com/videos/odn1pg/sport-report---gatorade-chemicals---chicken-wing-shortage",
        "http://thecolbertreport.cc.com/videos/7wymxs/craziest-f--king-thing-i-ve-ever-heard---crows-using-tools",
        "http://thecolbertreport.cc.com/videos/v42kz3/matthew-guerrieri",
        "http://thecolbertreport.cc.com/videos/o489no/sign-off---welcome-baby-sanchez-"
      ],
      "guest": "Matthew Guerrieri"
    },
    {
      "date": "2013-02-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iyrevo/intro---2-4-13",
        "http://thecolbertreport.cc.com/videos/kb76z3/super-bowl-xlvii",
        "http://thecolbertreport.cc.com/videos/vow0uy/bipartisan-immigration-reform",
        "http://thecolbertreport.cc.com/videos/ur7z4s/skeet-shooting-skeptics",
        "http://thecolbertreport.cc.com/videos/qxsatq/sonia-sotomayor",
        "http://thecolbertreport.cc.com/videos/cmttl3/sign-off---second-amendment"
      ],
      "guest": "Justice Sonia Sotomayor"
    },
    {
      "date": "2013-02-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2316uc/intro---2-5-13",
        "http://thecolbertreport.cc.com/videos/e96s3c/royal-remains",
        "http://thecolbertreport.cc.com/videos/t6wn9f/tip-wag---drunk-donating----the-job--reality-show",
        "http://thecolbertreport.cc.com/videos/a1z0cu/california-s-heroic-hitchhiker",
        "http://thecolbertreport.cc.com/videos/dyxduh/julie-andrews",
        "http://thecolbertreport.cc.com/videos/y7gdjs/sign-off---final-rose"
      ],
      "guest": "Julie Andrews"
    },
    {
      "date": "2013-02-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ae7fmq/intro---2-6-13",
        "http://thecolbertreport.cc.com/videos/33sahu/the-penny-pinch",
        "http://thecolbertreport.cc.com/videos/r6xbr9/stephen-s-sister-for-congress",
        "http://thecolbertreport.cc.com/videos/07240r/scientology-church-violence",
        "http://thecolbertreport.cc.com/videos/acokbc/lawrence-wright",
        "http://thecolbertreport.cc.com/videos/kt2abh/sign-off---watermelon-warning"
      ],
      "guest": "Lawrence Wright"
    },
    {
      "date": "2013-02-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/14j8d1/intro---2-7-13",
        "http://thecolbertreport.cc.com/videos/k4xzoo/winter-storm-nemo",
        "http://thecolbertreport.cc.com/videos/xknwhm/mr--smith-goes-to-the-state-legislature---stacey-campfield",
        "http://thecolbertreport.cc.com/videos/044mxj/-bang-with-friends--app",
        "http://thecolbertreport.cc.com/videos/eqsq39/benh-zeitlin",
        "http://thecolbertreport.cc.com/videos/xarh0o/sign-off---goodnight"
      ],
      "guest": "Behn Zeitlin"
    },
    {
      "date": "2013-02-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xstxbo/bush-family-email-hack",
        "http://thecolbertreport.cc.com/videos/s7p70k/pope-s-resignation---papal-speculatron-7500",
        "http://thecolbertreport.cc.com/videos/v1p2wr/pope-s-resignation---papal-speculatron-7500---james-martin",
        "http://thecolbertreport.cc.com/videos/he6l0j/garry-wills",
        "http://thecolbertreport.cc.com/videos/38op41/sign-off----why-priests--"
      ],
      "guest": "Garry Wills"
    },
    {
      "date": "2013-02-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hbhjqi/intro---2-12-13",
        "http://thecolbertreport.cc.com/videos/hwigu9/rnc-autopsy",
        "http://thecolbertreport.cc.com/videos/6t4bfw/conservative-victory-project",
        "http://thecolbertreport.cc.com/videos/b91wqa/arizona-s-gun-posse",
        "http://thecolbertreport.cc.com/videos/87jshg/roger-hodge",
        "http://thecolbertreport.cc.com/videos/4j42vn/sign-off---goodnight"
      ],
      "guest": "Roger Hodge"
    },
    {
      "date": "2013-02-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r8y2v4/obama-s-state-of-the-union",
        "http://thecolbertreport.cc.com/videos/7g4eal/state-of-the-rubio",
        "http://thecolbertreport.cc.com/videos/89tt3v/spanish-state-of-the-rubio",
        "http://thecolbertreport.cc.com/videos/wrywsk/dave-grohl",
        "http://thecolbertreport.cc.com/videos/rsui4q/sign-off---dry-mouth"
      ],
      "guest": "Dave Grohl"
    },
    {
      "date": "2013-02-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8k6qf1/st--valentine-s-day",
        "http://thecolbertreport.cc.com/videos/bg5se9/standard---poor-s-ratings-lawsuit",
        "http://thecolbertreport.cc.com/videos/a7o9iy/standard---poor-s-ratings-lawsuit---david-leonhardt",
        "http://thecolbertreport.cc.com/videos/gha2xx/nailed--em---richard-eggers",
        "http://thecolbertreport.cc.com/videos/jipac1/gavin-newsom",
        "http://thecolbertreport.cc.com/videos/tl6blx/sign-off----here-s-the-deal-"
      ],
      "guest": "Gavin Newsom"
    },
    {
      "date": "2013-02-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mk66vx/russian-meteor-strike",
        "http://thecolbertreport.cc.com/videos/18bt84/colbert-platinum---huayra-sports-car--phil-mickelson---belle-isle",
        "http://thecolbertreport.cc.com/videos/nzi8fo/obama-s-secretive-golf-outing",
        "http://thecolbertreport.cc.com/videos/qsppoj/emily-bazelon",
        "http://thecolbertreport.cc.com/videos/rivg1z/sign-off---goodnight"
      ],
      "guest": "Emily Bazelon"
    },
    {
      "date": "2013-02-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tq706t/u-k--horse-meat-scandal",
        "http://thecolbertreport.cc.com/videos/76hws3/sport-report---international-soccer-corruption",
        "http://thecolbertreport.cc.com/videos/t95tyj/sport-report---international-soccer-corruption---alexi-lalas",
        "http://thecolbertreport.cc.com/videos/oy70q1/norway-s--national-firewood-night-",
        "http://thecolbertreport.cc.com/videos/d68kfy/david-goldhill",
        "http://thecolbertreport.cc.com/videos/4869v6/sign-off---goodnight"
      ],
      "guest": "David Goldhill"
    },
    {
      "date": "2013-02-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5dzdoq/-friends-of-hamas--rumor",
        "http://thecolbertreport.cc.com/videos/0x6brn/geo-group-stadium",
        "http://thecolbertreport.cc.com/videos/yhhjej/corporate-twitter-hacks",
        "http://thecolbertreport.cc.com/videos/ef8eii/lil-buck"
      ],
      "guest": "Lil Buck"
    },
    {
      "date": "2013-02-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dysmy8/intro---2-25-13",
        "http://thecolbertreport.cc.com/videos/n5lz93/the-word---silent-but-deadly",
        "http://thecolbertreport.cc.com/videos/ub1skg/popewatch-2013---vatican-sex-parties",
        "http://thecolbertreport.cc.com/videos/ovpx97/simon-garfield",
        "http://thecolbertreport.cc.com/videos/7ucjsc/sign-off---goodnight"
      ],
      "guest": "Simon Garfield"
    },
    {
      "date": "2013-02-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8vjzyf/intro---2-26-13",
        "http://thecolbertreport.cc.com/videos/gy9em4/popewatch-indeschism-2013---one-pope-over-the-line",
        "http://thecolbertreport.cc.com/videos/f5k4cb/battleground-texas---jeremy-bird",
        "http://thecolbertreport.cc.com/videos/xdriyp/drone-ducking-tips",
        "http://thecolbertreport.cc.com/videos/wr3lk3/michio-kaku",
        "http://thecolbertreport.cc.com/videos/i7sahj/sign-off---goodnight"
      ],
      "guest": "Dr. Michio Kaku"
    },
    {
      "date": "2013-02-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6637zm/intro---2-27-13",
        "http://thecolbertreport.cc.com/videos/8okga0/halls-mentho-lyptus-cough-drops",
        "http://thecolbertreport.cc.com/videos/9mtjmn/khalid-sheikh-mohammed-s-trial-at-gitmo",
        "http://thecolbertreport.cc.com/videos/9mvj8u/khalid-sheikh-mohammed-s-trial-at-gitmo---neal-katyal",
        "http://thecolbertreport.cc.com/videos/r7gapm/john-kerry-s-dumb-talk",
        "http://thecolbertreport.cc.com/videos/cxjhmj/paola-antonelli",
        "http://thecolbertreport.cc.com/videos/7trotu/sign-off---halls-mentho-lyptus"
      ],
      "guest": "Paola Antonelli"
    },
    {
      "date": "2013-02-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hmyuom/intro---2-28-13",
        "http://thecolbertreport.cc.com/videos/1epo24/colbert-report-consumer-alert---demonic-goodwill-items",
        "http://thecolbertreport.cc.com/videos/d7le3o/pope-tbd---souvenir-sales",
        "http://thecolbertreport.cc.com/videos/tnbuj0/budget-sequestration",
        "http://thecolbertreport.cc.com/videos/66dbox/jon-favreau",
        "http://thecolbertreport.cc.com/videos/o5hoan/sign-off---goodnight"
      ],
      "guest": "Obama speechwriter Jon Favreau"
    },
    {
      "date": "2013-03-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ouzof3/sequestration---obama-s-sci-fi-flub",
        "http://thecolbertreport.cc.com/videos/xlk2nw/the-enemy-within---dr--skylar-bayer",
        "http://thecolbertreport.cc.com/videos/4v9opj/texas-gun-training-bill---free-shotgun-experiment",
        "http://thecolbertreport.cc.com/videos/ala255/kirk-bloodsworth",
        "http://thecolbertreport.cc.com/videos/7xfdsz/sign-off---goodnight"
      ],
      "guest": "Kirk Bloodsworth"
    },
    {
      "date": "2013-03-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/johtnl/intro---3-5-13",
        "http://thecolbertreport.cc.com/videos/d8ua02/hugo-chavez---jon-stewart-announcements",
        "http://thecolbertreport.cc.com/videos/yesa8j/obama-s-israel-trip",
        "http://thecolbertreport.cc.com/videos/xeotb9/obama-s-israel-trip---michael-oren",
        "http://thecolbertreport.cc.com/videos/r5gahs/dennis-tito-s-mars-flyby-mission",
        "http://thecolbertreport.cc.com/videos/23396i/james-franco",
        "http://thecolbertreport.cc.com/videos/ki0n4m/sign-off---goodnight"
      ],
      "guest": "James Franco"
    },
    {
      "date": "2013-03-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5pvbru/-snowquester-",
        "http://thecolbertreport.cc.com/videos/2ox5xp/voting-rights-act",
        "http://thecolbertreport.cc.com/videos/5yipjs/voting-rights-act---julian-bond",
        "http://thecolbertreport.cc.com/videos/3ddous/thought-for-food---bloomberg---the-nacho-bliss-point",
        "http://thecolbertreport.cc.com/videos/25fidf/brendan-o-connell",
        "http://thecolbertreport.cc.com/videos/76de2t/sign-off---tostitos-scoops"
      ],
      "guest": "Brendan O'Connell"
    },
    {
      "date": "2013-03-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7nblia/rand-paul-s-filibuster",
        "http://thecolbertreport.cc.com/videos/aq09bw/north-korea-s-armistice-breach----we-are-the-world--propaganda-video",
        "http://thecolbertreport.cc.com/videos/rz6ppl/the-bachelor",
        "http://thecolbertreport.cc.com/videos/uldxcb/john-sexton",
        "http://thecolbertreport.cc.com/videos/mhruf7/sign-off---land-of-romance"
      ],
      "guest": "John Sexton"
    },
    {
      "date": "2013-03-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6zcxhr/election-of-pope-francis",
        "http://thecolbertreport.cc.com/videos/t23n7e/history-channel-s--the-bible-",
        "http://thecolbertreport.cc.com/videos/7cya4y/colbert-super-pac---ham-rove-memorial-conference-room",
        "http://thecolbertreport.cc.com/videos/bwz16t/junot-diaz",
        "http://thecolbertreport.cc.com/videos/vwhyh8/sign-off----the-bible-"
      ],
      "guest": "Junot Diaz"
    },
    {
      "date": "2013-03-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ftxoqq/gop-growth---opportunity-project",
        "http://thecolbertreport.cc.com/videos/k5798h/the-word---narcicitizenship",
        "http://thecolbertreport.cc.com/videos/rj8f1x/stephen-colbert-is-watching-your-kids---whale-bone-porn",
        "http://thecolbertreport.cc.com/videos/udr4lu/eric-topol",
        "http://thecolbertreport.cc.com/videos/755nas/sign-off---medical-smartphone"
      ],
      "guest": "Dr. Eric Topol"
    },
    {
      "date": "2013-03-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lapsll/intro---3-27-13",
        "http://thecolbertreport.cc.com/videos/8f2crl/bill-o-reilly-on-gay-marriage",
        "http://thecolbertreport.cc.com/videos/jk0icd/facebook--like--button-science",
        "http://thecolbertreport.cc.com/videos/gd7ki7/sharia-mops",
        "http://thecolbertreport.cc.com/videos/0i05bg/carl-edgar-blake-ii",
        "http://thecolbertreport.cc.com/videos/8g5b2m/sign-off---hamlet"
      ],
      "guest": "Carl Edgar Blake II"
    },
    {
      "date": "2013-03-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mmwqg6/supreme-court-hearings-on-gay-marriage",
        "http://thecolbertreport.cc.com/videos/o26xyc/supreme-court-hearings-on-gay-marriage---emily-bazelon-pt--1",
        "http://thecolbertreport.cc.com/videos/qbupod/supreme-court-hearings-on-gay-marriage---emily-bazelon-pt--2",
        "http://thecolbertreport.cc.com/videos/sliefv/robert-lustig",
        "http://thecolbertreport.cc.com/videos/qlgxw8/sign-off---goodnight"
      ],
      "guest": "Dr. Robert Lustig"
    },
    {
      "date": "2013-04-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j7yyx1/intro---4-1-13",
        "http://thecolbertreport.cc.com/videos/mbhysf/easter-under-attack---pope-edition",
        "http://thecolbertreport.cc.com/videos/egcbz2/health-care-lottery",
        "http://thecolbertreport.cc.com/videos/g3wft7/utah-s-earth-day-celebration",
        "http://thecolbertreport.cc.com/videos/rmu5w0/sigourney-weaver",
        "http://thecolbertreport.cc.com/videos/lt4lab/sign-off---welcome-baby-nurick-"
      ],
      "guest": "Sigourney Weaver"
    },
    {
      "date": "2013-04-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dgrhqs/gay-marriage-fraud",
        "http://thecolbertreport.cc.com/videos/sq7yjh/we-are-at-war---north-korea",
        "http://thecolbertreport.cc.com/videos/0pozxj/we-are-at-war---north-korea---victor-cha",
        "http://thecolbertreport.cc.com/videos/w7owfy/florida-s-bong-bill",
        "http://thecolbertreport.cc.com/videos/7qy183/jim-mcgreevey",
        "http://thecolbertreport.cc.com/videos/1qietk/sign-off---goodnight"
      ],
      "guest": "Jim McGreevey"
    },
    {
      "date": "2013-04-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3ci6sy/-morning-joe--vs--the-colbert-report",
        "http://thecolbertreport.cc.com/videos/54w6pz/gun-control---barn-orgies",
        "http://thecolbertreport.cc.com/videos/heku72/rnc-young-voters-survey",
        "http://thecolbertreport.cc.com/videos/tnl1m7/a-c--grayling",
        "http://thecolbertreport.cc.com/videos/kfs88u/sign-off---campaign-poster"
      ],
      "guest": "A.C. Grayling"
    },
    {
      "date": "2013-04-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6sjovw/intro---4-4-13",
        "http://thecolbertreport.cc.com/videos/2h8ym1/pegasus-pipeline-spill",
        "http://thecolbertreport.cc.com/videos/0tmqs0/koko---jeremy-irons-on-gay-marriage",
        "http://thecolbertreport.cc.com/videos/97bihb/obama-s-brain-initiative",
        "http://thecolbertreport.cc.com/videos/wb31l0/francis-collins",
        "http://thecolbertreport.cc.com/videos/jpb3iv/sign-off---eeg-cap"
      ],
      "guest": "Dr. Francis Collins"
    },
    {
      "date": "2013-04-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2htlq3/colbert-galactic-initiative",
        "http://thecolbertreport.cc.com/videos/z4m9xu/colbert-galactic-initiative---bill-clinton-pt--1",
        "http://thecolbertreport.cc.com/videos/y3hr34/colbert-galactic-initiative---bill-clinton-pt--2",
        "http://thecolbertreport.cc.com/videos/hmills/colbert-galactic-initiative---bill-clinton-pt--3",
        "http://thecolbertreport.cc.com/videos/jmsckt/sign-off---colbert-galactic-initiative"
      ],
      "guest": "Bill Clinton"
    },
    {
      "date": "2013-04-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dzx936/intro---4-9-13",
        "http://thecolbertreport.cc.com/videos/9a1zbe/prez-billy-jeff-clinton",
        "http://thecolbertreport.cc.com/videos/k04x7j/clinton-global-initiative-university-exchange-fair",
        "http://thecolbertreport.cc.com/videos/yq6m6x/exxon-s-disaster-relief",
        "http://thecolbertreport.cc.com/videos/qa420d/charlie-leduff",
        "http://thecolbertreport.cc.com/videos/jti3ea/sign-off---potato-clock"
      ],
      "guest": "Charlie LeDuff"
    },
    {
      "date": "2013-04-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r4g4o0/navy-laser-technology",
        "http://thecolbertreport.cc.com/videos/b0yf3a/tip-wag---gun-edition---united-nations--senate-republicans---video-games",
        "http://thecolbertreport.cc.com/videos/xr32ry/anthony-weiner-s-comeback",
        "http://thecolbertreport.cc.com/videos/mvszff/shane-smith",
        "http://thecolbertreport.cc.com/videos/fhj67z/sign-off---laser-tag"
      ],
      "guest": "Shane Smith"
    },
    {
      "date": "2013-04-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ycrshs/nasa-lasso",
        "http://thecolbertreport.cc.com/videos/2ixasd/america-s-pot-astrophe",
        "http://thecolbertreport.cc.com/videos/t10bgi/america-s-pot-astrophe---nick-gillespie",
        "http://thecolbertreport.cc.com/videos/82a7wi/times-square-mascots-ban",
        "http://thecolbertreport.cc.com/videos/oiajpp/cass-sunstein",
        "http://thecolbertreport.cc.com/videos/5r04eq/sign-off---goodnight"
      ],
      "guest": "Cass Sunstein"
    },
    {
      "date": "2013-04-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ifpmy1/intro---4-16-13",
        "http://thecolbertreport.cc.com/videos/s94ied/tip-wag---brood-ii-cicadas--sexcereal---gop-internet-memes",
        "http://thecolbertreport.cc.com/videos/h77c6i/rollie-eggmaster",
        "http://thecolbertreport.cc.com/videos/c5i1jr/caroline-kennedy",
        "http://thecolbertreport.cc.com/videos/yygt35/sign-off---goodnight"
      ],
      "guest": "Caroline Kennedy"
    },
    {
      "date": "2013-04-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yfwqpo/ricin-letters---boston-bombing-suspects",
        "http://thecolbertreport.cc.com/videos/b1ekda/bitcoin-plunge",
        "http://thecolbertreport.cc.com/videos/rxy9ze/bitcoin-plunge---adam-davidson",
        "http://thecolbertreport.cc.com/videos/2sml1x/-accidental-racist--song",
        "http://thecolbertreport.cc.com/videos/n7jblw/alan-cumming",
        "http://thecolbertreport.cc.com/videos/4y7jmv/sign-off---goodnight"
      ],
      "guest": "Alan Cumming"
    },
    {
      "date": "2013-04-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jr70gq/boston-marathon--bag-men-",
        "http://thecolbertreport.cc.com/videos/de4kxw/the-bucket-maiden-voyage",
        "http://thecolbertreport.cc.com/videos/x7fhfp/gun-control-block",
        "http://thecolbertreport.cc.com/videos/tvksjy/richard-engel",
        "http://thecolbertreport.cc.com/videos/17gkl6/sign-off---the-bucket"
      ],
      "guest": "Richard Engel"
    },
    {
      "date": "2013-04-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nc9lav/intro---4-22-13",
        "http://thecolbertreport.cc.com/videos/vlo1dt/boston-bombers",
        "http://thecolbertreport.cc.com/videos/pd1fay/toronto-terror-plot",
        "http://thecolbertreport.cc.com/videos/06tavh/tiny-triumphs---infrastructure---river-pollution",
        "http://thecolbertreport.cc.com/videos/hkxcsa/george-w--bush-presidential-library",
        "http://thecolbertreport.cc.com/videos/d8p3y1/michael-pollan",
        "http://thecolbertreport.cc.com/videos/34u7cu/sign-off---goodnight"
      ],
      "guest": "Michael Pollan"
    },
    {
      "date": "2013-04-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/12jjaw/scoobygate",
        "http://thecolbertreport.cc.com/videos/dcyvro/austerity-s-spreadsheet-error",
        "http://thecolbertreport.cc.com/videos/kbgnf0/austerity-s-spreadsheet-error---thomas-herndon",
        "http://thecolbertreport.cc.com/videos/54pqtc/eric-schmidt",
        "http://thecolbertreport.cc.com/videos/uwzpai/sign-off---goodnight"
      ],
      "guest": "Eric Schmidt"
    },
    {
      "date": "2013-04-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kwa0vp/ap-twitter-hack",
        "http://thecolbertreport.cc.com/videos/tk4his/bill-clinton-s-twitter-lessons",
        "http://thecolbertreport.cc.com/videos/r1hl69/tiny-triumphs---nasa-s-giant-penis-doodle",
        "http://thecolbertreport.cc.com/videos/zi0nnq/danica-patrick",
        "http://thecolbertreport.cc.com/videos/zwp3mi/sign-off---goodnight"
      ],
      "guest": "Danica Patrick"
    },
    {
      "date": "2013-04-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/md1l1j/exclusive---better-know-a-district---pennsylvania-s-17th---matt-cartwright",
        "http://thecolbertreport.cc.com/videos/1waayt/colbert-s-book-club",
        "http://thecolbertreport.cc.com/videos/zfq57f/better-know-a-district---pennsylvania-s-17th---matt-cartwright",
        "http://thecolbertreport.cc.com/videos/ypl8dh/miranda-rights-for-boston-bomber",
        "http://thecolbertreport.cc.com/videos/9j0img/gene-robinson",
        "http://thecolbertreport.cc.com/videos/vqrjkz/sign-off---welcome-baby-matheson-"
      ],
      "guest": "Bishop Gene Robinson"
    },
    {
      "date": "2013-04-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lceacn/intro---4-29-13",
        "http://thecolbertreport.cc.com/videos/s55dpi/stephen-s-worst-sports-nightmare",
        "http://thecolbertreport.cc.com/videos/q8gaki/the-final-days-of-straight-america",
        "http://thecolbertreport.cc.com/videos/su6rj1/the-word---we-shall-undermine",
        "http://thecolbertreport.cc.com/videos/u2ew19/yelp-prison-reviews",
        "http://thecolbertreport.cc.com/videos/8ewxg4/iggy-pop"
      ],
      "guest": "Iggy &amp; the Stooges"
    },
    {
      "date": "2013-04-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9ab72e/intro---4-30-13",
        "http://thecolbertreport.cc.com/videos/6brvhc/forced-tank-spending",
        "http://thecolbertreport.cc.com/videos/yxooec/the-word---medical-leave",
        "http://thecolbertreport.cc.com/videos/4iphqy/thought-for-food---spreadable-sharia---buddy-cup",
        "http://thecolbertreport.cc.com/videos/z5q514/evan-spiegel---bobby-murphy",
        "http://thecolbertreport.cc.com/videos/i4mbhv/sign-off---snapchat"
      ],
      "guest": "Evan Spiegel &amp; Bobby Murphy"
    },
    {
      "date": "2013-05-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/82vhzw/over-the-counter-plan-b",
        "http://thecolbertreport.cc.com/videos/7a77hc/background-check-backlash",
        "http://thecolbertreport.cc.com/videos/rf6pzs/the-word---n-r-a--vana",
        "http://thecolbertreport.cc.com/videos/cm8gvz/macklemore---ryan-lewis",
        "http://thecolbertreport.cc.com/videos/sq79ll/sign-off----the-heist-"
      ],
      "guest": "Macklemore &amp; Ryan Lewis"
    },
    {
      "date": "2013-05-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tqo262/intro---5-2-13",
        "http://thecolbertreport.cc.com/videos/7emy7s/boston-bomber-accomplices",
        "http://thecolbertreport.cc.com/videos/2k1660/gitmo-hunger-strike",
        "http://thecolbertreport.cc.com/videos/is0h3a/gitmo-hunger-strike---charles-swift",
        "http://thecolbertreport.cc.com/videos/nhiiwp/movies-that-are-destroying-america---summer-movie-edition----man-of-steel-----iron-man-3-",
        "http://thecolbertreport.cc.com/videos/mqwnf6/ben-kingsley",
        "http://thecolbertreport.cc.com/videos/t46my4/sign-off---montclair-film-festival"
      ],
      "guest": "Ben Kingsley"
    },
    {
      "date": "2013-05-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1mqcyb/intro---5-6-13",
        "http://thecolbertreport.cc.com/videos/tnugl6/colbert-s-book-club----the-great-gatsby-",
        "http://thecolbertreport.cc.com/videos/rxk0vp/stephen-colbert-s-bats--t-serious---bullet-conspiracy-theory",
        "http://thecolbertreport.cc.com/videos/ltsnqq/tip-wag---catholic-diocese-of-brooklyn---stoner-dogs",
        "http://thecolbertreport.cc.com/videos/wm2xsq/robert-caro",
        "http://thecolbertreport.cc.com/videos/479h8q/sign-off---south-carolina-special-election"
      ],
      "guest": "Robert Caro"
    },
    {
      "date": "2013-05-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bpnvtc/breaking-news---benghazi-whistleblowers",
        "http://thecolbertreport.cc.com/videos/wwbl80/better-know-a-district---maryland-s-4th---donna-edwards",
        "http://thecolbertreport.cc.com/videos/p3cofn/promposals",
        "http://thecolbertreport.cc.com/videos/eyzxx1/douglas-rushkoff",
        "http://thecolbertreport.cc.com/videos/ampziq/sign-off---goodnight"
      ],
      "guest": "Douglas Rushkoff"
    },
    {
      "date": "2013-05-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mpvlti/intro---5-8-13",
        "http://thecolbertreport.cc.com/videos/fyx23e/south-carolina-election-results",
        "http://thecolbertreport.cc.com/videos/m0huaq/spiteful-partisanship",
        "http://thecolbertreport.cc.com/videos/gbxmpo/going-diaperless",
        "http://thecolbertreport.cc.com/videos/xg0uqu/richard-besser",
        "http://thecolbertreport.cc.com/videos/in85s8/sign-off---helium-voice"
      ],
      "guest": "Dr. Richard Besser"
    },
    {
      "date": "2013-05-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t96yfm/colbert-s-book-club----the-great-gatsby-",
        "http://thecolbertreport.cc.com/videos/1i7t2j/colbert-s-book-club---learning--the-great-gatsby-",
        "http://thecolbertreport.cc.com/videos/4apw9e/colbert-s-book-club---jennifer-egan----the-great-gatsby-",
        "http://thecolbertreport.cc.com/videos/tetoi9/baz-luhrmann",
        "http://thecolbertreport.cc.com/videos/uuyuly/sign-off----the-great-gatsby-"
      ],
      "guest": "Jennifer Egan, Baz Luhrmann"
    },
    {
      "date": "2013-05-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hdvhlq/benghazi-attacks-talking-points",
        "http://thecolbertreport.cc.com/videos/gxwgja/colbert-super-pac-shh----irs-special-scrutiny",
        "http://thecolbertreport.cc.com/videos/jgqf2m/threatdown---planet-gay--world-wide-wood---junkie-bears",
        "http://thecolbertreport.cc.com/videos/l06a4l/jessica-buchanan---erik-landemalm",
        "http://thecolbertreport.cc.com/videos/ny9pcg/sign-off---goodnight"
      ],
      "guest": "Jessica Buchanan &amp; Erik Landemalm"
    },
    {
      "date": "2013-05-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g6ij84/intro---5-14-13",
        "http://thecolbertreport.cc.com/videos/1nghxb/obamacare-repeal-vote",
        "http://thecolbertreport.cc.com/videos/0jjvya/heritage-foundation-s-immigration-study",
        "http://thecolbertreport.cc.com/videos/h5zenk/who-s-not-honoring-me-now----maxim",
        "http://thecolbertreport.cc.com/videos/tq7jny/dan-brown",
        "http://thecolbertreport.cc.com/videos/ftry54/sign-off---maxim-s-hot-100"
      ],
      "guest": "Dan Brown"
    },
    {
      "date": "2013-05-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c91oeg/bug-protein",
        "http://thecolbertreport.cc.com/videos/qxjgw6/better-know-a-district---wisconsin-s-4th---gwen-moore-pt--1",
        "http://thecolbertreport.cc.com/videos/ft1gyx/better-know-a-district---wisconsin-s-4th---gwen-moore-pt--2",
        "http://thecolbertreport.cc.com/videos/xjltw5/cyndi-lauper",
        "http://thecolbertreport.cc.com/videos/f06og4/sign-off---kinky-boots"
      ],
      "guest": "Cyndi Lauper"
    },
    {
      "date": "2013-05-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ru2qad/intro---5-16-13",
        "http://thecolbertreport.cc.com/videos/vshddv/asparagusgate",
        "http://thecolbertreport.cc.com/videos/x9725b/tip-wag---wind-turbines---china",
        "http://thecolbertreport.cc.com/videos/6685w4/3d-printed-guns",
        "http://thecolbertreport.cc.com/videos/7xqphc/daniel-lieberman",
        "http://thecolbertreport.cc.com/videos/yktive/sign-off---barefoot-shoes"
      ],
      "guest": "Dr. Daniel Lieberman"
    },
    {
      "date": "2013-05-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iqqmsb/mazda-scandal-booth---benghazi",
        "http://thecolbertreport.cc.com/videos/xwopvb/mazda-scandal-booth---the-irs",
        "http://thecolbertreport.cc.com/videos/5qyy0w/mazda-scandal-booth---the-irs---trevor-potter",
        "http://thecolbertreport.cc.com/videos/irj43w/david-sassoon",
        "http://thecolbertreport.cc.com/videos/m9mkd8/sign-off---mazda-scandal-booth"
      ],
      "guest": "David Sassoon"
    },
    {
      "date": "2013-05-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wp98kg/intro---5-21-13",
        "http://thecolbertreport.cc.com/videos/7fm2v2/irish-potato-famine-pathogen",
        "http://thecolbertreport.cc.com/videos/pbfcaq/cheating-death---sun-exposure---marijuana",
        "http://thecolbertreport.cc.com/videos/3jp6f3/census-bureau-harassment",
        "http://thecolbertreport.cc.com/videos/cqajs7/noah-feldman",
        "http://thecolbertreport.cc.com/videos/2jhy5w/sign-off---goodnight"
      ],
      "guest": "Noah Feldman"
    },
    {
      "date": "2013-05-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c02847/intro---5-22-13",
        "http://thecolbertreport.cc.com/videos/24adff/irs-tea-party-scandal",
        "http://thecolbertreport.cc.com/videos/icnp2y/tip-wag---senators-mitch-and-chong---resourceful-rich-folk",
        "http://thecolbertreport.cc.com/videos/60entl/-citizen-koch-",
        "http://thecolbertreport.cc.com/videos/15h43y/matt-berninger"
      ],
      "guest": "The National"
    },
    {
      "date": "2013-05-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2j741e/aumf-repeal",
        "http://thecolbertreport.cc.com/videos/khhujw/aumf-repeal---andrew-bacevich",
        "http://thecolbertreport.cc.com/videos/0bv6m0/redemption-for-all",
        "http://thecolbertreport.cc.com/videos/ur1l6x/c-j--chivers",
        "http://thecolbertreport.cc.com/videos/ahpe36/sign-off---goodnight"
      ],
      "guest": "C.J. Chivers"
    },
    {
      "date": "2013-06-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ex0o10/stephen-s-week-off",
        "http://thecolbertreport.cc.com/videos/ervy41/better-know-a-district---wisconsin-s-2nd---mark-pocan",
        "http://thecolbertreport.cc.com/videos/s86l5y/trackingpoint-rifle",
        "http://thecolbertreport.cc.com/videos/4fwbkt/john-dingell",
        "http://thecolbertreport.cc.com/videos/yrhc20/sign-off---goodnight"
      ],
      "guest": "Rep. John Dingell"
    },
    {
      "date": "2013-06-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fivedj/michele-bachmann-s-last-term",
        "http://thecolbertreport.cc.com/videos/x7wc5a/tip-wag---google-glass---the-lone-ranger----3d-printed-food",
        "http://thecolbertreport.cc.com/videos/u1fvmr/irs-political-targeting---line-dancing-scandals",
        "http://thecolbertreport.cc.com/videos/tz8gve/alex-gibney",
        "http://thecolbertreport.cc.com/videos/fbuavt/sign-off---goodnight"
      ],
      "guest": "Alex Gibney"
    },
    {
      "date": "2013-06-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2ntvt9/intro---6-5-13",
        "http://thecolbertreport.cc.com/videos/eogja8/commando-of-steel",
        "http://thecolbertreport.cc.com/videos/fva65v/monsanto-s-modified-wheat",
        "http://thecolbertreport.cc.com/videos/ibdfsk/monsanto-s-modified-wheat---laurie-garrett",
        "http://thecolbertreport.cc.com/videos/bqahez/photojournalists-vs--iphones",
        "http://thecolbertreport.cc.com/videos/wqd06c/jonathan-alter",
        "http://thecolbertreport.cc.com/videos/el0t4o/sign-off---amber-waves-of-frankengrain"
      ],
      "guest": "Jonathan Alter"
    },
    {
      "date": "2013-06-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/onw7lq/nsa-phone-surveillance",
        "http://thecolbertreport.cc.com/videos/hbmw2f/colbert-classic---spy-training-with-peter-earnest",
        "http://thecolbertreport.cc.com/videos/zhz7uc/john-mellencamp--stephen-king---t-bone-burnett---pt--1",
        "http://thecolbertreport.cc.com/videos/lcf7d3/john-mellencamp--stephen-king---t-bone-burnett---pt--2",
        "http://thecolbertreport.cc.com/videos/46x6yt/sign-off---nose-tap"
      ],
      "guest": "Stephen King, John Mellencamp, T Bone Burnett"
    },
    {
      "date": "2013-06-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oc2w3x/edward-snowden-s-nsa-leaks",
        "http://thecolbertreport.cc.com/videos/bkbpaj/the-imploding-muslim-country-of-the-week---turkey",
        "http://thecolbertreport.cc.com/videos/rnftw3/the-imploding-muslim-country-of-the-week---turkey---omer-taspinar",
        "http://thecolbertreport.cc.com/videos/147u1d/cold-war-update---nuclear-launch-careers",
        "http://thecolbertreport.cc.com/videos/vii2l9/dan-savage",
        "http://thecolbertreport.cc.com/videos/kmqz9h/sign-off---the-imploding-muslim-country-of-the-week-booth"
      ],
      "guest": "Dan Savage"
    },
    {
      "date": "2013-06-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ctjh9s/intro---6-11-13",
        "http://thecolbertreport.cc.com/videos/1mm086/prism-surveillance-program",
        "http://thecolbertreport.cc.com/videos/jejy0d/prism-surveillance-program---jeffrey-rosen",
        "http://thecolbertreport.cc.com/videos/sa86i9/chewbacca-s-tsa-encounter",
        "http://thecolbertreport.cc.com/videos/s2d0lp/daniel-bergner",
        "http://thecolbertreport.cc.com/videos/x7nfzj/sign-off---goodnight"
      ],
      "guest": "Daniel Bergner"
    },
    {
      "date": "2013-06-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jdqve3/stephen-colbert-s-tribute-to-having-paul-mccartney-on-his-show",
        "http://thecolbertreport.cc.com/videos/eweibb/nsa-scandal-developments",
        "http://thecolbertreport.cc.com/videos/9i45f0/paul-mccartney",
        "http://thecolbertreport.cc.com/videos/2ildb8/nyc-bike-share"
      ],
      "guest": "Paul McCartney"
    },
    {
      "date": "2013-06-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yxgnju/remembering-lorna-colbert",
        "http://thecolbertreport.cc.com/videos/jm7bya/cap-n-crunch-scandal",
        "http://thecolbertreport.cc.com/videos/rtfkei/tip-wag---wall-street---north-carolina",
        "http://thecolbertreport.cc.com/videos/vztqfg/the-postal-service",
        "http://thecolbertreport.cc.com/videos/7vr4pz/sign-off---stage-fall"
      ],
      "guest": "The Postal Service"
    },
    {
      "date": "2013-06-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/616g0e/intro---6-20-13",
        "http://thecolbertreport.cc.com/videos/v8ee5f/iran-s-presidential-election",
        "http://thecolbertreport.cc.com/videos/k3dodo/steve-king-on-chicken-cages",
        "http://thecolbertreport.cc.com/videos/7udg5z/nestle-s-natural-resource",
        "http://thecolbertreport.cc.com/videos/0mw5zk/joss-whedon",
        "http://thecolbertreport.cc.com/videos/ooshhr/sign-off---paper-towel-tube-cage"
      ],
      "guest": "Joss Whedon"
    },
    {
      "date": "2013-06-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6gyv8z/the-irs---darrell-issa-s-gut",
        "http://thecolbertreport.cc.com/videos/oztyjs/the-word---truthinews",
        "http://thecolbertreport.cc.com/videos/93t9s1/tiny-triumphs---laser-klan",
        "http://thecolbertreport.cc.com/videos/dzzcx7/andrew-solomon",
        "http://thecolbertreport.cc.com/videos/h7v6sr/sign-off---goodnight"
      ],
      "guest": "Andrew Solomon"
    },
    {
      "date": "2013-06-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g5p8y4/intro---6-25-13",
        "http://thecolbertreport.cc.com/videos/348hon/scotus-on-the-voting-rights-act",
        "http://thecolbertreport.cc.com/videos/ysuxww/brazil-s-political-protests",
        "http://thecolbertreport.cc.com/videos/3gv8et/brazil-s-political-protests---larry-rohter",
        "http://thecolbertreport.cc.com/videos/mnxaxk/george-zimmerman-s-murder-trial",
        "http://thecolbertreport.cc.com/videos/ip1pn0/peniel-joseph",
        "http://thecolbertreport.cc.com/videos/b4zgvh/sign-off---goodnight"
      ],
      "guest": "Peniel Joseph"
    },
    {
      "date": "2013-06-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m2xuu4/intro---6-26-13",
        "http://thecolbertreport.cc.com/videos/nzd784/the-supreme-court-rules-on-doma",
        "http://thecolbertreport.cc.com/videos/um981i/the-end-of-the-voting-rights-act",
        "http://thecolbertreport.cc.com/videos/btpztg/the-voting-rights-act---gay-marriage---emily-bazelon",
        "http://thecolbertreport.cc.com/videos/3ca2a0/bill-moyers",
        "http://thecolbertreport.cc.com/videos/09w1k9/sign-off---goodnight"
      ],
      "guest": "Bill Moyers"
    },
    {
      "date": "2013-06-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9lyyd3/4th-of-july-under-attack",
        "http://thecolbertreport.cc.com/videos/3wbx1d/stephen-colbert-s-big-gay-roundup",
        "http://thecolbertreport.cc.com/videos/ncxmfs/-gang-of-eight--immigration-reform-bill",
        "http://thecolbertreport.cc.com/videos/0gj3ie/chuck-schumer",
        "http://thecolbertreport.cc.com/videos/6kec7y/sign-off---goodnight"
      ],
      "guest": "Sen. Chuck Schumer"
    },
    {
      "date": "2013-07-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6jl3zv/stephen-s-vacation",
        "http://thecolbertreport.cc.com/videos/0gzuno/george-zimmerman-verdict",
        "http://thecolbertreport.cc.com/videos/9nhthn/people-who-are-destroying-america---lynn-harrell",
        "http://thecolbertreport.cc.com/videos/6dlnrd/ktvu-tv-on-asiana-airlines-crash",
        "http://thecolbertreport.cc.com/videos/vwtsg0/jeremy-scahill",
        "http://thecolbertreport.cc.com/videos/88fai0/sign-off---goodnight"
      ],
      "guest": "Jeremy Scahill"
    },
    {
      "date": "2013-07-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2ymeh3/intro---7-16-13",
        "http://thecolbertreport.cc.com/videos/rr5gb5/royal-baby-bump",
        "http://thecolbertreport.cc.com/videos/dd82ys/tip-wag---non-rioting-black-people---fox-news",
        "http://thecolbertreport.cc.com/videos/e8110o/npr-on-multitasking",
        "http://thecolbertreport.cc.com/videos/e5obyh/david-karp",
        "http://thecolbertreport.cc.com/videos/0mvlz8/sign-off---macbox"
      ],
      "guest": "David Karp"
    },
    {
      "date": "2013-07-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/84x6wp/rolling-stone-s-boston-bomber-cover",
        "http://thecolbertreport.cc.com/videos/eiwwmp/dysfunctional-house-republicans---immigration-reform",
        "http://thecolbertreport.cc.com/videos/dii80x/food-stamp-funding",
        "http://thecolbertreport.cc.com/videos/279goq/jerry-seinfeld-pt--1",
        "http://thecolbertreport.cc.com/videos/pw17w7/jerry-seinfeld-pt--2",
        "http://thecolbertreport.cc.com/videos/qfpfy4/sign-off---paper-fan"
      ],
      "guest": "Jerry Seinfeld"
    },
    {
      "date": "2013-07-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r4piw8/edward-snowden-s-asylum-option",
        "http://thecolbertreport.cc.com/videos/2m27vd/political-sex-scandals---new-york-city-elections",
        "http://thecolbertreport.cc.com/videos/dpebt7/political-sex-scandals---new-york-city-elections---eliot-spitzer",
        "http://thecolbertreport.cc.com/videos/m8rn8j/breaking-news-on-college-sex",
        "http://thecolbertreport.cc.com/videos/y56hes/jeff-bridges",
        "http://thecolbertreport.cc.com/videos/fiop8t/sign-off----operation-javelin-"
      ],
      "guest": "Jeff Bridges"
    },
    {
      "date": "2013-07-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/20zlbx/britain-s-royal-baby",
        "http://thecolbertreport.cc.com/videos/d0bn33/geraldo-rivera-s-tribute-to-helen-thomas",
        "http://thecolbertreport.cc.com/videos/8fg72p/minimum-wage---mcdonald-s-spending-journal",
        "http://thecolbertreport.cc.com/videos/0p9n45/neil-degrasse-tyson-s-alien-theory",
        "http://thecolbertreport.cc.com/videos/3azmuc/kjerstin-gruys",
        "http://thecolbertreport.cc.com/videos/mritg0/sign-off---linguini-worm"
      ],
      "guest": "Kjerstin Gruys"
    },
    {
      "date": "2013-07-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y6fmk6/royal-afterbirth--013-",
        "http://thecolbertreport.cc.com/videos/adczam/george-zimmerman---racial-tensions",
        "http://thecolbertreport.cc.com/videos/3vijkd/the-word---color-bind",
        "http://thecolbertreport.cc.com/videos/vbghld/domino-s-pizza-drone",
        "http://thecolbertreport.cc.com/videos/5tqazj/kenneth-goldsmith",
        "http://thecolbertreport.cc.com/videos/fvgc0u/sign-off---goodnight"
      ],
      "guest": "Kenneth Goldsmith"
    },
    {
      "date": "2013-07-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/508jwm/royal-baby-fever",
        "http://thecolbertreport.cc.com/videos/eodctw/anthony-weiner-s-penis",
        "http://thecolbertreport.cc.com/videos/4sgopv/carlos-danger--secret-mayor",
        "http://thecolbertreport.cc.com/videos/bf89i9/kanye-west-s-clothing-line",
        "http://thecolbertreport.cc.com/videos/zwqhae/anant-agarwal",
        "http://thecolbertreport.cc.com/videos/gbago4/sign-off---goodnight"
      ],
      "guest": "Anant Agarwal"
    },
    {
      "date": "2013-07-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/l1dtzt/london-s-fake-town-crier",
        "http://thecolbertreport.cc.com/videos/lyjdmu/detroit-s-bankruptcy",
        "http://thecolbertreport.cc.com/videos/h9c7gh/detroit-s-bankruptcy---stephen-henderson",
        "http://thecolbertreport.cc.com/videos/8chokd/steve-king-s-immigrant-analogy",
        "http://thecolbertreport.cc.com/videos/263vwc/olympia-snowe",
        "http://thecolbertreport.cc.com/videos/kx84kd/sign-off---hand-bell"
      ],
      "guest": "Olympia Snowe"
    },
    {
      "date": "2013-07-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uw17hh/intro---7-29-13",
        "http://thecolbertreport.cc.com/videos/n0w3zw/obamacare-cards",
        "http://thecolbertreport.cc.com/videos/pna3x8/tip-wag---steve-stockman--david-cameron---north-carolina-legislature",
        "http://thecolbertreport.cc.com/videos/2i98l3/the-lumineers",
        "http://thecolbertreport.cc.com/videos/1i7dzf/sign-off---tambourine"
      ],
      "guest": "The Lumineers"
    },
    {
      "date": "2013-07-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/trrcbd/intro---7-30-13",
        "http://thecolbertreport.cc.com/videos/mulhwo/smokin--pole---the-quest-for-arctic-riches--north-pole-lake",
        "http://thecolbertreport.cc.com/videos/gr77sg/senator-gridlock",
        "http://thecolbertreport.cc.com/videos/hrha3p/the-word---secrets---laws",
        "http://thecolbertreport.cc.com/videos/jah6al/ted-cruz-s-humble-portrait",
        "http://thecolbertreport.cc.com/videos/bhod50/atul-gawande",
        "http://thecolbertreport.cc.com/videos/c1f9z7/sign-off---sleigh-bells"
      ],
      "guest": "Atul Gawande"
    },
    {
      "date": "2013-07-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4dtx20/intro---7-31-13",
        "http://thecolbertreport.cc.com/videos/6p4joy/bradley-manning-verdict",
        "http://thecolbertreport.cc.com/videos/hcbpix/lunch-or-campaign-2016-",
        "http://thecolbertreport.cc.com/videos/21zxm1/chris-christie-vs--rand-paul",
        "http://thecolbertreport.cc.com/videos/zyu4c8/stephen-colbert-s-super-coin-toss",
        "http://thecolbertreport.cc.com/videos/ngxjwr/emily-matchar",
        "http://thecolbertreport.cc.com/videos/f1q01l/sign-off---game-over"
      ],
      "guest": "Emily Matchar"
    },
    {
      "date": "2013-08-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s9hzk7/intro---8-1-13",
        "http://thecolbertreport.cc.com/videos/09hbf0/edward-snowden-s-asylum",
        "http://thecolbertreport.cc.com/videos/o0rsdt/oppressed-white-male-alert---bob-filner",
        "http://thecolbertreport.cc.com/videos/y8ilbl/grab-ask-5800",
        "http://thecolbertreport.cc.com/videos/opj4x1/threatdown---global-erotic-extremism--mini-muslims---stripper-bears",
        "http://thecolbertreport.cc.com/videos/gyog46/bryan-cranston",
        "http://thecolbertreport.cc.com/videos/qv7up3/sign-off---goodnight"
      ],
      "guest": "Bryan Cranston"
    },
    {
      "date": "2013-08-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/n525ux/global-terror-warning",
        "http://thecolbertreport.cc.com/videos/1y9s5s/sport-report---a-rod-s-drug-scandal---combat-juggling",
        "http://thecolbertreport.cc.com/videos/91y2gj/hugh-laurie",
        "http://thecolbertreport.cc.com/videos/g0yu17/broadcast-networks-want-more-indecency",
        "http://thecolbertreport.cc.com/videos/n9o8qy/sign-off---glossary-of-terms"
      ],
      "guest": "Hugh Laurie"
    },
    {
      "date": "2013-08-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4ybtps/stephest-colbchella--013---the-song-of-the-summer-of-the-century",
        "http://thecolbertreport.cc.com/videos/s9j4ux/stephest-colbchella--013---special-guest-stephen-colbert-"
      ],
      "guest": "Robin Thicke"
    },
    {
      "date": "2013-08-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0t0r8t/stephest-colbchella--013---disco-decepticons",
        "http://thecolbertreport.cc.com/videos/je51p5/rich-white-guys-agreeing-with-each-other-alert---neil-cavuto",
        "http://thecolbertreport.cc.com/videos/m9o287/fast-food-workers-strike---mary-kay-henry",
        "http://thecolbertreport.cc.com/videos/b0jyca/sec-vs--fabulous-fab",
        "http://thecolbertreport.cc.com/videos/rrfnhj/ashton-kutcher",
        "http://thecolbertreport.cc.com/videos/iqw6df/sign-off---goodnight"
      ],
      "guest": "Ashton Kutcher"
    },
    {
      "date": "2013-08-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ehgkke/ganjay-supta",
        "http://thecolbertreport.cc.com/videos/x55kjy/hollywood-heroes",
        "http://thecolbertreport.cc.com/videos/lual8r/hollywood-heroes---matt-damon",
        "http://thecolbertreport.cc.com/videos/qqmmcz/the-ronald-wilson-reagan-economic-breathing-zone",
        "http://thecolbertreport.cc.com/videos/6duz1s/colum-mccann",
        "http://thecolbertreport.cc.com/videos/fama3f/sign-off----fifty-shades-of-grey-"
      ],
      "guest": "Colum McCann"
    },
    {
      "date": "2013-08-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m7rv7i/badonkadonk-journalism",
        "http://thecolbertreport.cc.com/videos/qokabz/better-know-a-district---new-jersey-s-12th",
        "http://thecolbertreport.cc.com/videos/vni3w0/better-know-a-district---new-jersey-s-12th---rush-holt",
        "http://thecolbertreport.cc.com/videos/swss3n/innocent-tourist-mistake",
        "http://thecolbertreport.cc.com/videos/lixrq0/sheldon-whitehouse",
        "http://thecolbertreport.cc.com/videos/ck9vu0/sign-off---goodnight"
      ],
      "guest": "Sen. Sheldon Whitehouse"
    },
    {
      "date": "2013-08-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jtshn3/stop-and-frisk---mandatory-minimums",
        "http://thecolbertreport.cc.com/videos/o5aiwi/tsa-expansion-program",
        "http://thecolbertreport.cc.com/videos/miwb3z/tsa-expansion-program---steven-pinker",
        "http://thecolbertreport.cc.com/videos/pd148a/john-lewis-pt--1",
        "http://thecolbertreport.cc.com/videos/ocqoae/john-lewis-pt--2",
        "http://thecolbertreport.cc.com/videos/z6ytj0/sign-off----the-better-angels-of-our-nature-"
      ],
      "guest": "Rep. John Lewis"
    },
    {
      "date": "2013-08-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/als8jg/intro---8-14-13",
        "http://thecolbertreport.cc.com/videos/wjgfbx/sochi-2014-winter-olympics",
        "http://thecolbertreport.cc.com/videos/y58ew9/people-who-are-destroying-america---johnny-cummings",
        "http://thecolbertreport.cc.com/videos/oafmw7/big-mother-government",
        "http://thecolbertreport.cc.com/videos/wc12me/kevin-spacey",
        "http://thecolbertreport.cc.com/videos/o1qztj/sign-off---goodnight"
      ],
      "guest": "Kevin Spacey"
    },
    {
      "date": "2013-08-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fwx35y/obama-rodeo-clown",
        "http://thecolbertreport.cc.com/videos/0bdl0z/golden-age-of-flammability",
        "http://thecolbertreport.cc.com/videos/r9ju4t/the-word---gag-gift",
        "http://thecolbertreport.cc.com/videos/jngkv0/nsa-press-conference-on-domestic-spying",
        "http://thecolbertreport.cc.com/videos/8ax5jq/richard-brodhead",
        "http://thecolbertreport.cc.com/videos/42qo92/sign-off---second-installment-of-colbert-s-book-club"
      ],
      "guest": "Richard Brodhead"
    },
    {
      "date": "2013-09-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pkboc3/exclusive---better-know-a-district---michigan-s-5th---dan-kildee",
        "http://thecolbertreport.cc.com/videos/pnf1sx/intro---9-3-13",
        "http://thecolbertreport.cc.com/videos/tx5zzr/stephen-s-science-project---chemical-weapons-in-syria",
        "http://thecolbertreport.cc.com/videos/dhyi3l/better-know-a-district---michigan-s-5th---dan-kildee",
        "http://thecolbertreport.cc.com/videos/pwzlgj/timothy-dolan-pt--1",
        "http://thecolbertreport.cc.com/videos/m4p07o/timothy-dolan-pt--2",
        "http://thecolbertreport.cc.com/videos/xws5t1/sign-off---welcome-baby-rosta-"
      ],
      "guest": "Timothy Cardinal Dolan"
    },
    {
      "date": "2013-09-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4obytf/intro---9-4-13",
        "http://thecolbertreport.cc.com/videos/020ri3/cris-ish-in-syri-eh",
        "http://thecolbertreport.cc.com/videos/jtjmpo/cris-ish-in-syri-eh---steve-coll",
        "http://thecolbertreport.cc.com/videos/hrfvxe/perfect-polly",
        "http://thecolbertreport.cc.com/videos/q9zsg7/gary-england",
        "http://thecolbertreport.cc.com/videos/jnebqk/sign-off---goodnight"
      ],
      "guest": "Gary England"
    },
    {
      "date": "2013-09-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fzzhny/intro---9-5-13",
        "http://thecolbertreport.cc.com/videos/cgxdol/smile-file---ariel-castro---the-eric-bolling-sunshine-express",
        "http://thecolbertreport.cc.com/videos/cn86ce/kitten-subway-crisis---the-new-york-city-mayoral-race",
        "http://thecolbertreport.cc.com/videos/l0disu/colbert-s-book-club---the-couch-bunker",
        "http://thecolbertreport.cc.com/videos/ub6jy0/john-prine"
      ],
      "guest": "John Prine"
    },
    {
      "date": "2013-09-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m0qnfl/egypt-s-stork-bust",
        "http://thecolbertreport.cc.com/videos/4zp755/syrian-conflict-action-plan",
        "http://thecolbertreport.cc.com/videos/jvhzt0/ronald-reagan-on-the-syrian-conflict",
        "http://thecolbertreport.cc.com/videos/a4utu0/tip-wag---iowa--bigger-pants---recent-articles",
        "http://thecolbertreport.cc.com/videos/f9cuxl/billie-jean-king",
        "http://thecolbertreport.cc.com/videos/2dw2cm/sign-off---spider-reagan"
      ],
      "guest": "Billie Jean King"
    },
    {
      "date": "2013-09-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/o8sjcq/colbert-s-book-club---j-d--salinger",
        "http://thecolbertreport.cc.com/videos/49qji6/colbert-s-book-club---better-know-a-salinger",
        "http://thecolbertreport.cc.com/videos/ueo7a2/colbert-s-book-club---tobias-wolff----the-catcher-in-the-rye-",
        "http://thecolbertreport.cc.com/videos/f2a6ao/colbert-s-book-club---shane-salerno-on-j-d--salinger",
        "http://thecolbertreport.cc.com/videos/2p7nwl/sign-off---colbert-s-book-club---j-d--salinger-s-glass-family"
      ],
      "guest": "Shane Salerno"
    },
    {
      "date": "2013-09-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lop9g2/new-york-city-mayoral-primary",
        "http://thecolbertreport.cc.com/videos/pymjnx/america-s-got-serious-reservations-about-this---syria",
        "http://thecolbertreport.cc.com/videos/cta0kn/america-s-got-serious-reservations-about-this---syria---rand-paul",
        "http://thecolbertreport.cc.com/videos/w9ejb1/barack-obama-s-footgate---secret-muslim-code",
        "http://thecolbertreport.cc.com/videos/p83qs9/sheryl-crow"
      ],
      "guest": "Sheryl Crow"
    },
    {
      "date": "2013-09-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r3zogj/vladimir-putin-s-op-ed-photos",
        "http://thecolbertreport.cc.com/videos/bujbay/better-know-a-district---washington-s-7th---jim-mcdermott",
        "http://thecolbertreport.cc.com/videos/7z7vfu/vladimir-putin-s-op-ed-on-u-s--intervention-in-syria",
        "http://thecolbertreport.cc.com/videos/cm16zd/philip-mudd",
        "http://thecolbertreport.cc.com/videos/4lw1cp/sign-off---goodnight"
      ],
      "guest": "Philip Mudd"
    },
    {
      "date": "2013-09-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/weeyn5/intro---9-16-13",
        "http://thecolbertreport.cc.com/videos/2lxvvp/lehman-brothers-anniversary---economic-recovery",
        "http://thecolbertreport.cc.com/videos/ggices/the-word---the-guilted-age",
        "http://thecolbertreport.cc.com/videos/vui8um/miss-america-2013",
        "http://thecolbertreport.cc.com/videos/v77k60/andrew-bacevich",
        "http://thecolbertreport.cc.com/videos/c31p0i/sign-off---financial-crisis-anniversary-cake"
      ],
      "guest": "Andrew Bacevich"
    },
    {
      "date": "2013-09-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qkhrkt/intro---9-17-13",
        "http://thecolbertreport.cc.com/videos/hwlkz5/the-people-s-republic-of-obamastan---forbes-400-losers",
        "http://thecolbertreport.cc.com/videos/cgb0cw/colbert-platinum---luxury-ice---hot-dic-tip",
        "http://thecolbertreport.cc.com/videos/rkpujl/soul-rending-cheerios-ad",
        "http://thecolbertreport.cc.com/videos/2dwhox/arne-duncan",
        "http://thecolbertreport.cc.com/videos/ukxkfk/sign-off---goodnight"
      ],
      "guest": "Arne Duncan"
    },
    {
      "date": "2013-09-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g7l8kk/syria-conflict---end-times-prophecy",
        "http://thecolbertreport.cc.com/videos/8pp3si/united-nations-on-syria-conflict---andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/v0wk5h/navy-yard-shooting---gun-violence-causes",
        "http://thecolbertreport.cc.com/videos/ft7l84/nicholson-baker",
        "http://thecolbertreport.cc.com/videos/lpg81o/sign-off----damascus-countdown-"
      ],
      "guest": "Nicholson Baker"
    },
    {
      "date": "2013-09-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1j1cxh/michelle-obama-s-h2o-campaign",
        "http://thecolbertreport.cc.com/videos/4iux0d/obamacare-government-shutdown",
        "http://thecolbertreport.cc.com/videos/6nrq55/obamacare-navigators",
        "http://thecolbertreport.cc.com/videos/7qwiwv/tip-wag---hammunition---george-clooney",
        "http://thecolbertreport.cc.com/videos/x5xw6g/jack-johnson"
      ],
      "guest": "Jack Johnson"
    },
    {
      "date": "2013-09-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ecu59e/stephen-s-emmy-awards",
        "http://thecolbertreport.cc.com/videos/nsfkr7/on-notice---pope-francis",
        "http://thecolbertreport.cc.com/videos/vb7ms1/on-notice---pope-francis---jim-martin",
        "http://thecolbertreport.cc.com/videos/7xtam8/metallica",
        "http://thecolbertreport.cc.com/videos/g9dzis/sign-off---emmy-exhibition"
      ],
      "guest": "Metallica"
    },
    {
      "date": "2013-09-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8fmvel/censorship-for-youtube-comments",
        "http://thecolbertreport.cc.com/videos/lsiidb/sport-report---cranium-coddlers---san-francisco-street-chess---floyd-mayweather",
        "http://thecolbertreport.cc.com/videos/ks6rd5/ted-cruz-s-obamacare--filibuster-",
        "http://thecolbertreport.cc.com/videos/urqr8j/joseph-gordon-levitt",
        "http://thecolbertreport.cc.com/videos/93nnw6/sign-off---ring-announcer"
      ],
      "guest": "Joseph Gordon-Levitt"
    },
    {
      "date": "2013-09-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/itk7kp/americone-dream-product-placement",
        "http://thecolbertreport.cc.com/videos/u1mo7v/chris-fischer",
        "http://thecolbertreport.cc.com/videos/lo2m3c/intro---9-26-13",
        "http://thecolbertreport.cc.com/videos/153u0a/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/87ddew/time-travel-adventures-with-conservatives"
      ],
      "guest": "Chris Fischer"
    },
    {
      "date": "2013-09-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mp715j/rockin--government-shutdown-eve",
        "http://thecolbertreport.cc.com/videos/pbvraa/tip-wag---butterball--ashley-merryman---science",
        "http://thecolbertreport.cc.com/videos/wzj7bh/vince-gilligan-pt--1",
        "http://thecolbertreport.cc.com/videos/xid9jc/vince-gilligan-pt--2"
      ],
      "guest": "Vince Gilligan"
    },
    {
      "date": "2013-10-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/99odk6/federal-government-shutdown",
        "http://thecolbertreport.cc.com/videos/cn352h/affordable-care-act---obama-s-computerized-america",
        "http://thecolbertreport.cc.com/videos/1ntmd2/adorable-care-act---generation-opportunity",
        "http://thecolbertreport.cc.com/videos/gfz4h7/national-hispanic-heritage-month",
        "http://thecolbertreport.cc.com/videos/obk0r1/daniel-radcliffe",
        "http://thecolbertreport.cc.com/videos/7ni2qs/sign-off---goodnight"
      ],
      "guest": "Daniel Radcliffe"
    },
    {
      "date": "2013-10-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/aykl9k/intro---10-2-13",
        "http://thecolbertreport.cc.com/videos/qx1ar9/1995-shutdown-survival-bunker",
        "http://thecolbertreport.cc.com/videos/qz6a9i/government--slimdown----potus-meeting",
        "http://thecolbertreport.cc.com/videos/xjdheq/blood-in-the-water---bill-o-reilly-s--killing-jesus-",
        "http://thecolbertreport.cc.com/videos/5ynb8q/chris-matthews",
        "http://thecolbertreport.cc.com/videos/mvs3wz/sign-off---shutdown-survival-bunker"
      ],
      "guest": "Chris Matthews"
    },
    {
      "date": "2013-10-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7l0bys/government-shutdown-day-three",
        "http://thecolbertreport.cc.com/videos/amjasd/the-2013-government-shutdown-wedding-of-the-century-pt--1",
        "http://thecolbertreport.cc.com/videos/qt2vrd/david-finkel",
        "http://thecolbertreport.cc.com/videos/6as11u/sign-off---audra-mcdonald-s-availability"
      ],
      "guest": "David Finkel"
    },
    {
      "date": "2013-10-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iyj9i2/government-shutdown-s-one-week-anniversary",
        "http://thecolbertreport.cc.com/videos/f9ohl9/bond-v--united-states",
        "http://thecolbertreport.cc.com/videos/rodf66/mccutcheon-v--fec---emily-bazelon",
        "http://thecolbertreport.cc.com/videos/d10tae/banksy-s-new-york-reign-of-terror",
        "http://thecolbertreport.cc.com/videos/feyjl3/james-spithill",
        "http://thecolbertreport.cc.com/videos/m7oe3o/sign-off----not-a-game--game"
      ],
      "guest": "James Spithill"
    },
    {
      "date": "2013-10-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/phldtj/intro---10-8-13",
        "http://thecolbertreport.cc.com/videos/u5kkik/debt-ceiling-deadline",
        "http://thecolbertreport.cc.com/videos/2b5rst/pro-pot-laws---pointers",
        "http://thecolbertreport.cc.com/videos/049124/thanksgiving-under-attack---hanukkah",
        "http://thecolbertreport.cc.com/videos/llhqmr/paul-giamatti",
        "http://thecolbertreport.cc.com/videos/tuzaza/sign-off----tj---dave-"
      ],
      "guest": "Paul Giamatti"
    },
    {
      "date": "2013-10-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pjgp86/intro---10-9-13",
        "http://thecolbertreport.cc.com/videos/ssksja/ride-for-the-constitution",
        "http://thecolbertreport.cc.com/videos/h502rh/twitter-s-ipo",
        "http://thecolbertreport.cc.com/videos/k9g3h2/tom-emmer-s-controversial-ad",
        "http://thecolbertreport.cc.com/videos/ldxsu2/tom-hanks",
        "http://thecolbertreport.cc.com/videos/uevql0/sign-off---goodnight"
      ],
      "guest": "Tom Hanks"
    },
    {
      "date": "2013-10-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xqbppa/government-shutdown-day-10---shep-smith-s-input",
        "http://thecolbertreport.cc.com/videos/bzo5fv/because-shep---fox-news-deck",
        "http://thecolbertreport.cc.com/videos/rt3php/because-shep---fox-news-deck---colbert-info-news-veranda",
        "http://thecolbertreport.cc.com/videos/r2mded/hanksy-s-grizzly-art",
        "http://thecolbertreport.cc.com/videos/twnvtr/reed-albergotti---vanessa-o-connell",
        "http://thecolbertreport.cc.com/videos/gn1hnb/sign-off---goodnight"
      ],
      "guest": "Reed Albergotti &amp; Vanessa O'Connell"
    },
    {
      "date": "2013-10-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zabrcj/end-of-the-government-shutdown",
        "http://thecolbertreport.cc.com/videos/fs5lvs/tip-wag---new-jersey--robo-teachers---amazon-erotica",
        "http://thecolbertreport.cc.com/videos/xmc07q/the-reflektors",
        "http://thecolbertreport.cc.com/videos/z30io4/sign-off----midnight"
      ],
      "guest": "The Reflektors"
    },
    {
      "date": "2013-10-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/0nhfjd/intro---10-22-13",
        "http://thecolbertreport.cc.com/videos/tpp3c7/the-in-box---lions-vs--tigers",
        "http://thecolbertreport.cc.com/videos/w4k85n/thought-for-food---kfc-s-go-cup---powerful-yogurt",
        "http://thecolbertreport.cc.com/videos/wv85sy/the-neiman-marcus-christmas-book",
        "http://thecolbertreport.cc.com/videos/413dai/a--scott-berg",
        "http://thecolbertreport.cc.com/videos/j9enbw/sign-off----the-heart-of-giving-"
      ],
      "guest": "A. Scott Berg"
    },
    {
      "date": "2013-10-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pfan07/obamacare-website-gate",
        "http://thecolbertreport.cc.com/videos/51c17c/i-tried-to-sign-up-for-obamacare---health-care-house-of-horrors",
        "http://thecolbertreport.cc.com/videos/w07qf1/i-tried-to-sign-up-for-obamacare---health-care-navigators",
        "http://thecolbertreport.cc.com/videos/j95qfd/judy-woodruff---gwen-ifill",
        "http://thecolbertreport.cc.com/videos/rtpako/sign-off---goodnight"
      ],
      "guest": "Gwen Ifill, Judy Woodruff"
    },
    {
      "date": "2013-10-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3cv3ae/intro---10-24-13",
        "http://thecolbertreport.cc.com/videos/8rabqj/girly-hats-for-the-marines",
        "http://thecolbertreport.cc.com/videos/6zcsyl/the-word---philantrophy",
        "http://thecolbertreport.cc.com/videos/60wsnw/craziest-f--king-thing-i-ve-ever-heard---tomtatoes",
        "http://thecolbertreport.cc.com/videos/9ak9w5/stephen-fry",
        "http://thecolbertreport.cc.com/videos/9py49q/sign-off---goodnight"
      ],
      "guest": "Stephen Fry"
    },
    {
      "date": "2013-10-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xfzjxy/healthcare-gov-s-missing-woman",
        "http://thecolbertreport.cc.com/videos/0m56pa/germany-s-nsa-outrage",
        "http://thecolbertreport.cc.com/videos/7egvpg/germany-s-nsa-outrage---mark-mazzetti",
        "http://thecolbertreport.cc.com/videos/boarwv/lifetime-of-furfillment",
        "http://thecolbertreport.cc.com/videos/kz8x10/orlando-bloom",
        "http://thecolbertreport.cc.com/videos/fl658q/sign-off---goodnight"
      ],
      "guest": "Orlando Bloom"
    },
    {
      "date": "2013-10-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dhae0b/intro---10-29-13",
        "http://thecolbertreport.cc.com/videos/qingaf/the-word---on-your-feet",
        "http://thecolbertreport.cc.com/videos/yxqllm/rand-paul-s-plagiarism-problem",
        "http://thecolbertreport.cc.com/videos/j9efvm/billy-collins",
        "http://thecolbertreport.cc.com/videos/fnaadw/sign-off----aimless-love-"
      ],
      "guest": "Billy Collins"
    },
    {
      "date": "2013-10-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wibml9/intro---10-30-13",
        "http://thecolbertreport.cc.com/videos/me8aye/the-gop-s-self-disapproval",
        "http://thecolbertreport.cc.com/videos/jns4fj/threatdown---divorce--undocumented-network-jumpers---global-warming",
        "http://thecolbertreport.cc.com/videos/ammjdj/shepard-smith-s-digital-dependency",
        "http://thecolbertreport.cc.com/videos/7frodo/jack-andraka",
        "http://thecolbertreport.cc.com/videos/s14fzp/sign-off---goodnight"
      ],
      "guest": "Jack Andraka"
    },
    {
      "date": "2013-10-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vr2jg3/intro---10-31-13",
        "http://thecolbertreport.cc.com/videos/8q3ppm/war-on-halloween---matt-lauer-s-costume",
        "http://thecolbertreport.cc.com/videos/2krnuz/blood-in-the-water---jim-wheeler-s-hypothetical-slavery-vote",
        "http://thecolbertreport.cc.com/videos/mzqttu/the-word---see-no-evil",
        "http://thecolbertreport.cc.com/videos/owduja/zach-sims",
        "http://thecolbertreport.cc.com/videos/53uet6/sign-off---the-glenlivet"
      ],
      "guest": "Zach Sims"
    },
    {
      "date": "2013-11-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hfr88n/intro---11-4-13",
        "http://thecolbertreport.cc.com/videos/v68n7l/obamacare-s-gender-blind-premiums",
        "http://thecolbertreport.cc.com/videos/oi11jp/the-word---inc--god-we-trust",
        "http://thecolbertreport.cc.com/videos/29w6fx/-realhumanpraise-for-fox-news",
        "http://thecolbertreport.cc.com/videos/z1sht0/david-folkenflik",
        "http://thecolbertreport.cc.com/videos/vl9eiz/sign-off---goodnight"
      ],
      "guest": "David Folkenflik"
    },
    {
      "date": "2013-11-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/owoy1b/exclusive---julius-erving-extended-interview",
        "http://thecolbertreport.cc.com/videos/7bd2cq/rob-ford-s-crack-scandal",
        "http://thecolbertreport.cc.com/videos/s5iv9f/difference-makers---tim-morrison-and-meagan-brame",
        "http://thecolbertreport.cc.com/videos/6abc8c/gay-sex-in-the-insect-world",
        "http://thecolbertreport.cc.com/videos/9v56tr/julius-erving",
        "http://thecolbertreport.cc.com/videos/du2t8n/sign-off---crack-pipe"
      ],
      "guest": "Julius Erving"
    },
    {
      "date": "2013-11-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rpo0ya/ms--marvel-s-reboot",
        "http://thecolbertreport.cc.com/videos/el55uc/tip-wag---toys--r--us--shroom-tombs---john-pike",
        "http://thecolbertreport.cc.com/videos/hdhamk/washington-state-s-gmo-labeling-initiative",
        "http://thecolbertreport.cc.com/videos/7nyym9/brian-lehrer",
        "http://thecolbertreport.cc.com/videos/snu1i2/sign-off---welcome-baby-fischel-"
      ],
      "guest": "Brian Lehrer"
    },
    {
      "date": "2013-11-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/d61yyh/employment-non-discrimination-act",
        "http://thecolbertreport.cc.com/videos/4cx9x8/sport-report---washington-redskins-name-controversy---miami-dolphins-bullying-allegations",
        "http://thecolbertreport.cc.com/videos/7cyanz/who-might-be-honoring-me-next----people-s-choice-awards",
        "http://thecolbertreport.cc.com/videos/80epmw/daniel-lieberman",
        "http://thecolbertreport.cc.com/videos/tx4mq5/sign-off---people-s-choice-awards"
      ],
      "guest": "Daniel Lieberman"
    },
    {
      "date": "2013-11-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/84rhzu/-60-minutes--benghazi-controversy",
        "http://thecolbertreport.cc.com/videos/uwudem/-60-minutes--benghazi-controversy---poncho-denews--bogus-bombshell",
        "http://thecolbertreport.cc.com/videos/bd4gnc/chris-christie-s-sunday-media-blitz",
        "http://thecolbertreport.cc.com/videos/2lqizl/peter-baker",
        "http://thecolbertreport.cc.com/videos/kglpif/sign-off---goodnight"
      ],
      "guest": "Peter Baker"
    },
    {
      "date": "2013-11-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iitiue/intro---11-12-13",
        "http://thecolbertreport.cc.com/videos/pqrcpb/obamacare-enrollment-troubles",
        "http://thecolbertreport.cc.com/videos/s7e3qv/iran-nuke-negotiations---french-resistance",
        "http://thecolbertreport.cc.com/videos/0qvety/iran-nuke-negotiations---trita-parsi",
        "http://thecolbertreport.cc.com/videos/9s2qhn/shantytown-glamour-camping",
        "http://thecolbertreport.cc.com/videos/91wur1/david-christian",
        "http://thecolbertreport.cc.com/videos/61ms6y/sign-off----a-single-roll-of-the-dice-"
      ],
      "guest": "David Christian"
    },
    {
      "date": "2013-11-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1p3who/u-s--drone-controversy",
        "http://thecolbertreport.cc.com/videos/h4v9zq/difference-makers---philip-steel",
        "http://thecolbertreport.cc.com/videos/w8qzgv/blood-in-the-water---richard-cohen-s-conventional-wisdom",
        "http://thecolbertreport.cc.com/videos/sn95d6/blind-boys-of-alabama---jimmy-carter"
      ],
      "guest": "Blind Boys of Alabama"
    },
    {
      "date": "2013-11-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2o6sb0/philippines-typhoon-relief",
        "http://thecolbertreport.cc.com/videos/8olyhc/rob-ford-s-defiance",
        "http://thecolbertreport.cc.com/videos/wrbvsm/alexis-ohanian",
        "http://thecolbertreport.cc.com/videos/nmbdiq/sign-off---kitten-cuddle"
      ],
      "guest": "Alexis Ohanian"
    },
    {
      "date": "2013-11-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yv49an/intro---11-18-13",
        "http://thecolbertreport.cc.com/videos/m7v6ee/philippines-relief-from-the-colbert-nation",
        "http://thecolbertreport.cc.com/videos/suwtn9/obamacare-backlash---pundit-hyperbole",
        "http://thecolbertreport.cc.com/videos/gnc6o8/obamacare-backlash---conservative-victory-lap",
        "http://thecolbertreport.cc.com/videos/12pe6a/alpha-dog-of-the-week---chip-wilson",
        "http://thecolbertreport.cc.com/videos/cdeggb/steve-mcqueen",
        "http://thecolbertreport.cc.com/videos/5ow82m/sign-off---goodnight"
      ],
      "guest": "Steve McQueen"
    },
    {
      "date": "2013-11-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kzu5qm/walmart-s-employee-food-drive",
        "http://thecolbertreport.cc.com/videos/fkmwr4/america-s-wealth-divide",
        "http://thecolbertreport.cc.com/videos/nj0wp7/america-s-wealth-divide---robert-reich",
        "http://thecolbertreport.cc.com/videos/ppx1hm/slate-s--minutes-to-read--feature",
        "http://thecolbertreport.cc.com/videos/g1usdl/rick-santorum",
        "http://thecolbertreport.cc.com/videos/jnk6o6/sign-off---sweater-vest"
      ],
      "guest": "Rick Santorum"
    },
    {
      "date": "2013-11-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kv4dxf/intro---11-20-13",
        "http://thecolbertreport.cc.com/videos/xxqfor/trey-radel-s-cocaine-arrest",
        "http://thecolbertreport.cc.com/videos/s2213y/tip-wag---hopped-up-pops--starbucks---american-consumers",
        "http://thecolbertreport.cc.com/videos/aiu6v1/sport-report---russia-s-anti-gay-winter-games",
        "http://thecolbertreport.cc.com/videos/bjap7z/m-i-a-"
      ],
      "guest": "M.I.A."
    },
    {
      "date": "2013-11-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bz75lg/intro---11-21-13",
        "http://thecolbertreport.cc.com/videos/16t3na/nuclear-option-in-the-senate",
        "http://thecolbertreport.cc.com/videos/ynxkze/mary-fallin-and-same-sex-benefits",
        "http://thecolbertreport.cc.com/videos/pqqitw/guess-who-s-coming-to-thanksgiving-dinner-",
        "http://thecolbertreport.cc.com/videos/5idfv3/j-j--abrams",
        "http://thecolbertreport.cc.com/videos/1xi9cj/sign-off----s-"
      ],
      "guest": "J.J. Abrams"
    },
    {
      "date": "2013-12-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a8rc4x/intro---12-2-13",
        "http://thecolbertreport.cc.com/videos/eax2go/healthcare-gov-revamp---presidential-turkey-pardon",
        "http://thecolbertreport.cc.com/videos/32fik6/amazon-s-delivery-drones",
        "http://thecolbertreport.cc.com/videos/kzzho9/blitzkrieg-on-grinchitude---bullet-catching-christmas-tree",
        "http://thecolbertreport.cc.com/videos/tllp9w/daniel-goleman",
        "http://thecolbertreport.cc.com/videos/4pjxs1/sign-off---eighth-anniversary-portrait"
      ],
      "guest": "Daniel Goleman"
    },
    {
      "date": "2013-12-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/810uks/intro---12-3-13",
        "http://thecolbertreport.cc.com/videos/6yqi5n/the-pope-s-secret-life",
        "http://thecolbertreport.cc.com/videos/ojh0t8/thought-for-food---ban-on-trans-fats---mcdonald-s-mcrib-mystery",
        "http://thecolbertreport.cc.com/videos/fepuu2/the-double-robotics-office-robot",
        "http://thecolbertreport.cc.com/videos/g14s8s/ed-stone",
        "http://thecolbertreport.cc.com/videos/jkirej/sign-off---honoring-ed-stone"
      ],
      "guest": "Ed Stone"
    },
    {
      "date": "2013-12-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xzvt8w/do-nothing-congress",
        "http://thecolbertreport.cc.com/videos/vjdf7c/tip-wag---campaign-for-cursive---the-rnc",
        "http://thecolbertreport.cc.com/videos/y2lfd6/colbert-platinum---freedom-ship",
        "http://thecolbertreport.cc.com/videos/hzc351/bryan-stevenson",
        "http://thecolbertreport.cc.com/videos/eanv4b/sign-off"
      ],
      "guest": "Bryan Stevenson"
    },
    {
      "date": "2013-12-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/evhpy0/intro---12-5-13",
        "http://thecolbertreport.cc.com/videos/r2orue/the-in-box---flight-vs--invisibility",
        "http://thecolbertreport.cc.com/videos/t96lm4/legal-weed-in-colorado",
        "http://thecolbertreport.cc.com/videos/q1iez3/legal-weed-in-colorado---ricardo-baca",
        "http://thecolbertreport.cc.com/videos/zy6hlf/the-gop-s-lady-troubles",
        "http://thecolbertreport.cc.com/videos/blunby/alan-mulally",
        "http://thecolbertreport.cc.com/videos/xyy6ql/sign-off"
      ],
      "guest": "Allan Mulally"
    },
    {
      "date": "2013-12-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8h6usc/remembering-nelson-mandela",
        "http://thecolbertreport.cc.com/videos/w58dfp/the-case-against-charity---bill-o-reilly---john-stossel",
        "http://thecolbertreport.cc.com/videos/5y4hrs/the-case-against-charity---homeless-for-the-holidays",
        "http://thecolbertreport.cc.com/videos/76e84o/stephen-s-grammy-nomination",
        "http://thecolbertreport.cc.com/videos/lv0hd2/david-keith",
        "http://thecolbertreport.cc.com/videos/6p2s11/sign-off"
      ],
      "guest": "David Keith"
    },
    {
      "date": "2013-12-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/my8zmp/intro---12-10-13",
        "http://thecolbertreport.cc.com/videos/7yd7o2/walmart-s-job-acceptance-rate",
        "http://thecolbertreport.cc.com/videos/z9zxq1/the-word---channel-serfing",
        "http://thecolbertreport.cc.com/videos/kaj6y2/blitzkrieg-on-grinchitude---early-christmas-in-venezuela",
        "http://thecolbertreport.cc.com/videos/pt29fq/alex-blumberg",
        "http://thecolbertreport.cc.com/videos/99z3wt/sign-off---farewell-to-frank-lesser"
      ],
      "guest": "Alex Blumberg"
    },
    {
      "date": "2013-12-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zye2nw/blitzkrieg-on-grinchitude---festivus-pole-in-the-florida-capitol",
        "http://thecolbertreport.cc.com/videos/2vwk2a/obama-s-handshake-controversy",
        "http://thecolbertreport.cc.com/videos/ayrep6/sign-language-scandal-at-mandela-s-memorial",
        "http://thecolbertreport.cc.com/videos/jna07l/mike-huckabee-s--12-days-of-obamacare-",
        "http://thecolbertreport.cc.com/videos/ld1i97/elizabeth-gilbert",
        "http://thecolbertreport.cc.com/videos/nxssxf/sign-off---goodnight"
      ],
      "guest": "Elizabeth Gilbert"
    },
    {
      "date": "2013-12-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/juqc9w/bipartisan-budget-agreement",
        "http://thecolbertreport.cc.com/videos/ygi28a/cheating-death---sleep-health---cosmetic-surgery",
        "http://thecolbertreport.cc.com/videos/btidng/megyn-kelly-on-santa-s-skin-color",
        "http://thecolbertreport.cc.com/videos/gv6c5c/george-packer",
        "http://thecolbertreport.cc.com/videos/o3drqn/sign-off---goodnight"
      ],
      "guest": "George Packer"
    },
    {
      "date": "2013-12-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tch93k/intro---12-16-13",
        "http://thecolbertreport.cc.com/videos/t0srep/google-s-robot-acquisition",
        "http://thecolbertreport.cc.com/videos/4q1rc7/nsa-video-game-surveillance",
        "http://thecolbertreport.cc.com/videos/qepegb/stephen-s-grammy-nomination---billy-crystal",
        "http://thecolbertreport.cc.com/videos/1wx2c5/jonah-peretti"
      ],
      "guest": "Jonah Peretti, Gregg Allman, the National"
    },
    {
      "date": "2013-12-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ufkb4r/intro---12-17-13",
        "http://thecolbertreport.cc.com/videos/hdex9j/anti-nsa-ruling---edward-snowden-s-asylum-bid",
        "http://thecolbertreport.cc.com/videos/v7f6xw/tip-wag---all-china-edition",
        "http://thecolbertreport.cc.com/videos/18yj36/-ted-cruz-to-the-future-",
        "http://thecolbertreport.cc.com/videos/0hlwua/garry-trudeau"
      ],
      "guest": "Garry Trudeau, Cyndi Lauper, Alan Cumming"
    },
    {
      "date": "2013-12-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uqgbw6/intro---12-18-13",
        "http://thecolbertreport.cc.com/videos/w20rkq/rethinking-customer-satisfaction",
        "http://thecolbertreport.cc.com/videos/hqucv3/santa-claus-ethnicity-debate",
        "http://thecolbertreport.cc.com/videos/7ick9v/santa-claus-ethnicity-debate---hans-beinholtz",
        "http://thecolbertreport.cc.com/videos/vv4aaz/keanu-reeves",
        "http://thecolbertreport.cc.com/videos/52csyt/sign-off---goodnight"
      ],
      "guest": "Keanu Reeves, Aaron Neville"
    },
    {
      "date": "2013-12-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rdc6qs/jamie-dimon-s-christmas-card",
        "http://thecolbertreport.cc.com/videos/p9rfx1/fox-news-s--12-scams-of-christmas-",
        "http://thecolbertreport.cc.com/videos/na7pll/phil-robertson-s--duck-dynasty--suspension",
        "http://thecolbertreport.cc.com/videos/3q7h60/ben-stiller"
      ],
      "guest": "Ben Stiller, the Blind Boys of Alabama"
    }
  ],
  "2014": [
    {
      "date": "2014-01-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qaqhv8/intro---1-6-14",
        "http://thecolbertreport.cc.com/videos/vobbe1/polar-vortex",
        "http://thecolbertreport.cc.com/videos/3goywo/tip-wag---fda--toy-manufacturers---logo-party",
        "http://thecolbertreport.cc.com/videos/hyg1jb/recreational-pot-sales-in-colorado",
        "http://thecolbertreport.cc.com/videos/5qceid/ken-roth",
        "http://thecolbertreport.cc.com/videos/f9w0xq/sign-off---polar-vortex"
      ],
      "guest": "Kenneth Roth"
    },
    {
      "date": "2014-01-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/4uqurx/donald-trump-and-fox---friends-vs--global-warming",
        "http://thecolbertreport.cc.com/videos/s9iccj/income-inequality-debate",
        "http://thecolbertreport.cc.com/videos/v3sijl/income-inequality-debate---jim-martin",
        "http://thecolbertreport.cc.com/videos/b9gbou/time-travel-research-in-cyberspace",
        "http://thecolbertreport.cc.com/videos/bz0qvj/john-seigenthaler",
        "http://thecolbertreport.cc.com/videos/a4c8i8/sign-off----a-big-heart-open-to-god-"
      ],
      "guest": "John Seigenthaler"
    },
    {
      "date": "2014-01-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1vojc6/intro---1-8-14",
        "http://thecolbertreport.cc.com/videos/2zkpvh/chris-christie---the-george-washington-bridge-scandal",
        "http://thecolbertreport.cc.com/videos/bkjqeq/cheating-death---robo-sperm---health-roulette",
        "http://thecolbertreport.cc.com/videos/ct0fks/the-polar-vortex---fruit-tools",
        "http://thecolbertreport.cc.com/videos/i292oo/ishmael-beah",
        "http://thecolbertreport.cc.com/videos/srasr6/sign-off---cold-weather-fruit-hammer"
      ],
      "guest": "Ishmael Beah"
    },
    {
      "date": "2014-01-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3nlrc7/new-jersey-bridge-scandal---damning-emails",
        "http://thecolbertreport.cc.com/videos/ez26gi/new-jersey-bridge-scandal---chris-christie-s-someone-else-a-culpa",
        "http://thecolbertreport.cc.com/videos/gvlcow/robert-gates-s--duty-",
        "http://thecolbertreport.cc.com/videos/cjww9c/jeff-skoll",
        "http://thecolbertreport.cc.com/videos/zmnwvz/sign-off---people-s-choice-award"
      ],
      "guest": "Jeff Skoll"
    },
    {
      "date": "2014-01-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qh2gll/intro---1-13-14",
        "http://thecolbertreport.cc.com/videos/nmeif6/water-crisis-in-west-virginia",
        "http://thecolbertreport.cc.com/videos/l6fcm2/the-word---never-ender-s-game",
        "http://thecolbertreport.cc.com/videos/ekq6m6/mirriad---retroactive-product-placement",
        "http://thecolbertreport.cc.com/videos/zf2igg/sign-off---back-scratch"
      ],
      "guest": "David Fanning"
    },
    {
      "date": "2014-01-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e0ksix/sport-report---baseball",
        "http://thecolbertreport.cc.com/videos/8aoa48/sport-report---winter-sports",
        "http://thecolbertreport.cc.com/videos/4lplhb/sport-report---billie-jean-king",
        "http://thecolbertreport.cc.com/videos/1urzjl/deborah-solomon",
        "http://thecolbertreport.cc.com/videos/b5df4x/sign-off---goodnight"
      ],
      "guest": "Deborah Solomon"
    },
    {
      "date": "2014-01-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/daejaf/ad-for-america",
        "http://thecolbertreport.cc.com/videos/bxdt1w/sport-report---uneducated-college-athletes---peyton-manning-s-sponsor-shout-out",
        "http://thecolbertreport.cc.com/videos/rbh95h/alpha-dog-of-the-week---francois-hollande",
        "http://thecolbertreport.cc.com/videos/tkqmyv/gabriel-sherman",
        "http://thecolbertreport.cc.com/videos/efgh7j/sign-off---goodnight"
      ],
      "guest": "Gabriel Sherman"
    },
    {
      "date": "2014-01-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pqopug/nsa-software-implants",
        "http://thecolbertreport.cc.com/videos/6omuyc/colbert-platinum---diamond-pacifiers---financial-domination",
        "http://thecolbertreport.cc.com/videos/d589xx/stephen-s-grammy-nomination---carol-burnett",
        "http://thecolbertreport.cc.com/videos/4g3c4f/naquasia-legrand",
        "http://thecolbertreport.cc.com/videos/h6vhef/sign-off---colbert-s-book-club"
      ],
      "guest": "Naquasia LeGrand"
    },
    {
      "date": "2014-01-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2jaqbf/intro---1-20-13",
        "http://thecolbertreport.cc.com/videos/6qy0qw/peyton-manning-s--omaha--chant---marijuana-s-effects-on-football",
        "http://thecolbertreport.cc.com/videos/bg48ms/the-word---thrift-justice",
        "http://thecolbertreport.cc.com/videos/1ah0qw/pope-francis-s-breastfeeding-support---affordable-sainthood",
        "http://thecolbertreport.cc.com/videos/szyyzo/scott-stossel",
        "http://thecolbertreport.cc.com/videos/3kds6e/sign-off---colbert-s-book-club-reminder"
      ],
      "guest": "Scott Stossel"
    },
    {
      "date": "2014-01-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6g3tkl/sign-off---colbert-s-book-club---ernest-hemingway-s--a-farewell-to-arms-",
        "http://thecolbertreport.cc.com/videos/27el91/colbert-s-book-club---mariel-hemingway-on-ernest-hemingway",
        "http://thecolbertreport.cc.com/videos/c8gx08/colbert-s-book-club---michael-chabon----a-farewell-to-arms-",
        "http://thecolbertreport.cc.com/videos/2tt8np/colbert-s-book-club---better-know-a-hemingway",
        "http://thecolbertreport.cc.com/videos/8vzg0l/colbert-s-book-club---ernest-hemingway"
      ],
      "guest": "Michael Chabon, Mariel Hemingway"
    },
    {
      "date": "2014-01-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/o2dl8a/intro---1-22-14",
        "http://thecolbertreport.cc.com/videos/id8eug/mystery-doughnut-on-mars",
        "http://thecolbertreport.cc.com/videos/db8f37/tip-wag---air-force--dr--keith-ablow---westminster-dog-show",
        "http://thecolbertreport.cc.com/videos/wjov9z/tikker-death-watch",
        "http://thecolbertreport.cc.com/videos/y85ykp/charles-duhigg",
        "http://thecolbertreport.cc.com/videos/ihby00/sign-off---mutt"
      ],
      "guest": "Charles Duhigg"
    },
    {
      "date": "2014-01-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ay6diu/riots-in-the-ukraine",
        "http://thecolbertreport.cc.com/videos/nnj3ic/end-of-net-neutrality",
        "http://thecolbertreport.cc.com/videos/qatuhg/end-of-net-neutrality---tim-wu",
        "http://thecolbertreport.cc.com/videos/0i8pwp/china-s-colbert-report-rip-off",
        "http://thecolbertreport.cc.com/videos/fykny6/patricia-churchland",
        "http://thecolbertreport.cc.com/videos/5axbrg/sign-off---goodnight"
      ],
      "guest": "Patricia Churchland"
    },
    {
      "date": "2014-01-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qs3r6w/logo-restrictions-for-the-super-bowl",
        "http://thecolbertreport.cc.com/videos/51gnff/richard-sherman-s-rant-fallout",
        "http://thecolbertreport.cc.com/videos/mk6zsq/nate-silver",
        "http://thecolbertreport.cc.com/videos/c58bm1/sign-off---grammy-award"
      ],
      "guest": "Nate Silver"
    },
    {
      "date": "2014-01-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gzw6pe/superb-owl-xlviii---nfl-extra-point-debate",
        "http://thecolbertreport.cc.com/videos/g3ng7g/fallback-position---championship-nfl-quarterback",
        "http://thecolbertreport.cc.com/videos/y1y1q6/spotted-owls-vs--barred-owls---david-yarnold",
        "http://thecolbertreport.cc.com/videos/wx55bg/justin-tuck",
        "http://thecolbertreport.cc.com/videos/q6n89x/sign-off---tootsie-pop"
      ],
      "guest": "Justin Tuck"
    },
    {
      "date": "2014-01-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/79qyj3/superb-owl-xlviii---football-christmas",
        "http://thecolbertreport.cc.com/videos/pzw1hz/fallback-position---championship-nfl-quarterback-pt--2",
        "http://thecolbertreport.cc.com/videos/0czypw/distractions---reactions-at-the-state-of-the-union",
        "http://thecolbertreport.cc.com/videos/6h1tef/cris-carter"
      ],
      "guest": "Cris Carter"
    },
    {
      "date": "2014-01-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vp5oqx/superb-owl-xlviii---football-health-concerns",
        "http://thecolbertreport.cc.com/videos/8z0t1l/superb-owl-xlviii---football-health-concerns---steve-fainaru---mark-fainaru-wada",
        "http://thecolbertreport.cc.com/videos/b88aif/big-game-debate-with-ed-murray-and-michael-hancock",
        "http://thecolbertreport.cc.com/videos/7aqq1s/drew-brees",
        "http://thecolbertreport.cc.com/videos/yucj0t/sign-off---football-toss"
      ],
      "guest": "Drew Brees"
    },
    {
      "date": "2014-02-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kmzt7v/coca-cola-s-diverse--america-the-beautiful--ad",
        "http://thecolbertreport.cc.com/videos/65qhlv/tip-wag---litigious-cheerleaders--pope-francis---china",
        "http://thecolbertreport.cc.com/videos/nezg8b/j-k--rowling-s-ron-and-hermione-bombshell",
        "http://thecolbertreport.cc.com/videos/nocpjv/jennifer-senior",
        "http://thecolbertreport.cc.com/videos/msb2vl/sign-off---goodnight"
      ],
      "guest": "Jennifer Senior"
    },
    {
      "date": "2014-02-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m0k7nu/black-history-of-children-s-dental-health-month---chris-christie-s-bridge-scandal-connection",
        "http://thecolbertreport.cc.com/videos/81q2jm/chris-christie-vs--david-wildstein-on-the-new-jersey-bridge-scandal",
        "http://thecolbertreport.cc.com/videos/49r39y/pussy-riot-pt--1",
        "http://thecolbertreport.cc.com/videos/08f0xw/pussy-riot-pt--2",
        "http://thecolbertreport.cc.com/videos/ubzb8b/sign-off---pussy-riot----bringing-human-rights-back-home-"
      ],
      "guest": "Pussy Riot"
    },
    {
      "date": "2014-02-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nn8d7g/intro---2-5-14",
        "http://thecolbertreport.cc.com/videos/w3uorg/obamacare-jobs-debate",
        "http://thecolbertreport.cc.com/videos/djw49l/america-s-wealthy-under-siege---mort-zuckerman",
        "http://thecolbertreport.cc.com/videos/cjdkxj/lake-street-dive",
        "http://thecolbertreport.cc.com/videos/6itibl/sign-off---goodnight"
      ],
      "guest": "Lake Street Dive"
    },
    {
      "date": "2014-02-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tzqa3o/obama---the-keystone-xl-pipeline",
        "http://thecolbertreport.cc.com/videos/e3q55j/sochi-olympics-cry-athlon",
        "http://thecolbertreport.cc.com/videos/yzcp46/tip-wag---tsa-peeping-toms--domino-s-pizza-artists---federal-judges",
        "http://thecolbertreport.cc.com/videos/ze9n7p/paul-krugman",
        "http://thecolbertreport.cc.com/videos/1ur5x9/sign-off---welcome-baby-eli-"
      ],
      "guest": "Paul Krugman"
    },
    {
      "date": "2014-02-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/alv9kr/rocky-start-at-the-sochi-olympics",
        "http://thecolbertreport.cc.com/videos/155uge/sport-report---from-russia-with-love--but-no-gay-stuff-",
        "http://thecolbertreport.cc.com/videos/s385jl/taliban-dognappers",
        "http://thecolbertreport.cc.com/videos/hmu6hf/patrick-kennedy",
        "http://thecolbertreport.cc.com/videos/bl6jzi/sign-off---buddy-cole"
      ],
      "guest": "Patrick Kennedy"
    },
    {
      "date": "2014-02-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zddxmq/intro---2-11-14",
        "http://thecolbertreport.cc.com/videos/yesavg/blade-in-the-usa",
        "http://thecolbertreport.cc.com/videos/ow2caa/sport-report---from-russia-with-love--but-no-gay-stuff----u-s--speedskating-team",
        "http://thecolbertreport.cc.com/videos/cxui4b/sport-report---michael-sam-s-coming-out",
        "http://thecolbertreport.cc.com/videos/8yt2ar/charlie-crist",
        "http://thecolbertreport.cc.com/videos/v6h2iw/sign-off---goodnight"
      ],
      "guest": "Charlie Crist"
    },
    {
      "date": "2014-02-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mke8f4/white-house-state-dinner",
        "http://thecolbertreport.cc.com/videos/ngjlqq/bill-o-reilly-s-interview-of-the-decade",
        "http://thecolbertreport.cc.com/videos/f7yt2f/because-shep---white-house-menu-report",
        "http://thecolbertreport.cc.com/videos/zqevr4/godfrey-reggio",
        "http://thecolbertreport.cc.com/videos/wd8rlk/sign-off---au-revoir"
      ],
      "guest": "Godfrey Reggio"
    },
    {
      "date": "2014-02-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cb08sc/intro---2-18-14",
        "http://thecolbertreport.cc.com/videos/esabem/jimmy-fallon-s--tonight-show--debut",
        "http://thecolbertreport.cc.com/videos/icw75d/transgender-awareness",
        "http://thecolbertreport.cc.com/videos/px4k4w/transgender-awareness---janet-mock",
        "http://thecolbertreport.cc.com/videos/fpn2d7/brian-greene",
        "http://thecolbertreport.cc.com/videos/7cxypm/sign-off---goodnight"
      ],
      "guest": "Brian Greene"
    },
    {
      "date": "2014-02-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/8ht320/intro---2-19-14",        
        "http://thecolbertreport.cc.com/videos/z8viri/sport-report---from-russia-with-love--but-no-gay-stuff----buddy-cole-in-sochi",
        "http://thecolbertreport.cc.com/videos/k0fmq0/victory-and-vigilance-at-the-sochi-games",
        "http://thecolbertreport.cc.com/videos/pdgpm2/smile-file---al-qaeda-bomb-blunder",
        "http://thecolbertreport.cc.com/videos/80x11s/alexander-payne",
        "http://thecolbertreport.cc.com/videos/r3yso9/sign-off---goodnight"
      ],
      "guest": "Alexander Payne"
    },
    {
      "date": "2014-02-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gtx5i8/auction-for-bill-o-reilly-s-stolen-microwave",
        "http://thecolbertreport.cc.com/videos/7alqr9/sochi-olympics-2014---bode-miller",
        "http://thecolbertreport.cc.com/videos/i1pl20/stanley-mcchrystal",
        "http://thecolbertreport.cc.com/videos/3j3ziw/sign-off---microwave-auction---stanley-mcchrystal"
      ],
      "guest": "Gen. Stanley McChrystal"
    },
    {
      "date": "2014-02-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1x3cmv/intro---2-24-14",
        "http://thecolbertreport.cc.com/videos/dxcy1y/blade-in-the-usa---dutch-coach-s-anti-america-rant",
        "http://thecolbertreport.cc.com/videos/y1wxc3/crisis-in-ukraine",
        "http://thecolbertreport.cc.com/videos/8067fc/crisis-in-ukraine---gideon-rose",
        "http://thecolbertreport.cc.com/videos/2y58gs/darlene-love",        
        "http://thecolbertreport.cc.com/videos/illjzj/sign-off---remembering-harold-ramis"
      ],
      "guest": "Darlene Love"
    },
    {
      "date": "2014-02-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/blcgek/the-huffington-post-on-the-past-lives-of-children",
        "http://thecolbertreport.cc.com/videos/uov6m4/outrage-over-military-budget-cuts",
        "http://thecolbertreport.cc.com/videos/y2j7vo/the-word---jobsolete",
        "http://thecolbertreport.cc.com/videos/yw875l/consumers-for-paper-options",
        "http://thecolbertreport.cc.com/videos/w2zhlc/st--vincent"
      ],
      "guest": "St. Vincent"
    },
    {
      "date": "2014-02-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7vvoyf/michelle-obama-vs--child-obesity",
        "http://thecolbertreport.cc.com/videos/gs9vcz/colbert-s-very-wanted---who-took-gumby-",
        "http://thecolbertreport.cc.com/videos/y307f3/fox-news-on-hillary-clinton-s-age",
        "http://thecolbertreport.cc.com/videos/tb28zm/meryl-davis---charlie-white",
        "http://thecolbertreport.cc.com/videos/3w27qv/sign-off---chair-twirl"
      ],
      "guest": "Meryl Davis &amp; Charlie White"
    },
    {
      "date": "2014-02-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/11tivg/intro---2-27-14",
        "http://thecolbertreport.cc.com/videos/28qta1/defeat-for-arizona-s-anti-gay-legislation",
        "http://thecolbertreport.cc.com/videos/p8fj8f/black-history-month---stereotypes---racial-identity",
        "http://thecolbertreport.cc.com/videos/300ry4/black-history-month---laser-klan",
        "http://thecolbertreport.cc.com/videos/8ijgcp/jeff-goldblum",
        "http://thecolbertreport.cc.com/videos/axkpkj/sign-off---wedding-cake"
      ],
      "guest": "Jeff Goldblum"
    },
    {
      "date": "2014-03-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hbrhpe/magical-evening-at-the-2014-academy-awards",
        "http://thecolbertreport.cc.com/videos/q8u939/phony-obamacare-horror-stories",
        "http://thecolbertreport.cc.com/videos/8jpus1/phony-obamacare-horror-stories---patrick-stewart",
        "http://thecolbertreport.cc.com/videos/ysbw7d/sports-illustrated-barbie",
        "http://thecolbertreport.cc.com/videos/wwqhgn/caitlin-flanagan",
        "http://thecolbertreport.cc.com/videos/z2x5tb/sign-off----waiting-for-godot-"
      ],
      "guest": "Caitlin Flanagan"
    },
    {
      "date": "2014-03-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/y4s2js/intro---3-4-14",
        "http://thecolbertreport.cc.com/videos/avavv1/better-know-a-geopolitical-flashpoint---crimean-peninsula",
        "http://thecolbertreport.cc.com/videos/r79jgq/cold-war-update---obama-s-ukraine-response",
        "http://thecolbertreport.cc.com/videos/dpc49v/arizona-s-religious-freedom-bill---self-professed-gays",
        "http://thecolbertreport.cc.com/videos/bjwnn1/jaron-lanier",
        "http://thecolbertreport.cc.com/videos/38n33x/sign-off---shoe-answering-machine"
      ],
      "guest": "Jaron Lanier"
    },
    {
      "date": "2014-03-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a2cnjz/intro---3-5-14",
        "http://thecolbertreport.cc.com/videos/chbquj/bill-o-reilly-on-the-downside-of-a-woman-president",
        "http://thecolbertreport.cc.com/videos/ak3veo/tip-wag---chevron---fda",
        "http://thecolbertreport.cc.com/videos/ppqf1u/headline-news-rebrand",
        "http://thecolbertreport.cc.com/videos/0exuju/beau-willimon",
        "http://thecolbertreport.cc.com/videos/gexopu/sign-off---goodnight"
      ],
      "guest": "Beau Willimon"
    },
    {
      "date": "2014-03-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mmf7np/intro---3-6-14",
        "http://thecolbertreport.cc.com/videos/te4fyy/legal-upskirting-in-massachusetts",
        "http://thecolbertreport.cc.com/videos/awc6am/women-s-history-month---impossible-body-standards---appetizing-beauty-products",
        "http://thecolbertreport.cc.com/videos/3si7rs/warner-music-s--happy-birthday--copyright",
        "http://thecolbertreport.cc.com/videos/f3jjle/theaster-gates",
        "http://thecolbertreport.cc.com/videos/g6qd4x/sign-off---liberty-bell"
      ],
      "guest": "Theaster Gates"
    },
    {
      "date": "2014-03-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ag9578/intro---3-10-14",
        "http://thecolbertreport.cc.com/videos/a6f94j/cross-controversy-at-9-11-museum",
        "http://thecolbertreport.cc.com/videos/bn0fy6/the-word---pew--pew--pew-",
        "http://thecolbertreport.cc.com/videos/gh6urb/neil-degrasse-tyson-pt--1",
        "http://thecolbertreport.cc.com/videos/42g6iq/neil-degrasse-tyson-pt--2",
        "http://thecolbertreport.cc.com/videos/1bou2c/sign-off---goodnight"
      ],
      "guest": "Neil DeGrasse Tyson"
    },
    {
      "date": "2014-03-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g08oh5/intro---3-11-14",
        "http://thecolbertreport.cc.com/videos/usi00y/fan-magazine-for-pope-francis",
        "http://thecolbertreport.cc.com/videos/pis5qm/the-huffington-post-s-anal-sex-bombshell",
        "http://thecolbertreport.cc.com/videos/pvjhwj/the-huffington-post-s-anal-sex-bombshell---randy-ferrar",
        "http://thecolbertreport.cc.com/videos/qacc88/tip-wag---u-s--department-of-justice---wall-street",
        "http://thecolbertreport.cc.com/videos/nba46a/ronan-farrow",
        "http://thecolbertreport.cc.com/videos/hncfzx/sign-off---pope-centerfold"
      ],
      "guest": "Ronan Farrow"
    },
    {
      "date": "2014-03-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ut2zdq/president-obama-on--between-two-ferns-",
        "http://thecolbertreport.cc.com/videos/h6q3h4/vladimir-putin-s-propaganda-machine---russia-today",
        "http://thecolbertreport.cc.com/videos/i7q6ld/vladimir-putin-s-propaganda-machine---russia-today---liz-wahl",
        "http://thecolbertreport.cc.com/videos/wp6hv1/nsa-s--ask-zelda--advice-column",
        "http://thecolbertreport.cc.com/videos/2qsrw5/maria-shriver",
        "http://thecolbertreport.cc.com/videos/i6cs26/sign-off---goodnight"
      ],
      "guest": "Maria Shriver"
    },
    {
      "date": "2014-03-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5js43m/colorado-s-booming-marijuana-industry",
        "http://thecolbertreport.cc.com/videos/a1ejoq/bears---balls---ganjapreneurs",
        "http://thecolbertreport.cc.com/videos/xkuwmd/obama-s-overtime-pay-expansion",
        "http://thecolbertreport.cc.com/videos/k9goh1/simon-schama",
        "http://thecolbertreport.cc.com/videos/tl1mce/sign-off---goodnight"
      ],
      "guest": "Simon Schama"
    },
    {
      "date": "2014-03-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hjb6kt/back-from-spring-break",
        "http://thecolbertreport.cc.com/videos/imczen/better-know-a-district---north-carolina-s-1st---g-k--butterfield",
        "http://thecolbertreport.cc.com/videos/8cy48v/malaysia-airlines--missing-plane",
        "http://thecolbertreport.cc.com/videos/g4poyv/bryan-cranston",
        "http://thecolbertreport.cc.com/videos/a2iw3f/sign-off---goodnight"
      ],
      "guest": "Bryan Cranston"
    },
    {
      "date": "2014-03-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9n1euv/hugely-historic-night-with-jimmy-carter",
        "http://thecolbertreport.cc.com/videos/0k0w7y/president-jimmy-carter---the-colbert-interviews",
        "http://thecolbertreport.cc.com/videos/xepzs5/jimmy-carter-pt--1",
        "http://thecolbertreport.cc.com/videos/t3jp2g/jimmy-carter-pt--2",
        "http://thecolbertreport.cc.com/videos/uyisf5/sign-off---goodnight--carter-library"
      ],
      "guest": "Jimmy Carter"
    },
    {
      "date": "2014-03-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1zhwtt/drunk-secret-service-agents-in-amsterdam",
        "http://thecolbertreport.cc.com/videos/b6cwb3/sport-report---professional-soccer-toddler--golf-innovations---washington-redskins-charm-offensive",
        "http://thecolbertreport.cc.com/videos/q8pyub/bright-prospects-for-the-gop-in-2016",
        "http://thecolbertreport.cc.com/videos/mcpvbd/errol-morris",
        "http://thecolbertreport.cc.com/videos/ycwnol/sign-off---goodnight"
      ],
      "guest": "Errol Morris"
    },
    {
      "date": "2014-03-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qforig/intro---3-27-14",
        "http://thecolbertreport.cc.com/videos/uqmqua/ukraine-s-dolphin-army",
        "http://thecolbertreport.cc.com/videos/cabdj6/morning-news-for-millennials",
        "http://thecolbertreport.cc.com/videos/srj2lz/hawaii-s-prostitution-exemption-for-cops",
        "http://thecolbertreport.cc.com/videos/77oyfl/darren-aronofsky",
        "http://thecolbertreport.cc.com/videos/tyuheg/sign-off---playdate-with-charlie-rose"
      ],
      "guest": "Darren Aronofsky"
    },
    {
      "date": "2014-03-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lumbga/intro---3-31-14",
        "http://thecolbertreport.cc.com/videos/3yhe9h/emoji-ethnicity",
        "http://thecolbertreport.cc.com/videos/1zkr18/who-s-attacking-me-now-----cancelcolbert",
        "http://thecolbertreport.cc.com/videos/35dcpo/stephen-s--cancelcolbert-mea-culpa",
        "http://thecolbertreport.cc.com/videos/vj7n1j/biz-stone-pt--1",
        "http://thecolbertreport.cc.com/videos/yc8huq/biz-stone-pt--2",
        "http://thecolbertreport.cc.com/videos/adyesn/sign-off---bud-light-lime",
        "http://thecolbertreport.cc.com/videos/p65waq/3-31-14-in--60-seconds"
      ],
      "guest": "Biz Stone"
    },
    {
      "date": "2014-04-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/3ljnpx/obamacare-victory-lap",
        "http://thecolbertreport.cc.com/videos/cviqog/union-push-for-college-athletes",
        "http://thecolbertreport.cc.com/videos/64v4nu/union-push-for-college-athletes---ramogi-huma",
        "http://thecolbertreport.cc.com/videos/784uo8/john-malkovich",
        "http://thecolbertreport.cc.com/videos/rc1p9n/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/c9xd2d/4-1-14-in--60-seconds"
      ],
      "guest": "John Malkovich"
    },
    {
      "date": "2014-04-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zxr7i2/u-n--climate-change-report",
        "http://thecolbertreport.cc.com/videos/o639ag/the-word---silent-but-deadly",
        "http://thecolbertreport.cc.com/videos/1ypxfz/silicon-valley-s-cosmetic-surgery-boom",
        "http://thecolbertreport.cc.com/videos/pnhs3f/dan-harris",
        "http://thecolbertreport.cc.com/videos/wrxyua/sign-off---comedy-central-app"
      ],
      "guest": "Dan Harris"
    },
    {
      "date": "2014-04-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kas793/holy-grail-discovery",
        "http://thecolbertreport.cc.com/videos/n79fg2/supreme-court-ruling-on-aggregate-campaign-funding",
        "http://thecolbertreport.cc.com/videos/n6lhb9/supreme-court-ruling-on-aggregate-campaign-funding---emily-bazelon",
        "http://thecolbertreport.cc.com/videos/4vb00q/bill-o-reilly-s-defense-of-inequality",
        "http://thecolbertreport.cc.com/videos/fgsnrb/mark-mazzetti",
        "http://thecolbertreport.cc.com/videos/255jt7/sign-off---coffee-break"
      ],
      "guest": "Mark Mazzetti"
    },
    {
      "date": "2014-04-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/lz94c9/jeb-bush-on-illegal-immigrants",
        "http://thecolbertreport.cc.com/videos/jjifoz/tip-wag---new-york-times--alaska-board-of-game---mazda",
        "http://thecolbertreport.cc.com/videos/jvziju/matt-bevin-s-cockfighting-controversy",
        "http://thecolbertreport.cc.com/videos/xj9d66/edward-frenkel",
        "http://thecolbertreport.cc.com/videos/2dvxf1/sign-off---newspaper"
      ],
      "guest": "Edward Frenkel"
    },
    {
      "date": "2014-04-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/m6pj8n/intro---4-8-14",
        "http://thecolbertreport.cc.com/videos/wpor0d/america-s-uninformed-opinion-on-ukraine",
        "http://thecolbertreport.cc.com/videos/ncl2k5/cia-interrogation-report",
        "http://thecolbertreport.cc.com/videos/nemi1a/common-core-confusion",
        "http://thecolbertreport.cc.com/videos/uyjkgv/jane-goodall",
        "http://thecolbertreport.cc.com/videos/2v7871/sign-off---cheers"
      ],
      "guest": "Jane Goodall"
    },
    {
      "date": "2014-04-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/53uymc/intro---4-9-14",
        "http://thecolbertreport.cc.com/videos/o3rniz/heartbleed-internet-bug",
        "http://thecolbertreport.cc.com/videos/8a5aao/brendan-eich-s-forced-resignation",
        "http://thecolbertreport.cc.com/videos/3pg0sn/brendan-eich-s-forced-resignation---andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/l9zuu1/obama-s-equal-pay-orders",
        "http://thecolbertreport.cc.com/videos/wr794b/sheryl-sandberg",
        "http://thecolbertreport.cc.com/videos/mroadr/sign-off---goodnight"
      ],
      "guest": "Sheryl Sandberg"
    },
    {
      "date": "2014-04-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/k436zi/david-letterman-s-retirement",
        "http://thecolbertreport.cc.com/videos/kv1taq/cheating-death---depression-edition",
        "http://thecolbertreport.cc.com/videos/3a9611/bill-o-reilly-on-america-s--grievance-industry-",
        "http://thecolbertreport.cc.com/videos/yi8cxa/sting"
      ],
      "guest": "Sting"
    },
    {
      "date": "2014-04-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1tyawq/intro---4-21-14",
        "http://thecolbertreport.cc.com/videos/0w61r2/al-qaeda-s-overly-public-pep-rally",
        "http://thecolbertreport.cc.com/videos/055g6r/hillary-clinton-s-grandmother-status",
        "http://thecolbertreport.cc.com/videos/7d5y74/stephen-colbert-s-bats--t-serious---hillary-clinton-shoe-spiracy-theory",
        "http://thecolbertreport.cc.com/videos/hls49q/extreme-measures-for-boosting-church-attendance",
        "http://thecolbertreport.cc.com/videos/p5o99a/ken-burns",
        "http://thecolbertreport.cc.com/videos/v2nud8/sign-off---goodnight"
      ],
      "guest": "Ken Burns"
    },
    {
      "date": "2014-04-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/t2msi7/intro---4-22-14",
        "http://thecolbertreport.cc.com/videos/1j1m90/postage-stamp-for-harvey-milk",
        "http://thecolbertreport.cc.com/videos/0bsy88/better-know-a-district---california-s-29th",
        "http://thecolbertreport.cc.com/videos/kg42wy/bad-news-for-ethanol-on-earth-day",
        "http://thecolbertreport.cc.com/videos/yeczpa/george-will",
        "http://thecolbertreport.cc.com/videos/0b7ymc/sign-off---goodnight"
      ],
      "guest": "George Will"
    },
    {
      "date": "2014-04-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vnbuc3/intro---4-23-14",
        "http://thecolbertreport.cc.com/videos/8l716g/canada-s-booming-middle-class",
        "http://thecolbertreport.cc.com/videos/tn3469/sport-report---snacks-for-students---cockfighting",
        "http://thecolbertreport.cc.com/videos/lz21l6/america-s-lime-crisis",
        "http://thecolbertreport.cc.com/videos/g5cgj8/john-calipari",
        "http://thecolbertreport.cc.com/videos/6glbo4/sign-off---goodnight"
      ],
      "guest": "John Calipari"
    },
    {
      "date": "2014-04-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2c27q9/supreme-court-affirmative-action-ruling",
        "http://thecolbertreport.cc.com/videos/ehanpl/the-ballad-of-cliven-bundy",
        "http://thecolbertreport.cc.com/videos/5mf7zk/phyllis-schlafly-vs--equal-pay-for-women",
        "http://thecolbertreport.cc.com/videos/ufdzm1/george-saunders",
        "http://thecolbertreport.cc.com/videos/vtuwb7/sign-off---country-boy"
      ],
      "guest": "George Saunders"
    },
    {
      "date": "2014-04-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6fq0xa/popechella",
        "http://thecolbertreport.cc.com/videos/yhq2cw/preventable-diseases-on-the-rise",
        "http://thecolbertreport.cc.com/videos/svsc0q/preventable-diseases-on-the-rise---paul-offit",
        "http://thecolbertreport.cc.com/videos/5my1ja/outrage-over-obama-s-bowing",
        "http://thecolbertreport.cc.com/videos/i1lidr/michael-mcfaul",
        "http://thecolbertreport.cc.com/videos/gu3d7a/sign-off----deadly-choices-"
      ],
      "guest": "Michael McFaul"
    },
    {
      "date": "2014-04-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cxn6h3/intro---4-29-14",
        "http://thecolbertreport.cc.com/videos/jfz395/donald-sterling-s-racist-comments",
        "http://thecolbertreport.cc.com/videos/td7npw/tip-wag---j-j--abrams---u-s--congress",
        "http://thecolbertreport.cc.com/videos/8pyjlg/clemency-push-for-drug-convicts",
        "http://thecolbertreport.cc.com/videos/eyae6k/robert-rodriguez",
        "http://thecolbertreport.cc.com/videos/11mf9t/sign-off---goodnight"
      ],
      "guest": "Robert Rodriguez"
    },
    {
      "date": "2014-04-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kdwdgq/intro---4-30-14",
        "http://thecolbertreport.cc.com/videos/6lmqu6/president-assad-s-reelection-bid",
        "http://thecolbertreport.cc.com/videos/so1kau/republican-advantage-in-the-2014-midterms",
        "http://thecolbertreport.cc.com/videos/2nuw76/republican-advantage-in-the-2014-midterms---clay-aiken",
        "http://thecolbertreport.cc.com/videos/tfpj0x/america-s-first-lesbian-throuple",
        "http://thecolbertreport.cc.com/videos/fs6gac/audra-mcdonald"
      ],
      "guest": "Audra McDonald"
    },
    {
      "date": "2014-05-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/798k8c/-watters--world-",
        "http://thecolbertreport.cc.com/videos/1e524e/-watters--world----tad-s-turf",
        "http://thecolbertreport.cc.com/videos/zbjl95/cnn-s-endless-wait-for-flight-370-news",
        "http://thecolbertreport.cc.com/videos/hji3d3/saul-williams",
        "http://thecolbertreport.cc.com/videos/ie7s2m/saul-williams----amethyst-rocks-"
      ],
      "guest": "Saul Williams"
    },
    {
      "date": "2014-05-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/unhuhc/intro---5-5-14",
        "http://thecolbertreport.cc.com/videos/oxvwlw/nancy-pelosi-s-cinco-de-mayo-celebration",
        "http://thecolbertreport.cc.com/videos/0hu2aq/better-know-a-district---virginia-s-3rd",
        "http://thecolbertreport.cc.com/videos/fo52kn/kareem-abdul-jabbar-on-racism-and-ghosts",
        "http://thecolbertreport.cc.com/videos/c0s4ec/edward-o--wilson",
        "http://thecolbertreport.cc.com/videos/4tegd5/sign-off---goodnight"
      ],
      "guest": "Edward O. Wilson"
    },
    {
      "date": "2014-05-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/pnqv06/intro---5-6-14",
        "http://thecolbertreport.cc.com/videos/khlwzq/rand-paul-s-derby-date-with-rupert-murdoch",
        "http://thecolbertreport.cc.com/videos/s4me1v/nra-annual-meeting---guns-everywhere-in-georgia",
        "http://thecolbertreport.cc.com/videos/zekn1k/satanic-monument-for-the-oklahoma-state-house",
        "http://thecolbertreport.cc.com/videos/iihdkg/bette-midler",
        "http://thecolbertreport.cc.com/videos/n572qd/sign-off---nightcap"
      ],
      "guest": "Bette Midler"
    },
    {
      "date": "2014-05-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1ztozi/intro---5-7-14",
        "http://thecolbertreport.cc.com/videos/p4t1a2/vibrant-constipation-pill",
        "http://thecolbertreport.cc.com/videos/ywt77c/tip-wag---herald-embroidery--bug-scientists---dana-perino",
        "http://thecolbertreport.cc.com/videos/2u61x6/ukraine-in-the-membrane",
        "http://thecolbertreport.cc.com/videos/uz2nio/david-remnick",
        "http://thecolbertreport.cc.com/videos/q5zpsy/sign-off---goodnight"
      ],
      "guest": "David Remnick"
    },
    {
      "date": "2014-05-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/84cvwk/exclusive---better-know-a-challenger---florida-s-3rd---jake-rush",
        "http://thecolbertreport.cc.com/videos/1u7a5d/vampire-for-congress-in-florida",
        "http://thecolbertreport.cc.com/videos/vkcose/better-know-a-challenger---florida-s-3rd---jake-rush",
        "http://thecolbertreport.cc.com/videos/8jno3s/stu-varney-among-the-common-people",
        "http://thecolbertreport.cc.com/videos/m2n3c9/ellen-page",
        "http://thecolbertreport.cc.com/videos/u05pdf/sign-off---spinning-top"
      ],
      "guest": "Ellen Page"
    },
    {
      "date": "2014-05-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nnz78u/michael-sam-s-nfl-draft-kiss",
        "http://thecolbertreport.cc.com/videos/g2hf60/stephen-colbert-s-bats--t-serious---monica-lewinsky-s-conveniently-timed-essay",
        "http://thecolbertreport.cc.com/videos/2j80wh/glenn-greenwald-pt--1",
        "http://thecolbertreport.cc.com/videos/31s76v/glenn-greenwald-pt--2",
        "http://thecolbertreport.cc.com/videos/xovmc1/sign-off---penalty-whistle"
      ],
      "guest": "Glenn Greenwald"
    },
    {
      "date": "2014-05-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wn13ym/pope-francis-s-crusade-against-capitalism",
        "http://thecolbertreport.cc.com/videos/vmje6p/-bringbackourgirls",
        "http://thecolbertreport.cc.com/videos/2rgt3x/-bringbackourgirls---rosemary-nyirumbe",
        "http://thecolbertreport.cc.com/videos/jrmo9v/koch-brothers-vs--the-columbus-zoo",
        "http://thecolbertreport.cc.com/videos/s46r2u/the-black-keys",
        "http://thecolbertreport.cc.com/videos/7bxzr7/sign-off---sisters-united-bags"
      ],
      "guest": "The Black Keys"
    },
    {
      "date": "2014-05-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mwq7dh/intro---5-14-14",
        "http://thecolbertreport.cc.com/videos/5ob1j2/pope-francis-on-baptizing-martians",
        "http://thecolbertreport.cc.com/videos/k6jlhl/the-word---f--k-it",
        "http://thecolbertreport.cc.com/videos/4a4ahs/amazon-s-audacious-photography-patent",
        "http://thecolbertreport.cc.com/videos/hffa7o/keri-russell",
        "http://thecolbertreport.cc.com/videos/2b3fgm/sign-off---goodnight"
      ],
      "guest": "Keri Russell"
    },
    {
      "date": "2014-05-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bvzi2n/vladimir-putin-s-space-station-ban",
        "http://thecolbertreport.cc.com/videos/pb1byh/karl-rove-on-hillary-clinton-s-health",
        "http://thecolbertreport.cc.com/videos/o2wt62/morality-lessons-for-robots",
        "http://thecolbertreport.cc.com/videos/lmgmhg/thomas-friedman",
        "http://thecolbertreport.cc.com/videos/z8ndeb/sign-off---mirror"
      ],
      "guest": "Thomas Friedman"
    },
    {
      "date": "2014-05-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/r5l7zc/intro---5-19-14",
        "http://thecolbertreport.cc.com/videos/el90zp/co-ed-lab-rats",
        "http://thecolbertreport.cc.com/videos/7oum5k/elizabeth-warren-vs--wall-street",
        "http://thecolbertreport.cc.com/videos/7sujj3/colbert-report-consumer-alert---jerky-blaster",
        "http://thecolbertreport.cc.com/videos/79q9bs/elizabeth-warren",
        "http://thecolbertreport.cc.com/videos/igbz3e/sign-off---goodnight"
      ],
      "guest": "Elizabeth Warren"
    },
    {
      "date": "2014-05-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oimxrw/china-s-cyber-spies",
        "http://thecolbertreport.cc.com/videos/zfayee/the-gop-s-gloves-off-approach-to-hillary-clinton",
        "http://thecolbertreport.cc.com/videos/dbim9j/google-and-the-right-to-be-forgotten",
        "http://thecolbertreport.cc.com/videos/zopbx2/matthew-weiner",
        "http://thecolbertreport.cc.com/videos/g4ax73/sign-off---goodbye-kiss"
      ],
      "guest": "Matt Weiner"
    },
    {
      "date": "2014-05-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6uijkp/tea-party-defeat-in-the-gop-primaries",
        "http://thecolbertreport.cc.com/videos/sk5fyk/idaho-s-bizarre-gubernatorial-debate",
        "http://thecolbertreport.cc.com/videos/zn3est/mers-virus-in-america",
        "http://thecolbertreport.cc.com/videos/xnk3xl/patrick-stewart",
        "http://thecolbertreport.cc.com/videos/8pgnos/sign-off---goodnight"
      ],
      "guest": "Patrick Stewart"
    },
    {
      "date": "2014-05-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7q56w3/intro---5-22-14",
        "http://thecolbertreport.cc.com/videos/ouzxbu/va-hospital-outrage",
        "http://thecolbertreport.cc.com/videos/s6rmi7/va-hospital-outrage---paul-rieckhoff",
        "http://thecolbertreport.cc.com/videos/74fcac/marco-rubio-s-hazy-marijuana-history",
        "http://thecolbertreport.cc.com/videos/b40eb0/ray-mabus",
        "http://thecolbertreport.cc.com/videos/764wvl/sign-off---goodnight-and-good-week"
      ],
      "guest": "Ray Mabus"
    },
    {
      "date": "2014-06-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xtbsgf/obama-s-prisoner-exchange-with-the-taliban",
        "http://thecolbertreport.cc.com/videos/i8fthl/difference-makers---doug-varrieur",
        "http://thecolbertreport.cc.com/videos/oq97o4/thomas-piketty-vs--billionaire-heroes",
        "http://thecolbertreport.cc.com/videos/e301vf/thomas-piketty",
        "http://thecolbertreport.cc.com/videos/lyrlrc/sign-off---goatee"
      ],
      "guest": "Thomas Piketty"
    },
    {
      "date": "2014-06-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/o4pou7/intro---6-3-14",
        "http://thecolbertreport.cc.com/videos/u6nqsd/open-carry-backlash",
        "http://thecolbertreport.cc.com/videos/57iigb/obama-s-global-warming-initiative",
        "http://thecolbertreport.cc.com/videos/ifxi76/obama-s-global-warming-initiative---dan-esty",
        "http://thecolbertreport.cc.com/videos/vf38fj/medicare-coverage-for-sex-change-surgery",
        "http://thecolbertreport.cc.com/videos/ttwu42/morgan-freeman",
        "http://thecolbertreport.cc.com/videos/qmezm2/sign-off---goodnight"
      ],
      "guest": "Morgan Freeman"
    },
    {
      "date": "2014-06-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/yuxdmx/the-perils-of-girly-hurricanes",
        "http://thecolbertreport.cc.com/videos/ukf9gv/amazon-vs--hachette",
        "http://thecolbertreport.cc.com/videos/t1nxwu/amazon-vs--hachette---sherman-alexie",
        "http://thecolbertreport.cc.com/videos/w5wvxu/the-colbert-report-s-unintended-educational-value",
        "http://thecolbertreport.cc.com/videos/olnbg3/jonah-hill",
        "http://thecolbertreport.cc.com/videos/k89vi0/sign-off----california-"
      ],
      "guest": "Jonah Hill"
    },
    {
      "date": "2014-06-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7fyrr9/intro---6-5-14",
        "http://thecolbertreport.cc.com/videos/hfogr3/bergdghazi",
        "http://thecolbertreport.cc.com/videos/2408x6/sport-report---mushroom-sports-drink--nfl-pill-pushers---rio-de-janeiro-s-olympic-problems",
        "http://thecolbertreport.cc.com/videos/q8dzb2/the-drudge-report-on-hillary-clinton-s--walker-",
        "http://thecolbertreport.cc.com/videos/muek3m/chrissie-hynde"
      ],
      "guest": "Chrissie Hynde"
    },
    {
      "date": "2014-06-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tpxhoo/scott-fistler-s--cesar-chavez--strategy",
        "http://thecolbertreport.cc.com/videos/7uozsl/fox-news-s-war-on-bowe-bergdahl",
        "http://thecolbertreport.cc.com/videos/uyh5xo/craziest-f--king-thing-i-ve-ever-heard---vincent-van-gogh-s-reanimated-ear",
        "http://thecolbertreport.cc.com/videos/allxmi/esther-perel",
        "http://thecolbertreport.cc.com/videos/x78nyg/sign-off---goodnight"
      ],
      "guest": "Esther Perel"
    },
    {
      "date": "2014-06-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gdbreq/turing-test-breakthrough",
        "http://thecolbertreport.cc.com/videos/p8wqsa/the-enemy-within---bina-the-activist-android",
        "http://thecolbertreport.cc.com/videos/n30nzb/sport-report---swimming-pools-for-football-fans---governors--hockey-wager",
        "http://thecolbertreport.cc.com/videos/2lc1uv/john-waters",
        "http://thecolbertreport.cc.com/videos/dxz774/sign-off---goodnight"
      ],
      "guest": "John Waters"
    },
    {
      "date": "2014-06-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/s8uwwo/intro---6-11-14",
        "http://thecolbertreport.cc.com/videos/1d3kl4/eric-cantor-s-shocking-defeat",
        "http://thecolbertreport.cc.com/videos/m87g43/the-word---debt-or-prison",
        "http://thecolbertreport.cc.com/videos/2kgoki/rob-rhinehart",
        "http://thecolbertreport.cc.com/videos/6v0f1z/sign-off---spiked-drink"
      ],
      "guest": "Rob Rhinehart"
    },
    {
      "date": "2014-06-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/iywdca/amazon-s-scorched-earth-tactics-and-edan-lepucki-s--california-",
        "http://thecolbertreport.cc.com/videos/4n51kp/tip-wag---ted-cruz---led-zeppelin",
        "http://thecolbertreport.cc.com/videos/0z44gm/sport-report---team-usa-vs--the-group-of-death---hans-beinholtz-on-the-world-cup",
        "http://thecolbertreport.cc.com/videos/sqbqhw/james-webb",
        "http://thecolbertreport.cc.com/videos/pjws58/sign-off---necktie"
      ],
      "guest": "James Webb"
    },
    {
      "date": "2014-06-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6mpwy3/isis-militants-in-iraq",
        "http://thecolbertreport.cc.com/videos/wlnavl/isis-militants-in-iraq---ben-van-heuvelen",
        "http://thecolbertreport.cc.com/videos/eozrlj/racial-perceptions-and-economic-stress",
        "http://thecolbertreport.cc.com/videos/n3etz1/ta-nehisi-coates",
        "http://thecolbertreport.cc.com/videos/200z2y/sign-off---hand-mirror"
      ],
      "guest": "Ta-Nehisi Coates"
    },
    {
      "date": "2014-06-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ddo89r/world-cup-victory-for-team-usa",
        "http://thecolbertreport.cc.com/videos/xoa360/the-word---a-darker-shade-of-pale",
        "http://thecolbertreport.cc.com/videos/qpaogb/majority-support-for-same-sex-marriage",
        "http://thecolbertreport.cc.com/videos/8buw4s/david-boies---theodore-b--olson",
        "http://thecolbertreport.cc.com/videos/4gkwgg/sign-off---foam-finger"
      ],
      "guest": "David Boies &amp; Theodore B. Olson"
    },
    {
      "date": "2014-06-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/exebzv/intro---6-18-14",
        "http://thecolbertreport.cc.com/videos/hgs925/arrest-of-benghazi-terror-mastermind",
        "http://thecolbertreport.cc.com/videos/a1yfmv/hillary-clinton-vs--the-rnc-squirrel",
        "http://thecolbertreport.cc.com/videos/qj2x93/thad-cochran-on-doing-indecent-things-with-animals",
        "http://thecolbertreport.cc.com/videos/3ul9zn/katty-kay---claire-shipman",
        "http://thecolbertreport.cc.com/videos/och071/sign-off---goodnight"
      ],
      "guest": "Katty Kay &amp; Claire Shipman"
    },
    {
      "date": "2014-06-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/gt99v3/the-iraq-pack",
        "http://thecolbertreport.cc.com/videos/445utq/thought-for-food---domino-s-smart-slice---doritos-jacked",
        "http://thecolbertreport.cc.com/videos/cbr3yz/-yo--smartphone-app",
        "http://thecolbertreport.cc.com/videos/3abzv4/jay-carney",
        "http://thecolbertreport.cc.com/videos/h0b8ou/sign-off---goodnight"
      ],
      "guest": "Jay Carney"
    },
    {
      "date": "2014-06-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7bqhfd/team-usa-s-tragic-tie-with-portugal",
        "http://thecolbertreport.cc.com/videos/k8orr2/obama-s-response-to-isis-in-iraq---mark-mazzetti",
        "http://thecolbertreport.cc.com/videos/72elnv/jeremy-meeks-s-handsome-mug-shot",
        "http://thecolbertreport.cc.com/videos/07oysy/john-green",
        "http://thecolbertreport.cc.com/videos/mwnvtk/sign-off---goodnight"
      ],
      "guest": "John Green"
    },
    {
      "date": "2014-06-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tmjbzp/intro---6-24-14",
        "http://thecolbertreport.cc.com/videos/ee0zj7/isis-invades-hashtagistan",
        "http://thecolbertreport.cc.com/videos/bveu0w/tip-wag---fda---ben---jerry-s",
        "http://thecolbertreport.cc.com/videos/bu43e8/new-york-s-ban-on-tiger-selfies",
        "http://thecolbertreport.cc.com/videos/bo739z/edie-falco",
        "http://thecolbertreport.cc.com/videos/hgf6rh/sign-off---goodnight"
      ],
      "guest": "Edie Falco"
    },
    {
      "date": "2014-06-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/rpnj8s/obama-s-chipotle-blunder",
        "http://thecolbertreport.cc.com/videos/glsyx9/stephen-colbert-s-bats--t-serious---child-immigrant-intrigue",
        "http://thecolbertreport.cc.com/videos/nx3ix1/stephen-colbert-s-bats--t-serious---child-immigrant-intrigue---john-burnett",
        "http://thecolbertreport.cc.com/videos/rki77c/primary-victory-for-thad-cochran",
        "http://thecolbertreport.cc.com/videos/rn2gd8/eleanor-holmes-norton",
        "http://thecolbertreport.cc.com/videos/q6den3/sign-off---goodnight"
      ],
      "guest": "Rep. Eleanor Holmes Norton"
    },
    {
      "date": "2014-06-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/suqg0f/stephen-colbert-s-bats--t-serious---the-vast-government-soccer-conspiracy",
        "http://thecolbertreport.cc.com/videos/autzis/tip-wag---north-carolina-state-legislature---cereal-manufacturers",
        "http://thecolbertreport.cc.com/videos/jrdas9/paul-rudd-pt--1",
        "http://thecolbertreport.cc.com/videos/rb9bo7/paul-rudd-pt--2",
        "http://thecolbertreport.cc.com/videos/8vp2bp/sign-off---so-long-for-two-weeks"
      ],
      "guest": "Paul Rudd"
    },
    {
      "date": "2014-07-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fy2b19/intro---7-14-14",
        "http://thecolbertreport.cc.com/videos/9cspva/world-cup-recap",
        "http://thecolbertreport.cc.com/videos/mlyvqh/thank-you--racism---boehner-v--obama",
        "http://thecolbertreport.cc.com/videos/xivy3m/hobby-lobby-case",
        "http://thecolbertreport.cc.com/videos/9nzwjt/vessyl-digital-cup",
        "http://thecolbertreport.cc.com/videos/6cvwe6/jad-abumrad---robert-krulwich",
        "http://thecolbertreport.cc.com/videos/rpfaco/sign-off---goodnight"
      ],
      "guest": "Jad Abumrad, Robert Krulwich"
    },
    {
      "date": "2014-07-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/nnucn6/obama-s-senioritis",
        "http://thecolbertreport.cc.com/videos/f0uh68/threatdown---all-bear-edition",
        "http://thecolbertreport.cc.com/videos/08a2dg/vint-cerf-pt--1",
        "http://thecolbertreport.cc.com/videos/x9hnxr/vint-cerf-pt--2",
        "http://thecolbertreport.cc.com/videos/dixoxg/sign-off---goodnight"
      ],
      "guest": "Vint Cerf"
    },
    {
      "date": "2014-07-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/anklfa/intro---7-16-14",
        "http://thecolbertreport.cc.com/videos/53n0nf/conservative-contempt-for-bill-de-blasio",
        "http://thecolbertreport.cc.com/videos/cbs1n7/rick-perry-s-makeover---uncensored",
        "http://thecolbertreport.cc.com/videos/1flr4c/filling-captain-america-s-shoes---joe-quesada",
        "http://thecolbertreport.cc.com/videos/ypm476/bill-de-blasio",
        "http://thecolbertreport.cc.com/videos/slmbh6/sign-off----captain-america-"
      ],
      "guest": "Mayor Bill de Blasio"
    },
    {
      "date": "2014-07-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ket4ms/malaysia-airlines-crash---hamas-israel-violence",
        "http://thecolbertreport.cc.com/videos/z3gi0q/questionable-compassion-for-child-immigrants",
        "http://thecolbertreport.cc.com/videos/bfvmgh/coal-rolling",
        "http://thecolbertreport.cc.com/videos/70ezhu/steven-m--wise",
        "http://thecolbertreport.cc.com/videos/n00bpi/sign-off---soot-blast"
      ],
      "guest": "Steven Wise"
    },
    {
      "date": "2014-07-21",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qimhj6/intro---7-21-14",
        "http://thecolbertreport.cc.com/videos/n71mkf/world-news-wrap-up",
        "http://thecolbertreport.cc.com/videos/8e5dyu/colbert-nation-vs--amazon---edan-lepucki",
        "http://thecolbertreport.cc.com/videos/egw3ua/nancy-pelosi-pt--1",
        "http://thecolbertreport.cc.com/videos/q8mj7b/nancy-pelosi-pt--2",
        "http://thecolbertreport.cc.com/videos/98szje/sign-off----sweetness--9-"
      ],
      "guest": "Rep. Nancy Pelosi"
    },
    {
      "date": "2014-07-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/a6s2qu/rep--steve-pearce-s-fact-finding-mission-in-central-america",
        "http://thecolbertreport.cc.com/videos/d24npe/rising-calls-for-obama-s-impeachment",
        "http://thecolbertreport.cc.com/videos/stx9ln/rising-calls-for-obama-s-impeachment---p-k--winsome",
        "http://thecolbertreport.cc.com/videos/qf023x/rory-mcilroy-and-caroline-wozniacki-s-post-breakup-triumph",
        "http://thecolbertreport.cc.com/videos/1872w0/julia-ioffe",
        "http://thecolbertreport.cc.com/videos/rxjlpc/sign-off---p-k--winsome"
      ],
      "guest": "Julia Ioffe"
    },
    {
      "date": "2014-07-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/74ly7x/housing-crisis-for-child-immigrants",
        "http://thecolbertreport.cc.com/videos/w0dhco/six-californias",
        "http://thecolbertreport.cc.com/videos/rmgh1u/six-californias---tim-draper",
        "http://thecolbertreport.cc.com/videos/qb2d4f/lowe-s-vs--veterans-affairs",
        "http://thecolbertreport.cc.com/videos/a368r9/mary-mazzio---oscar-vazquez",
        "http://thecolbertreport.cc.com/videos/8nsg9g/sign-off---goodnight"
      ],
      "guest": "Mary Mazzio, Oscar Vazquez"
    },
    {
      "date": "2014-07-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/9bfzta/darth-vader-for-president",
        "http://thecolbertreport.cc.com/videos/br4k5m/tip-wag----true-blood----washington--d-c---court-of-appeals",
        "http://thecolbertreport.cc.com/videos/o26y1r/elon-musk-pt--1",
        "http://thecolbertreport.cc.com/videos/s4aaoq/elon-musk-pt--2",
        "http://thecolbertreport.cc.com/videos/baab8l/exclusive---elon-musk-discusses-mars",
        "http://thecolbertreport.cc.com/videos/9pmgk5/sign-off---goodnight"
      ],
      "guest": "Elon Musk"
    },
    {
      "date": "2014-07-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/99fqm5/magical-afternoon-at-comic-con",
        "http://thecolbertreport.cc.com/videos/yxerhp/the-word---see-no-equal",
        "http://thecolbertreport.cc.com/videos/c8gyzb/-kim-kardashian--hollywood--game",
        "http://thecolbertreport.cc.com/videos/me3jxh/beck"
      ],
      "guest": "Beck"
    },
    {
      "date": "2014-07-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/go3xsz/stephen-colbert-s-i-need-a-drink",
        "http://thecolbertreport.cc.com/videos/zo7j8y/the-sarah-palin-channel",
        "http://thecolbertreport.cc.com/videos/oeurov/jon-batiste-and-stay-human",
        "http://thecolbertreport.cc.com/videos/84mh53/sign-off---jon-batiste-and-stay-human"
      ],
      "guest": "Jon Batiste &amp; Stay Human"
    },
    {
      "date": "2014-07-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/vy7myr/orlando-bloom-s-altercation-with-justin-bieber",
        "http://thecolbertreport.cc.com/videos/mfm78m/corporate-inversions",
        "http://thecolbertreport.cc.com/videos/gv7xvj/corporate-inversions---allan-sloan",
        "http://thecolbertreport.cc.com/videos/psbsuw/naked-tv",
        "http://thecolbertreport.cc.com/videos/lb70bp/james-franco",
        "http://thecolbertreport.cc.com/videos/n2673s/sign-off---goodnight"
      ],
      "guest": "James Franco"
    },
    {
      "date": "2014-07-31",
      "videos": [
        "http://thecolbertreport.cc.com/videos/dwf82q/women-on-american-currency",
        "http://thecolbertreport.cc.com/videos/cruj3s/the-conflict-over-covering-the-conflict-in-gaza",
        "http://thecolbertreport.cc.com/videos/m4juon/tip-wag---beelzebub---nasa",
        "http://thecolbertreport.cc.com/videos/2mpwlv/campbell-brown",
        "http://thecolbertreport.cc.com/videos/26ag1q/sign-off---monitoring-system"
      ],
      "guest": "Campbell Brown"
    },
    {
      "date": "2014-08-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zcyj0l/40th-anniversary-of-nixon-s-resignation",
        "http://thecolbertreport.cc.com/videos/9hxmyy/a-nation-betrayed---a-fond-look-back---74",
        "http://thecolbertreport.cc.com/videos/c505xx/pat-buchanan",
        "http://thecolbertreport.cc.com/videos/ecplh0/john-w--dean",
        "http://thecolbertreport.cc.com/videos/jg7vda/sign-off---retrospectacular",
        "http://thecolbertreport.cc.com/videos/2kctj0/exclusive---pat-buchanan"
      ],
      "guest": "Pat Buchanan, John W. Dean"
    },
    {
      "date": "2014-08-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/eu8j9u/open-carry-trailblazers",
        "http://thecolbertreport.cc.com/videos/imtefo/-hard-choices----hillary-clinton",
        "http://thecolbertreport.cc.com/videos/8tvtmw/language-lessons-from-america-s-senior-citizens",
        "http://thecolbertreport.cc.com/videos/wb06vr/james-cameron",
        "http://thecolbertreport.cc.com/videos/tovjr3/sign-off---goodnight"
      ],
      "guest": "James Cameron"
    },
    {
      "date": "2014-08-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v652g6/smile-file---kim-jong-un-at-the-lube-factory",
        "http://thecolbertreport.cc.com/videos/mrntln/rand-paul-s-hasty-exit",
        "http://thecolbertreport.cc.com/videos/82nvgq/news-anchor-baby",
        "http://thecolbertreport.cc.com/videos/gn8hz0/michael-fassbender"
      ],
      "guest": "Michael Fassbender"
    },
    {
      "date": "2014-08-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2mrfmc/intro---8-7-14",
        "http://thecolbertreport.cc.com/videos/bmd26v/vladimir-putin-s-food-sanctions",
        "http://thecolbertreport.cc.com/videos/nm2atj/ebola-panic",
        "http://thecolbertreport.cc.com/videos/7a9ir7/the-in-box---blt-vs--club",
        "http://thecolbertreport.cc.com/videos/ddvyto/brian-chesky",
        "http://thecolbertreport.cc.com/videos/dc3x0v/sign-off---bourbon-and-chicken"
      ],
      "guest": "Brian Chesky"
    },
    {
      "date": "2014-08-26",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xfa2tc/intro---8-26-14",
        "http://thecolbertreport.cc.com/videos/pupsy6/better-know-a-district---ohio-s-11th---marcia-fudge-pt--1",
        "http://thecolbertreport.cc.com/videos/llmmz6/better-know-a-district---ohio-s-11th---marcia-fudge-pt--2",
        "http://thecolbertreport.cc.com/videos/crpfrn/jeff-bridges---lois-lowry",
        "http://thecolbertreport.cc.com/videos/30umwt/sign-off---goodnight"
      ],
      "guest": "Jeff Bridges, Lois Lowry"
    },
    {
      "date": "2014-08-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/12kfzg/intro---8-27-14",
        "http://thecolbertreport.cc.com/videos/4komvc/outrage-in-ferguson",
        "http://thecolbertreport.cc.com/videos/h1itnw/outrage-in-ferguson---a-national-conversation-on-race",
        "http://thecolbertreport.cc.com/videos/8ye61k/scrabble-s-updated-dictionary",
        "http://thecolbertreport.cc.com/videos/v6x4qn/michael-sheen",
        "http://thecolbertreport.cc.com/videos/4g1qgo/sign-off---welcome-baby-eva-"
      ],
      "guest": "Michael Sheen"
    },
    {
      "date": "2014-08-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/2x4lop/isis-panic",
        "http://thecolbertreport.cc.com/videos/yr7egy/isis-panic---announcing-reagan-s-return",
        "http://thecolbertreport.cc.com/videos/bac98y/vapshot-alcohol-vaporizer",
        "http://thecolbertreport.cc.com/videos/vmcz6o/jr",
        "http://thecolbertreport.cc.com/videos/q6o47f/sign-off---goodnight"
      ],
      "guest": "JR"
    },
    {
      "date": "2014-09-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7ohwx8/celebrity-nude-photo-scandal",
        "http://thecolbertreport.cc.com/videos/kc4ojp/police-militarization-in-america",
        "http://thecolbertreport.cc.com/videos/ukyqb3/police-militarization-in-america---norm-stamper",
        "http://thecolbertreport.cc.com/videos/xuzel5/good-news-for-sleep-deprived-teens",
        "http://thecolbertreport.cc.com/videos/sximkb/mandy-patinkin",
        "http://thecolbertreport.cc.com/videos/hpkdp0/sign-off---goodnight"
      ],
      "guest": "Mandy Patinkin"
    },
    {
      "date": "2014-09-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mrdb7o/intro---9-3-14",
        "http://thecolbertreport.cc.com/videos/v7c4zm/obama-s-isis-strategy",
        "http://thecolbertreport.cc.com/videos/2ccwew/obama-s-isis-strategy---frank-underwood",
        "http://thecolbertreport.cc.com/videos/r6svso/coach-class-conflicts",
        "http://thecolbertreport.cc.com/videos/ewijdy/randall-munroe",
        "http://thecolbertreport.cc.com/videos/cs2fnl/sign-off---goodnight"
      ],
      "guest": "Randall Munroe"
    },
    {
      "date": "2014-09-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/30z1ut/intro---9-4-14",
        "http://thecolbertreport.cc.com/videos/lo5wee/gays-in-the-st--patrick-s-day-parade",
        "http://thecolbertreport.cc.com/videos/zq72u5/the-midterm-round-up",
        "http://thecolbertreport.cc.com/videos/g7yyhh/al-qaeda-s-indian-franchise",
        "http://thecolbertreport.cc.com/videos/s4ds82/doris-kearns-goodwin",
        "http://thecolbertreport.cc.com/videos/fj6l1s/sign-off---ship-christening"
      ],
      "guest": "Doris Kearns Goodwin"
    },
    {
      "date": "2014-09-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g9wav3/intro---9-8-14",
        "http://thecolbertreport.cc.com/videos/dzxra6/william-and-kate-s-royal-pregnancy",
        "http://thecolbertreport.cc.com/videos/3160bg/waiting-forever-for-immigration-reform",
        "http://thecolbertreport.cc.com/videos/jz3rdd/pavlok-fitness-band",
        "http://thecolbertreport.cc.com/videos/23mu4v/john-lithgow",
        "http://thecolbertreport.cc.com/videos/a0x0bs/sign-off---goodnight"
      ],
      "guest": "John Lithgow"
    },
    {
      "date": "2014-09-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j5s4z1/apple-unveils-its-smartwatch",
        "http://thecolbertreport.cc.com/videos/s6gte9/the-midterm-round-up---the-gop-s-lady-problems",
        "http://thecolbertreport.cc.com/videos/hkfm7z/hometown-hero-town---detroit",
        "http://thecolbertreport.cc.com/videos/e4y7wx/jason-segel",
        "http://thecolbertreport.cc.com/videos/93zpki/sign-off---jason-segel-s-latest-award"
      ],
      "guest": "Jason Segel"
    },
    {
      "date": "2014-09-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u5vu07/intro---9-10-14",
        "http://thecolbertreport.cc.com/videos/p2b64y/obama-s-isis-speech",
        "http://thecolbertreport.cc.com/videos/lqm25y/dalai-lama-drama",
        "http://thecolbertreport.cc.com/videos/4pdz7v/tip-wag---nasa---trump-entertainment-resorts",
        "http://thecolbertreport.cc.com/videos/wn86jw/the-buypartisan-app",
        "http://thecolbertreport.cc.com/videos/hyx04c/henry-kissinger",
        "http://thecolbertreport.cc.com/videos/bipiaj/sign-off---goodnight"
      ],
      "guest": "Henry Kissinger"
    },
    {
      "date": "2014-09-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/oeusg2/this-country-is-at-war-",
        "http://thecolbertreport.cc.com/videos/li99ni/republicans--predictions-of-the-iraq-crisis",
        "http://thecolbertreport.cc.com/videos/wna0mw/global-warming-threatens-bird-species",
        "http://thecolbertreport.cc.com/videos/ndpng7/lonn-taylor",
        "http://thecolbertreport.cc.com/videos/cl9arb/sign-off---jim-cornelison-sings-the-national-anthem"
      ],
      "guest": "Lonn Taylor"
    },
    {
      "date": "2014-09-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/848h60/the-next-miss-america",
        "http://thecolbertreport.cc.com/videos/lmtq66/the-vote-for-scottish-independence",
        "http://thecolbertreport.cc.com/videos/exs7p5/the-vote-for-scottish-independence---matt-wells",
        "http://thecolbertreport.cc.com/videos/0txz3z/think-tank-corruption",
        "http://thecolbertreport.cc.com/videos/m1a8gr/mindy-kaling",
        "http://thecolbertreport.cc.com/videos/0j1qdb/sign-off"
      ],
      "guest": "Mindy Kaling"
    },
    {
      "date": "2014-09-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/60e467/intro---9-16-14",
        "http://thecolbertreport.cc.com/videos/0agoip/the-kinda-sorta-war-and-the-u-s--s-mysterious-allies",
        "http://thecolbertreport.cc.com/videos/mzktzw/wall-street-meddles-with-restaurant-chain",
        "http://thecolbertreport.cc.com/videos/oyl7ka/unlocking-the-truth"
      ],
      "guest": "Unlocking the Truth"
    },
    {
      "date": "2014-09-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6d36zv/caped-cash-cows",
        "http://thecolbertreport.cc.com/videos/zryrry/undercover-at-comic-con---prince-hawkcat",
        "http://thecolbertreport.cc.com/videos/d791f1/undercover-at-comic-con---stephen-s-movie-pitches",
        "http://thecolbertreport.cc.com/videos/xq6f9b/military-vehicles-for-public-schools",
        "http://thecolbertreport.cc.com/videos/arckqm/viggo-mortensen",
        "http://thecolbertreport.cc.com/videos/bfflr6/sign-off---aragorn"
      ],
      "guest": "Viggo Mortensen"
    },
    {
      "date": "2014-09-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hn1ueg/checky",
        "http://thecolbertreport.cc.com/videos/yupbhd/no-boots-on-the-ground-in-iraq",
        "http://thecolbertreport.cc.com/videos/wjga35/sean-hannity-s-defense-of-adrian-peterson",
        "http://thecolbertreport.cc.com/videos/rd6gao/terry-gilliam",
        "http://thecolbertreport.cc.com/videos/148dzu/sign-off---stuffed-elephant"
      ],
      "guest": "Terry Gilliam"
    },
    {
      "date": "2014-09-22",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uc4f7i/awol-afghan-soldiers",
        "http://thecolbertreport.cc.com/videos/01cyc2/tip-wag---climate-change-marchers---senators-on-reality-tv",
        "http://thecolbertreport.cc.com/videos/x58aop/charles-krauthammer-on-obama-s-mental-state",
        "http://thecolbertreport.cc.com/videos/jq352p/tweedy"
      ],
      "guest": "Tweedy"
    },
    {
      "date": "2014-09-23",
      "videos": [
        "http://thecolbertreport.cc.com/videos/j6xqew/u-s--airstrikes-in-syria",
        "http://thecolbertreport.cc.com/videos/ybvlae/better-know-a-district---california-s-2nd---jared-huffman",
        "http://thecolbertreport.cc.com/videos/b5ni29/the-russians-buy-pbr",
        "http://thecolbertreport.cc.com/videos/k5a58t/naomi-klein",
        "http://thecolbertreport.cc.com/videos/ksh5pr/sign-off---pbr"
      ],
      "guest": "Naomi Klein"
    },
    {
      "date": "2014-09-24",
      "videos": [
        "http://thecolbertreport.cc.com/videos/5mneco/atone-phone---jeff-tweedy-calls",
        "http://thecolbertreport.cc.com/videos/tw7sr5/obama-s-coffee-cup-salute"
      ],
      "guest": "Bill Cosby"
    },
    {
      "date": "2014-09-25",
      "videos": [
        "http://thecolbertreport.cc.com/videos/p49ls4/the-suspicious-death-of-staten-island-chuck",
        "http://thecolbertreport.cc.com/videos/0hjuki/intro---9-25-14",
        "http://thecolbertreport.cc.com/videos/tjmnw0/eric-holder-s-resignation",
        "http://thecolbertreport.cc.com/videos/7dpl33/bill-o-reilly-s-elite-strike-force",
        "http://thecolbertreport.cc.com/videos/0w775u/smile-file---the-u-a-e--s-first-female-fighter-pilot-vs---the-five----uncensored",
        "http://thecolbertreport.cc.com/videos/g36k7p/walter-mischel",
        "http://thecolbertreport.cc.com/videos/fhpqlq/sign-off---marshmallows"
      ],
      "guest": "Walter Mischel"
    },
    {
      "date": "2014-09-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6ythcp/obama-s-rip-off-of-bush",
        "http://thecolbertreport.cc.com/videos/eecxwy/hillary-clinton-and-the-grandmother-of-all-scandals",
        "http://thecolbertreport.cc.com/videos/6w3vad/kim-jong-un-s-massive-cheese-consumption",
        "http://thecolbertreport.cc.com/videos/ojmtk8/jamie-oliver",
        "http://thecolbertreport.cc.com/videos/z231mw/sign-off---cake-and-cheese"
      ],
      "guest": "Jamie Oliver"
    },
    {
      "date": "2014-09-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/6k6hq3/muslims-in-the-end-zone",
        "http://thecolbertreport.cc.com/videos/h1yge9/highlights-of-the-values-voter-summit",
        "http://thecolbertreport.cc.com/videos/8x6lww/the-benefits-of-pessimism---hans-beinholtz",
        "http://thecolbertreport.cc.com/videos/qofokt/jeffrey-tambor",
        "http://thecolbertreport.cc.com/videos/pnsz05/sign-off---goodnight"
      ],
      "guest": "Jeffrey Tambor"
    },
    {
      "date": "2014-10-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v6tds1/protests-in-hong-kong",
        "http://thecolbertreport.cc.com/videos/v51zzo/protests-in-hong-kong---louisa-lim",
        "http://thecolbertreport.cc.com/videos/zzbhqi/bill-o-reilly-takes-offense",
        "http://thecolbertreport.cc.com/videos/oviilh/mike-mullen",
        "http://thecolbertreport.cc.com/videos/5tiz1y/sign-off---goodnight",
        "http://thecolbertreport.cc.com/videos/8f6kuv/exclusive---mike-mullen-extended-interview"
      ],
      "guest": "Adm. Mike Mullen"
    },
    {
      "date": "2014-10-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jyghug/intro---10-2-14",
        "http://thecolbertreport.cc.com/videos/x6d5sz/deathpocalypse-now---ebola-in-america---50-states-of-grave",
        "http://thecolbertreport.cc.com/videos/hhhqqd/deathpocalypse-now---ebola-in-america---kent-sepkowitz",
        "http://thecolbertreport.cc.com/videos/e72awe/solitocity",
        "http://thecolbertreport.cc.com/videos/ye2fnr/lynn-sherr",
        "http://thecolbertreport.cc.com/videos/7nl6i5/sign-off---hand-sanitizer"
      ],
      "guest": "Lynn Sherr"
    },
    {
      "date": "2014-10-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/g5stw6/intro---10-6-14",
        "http://thecolbertreport.cc.com/videos/heaxbs/victory-for-gay-marriage---the-rise-of-amicus-briefs",
        "http://thecolbertreport.cc.com/videos/ssmvma/victory-for-gay-marriage---the-rise-of-amicus-briefs---allison-orr-larsen",
        "http://thecolbertreport.cc.com/videos/ayvbym/a-rare-correction---no-ebola-outbreak-in-the-u-s-",
        "http://thecolbertreport.cc.com/videos/fcax26/james-m--mcpherson",
        "http://thecolbertreport.cc.com/videos/bfwqfb/sign-off---goodnight"
      ],
      "guest": "James McPherson"
    },
    {
      "date": "2014-10-07",
      "videos": [
        "http://thecolbertreport.cc.com/videos/hhqgbw/ebolapalooza",
        "http://thecolbertreport.cc.com/videos/nx3ewk/better-know-a-district---illinois-s-8th---tammy-duckworth",
        "http://thecolbertreport.cc.com/videos/q2857u/cheating-death---pandemic-health",
        "http://thecolbertreport.cc.com/videos/7swpxt/leon-wieseltier",
        "http://thecolbertreport.cc.com/videos/rete59/sign-off---cigarette"
      ],
      "guest": "Leon Wieseltier"
    },
    {
      "date": "2014-10-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e50viy/intro---10-8-14",
        "http://thecolbertreport.cc.com/videos/khi8w0/john-boehner-vs--america-s-anti-gay-marriage-crusaders",
        "http://thecolbertreport.cc.com/videos/m899eo/naming-the-war-against-isis",
        "http://thecolbertreport.cc.com/videos/hzou6l/carol-burnett",
        "http://thecolbertreport.cc.com/videos/hcc5br/sign-off---ear-tug"
      ],
      "guest": "Carol Burnett"
    },
    {
      "date": "2014-10-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/blfnlw/exclusive---robert-plant----little-maggie-",
        "http://thecolbertreport.cc.com/videos/jdri4u/robert-plant----rainbow-",
        "http://thecolbertreport.cc.com/videos/tyc0sx/intro---10-9-14",
        "http://thecolbertreport.cc.com/videos/0gscic/columbus-day-under-attack",
        "http://thecolbertreport.cc.com/videos/hpfwm4/raining-vs--sprinkling",
        "http://thecolbertreport.cc.com/videos/xfjyum/republicans-are-people--too",
        "http://thecolbertreport.cc.com/videos/jfanx7/robert-plant",
        "http://thecolbertreport.cc.com/videos/o2y6sr/sign-off----lullaby-and----the-ceaseless-roar-"
      ],
      "guest": "Robert Plant"
    },
    {
      "date": "2014-10-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fhnqjo/midterms--014---detour-to-gridlock---an-exciting-thing-that-i-am-totally-interested-in",
        "http://thecolbertreport.cc.com/videos/8zip3j/intro---10-13-14",
        "http://thecolbertreport.cc.com/videos/sx2hh2/32-episodes-left-for-the-report",
        "http://thecolbertreport.cc.com/videos/fp4xfy/walter-isaacson",
        "http://thecolbertreport.cc.com/videos/f4t3xr/sign-off---quality-time-with-americone-dream",
        "http://thecolbertreport.cc.com/videos/bxbwj4/midterms--014---detour-to-gridlock---dennis-daugaard"
      ],
      "guest": "Walter Isaacson"
    },
    {
      "date": "2014-10-14",
      "videos": [
        "http://thecolbertreport.cc.com/videos/zg3zai/neil-young----who-s-gonna-stand-up---and-save-the-earth--",
        "http://thecolbertreport.cc.com/videos/wcjcgn/a-week-of-victories-for-gay-rights",
        "http://thecolbertreport.cc.com/videos/akzlpt/say-yes-to-rick-scott",
        "http://thecolbertreport.cc.com/videos/namhpu/neil-young",
        "http://thecolbertreport.cc.com/videos/veswmj/sign-off----special-deluxe-"
      ],
      "guest": "Neil Young"
    },
    {
      "date": "2014-10-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qw8rwv/who-s-attacking-me-now----larry-page",
        "http://thecolbertreport.cc.com/videos/q2u206/tip-wag---barack-obama---stan-lee",
        "http://thecolbertreport.cc.com/videos/xv3cdl/sean-hannity-s-question-of-the-day",
        "http://thecolbertreport.cc.com/videos/18x57e/justin-simien",
        "http://thecolbertreport.cc.com/videos/4tsbtt/sign-off---goodnight"
      ],
      "guest": "Justin Simien"
    },
    {
      "date": "2014-10-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/uebndp/abandoned-wmds-in-iraq",
        "http://thecolbertreport.cc.com/videos/aywapn/abandoned-wmds-in-iraq---c-j--chivers",
        "http://thecolbertreport.cc.com/videos/3o1uzs/rick-scott-and-charlie-crist-s-bizarre-debate",
        "http://thecolbertreport.cc.com/videos/z4umi5/william-deresiewicz",
        "http://thecolbertreport.cc.com/videos/xrvm7x/stephen-s-old-ipod"
      ],
      "guest": "Bill Deresiewicz"
    },
    {
      "date": "2014-10-27",
      "videos": [
        "http://thecolbertreport.cc.com/videos/e27u8w/intro---10-27-14",
        "http://thecolbertreport.cc.com/videos/8hjpi2/ebola-in-new-york",
        "http://thecolbertreport.cc.com/videos/whfeyg/louie-gohmert-on-gays-in-the-military",
        "http://thecolbertreport.cc.com/videos/jjpinj/meredith-vieira",
        "http://thecolbertreport.cc.com/videos/a0zbrf/sign-off---sundae"
      ],
      "guest": "Meredith Vieira"
    },
    {
      "date": "2014-10-28",
      "videos": [
        "http://thecolbertreport.cc.com/videos/xxvx4u/war-on-halloween---flaming-bags-of-government",
        "http://thecolbertreport.cc.com/videos/jxddq4/the-nra-vs--pennsylvania-s-pet-eating-ban",
        "http://thecolbertreport.cc.com/videos/6cj1fk/tom-corbett-s-photoshopped-diversity",
        "http://thecolbertreport.cc.com/videos/nzy3nz/sport-report---fall-experimental-football-league",
        "http://thecolbertreport.cc.com/videos/c7wjzg/michael-lewis",
        "http://thecolbertreport.cc.com/videos/64x2gg/sign-off---goodnight"
      ],
      "guest": "Michael Lewis"
    },
    {
      "date": "2014-10-29",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ladjef/gamergate",
        "http://thecolbertreport.cc.com/videos/wr7hqq/gamergate---anita-sarkeesian",
        "http://thecolbertreport.cc.com/videos/ll1e16/heroism-in-canada",
        "http://thecolbertreport.cc.com/videos/1h66nr/jill-lepore",
        "http://thecolbertreport.cc.com/videos/1fc6m9/sign-off---microphone"
      ],
      "guest": "Jill Lepore"
    },
    {
      "date": "2014-10-30",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qvw67z/intro---10-30-14",
        "http://thecolbertreport.cc.com/videos/hxvn8w/-america-again--in-paperback",
        "http://thecolbertreport.cc.com/videos/365nm9/america-s-midterm-indifference---george-takei",
        "http://thecolbertreport.cc.com/videos/cykxut/the-perils-of-anchor-zygotes",
        "http://thecolbertreport.cc.com/videos/tqbn3t/david-miliband",
        "http://thecolbertreport.cc.com/videos/4rgfpm/sign-off---goodnight"
      ],
      "guest": "David Miliband"
    },
    {
      "date": "2014-11-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/cvjwus/intro---11-3-14",
        "http://thecolbertreport.cc.com/videos/p6uab8/midterms--014---detour-to-gridlock---midterm-flyer-of-shame",
        "http://thecolbertreport.cc.com/videos/qmg04s/tip-wag---nazi-dairy-products--tim-cook---prostate-health-researchers",
        "http://thecolbertreport.cc.com/videos/rw2v1b/stephen-colbert-s-enchanted-princess-pixie-wedding-cake",
        "http://thecolbertreport.cc.com/videos/lffyr9/chuck-todd",
        "http://thecolbertreport.cc.com/videos/xrfsl8/sign-off---goodnight"
      ],
      "guest": "Chuck Todd"
    },
    {
      "date": "2014-11-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/1g0aji/midterms--014---detour-to-gridlock---live-coverage",
        "http://thecolbertreport.cc.com/videos/cmr0z4/midterms--014---detour-to-gridlock---mountains-of-midterm-madness",
        "http://thecolbertreport.cc.com/videos/w3muth/midterms--014---detour-to-gridlock---social-tracker-8700",
        "http://thecolbertreport.cc.com/videos/ekj19q/andrew-sullivan",
        "http://thecolbertreport.cc.com/videos/ckxbqk/sign-off---stephen-s-last-election-special"
      ],
      "guest": "Andrew Sullivan"
    },
    {
      "date": "2014-11-05",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c5okdm/intro---11-5-14",
        "http://thecolbertreport.cc.com/videos/ywqnjy/the-republicans-win-everything",
        "http://thecolbertreport.cc.com/videos/wq84nn/better-know-a-district---california-s-13th---barbara-lee",
        "http://thecolbertreport.cc.com/videos/7feu8t/legalized-marijuana-in-washington--d-c-",
        "http://thecolbertreport.cc.com/videos/w2qs7x/kirsten-gillibrand",
        "http://thecolbertreport.cc.com/videos/tno5bj/sign-off---goodnight"
      ],
      "guest": "Sen. Kirsten Gillibrand"
    },
    {
      "date": "2014-11-06",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kk2x1a/intro---11-6-14",
        "http://thecolbertreport.cc.com/videos/rtdlsr/busted-for-feeding-the-homeless",
        "http://thecolbertreport.cc.com/videos/3rw0tz/cheating-death---aging---women-s-health",
        "http://thecolbertreport.cc.com/videos/sc6mpp/the-republicans--inspiring-climate-change-message",
        "http://thecolbertreport.cc.com/videos/v06v9z/steven-johnson",
        "http://thecolbertreport.cc.com/videos/yzaj23/sign-off---goodnight"
      ],
      "guest": "Steven Johnson"
    },
    {
      "date": "2014-11-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/erbk9q/intro---11-10-14",
        "http://thecolbertreport.cc.com/videos/xnwueh/big-news-from-the-hermit-kingdom",
        "http://thecolbertreport.cc.com/videos/avadrz/the-word---it-s-a-trap-",
        "http://thecolbertreport.cc.com/videos/87vgoo/adventures-in-snackology",
        "http://thecolbertreport.cc.com/videos/sbmlul/andy-cohen",
        "http://thecolbertreport.cc.com/videos/7uog9s/sign-off---goodnight"
      ],
      "guest": "Andy Cohen"
    },
    {
      "date": "2014-11-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/mnkz05/intro---11-11-14",
        "http://thecolbertreport.cc.com/videos/wht7i8/uncertain-death-for-isis-s-leader",
        "http://thecolbertreport.cc.com/videos/thgfth/blowback-from-obama-s-visit-to-china",
        "http://thecolbertreport.cc.com/videos/uqricc/tip-wag---breitbart",
        "http://thecolbertreport.cc.com/videos/41fe1h/diane-von-furstenberg",
        "http://thecolbertreport.cc.com/videos/ncl44x/sign-off---cheerful-reflection"
      ],
      "guest": "Diane Von Furstenberg"
    },
    {
      "date": "2014-11-12",
      "videos": [
        "http://thecolbertreport.cc.com/videos/80wk4b/intro---11-12-14",
        "http://thecolbertreport.cc.com/videos/a1b4ph/new-york-city-s-rat-deficiency",
        "http://thecolbertreport.cc.com/videos/rn92gg/stephen-colbert-s-auto-robotic-fixation",
        "http://thecolbertreport.cc.com/videos/hhmb28/mr--smith-goes-to-the-state-legislature--then-later-possibly-washington---gordon-klingenschmitt",
        "http://thecolbertreport.cc.com/videos/6wtwlg/terence-tao",
        "http://thecolbertreport.cc.com/videos/a1eex6/sign-off---red-wine"
      ],
      "guest": "Terence Tao"
    },
    {
      "date": "2014-11-13",
      "videos": [
        "http://thecolbertreport.cc.com/videos/jtbvle/reforming-health-care-reform",
        "http://thecolbertreport.cc.com/videos/fe3wjm/reforming-health-care-reform---emily-bazelon",
        "http://thecolbertreport.cc.com/videos/cvq86c/gay-marriage-victory-in-south-carolina",
        "http://thecolbertreport.cc.com/videos/3pu1ey/jennifer-lawrence",
        "http://thecolbertreport.cc.com/videos/9aqahd/sign-off---goodnight"
      ],
      "guest": "Jennifer Lawrence"
    },
    {
      "date": "2014-11-17",
      "videos": [
        "http://thecolbertreport.cc.com/videos/qed7bp/bono-s-missing-luggage",
        "http://thecolbertreport.cc.com/videos/9dr12d/survival-tips-from--good-morning-america-",
        "http://thecolbertreport.cc.com/videos/7vjzxb/bernie-sanders-pt--1",
        "http://thecolbertreport.cc.com/videos/67tlr7/bernie-sanders-pt--2",
        "http://thecolbertreport.cc.com/videos/uqho5w/sign-off---goodnight"
      ],
      "guest": "Sen. Bernie Sanders"
    },
    {
      "date": "2014-11-18",
      "videos": [
        "http://thecolbertreport.cc.com/videos/fys4c2/intro---11-18-14",
        "http://thecolbertreport.cc.com/videos/ib2b3k/polar-plunge",
        "http://thecolbertreport.cc.com/videos/iw2iwg/obama-s-immigration-plan---esteban-colberto",
        "http://thecolbertreport.cc.com/videos/bbfckz/tip-wag---salvage-stores---maine",
        "http://thecolbertreport.cc.com/videos/o8su6y/eva-longoria",
        "http://thecolbertreport.cc.com/videos/vu8jpe/sign-off---goodnight"
      ],
      "guest": "Eva Longoria"
    },
    {
      "date": "2014-11-19",
      "videos": [
        "http://thecolbertreport.cc.com/videos/7mkltp/simulated-school-attack-in-florida",
        "http://thecolbertreport.cc.com/videos/dvppp6/difference-makers---the-free-keene-squad",
        "http://thecolbertreport.cc.com/videos/sdqbxm/black-friday-sale",
        "http://thecolbertreport.cc.com/videos/9yc4ry/toni-morrison",
        "http://thecolbertreport.cc.com/videos/y4ygag/sign-off---goodnight"
      ],
      "guest": "Toni Morrison"
    },
    {
      "date": "2014-11-20",
      "videos": [
        "http://thecolbertreport.cc.com/videos/01iemp/obama-s-executive-amnesty",
        "http://thecolbertreport.cc.com/videos/fie7ef/threatdown---declining-standards-of-sexiness--people-who-eat-chocolate---invaders-of-the-new-world",
        "http://thecolbertreport.cc.com/videos/e55wo4/jon-stewart-pt--1",
        "http://thecolbertreport.cc.com/videos/vbi9v5/jon-stewart-pt--2",
        "http://thecolbertreport.cc.com/videos/zwcggy/sign-off---goodnight"
      ],
      "guest": "Jon Stewart"
    },
    {
      "date": "2014-12-01",
      "videos": [
        "http://thecolbertreport.cc.com/videos/wmtufg/intro---12-1-14",
        "http://thecolbertreport.cc.com/videos/umsrnb/lightsaber-controversy",
        "http://thecolbertreport.cc.com/videos/wud7e1/ferguson-fallout-and-the-st--louis-rams",
        "http://thecolbertreport.cc.com/videos/d6xq50/jihadis-of-the-high-seas",
        "http://thecolbertreport.cc.com/videos/3h1qqa/john-mccain",
        "http://thecolbertreport.cc.com/videos/dnrg1a/sign-off---goodnight"
      ],
      "guest": "Sen. John McCain"
    },
    {
      "date": "2014-12-02",
      "videos": [
        "http://thecolbertreport.cc.com/videos/v8mtsf/intro---12-2-14",
        "http://thecolbertreport.cc.com/videos/hyqrm1/announcing-the-mr--colbert-goes-to-washington-special",
        "http://thecolbertreport.cc.com/videos/ethq4d/the-word---crook-and-ladder",
        "http://thecolbertreport.cc.com/videos/lje2l4/blitzkrieg-on-grinchitude---mistletoe-drones",
        "http://thecolbertreport.cc.com/videos/z0hz76/tony-bennett-and-lady-gaga"
      ],
      "guest": "Tony Bennett &amp; Lady Gaga"
    },
    {
      "date": "2014-12-03",
      "videos": [
        "http://thecolbertreport.cc.com/videos/c9s1cs/intro---12-3-14",
        "http://thecolbertreport.cc.com/videos/nxwili/the-no-social-security-for-nazis-act",
        "http://thecolbertreport.cc.com/videos/ziipwv/thought-for-food---fairlife-milk---pizza-hut-s-subconscious-menu",
        "http://thecolbertreport.cc.com/videos/fpdlpw/surprise-visit-from-amy-sedaris",
        "http://thecolbertreport.cc.com/videos/4r9o52/christopher-nolan",
        "http://thecolbertreport.cc.com/videos/nwo3n2/sign-off---goodnight"
      ],
      "guest": "Christopher Nolan"
    },
    {
      "date": "2014-12-04",
      "videos": [
        "http://thecolbertreport.cc.com/videos/ik935r/president-barack-obama-to-appear-on-the-report",
        "http://thecolbertreport.cc.com/videos/d5k5nz/outrage-over-eric-garner-decision",
        "http://thecolbertreport.cc.com/videos/pxune6/obama-s-bold-and-beautiful-ambassador-pick",
        "http://thecolbertreport.cc.com/videos/nucbbu/paul-farmer",
        "http://thecolbertreport.cc.com/videos/82d47r/sign-off---grimmy"
      ],
      "guest": "Dr. Paul Farmer"
    },
    {
      "date": "2014-12-08",
      "videos": [
        "http://thecolbertreport.cc.com/videos/u8bqev/mr--colbert-goes-to-washington",
        "http://thecolbertreport.cc.com/videos/cnlqbr/better-know-a-america---the-fightin--us",
        "http://thecolbertreport.cc.com/videos/88p9oh/the-word---president-barack-obama---to-health-in-a-handbasket",
        "http://thecolbertreport.cc.com/videos/i14vel/president-barack-obama-pt--1",
        "http://thecolbertreport.cc.com/videos/mpmtan/president-barack-obama-pt--2",
        "http://thecolbertreport.cc.com/videos/3mcn6y/sign-off---see-ya",
        "http://thecolbertreport.cc.com/videos/4mkbqz/exclusive---president-barack-obama-extended-interview"
      ],
      "guest": "President Barack Obama"
    },
    {
      "date": "2014-12-09",
      "videos": [
        "http://thecolbertreport.cc.com/videos/tgnj0t/-eaten-alive--outrage",
        "http://thecolbertreport.cc.com/videos/vd3icz/better-know-a-district---georgia-s-1st---reuniting-with-rep--jack-kingston",
        "http://thecolbertreport.cc.com/videos/pz35hw/who-s-honoring-me-now----entertainment-weekly",
        "http://thecolbertreport.cc.com/videos/2kz4pi/james-corden",
        "http://thecolbertreport.cc.com/videos/0frj3t/sign-off---sting"
      ],
      "guest": "James Corden"
    },
    {
      "date": "2014-12-10",
      "videos": [
        "http://thecolbertreport.cc.com/videos/kquici/cia-torture-report",
        "http://thecolbertreport.cc.com/videos/rlpjf5/cia-torture-report---pundits-defend-america",
        "http://thecolbertreport.cc.com/videos/z4grj8/cia-torture-report---tom-blanton",
        "http://thecolbertreport.cc.com/videos/8i6klx/sarah-koenig",
        "http://thecolbertreport.cc.com/videos/im3k81/sign-off---headphones"
      ],
      "guest": "Sarah Koenig"
    },
    {
      "date": "2014-12-11",
      "videos": [
        "http://thecolbertreport.cc.com/videos/anckrc/scott-walker-s-hanukkah-gaffe",
        "http://thecolbertreport.cc.com/videos/399enl/yahweh-or-no-way---epic-casting-controversy",
        "http://thecolbertreport.cc.com/videos/p9nk9d/announcing-the-colbert-report-raffle",
        "http://thecolbertreport.cc.com/videos/509747/smaug",
        "http://thecolbertreport.cc.com/videos/mfxigz/sign-off---aftermath-of-smaug"
      ],
      "guest": "\"The Hobbit: Battle of the Five Armies\" special"
    },
    {
      "date": "2014-12-15",
      "videos": [
        "http://thecolbertreport.cc.com/videos/bt8vk8/intro---12-15-14",
        "http://thecolbertreport.cc.com/videos/lwna3x/michele-bachmann-s-extreme-holiday-cheer",
        "http://thecolbertreport.cc.com/videos/0frisd/formidable-opponent---torture-report",
        "http://thecolbertreport.cc.com/videos/9xetgg/kim-jong-un-s-exclusive-name---sony-s-hack-attack",
        "http://thecolbertreport.cc.com/videos/j9u5in/seth-rogen",
        "http://thecolbertreport.cc.com/videos/bhrczk/sign-off---goodnight"
      ],
      "guest": "Seth Rogen"
    },
    {
      "date": "2014-12-16",
      "videos": [
        "http://thecolbertreport.cc.com/videos/arfo3o/jeb-bush-s-presidential-ambitions",
        "http://thecolbertreport.cc.com/videos/tnwzte/oil-war---jason-bordoff",
        "http://thecolbertreport.cc.com/videos/vd8ci4/colbert-platinum---holiday-gift-edition",
        "http://thecolbertreport.cc.com/videos/w5h8eb/kendrick-lamar",
        "http://thecolbertreport.cc.com/videos/pjrqsj/kendrick-lamar---debut-of-untitled-track"
      ],
      "guest": "Kendrick Lamar"
    }
  ]
}


working_folder = 'G:/Downloads'
for colbDate in testP['2014']:
    if 1:
        newfileResize = 'G:/downloads/The Colbert Report 2014/TheColbertReport '+colbDate['date']+'.mp4'
        if not os.path.exists(newfileResize):
            folderName = 'G:/downloads/The Colbert Report 2014/'+colbDate['date']
            try:
                os.mkdir(folderName)
            except:
                pass
            pos = 0
        
            for vid in colbDate['videos']:
                pos+=1
                done = False            
                while not done:
                    folderContents = os.listdir(folderName)                
                    for folderContent in folderContents:
                        if folderContent.startswith(str(pos)+' ') and (not folderContent.endswith('.part')):
                            done = True
                    
                    if not done:
                        cmd = os.path.join(working_folder,'youtube-dl.exe') + ' --no-continue -o "'+folderName+'/'+str(pos)+' %(title)s.%(ext)s" '+vid
                        subprocess.call(cmd,shell=True)
            vids = []
            for vid in os.listdir(folderName):
                if vid.endswith('.mp4'):
                    vids.append(os.path.join(folderName,vid))
            vids.sort()
            newfile = 'G:/downloads/The Colbert Report 2014/TheColbertReport '+colbDate['date']+'temp.mp4'
            
            if not os.path.exists(newfileResize):            
                cmd = r' -cat "' + r'" -cat "'.join(vids) + r'" -new "'+newfile+'"'
                exc = "G:/Downloads/mp4box.exe -tmp G:/temp/ " + cmd
                subprocess.call(exc,shell=True)
                cmd = "G:/Downloads/ffmpeg/bin/ffmpeg.exe -i \"" + newfile + "\" -vf scale=1024:576 \""+newfileResize+"\""
                subprocess.call(cmd,shell=True)
                while os.path.exists(newfile):
                    try:
                        os.remove(newfile)
                    except:
                        pass
            else:
                print 'file found ' + newfile
        
        
                 
     

