--
-- PostgreSQL database dump
--

-- Dumped from database version 17.2
-- Dumped by pg_dump version 17.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4972 (class 1262 OID 19609)
-- Name: Survey_Responses_10_30_24; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE "Survey_Responses_10_30_24" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';


\connect "Survey_Responses_10_30_24"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 226 (class 1259 OID 20268)
-- Name: EL Ratings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."EL Ratings" (
    "LogisticsID" integer NOT NULL,
    "Description" character varying NOT NULL
);


--
-- TOC entry 225 (class 1259 OID 20267)
-- Name: EL Ratings_LogisticsID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."EL Ratings_LogisticsID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4973 (class 0 OID 0)
-- Dependencies: 225
-- Name: EL Ratings_LogisticsID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."EL Ratings_LogisticsID_seq" OWNED BY public."EL Ratings"."LogisticsID";


--
-- TOC entry 220 (class 1259 OID 20241)
-- Name: Event Interest Ratings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Event Interest Ratings" (
    "RatingID" integer NOT NULL,
    "Description" character varying NOT NULL
);


--
-- TOC entry 219 (class 1259 OID 20240)
-- Name: Event Interest Ratings_RatingID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Event Interest Ratings_RatingID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4974 (class 0 OID 0)
-- Dependencies: 219
-- Name: Event Interest Ratings_RatingID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Event Interest Ratings_RatingID_seq" OWNED BY public."Event Interest Ratings"."RatingID";


--
-- TOC entry 239 (class 1259 OID 20315)
-- Name: Event Interests; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Event Interests" (
    "EvIn_ID" integer NOT NULL,
    "ResponseID" integer NOT NULL,
    "EventName" character varying NOT NULL,
    "InterestRating" character varying,
    "RatingID" integer NOT NULL
);


--
-- TOC entry 236 (class 1259 OID 20312)
-- Name: Event Interests_EvIn_ID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Event Interests_EvIn_ID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4975 (class 0 OID 0)
-- Dependencies: 236
-- Name: Event Interests_EvIn_ID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Event Interests_EvIn_ID_seq" OWNED BY public."Event Interests"."EvIn_ID";


--
-- TOC entry 238 (class 1259 OID 20314)
-- Name: Event Interests_RatingID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Event Interests_RatingID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4976 (class 0 OID 0)
-- Dependencies: 238
-- Name: Event Interests_RatingID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Event Interests_RatingID_seq" OWNED BY public."Event Interests"."RatingID";


--
-- TOC entry 237 (class 1259 OID 20313)
-- Name: Event Interests_ResponseID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Event Interests_ResponseID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4977 (class 0 OID 0)
-- Dependencies: 237
-- Name: Event Interests_ResponseID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Event Interests_ResponseID_seq" OWNED BY public."Event Interests"."ResponseID";


--
-- TOC entry 228 (class 1259 OID 20277)
-- Name: NS Ratings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."NS Ratings" (
    "NetwSatisfID" integer NOT NULL,
    "Description" character varying NOT NULL
);


--
-- TOC entry 227 (class 1259 OID 20276)
-- Name: NS Ratings_NetwSatisfID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."NS Ratings_NetwSatisfID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4978 (class 0 OID 0)
-- Dependencies: 227
-- Name: NS Ratings_NetwSatisfID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."NS Ratings_NetwSatisfID_seq" OWNED BY public."NS Ratings"."NetwSatisfID";


--
-- TOC entry 222 (class 1259 OID 20250)
-- Name: OCE Ratings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."OCE Ratings" (
    "ConfExpID" integer NOT NULL,
    "Description" character varying NOT NULL
);


--
-- TOC entry 221 (class 1259 OID 20249)
-- Name: OCE Ratings_ConfExpID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."OCE Ratings_ConfExpID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4979 (class 0 OID 0)
-- Dependencies: 221
-- Name: OCE Ratings_ConfExpID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."OCE Ratings_ConfExpID_seq" OWNED BY public."OCE Ratings"."ConfExpID";


--
-- TOC entry 224 (class 1259 OID 20259)
-- Name: PEI Ratings; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."PEI Ratings" (
    "PresEngID" integer NOT NULL,
    "Description" character varying NOT NULL
);


--
-- TOC entry 223 (class 1259 OID 20258)
-- Name: PEI Ratings_PresEngID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."PEI Ratings_PresEngID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4980 (class 0 OID 0)
-- Dependencies: 223
-- Name: PEI Ratings_PresEngID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."PEI Ratings_PresEngID_seq" OWNED BY public."PEI Ratings"."PresEngID";


--
-- TOC entry 218 (class 1259 OID 20232)
-- Name: Respondent; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Respondent" (
    "RespondentID" integer NOT NULL,
    "Name" character varying,
    "Company" character varying,
    "Job Title" character varying
);


--
-- TOC entry 217 (class 1259 OID 20231)
-- Name: Respondent_RespondentID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Respondent_RespondentID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4981 (class 0 OID 0)
-- Dependencies: 217
-- Name: Respondent_RespondentID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Respondent_RespondentID_seq" OWNED BY public."Respondent"."RespondentID";


--
-- TOC entry 235 (class 1259 OID 20291)
-- Name: Survey Response; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."Survey Response" (
    "ResponseID" integer NOT NULL,
    "RespondentID" integer NOT NULL,
    "ConfExpID" integer NOT NULL,
    "PresEngID" integer NOT NULL,
    "LogisticsID" integer NOT NULL,
    "NetwSatisfID" integer NOT NULL,
    "Overall_Conf_Exp" character varying,
    "Pres_Eng_Inf" character varying,
    "Insigh_Speakers" character varying,
    "Miss_Topics" character varying,
    "Netw_Satisf" character varying,
    "Netw_Sugg" character varying,
    "Eval_Logistics" character varying,
    "Feed_Fut_Confs" character varying,
    "Cont_Ideation" character varying,
    "Gen_Feed" character varying
);


--
-- TOC entry 231 (class 1259 OID 20287)
-- Name: Survey Response_ConfExpID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Survey Response_ConfExpID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4982 (class 0 OID 0)
-- Dependencies: 231
-- Name: Survey Response_ConfExpID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Survey Response_ConfExpID_seq" OWNED BY public."Survey Response"."ConfExpID";


--
-- TOC entry 233 (class 1259 OID 20289)
-- Name: Survey Response_LogisticsID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Survey Response_LogisticsID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4983 (class 0 OID 0)
-- Dependencies: 233
-- Name: Survey Response_LogisticsID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Survey Response_LogisticsID_seq" OWNED BY public."Survey Response"."LogisticsID";


--
-- TOC entry 234 (class 1259 OID 20290)
-- Name: Survey Response_NetwSatisfID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Survey Response_NetwSatisfID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4984 (class 0 OID 0)
-- Dependencies: 234
-- Name: Survey Response_NetwSatisfID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Survey Response_NetwSatisfID_seq" OWNED BY public."Survey Response"."NetwSatisfID";


--
-- TOC entry 232 (class 1259 OID 20288)
-- Name: Survey Response_PresEngID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Survey Response_PresEngID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4985 (class 0 OID 0)
-- Dependencies: 232
-- Name: Survey Response_PresEngID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Survey Response_PresEngID_seq" OWNED BY public."Survey Response"."PresEngID";


--
-- TOC entry 230 (class 1259 OID 20286)
-- Name: Survey Response_RespondentID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Survey Response_RespondentID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4986 (class 0 OID 0)
-- Dependencies: 230
-- Name: Survey Response_RespondentID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Survey Response_RespondentID_seq" OWNED BY public."Survey Response"."RespondentID";


--
-- TOC entry 229 (class 1259 OID 20285)
-- Name: Survey Response_ResponseID_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Survey Response_ResponseID_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4987 (class 0 OID 0)
-- Dependencies: 229
-- Name: Survey Response_ResponseID_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Survey Response_ResponseID_seq" OWNED BY public."Survey Response"."ResponseID";


--
-- TOC entry 4780 (class 2604 OID 20271)
-- Name: EL Ratings LogisticsID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EL Ratings" ALTER COLUMN "LogisticsID" SET DEFAULT nextval('public."EL Ratings_LogisticsID_seq"'::regclass);


--
-- TOC entry 4777 (class 2604 OID 20244)
-- Name: Event Interest Ratings RatingID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interest Ratings" ALTER COLUMN "RatingID" SET DEFAULT nextval('public."Event Interest Ratings_RatingID_seq"'::regclass);


--
-- TOC entry 4788 (class 2604 OID 20318)
-- Name: Event Interests EvIn_ID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interests" ALTER COLUMN "EvIn_ID" SET DEFAULT nextval('public."Event Interests_EvIn_ID_seq"'::regclass);


--
-- TOC entry 4789 (class 2604 OID 20319)
-- Name: Event Interests ResponseID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interests" ALTER COLUMN "ResponseID" SET DEFAULT nextval('public."Event Interests_ResponseID_seq"'::regclass);


--
-- TOC entry 4790 (class 2604 OID 20320)
-- Name: Event Interests RatingID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interests" ALTER COLUMN "RatingID" SET DEFAULT nextval('public."Event Interests_RatingID_seq"'::regclass);


--
-- TOC entry 4781 (class 2604 OID 20280)
-- Name: NS Ratings NetwSatisfID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."NS Ratings" ALTER COLUMN "NetwSatisfID" SET DEFAULT nextval('public."NS Ratings_NetwSatisfID_seq"'::regclass);


--
-- TOC entry 4778 (class 2604 OID 20253)
-- Name: OCE Ratings ConfExpID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."OCE Ratings" ALTER COLUMN "ConfExpID" SET DEFAULT nextval('public."OCE Ratings_ConfExpID_seq"'::regclass);


--
-- TOC entry 4779 (class 2604 OID 20262)
-- Name: PEI Ratings PresEngID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PEI Ratings" ALTER COLUMN "PresEngID" SET DEFAULT nextval('public."PEI Ratings_PresEngID_seq"'::regclass);


--
-- TOC entry 4776 (class 2604 OID 20235)
-- Name: Respondent RespondentID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Respondent" ALTER COLUMN "RespondentID" SET DEFAULT nextval('public."Respondent_RespondentID_seq"'::regclass);


--
-- TOC entry 4782 (class 2604 OID 20294)
-- Name: Survey Response ResponseID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response" ALTER COLUMN "ResponseID" SET DEFAULT nextval('public."Survey Response_ResponseID_seq"'::regclass);


--
-- TOC entry 4783 (class 2604 OID 20295)
-- Name: Survey Response RespondentID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response" ALTER COLUMN "RespondentID" SET DEFAULT nextval('public."Survey Response_RespondentID_seq"'::regclass);


--
-- TOC entry 4784 (class 2604 OID 20296)
-- Name: Survey Response ConfExpID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response" ALTER COLUMN "ConfExpID" SET DEFAULT nextval('public."Survey Response_ConfExpID_seq"'::regclass);


--
-- TOC entry 4785 (class 2604 OID 20297)
-- Name: Survey Response PresEngID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response" ALTER COLUMN "PresEngID" SET DEFAULT nextval('public."Survey Response_PresEngID_seq"'::regclass);


--
-- TOC entry 4786 (class 2604 OID 20298)
-- Name: Survey Response LogisticsID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response" ALTER COLUMN "LogisticsID" SET DEFAULT nextval('public."Survey Response_LogisticsID_seq"'::regclass);


--
-- TOC entry 4787 (class 2604 OID 20299)
-- Name: Survey Response NetwSatisfID; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response" ALTER COLUMN "NetwSatisfID" SET DEFAULT nextval('public."Survey Response_NetwSatisfID_seq"'::regclass);


--
-- TOC entry 4800 (class 2606 OID 20275)
-- Name: EL Ratings EL Ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."EL Ratings"
    ADD CONSTRAINT "EL Ratings_pkey" PRIMARY KEY ("LogisticsID");


--
-- TOC entry 4794 (class 2606 OID 20248)
-- Name: Event Interest Ratings Event Interest Ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interest Ratings"
    ADD CONSTRAINT "Event Interest Ratings_pkey" PRIMARY KEY ("RatingID");


--
-- TOC entry 4814 (class 2606 OID 20324)
-- Name: Event Interests Event Interests_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interests"
    ADD CONSTRAINT "Event Interests_pkey" PRIMARY KEY ("EvIn_ID");


--
-- TOC entry 4802 (class 2606 OID 20284)
-- Name: NS Ratings NS Ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."NS Ratings"
    ADD CONSTRAINT "NS Ratings_pkey" PRIMARY KEY ("NetwSatisfID");


--
-- TOC entry 4796 (class 2606 OID 20257)
-- Name: OCE Ratings OCE Ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."OCE Ratings"
    ADD CONSTRAINT "OCE Ratings_pkey" PRIMARY KEY ("ConfExpID");


--
-- TOC entry 4798 (class 2606 OID 20266)
-- Name: PEI Ratings PEI Ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."PEI Ratings"
    ADD CONSTRAINT "PEI Ratings_pkey" PRIMARY KEY ("PresEngID");


--
-- TOC entry 4792 (class 2606 OID 20239)
-- Name: Respondent Respondent_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Respondent"
    ADD CONSTRAINT "Respondent_pkey" PRIMARY KEY ("RespondentID");


--
-- TOC entry 4804 (class 2606 OID 20305)
-- Name: Survey Response Survey Response_ConfExpID_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_ConfExpID_key" UNIQUE ("ConfExpID");


--
-- TOC entry 4806 (class 2606 OID 20309)
-- Name: Survey Response Survey Response_LogisticsID_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_LogisticsID_key" UNIQUE ("LogisticsID");


--
-- TOC entry 4808 (class 2606 OID 20311)
-- Name: Survey Response Survey Response_NetwSatisfID_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_NetwSatisfID_key" UNIQUE ("NetwSatisfID");


--
-- TOC entry 4810 (class 2606 OID 20307)
-- Name: Survey Response Survey Response_PresEngID_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_PresEngID_key" UNIQUE ("PresEngID");


--
-- TOC entry 4812 (class 2606 OID 20303)
-- Name: Survey Response Survey Response_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_pkey" PRIMARY KEY ("ResponseID");


--
-- TOC entry 4820 (class 2606 OID 20330)
-- Name: Event Interests Event Interests_RatingID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interests"
    ADD CONSTRAINT "Event Interests_RatingID_fkey" FOREIGN KEY ("RatingID") REFERENCES public."Event Interest Ratings"("RatingID");


--
-- TOC entry 4821 (class 2606 OID 20325)
-- Name: Event Interests Event Interests_ResponseID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Event Interests"
    ADD CONSTRAINT "Event Interests_ResponseID_fkey" FOREIGN KEY ("ResponseID") REFERENCES public."Survey Response"("ResponseID");


--
-- TOC entry 4815 (class 2606 OID 20340)
-- Name: Survey Response Survey Response_ConfExpID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_ConfExpID_fkey" FOREIGN KEY ("ConfExpID") REFERENCES public."OCE Ratings"("ConfExpID");


--
-- TOC entry 4816 (class 2606 OID 20350)
-- Name: Survey Response Survey Response_LogisticsID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_LogisticsID_fkey" FOREIGN KEY ("LogisticsID") REFERENCES public."EL Ratings"("LogisticsID");


--
-- TOC entry 4817 (class 2606 OID 20355)
-- Name: Survey Response Survey Response_NetwSatisfID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_NetwSatisfID_fkey" FOREIGN KEY ("NetwSatisfID") REFERENCES public."NS Ratings"("NetwSatisfID");


--
-- TOC entry 4818 (class 2606 OID 20345)
-- Name: Survey Response Survey Response_PresEngID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_PresEngID_fkey" FOREIGN KEY ("PresEngID") REFERENCES public."PEI Ratings"("PresEngID");


--
-- TOC entry 4819 (class 2606 OID 20335)
-- Name: Survey Response Survey Response_RespondentID_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."Survey Response"
    ADD CONSTRAINT "Survey Response_RespondentID_fkey" FOREIGN KEY ("RespondentID") REFERENCES public."Respondent"("RespondentID");




--
-- PostgreSQL database dump complete
--

