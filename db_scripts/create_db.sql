CREATE DATABASE szabadaba;

CREATE TABLE public."Image"
(
    id bigint NOT NULL,
    image bytea,
    format character varying(40),
    PRIMARY KEY (id)
);

ALTER TABLE public."Image"
    OWNER to postgres;