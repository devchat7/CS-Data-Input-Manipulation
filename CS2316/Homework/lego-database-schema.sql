drop database if exists lego;
create database lego;
use lego;

SET GLOBAL max_allowed_packet=1073741824;

create table colors(
    id int primary key,
    name varchar(100) not null,
    rgb varchar(50),
    is_trans boolean
);

create table themes(
    id int primary key,
    name varchar(50) not null,
    parent_id int
);

create table part_categories(
    id int primary key,
    name varchar(50)
);

create table sets(
    set_num varchar(50) primary key,
    name varchar(100) not null,
    year int,
    theme_id int,
    num_parts int,
    foreign key (theme_id) references themes(id)
);

create table inventories(
    id int primary key,
    version int,
    set_num varchar(50),
    foreign key (set_num) references sets(set_num)
);

create table inventory_sets(
    inventory_id int,
    set_num varchar(50),
    quantity int,
    primary key (inventory_id, set_num),
    foreign key (set_num) references sets(set_num),
    foreign key (inventory_id) references inventories(id)
);

create table parts(
    part_num varchar(50),
    name varchar(250) not null,
    part_cat_id int,
    primary key (part_num, name),
    foreign key (part_cat_id) references part_categories(id)
);

create table inventory_parts(
    row_id int,
    inventory_id int,
    part_num varchar(75),
    color_id int,
    quantity int,
    is_spare boolean,
    primary key (row_id),
    foreign key (inventory_id) references inventories(id),
    foreign key (color_id) references colors(id),
    foreign key (part_num) references parts(part_num)
);
