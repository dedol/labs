## Пример реализации паттернов Посредник и Адаптер
Имеется сайт для коммуникации пользователей (покупателя и продавца, реализованных классами Buyer и Seller). Пользователи могут отправлять друг другу сообщения с помощью мессенджера (класс Messenger), который выступает в роли посредника при общении. Также мессенджер может переводить сообщение от отправителя на язык получателя, таким образом, реализуется паттерн адаптер.