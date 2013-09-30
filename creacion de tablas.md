mesadeayuda
===========

creacion de tablas


CREATE TABLE anos (
    cod_ano character varying(4) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.anos OWNER TO postgres;

--
-- TOC entry 171 (class 1259 OID 17381)
-- Name: calificacion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE calificacion (
    cod_cal character varying(2) NOT NULL,
    det_cal character varying(20) NOT NULL
);


ALTER TABLE public.calificacion OWNER TO postgres;

--
-- TOC entry 172 (class 1259 OID 17386)
-- Name: cargos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE cargos (
    cod_cargo character varying(3) NOT NULL,
    det_cargo character varying(120) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.cargos OWNER TO postgres;

--
-- TOC entry 173 (class 1259 OID 17396)
-- Name: clase_proc_grpo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE clase_proc_grpo (
    clase_rep character varying(5) NOT NULL,
    cod_proc character varying(3) NOT NULL,
    cod_grpo character varying(3) NOT NULL
);


ALTER TABLE public.clase_proc_grpo OWNER TO postgres;

--
-- TOC entry 174 (class 1259 OID 17401)
-- Name: clase_proc_grpo_sbgrpo; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE clase_proc_grpo_sbgrpo (
    cod_proc character varying(3) NOT NULL,
    clase_rep character varying(5) NOT NULL,
    cod_grpo character varying(3) NOT NULL,
    cod_sbgrpo character varying(3) NOT NULL,
    porcentaje numeric(11,0) NOT NULL
);


ALTER TABLE public.clase_proc_grpo_sbgrpo OWNER TO postgres;

--
-- TOC entry 175 (class 1259 OID 17406)
-- Name: clase_rep; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE clase_rep (
    clase_rep character varying(5) NOT NULL,
    det_clase_rep character varying(500) DEFAULT NULL::character varying,
    cod_est character varying(3) DEFAULT NULL::character varying,
    reporte character varying(1) NOT NULL
);


ALTER TABLE public.clase_rep OWNER TO postgres;

--
-- TOC entry 176 (class 1259 OID 17426)
-- Name: conc_rep; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE conc_rep (
    conc_rep character varying(5) NOT NULL,
    clase_rep character varying(5) NOT NULL,
    cod_proc character varying(3) DEFAULT ''::character varying NOT NULL,
    cod_grpo character varying(3) DEFAULT ''::character varying NOT NULL,
    det_conc_rep character varying(500) DEFAULT NULL::character varying,
    cod_est character varying(3) DEFAULT NULL::character varying
);


ALTER TABLE public.conc_rep OWNER TO postgres;

--
-- TOC entry 177 (class 1259 OID 17438)
-- Name: dependencias; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE dependencias (
    cod_dep character varying(3) NOT NULL,
    det_dep character varying(200) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.dependencias OWNER TO postgres;

--
-- TOC entry 178 (class 1259 OID 17463)
-- Name: estado_reporte; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE estado_reporte (
    cod_est_rep character varying(3) NOT NULL,
    det_est_rep character varying(200) NOT NULL,
    campo character varying(120) NOT NULL,
    valida character varying(120) NOT NULL,
    orden numeric(11,0) NOT NULL
);


ALTER TABLE public.estado_reporte OWNER TO postgres;

--
-- TOC entry 179 (class 1259 OID 17473)
-- Name: estados; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE estados (
    cod_est character varying(3) NOT NULL,
    det_est character varying(200) NOT NULL,
    sigla character varying(2) NOT NULL
);


ALTER TABLE public.estados OWNER TO postgres;

--
-- TOC entry 180 (class 1259 OID 17478)
-- Name: funcionarios; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE funcionarios (
    cod_fun character varying(5) NOT NULL,
    nombres character varying(200) NOT NULL,
    apellidos character varying(200) NOT NULL,
    cod_cargo character varying(3) DEFAULT NULL::character varying,
    telefono character varying(25) DEFAULT NULL::character varying,
    celular character varying(25) DEFAULT NULL::character varying,
    login character varying(200) DEFAULT NULL::character varying,
    clave character varying(200) DEFAULT NULL::character varying,
    cod_est character varying(3) DEFAULT NULL::character varying,
    cod_perfil character varying(3) DEFAULT NULL::character varying,
    autoriza character varying(2) DEFAULT NULL::character varying,
    requisicion character varying(2) DEFAULT NULL::character varying,
    proveedor character varying(2) DEFAULT NULL::character varying,
    pagos character varying(2) DEFAULT NULL::character varying,
    audi_ind character varying(2) DEFAULT NULL::character varying
);


ALTER TABLE public.funcionarios OWNER TO postgres;

--
-- TOC entry 181 (class 1259 OID 17498)
-- Name: funcionarios_dependencias_unidades; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE funcionarios_dependencias_unidades (
    cod_uni character varying(3) NOT NULL,
    cod_dep character varying(3) NOT NULL,
    cod_fun character varying(5) NOT NULL
);


ALTER TABLE public.funcionarios_dependencias_unidades OWNER TO postgres;

--
-- TOC entry 182 (class 1259 OID 17503)
-- Name: funcionarios_macroprocesos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE funcionarios_macroprocesos (
    cod_fun character varying(5) NOT NULL,
    cod_proc character varying(3) NOT NULL
);


ALTER TABLE public.funcionarios_macroprocesos OWNER TO postgres;

--
-- TOC entry 183 (class 1259 OID 17508)
-- Name: grupos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE grupos (
    cod_proc character varying(3) NOT NULL,
    cod_grpo character varying(3) NOT NULL,
    det_grpo character varying(200) NOT NULL,
    cod_est character varying(3) NOT NULL,
    inventario character varying(1) NOT NULL
);


ALTER TABLE public.grupos OWNER TO postgres;

--
-- TOC entry 184 (class 1259 OID 17513)
-- Name: indicadores; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE indicadores (
    cod_indicador character varying(3) NOT NULL,
    porcentaje character varying(5) NOT NULL,
    cod_proc character varying(3) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.indicadores OWNER TO postgres;

--
-- TOC entry 185 (class 1259 OID 17518)
-- Name: indicadores_audita; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE indicadores_audita (
    cod_ind character varying(5) NOT NULL,
    cod_mes character varying(5) NOT NULL,
    cod_ano character varying(5) NOT NULL,
    fecha date NOT NULL,
    cod_fun character varying(5) NOT NULL,
    cod_proc character varying(5) NOT NULL,
    cod_uni character varying(3) NOT NULL,
    cod_dep character varying(3) NOT NULL,
    auditoria text NOT NULL
);


ALTER TABLE public.indicadores_audita OWNER TO postgres;

--
-- TOC entry 186 (class 1259 OID 17526)
-- Name: indicadores_gnral; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE indicadores_gnral (
    cod_ind character varying(5) NOT NULL,
    cod_mes character varying(5) NOT NULL,
    cod_ano character varying(5) NOT NULL,
    fecha date,
    cod_fun character varying(5) DEFAULT NULL::character varying,
    cod_uni character varying(3) DEFAULT ''::character varying NOT NULL,
    cod_dep character varying(3) DEFAULT ''::character varying NOT NULL,
    cod_proc character varying(5) DEFAULT ''::character varying NOT NULL,
    mano_obra text,
    maquinaria text,
    materia_prima text,
    metodo text,
    medicion text,
    medio_ambiente text,
    analisis_plan text,
    accion_plan text
);


ALTER TABLE public.indicadores_gnral OWNER TO postgres;

--
-- TOC entry 187 (class 1259 OID 17572)
-- Name: macro_proceso; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macro_proceso (
    cod_mac character varying(3) NOT NULL,
    cod_proc character varying(3) NOT NULL
);


ALTER TABLE public.macro_proceso OWNER TO postgres;

--
-- TOC entry 188 (class 1259 OID 17577)
-- Name: macroprocesos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macroprocesos (
    cod_proc character varying(3) NOT NULL,
    det_proc character varying(300) NOT NULL,
    valida_inv character varying(2) NOT NULL,
    cod_est character varying(3) NOT NULL,
    cod_hom numeric(11,0) DEFAULT NULL::numeric,
    cod_fun character varying(5) DEFAULT NULL::character varying,
    abrev character varying(8) DEFAULT NULL::character varying
);


ALTER TABLE public.macroprocesos OWNER TO postgres;

--
-- TOC entry 189 (class 1259 OID 17585)
-- Name: macroprocesos_unidades_funcionales; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE macroprocesos_unidades_funcionales (
    cod_proc character varying(3) NOT NULL,
    cod_uni character varying(3) NOT NULL
);


ALTER TABLE public.macroprocesos_unidades_funcionales OWNER TO postgres;

--
-- TOC entry 190 (class 1259 OID 17595)
-- Name: marcas_vehiculos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE marcas_vehiculos (
    cod_marca character varying(3) NOT NULL,
    det_marca character varying(100) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.marcas_vehiculos OWNER TO postgres;

--
-- TOC entry 191 (class 1259 OID 17607)
-- Name: meses; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE meses (
    cod_mes character varying(2) NOT NULL,
    det_mes character varying(50) NOT NULL
);


ALTER TABLE public.meses OWNER TO postgres;

--
-- TOC entry 192 (class 1259 OID 17642)
-- Name: perfiles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE perfiles (
    cod_perfil character varying(3) NOT NULL,
    det_perfil character varying(300) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.perfiles OWNER TO postgres;

--
-- TOC entry 193 (class 1259 OID 17647)
-- Name: permisos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE permisos (
    cod_per numeric(3,0) NOT NULL,
    det_per character varying(200) NOT NULL,
    menu character varying(3) NOT NULL,
    acceso character varying(200) NOT NULL,
    imagen character varying(200) NOT NULL,
    tipo character varying(1) NOT NULL,
    sistema character varying(1) NOT NULL
);


ALTER TABLE public.permisos OWNER TO postgres;

--
-- TOC entry 194 (class 1259 OID 17655)
-- Name: permisos_perfiles; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE permisos_perfiles (
    cod_per character varying(3) NOT NULL,
    cod_perfil character varying(3) NOT NULL,
    sistema character varying(1) NOT NULL
);


ALTER TABLE public.permisos_perfiles OWNER TO postgres;

--
-- TOC entry 195 (class 1259 OID 17660)
-- Name: pisos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE pisos (
    cod_piso numeric(3,0) NOT NULL,
    det_piso character varying(60) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.pisos OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 17665)
-- Name: preguntas_proceso_clase; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE preguntas_proceso_clase (
    cod_proc character varying(3) NOT NULL,
    clase_rep character varying(5) NOT NULL,
    cod_preg character varying(5) NOT NULL,
    det_preg character varying(500) NOT NULL,
    porcentaje numeric(11,0) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.preguntas_proceso_clase OWNER TO postgres;

--
-- TOC entry 197 (class 1259 OID 17673)
-- Name: prioridades; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE prioridades (
    cod_proc character varying(3) NOT NULL,
    cod_prio character varying(3) NOT NULL,
    clase_rep character varying(5) NOT NULL,
    det_prio character varying(200) NOT NULL,
    cod_est character varying(3) NOT NULL,
    cod_tiempo character varying(3) NOT NULL,
    dias character varying(30) NOT NULL,
    porcentaje numeric(11,0) NOT NULL
);


ALTER TABLE public.prioridades OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 17683)
-- Name: reporte; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE reporte (
    cod_reporte character varying(20) NOT NULL,
    cod_est_rep character varying(3) DEFAULT NULL::character varying,
    fec_req date,
    hora_req time without time zone,
    cod_req character varying(5) DEFAULT NULL::character varying,
    cod_dep character varying(3) DEFAULT NULL::character varying,
    cod_uni character varying(3) DEFAULT NULL::character varying,
    cod_piso character varying(3) DEFAULT NULL::character varying,
    cod_proc character varying(3) DEFAULT NULL::character varying,
    cod_grpo character varying(3) DEFAULT NULL::character varying,
    cod_sbgrpo character varying(3) DEFAULT NULL::character varying,
    placa character varying(20) DEFAULT NULL::character varying,
    problema text,
    clase_rep character varying(5) DEFAULT NULL::character varying,
    conc_rep character varying(5) DEFAULT NULL::character varying,
    fec_asig date,
    hora_asig time without time zone,
    cod_asig character varying(5) DEFAULT NULL::character varying,
    fec_reasig date,
    hora_reasig time without time zone,
    cod_reasig character varying(5) DEFAULT NULL::character varying,
    fec_aten date,
    hora_aten time without time zone,
    cod_aten character varying(5) DEFAULT NULL::character varying,
    atencion text,
    fec_sol date,
    hora_sol time without time zone,
    cod_sol character varying(5) DEFAULT NULL::character varying,
    fec_cierre date,
    hora_cierre time without time zone,
    preg_uno character varying(2) DEFAULT NULL::character varying,
    preg_dos character varying(2) DEFAULT NULL::character varying,
    obs_dos text,
    preg_tres character varying(2) DEFAULT NULL::character varying,
    obs_tres text,
    cod_seg character varying(5) DEFAULT NULL::character varying,
    fec_seg date,
    hora_seg time without time zone,
    cod_prio character varying(3) DEFAULT NULL::character varying,
    repuesto text,
    compra character varying(2) DEFAULT NULL::character varying,
    cod_anu character varying(5) DEFAULT NULL::character varying,
    fec_anu date,
    hor_anu time without time zone,
    observacion character varying(500) DEFAULT NULL::character varying,
    reprogramado character varying(20) DEFAULT NULL::character varying,
    proveedor character varying(2) DEFAULT NULL::character varying,
    cod_prov character varying(5) DEFAULT NULL::character varying,
    vehiculo character varying(2) DEFAULT NULL::character varying,
    facturado character varying(150) DEFAULT NULL::character varying,
    cod_fact character varying(5) DEFAULT NULL::character varying,
    fec_fact date
);


ALTER TABLE public.reporte OWNER TO postgres;

--
-- TOC entry 199 (class 1259 OID 17720)
-- Name: reporte_detalle; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE reporte_detalle (
    cod_reporte character varying(20) NOT NULL,
    cod_proc character varying(3) NOT NULL,
    cod_grpo character varying(3) NOT NULL,
    cod_sbgrpo character varying(3) NOT NULL,
    fecha date DEFAULT '0001-01-01'::date NOT NULL,
    hora time without time zone DEFAULT '00:00:00'::time without time zone NOT NULL,
    det_reporte text NOT NULL,
    cod_fun character varying(5) NOT NULL
);


ALTER TABLE public.reporte_detalle OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 17730)
-- Name: reporte_preguntas; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE reporte_preguntas (
    cod_reporte character varying(20) NOT NULL,
    cod_preg character varying(5) NOT NULL
);


ALTER TABLE public.reporte_preguntas OWNER TO postgres;

--
-- TOC entry 201 (class 1259 OID 17765)
-- Name: subgrupos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE subgrupos (
    cod_proc character varying(3) NOT NULL,
    cod_grpo character varying(3) NOT NULL,
    cod_sbgrpo character varying(3) NOT NULL,
    det_sbgrpo character varying(200) NOT NULL,
    cod_est character varying(3) NOT NULL,
    periferico character varying(1) NOT NULL
);


ALTER TABLE public.subgrupos OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 17770)
-- Name: tiempos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE tiempos (
    cod_tiempo character varying(3) NOT NULL,
    detalle character varying(300) NOT NULL
);


ALTER TABLE public.tiempos OWNER TO postgres;

--
-- TOC entry 203 (class 1259 OID 17800)
-- Name: uni_proc_grpo_sbgrpo_fun; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE uni_proc_grpo_sbgrpo_fun (
    cod_uni character varying(3) NOT NULL,
    cod_proc character varying(3) NOT NULL,
    cod_grpo character varying(3) NOT NULL,
    cod_sbgrpo character varying(3) NOT NULL,
    cod_fun character varying(5) NOT NULL
);


ALTER TABLE public.uni_proc_grpo_sbgrpo_fun OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 17805)
-- Name: unidades_dependencias; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE unidades_dependencias (
    cod_uni character varying(3) NOT NULL,
    cod_dep character varying(3) NOT NULL
);


ALTER TABLE public.unidades_dependencias OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 17810)
-- Name: unidades_funcionales; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE unidades_funcionales (
    cod_uni character varying(3) NOT NULL,
    det_uni_fun character varying(300) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.unidades_funcionales OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 17815)
-- Name: unidades_proceso_clase; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE unidades_proceso_clase (
    cod_uni character varying(3) NOT NULL,
    cod_proc character varying(3) NOT NULL,
    clase_rep character varying(5) NOT NULL,
    porcentaje numeric(11,0) NOT NULL
);


ALTER TABLE public.unidades_proceso_clase OWNER TO postgres;

--
-- TOC entry 207 (class 1259 OID 17820)
-- Name: unidades_usuarios; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE unidades_usuarios (
    cod_uni character varying(3) NOT NULL,
    cod_fun character varying(5) NOT NULL
);


ALTER TABLE public.unidades_usuarios OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 17825)
-- Name: vehiculos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vehiculos (
    cod_veh character varying(5) NOT NULL,
    det_veh character varying(100) NOT NULL,
    cod_marca character varying(3) NOT NULL,
    placa character varying(10) NOT NULL,
    cod_est character varying(3) NOT NULL
);


ALTER TABLE public.vehiculos OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 17830)
-- Name: vehiculos_procesos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vehiculos_procesos (
    cod_proc character varying(3) NOT NULL,
    cod_veh character varying(3) NOT NULL
);


ALTER TABLE public.vehiculos_procesos OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 17835)
-- Name: vehiculos_programacion; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vehiculos_programacion (
    cod_prog character varying(20) NOT NULL,
    cod_reporte character varying(20) NOT NULL,
    cod_veh character varying(5) NOT NULL,
    fec_reg date NOT NULL,
    fec_prog date NOT NULL,
    cod_fun_prog character varying(5) NOT NULL,
    realizado character varying(2) DEFAULT '0'::character varying,
    fec_realizado date,
    cod_fun_real character varying(5) DEFAULT NULL::character varying,
    fec_registro date,
    observacion text
);


ALTER TABLE public.vehiculos_programacion OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 17845)
-- Name: vitacora_casos; Type: TABLE; Schema: public; Owner: postgres; Tablespace: 
--

CREATE TABLE vitacora_casos (
    cod_reporte character varying(5) NOT NULL,
    cod_vitacora character varying(5) NOT NULL,
    fecha_vit date NOT NULL,
    hora_vit time without time zone NOT NULL,
    observacion text NOT NULL,
    cod_fun character varying(5) NOT NULL,
    cod_prov character varying(5) NOT NULL
);


ALTER TABLE public.vitacora_casos OWNER TO postgres;

--
-- TOC entry 2055 (class 2606 OID 17375)
-- Name: anos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY anos
    ADD CONSTRAINT anos_pkey PRIMARY KEY (cod_ano);


--
-- TOC entry 2057 (class 2606 OID 17385)
-- Name: calificacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY calificacion
    ADD CONSTRAINT calificacion_pkey PRIMARY KEY (cod_cal);


--
-- TOC entry 2059 (class 2606 OID 17390)
-- Name: cargos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY cargos
    ADD CONSTRAINT cargos_pkey PRIMARY KEY (cod_cargo);


--
-- TOC entry 2061 (class 2606 OID 17400)
-- Name: clase_proc_grpo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY clase_proc_grpo
    ADD CONSTRAINT clase_proc_grpo_pkey PRIMARY KEY (clase_rep, cod_proc, cod_grpo);


--
-- TOC entry 2063 (class 2606 OID 17405)
-- Name: clase_proc_grpo_sbgrpo_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY clase_proc_grpo_sbgrpo
    ADD CONSTRAINT clase_proc_grpo_sbgrpo_pkey PRIMARY KEY (cod_proc, clase_rep, cod_grpo, cod_sbgrpo);


--
-- TOC entry 2065 (class 2606 OID 17415)
-- Name: clase_rep_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY clase_rep
    ADD CONSTRAINT clase_rep_pkey PRIMARY KEY (clase_rep);


--
-- TOC entry 2067 (class 2606 OID 17437)
-- Name: conc_rep_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY conc_rep
    ADD CONSTRAINT conc_rep_pkey PRIMARY KEY (conc_rep, clase_rep, cod_proc, cod_grpo);


--
-- TOC entry 2069 (class 2606 OID 17442)
-- Name: dependencias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY dependencias
    ADD CONSTRAINT dependencias_pkey PRIMARY KEY (cod_dep);


--
-- TOC entry 2071 (class 2606 OID 17467)
-- Name: estado_reporte_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY estado_reporte
    ADD CONSTRAINT estado_reporte_pkey PRIMARY KEY (cod_est_rep);


--
-- TOC entry 2073 (class 2606 OID 17477)
-- Name: estados_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY estados
    ADD CONSTRAINT estados_pkey PRIMARY KEY (cod_est);


--
-- TOC entry 2077 (class 2606 OID 17502)
-- Name: funcionarios_dependencias_unidades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY funcionarios_dependencias_unidades
    ADD CONSTRAINT funcionarios_dependencias_unidades_pkey PRIMARY KEY (cod_uni, cod_dep, cod_fun);


--
-- TOC entry 2079 (class 2606 OID 17507)
-- Name: funcionarios_macroprocesos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY funcionarios_macroprocesos
    ADD CONSTRAINT funcionarios_macroprocesos_pkey PRIMARY KEY (cod_fun, cod_proc);


--
-- TOC entry 2075 (class 2606 OID 17497)
-- Name: funcionarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY funcionarios
    ADD CONSTRAINT funcionarios_pkey PRIMARY KEY (cod_fun);


--
-- TOC entry 2081 (class 2606 OID 17512)
-- Name: grupos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY grupos
    ADD CONSTRAINT grupos_pkey PRIMARY KEY (cod_proc, cod_grpo);


--
-- TOC entry 2085 (class 2606 OID 17525)
-- Name: indicadores_audita_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY indicadores_audita
    ADD CONSTRAINT indicadores_audita_pkey PRIMARY KEY (cod_ind, cod_mes, cod_ano, fecha, cod_fun, cod_proc, cod_uni, cod_dep);


--
-- TOC entry 2087 (class 2606 OID 17537)
-- Name: indicadores_gnral_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY indicadores_gnral
    ADD CONSTRAINT indicadores_gnral_pkey PRIMARY KEY (cod_ind, cod_mes, cod_ano, cod_uni, cod_dep, cod_proc);


--
-- TOC entry 2083 (class 2606 OID 17517)
-- Name: indicadores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY indicadores
    ADD CONSTRAINT indicadores_pkey PRIMARY KEY (cod_indicador, cod_proc);


--
-- TOC entry 2089 (class 2606 OID 17576)
-- Name: macro_proceso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY macro_proceso
    ADD CONSTRAINT macro_proceso_pkey PRIMARY KEY (cod_mac, cod_proc);


--
-- TOC entry 2091 (class 2606 OID 17584)
-- Name: macroprocesos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY macroprocesos
    ADD CONSTRAINT macroprocesos_pkey PRIMARY KEY (cod_proc);


--
-- TOC entry 2093 (class 2606 OID 17589)
-- Name: macroprocesos_unidades_funcionales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY macroprocesos_unidades_funcionales
    ADD CONSTRAINT macroprocesos_unidades_funcionales_pkey PRIMARY KEY (cod_proc, cod_uni);


--
-- TOC entry 2095 (class 2606 OID 17599)
-- Name: marcas_vehiculos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY marcas_vehiculos
    ADD CONSTRAINT marcas_vehiculos_pkey PRIMARY KEY (cod_marca);


--
-- TOC entry 2097 (class 2606 OID 17611)
-- Name: meses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY meses
    ADD CONSTRAINT meses_pkey PRIMARY KEY (cod_mes);


--
-- TOC entry 2099 (class 2606 OID 17646)
-- Name: perfiles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY perfiles
    ADD CONSTRAINT perfiles_pkey PRIMARY KEY (cod_perfil);


--
-- TOC entry 2103 (class 2606 OID 17659)
-- Name: permisos_perfiles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY permisos_perfiles
    ADD CONSTRAINT permisos_perfiles_pkey PRIMARY KEY (cod_per, cod_perfil, sistema);


--
-- TOC entry 2101 (class 2606 OID 17654)
-- Name: permisos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY permisos
    ADD CONSTRAINT permisos_pkey PRIMARY KEY (cod_per);


--
-- TOC entry 2105 (class 2606 OID 17664)
-- Name: pisos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY pisos
    ADD CONSTRAINT pisos_pkey PRIMARY KEY (cod_piso);


--
-- TOC entry 2107 (class 2606 OID 17672)
-- Name: preguntas_proceso_clase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY preguntas_proceso_clase
    ADD CONSTRAINT preguntas_proceso_clase_pkey PRIMARY KEY (cod_proc, clase_rep, cod_preg);


--
-- TOC entry 2109 (class 2606 OID 17677)
-- Name: prioridades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY prioridades
    ADD CONSTRAINT prioridades_pkey PRIMARY KEY (cod_proc, cod_prio, clase_rep);


--
-- TOC entry 2113 (class 2606 OID 17729)
-- Name: reporte_detalle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY reporte_detalle
    ADD CONSTRAINT reporte_detalle_pkey PRIMARY KEY (cod_reporte, cod_proc, cod_grpo, cod_sbgrpo, fecha, hora);


--
-- TOC entry 2111 (class 2606 OID 17719)
-- Name: reporte_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY reporte
    ADD CONSTRAINT reporte_pkey PRIMARY KEY (cod_reporte);


--
-- TOC entry 2115 (class 2606 OID 17734)
-- Name: reporte_preguntas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY reporte_preguntas
    ADD CONSTRAINT reporte_preguntas_pkey PRIMARY KEY (cod_reporte, cod_preg);


--
-- TOC entry 2117 (class 2606 OID 17769)
-- Name: subgrupos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY subgrupos
    ADD CONSTRAINT subgrupos_pkey PRIMARY KEY (cod_proc, cod_grpo, cod_sbgrpo);


--
-- TOC entry 2119 (class 2606 OID 17774)
-- Name: tiempos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY tiempos
    ADD CONSTRAINT tiempos_pkey PRIMARY KEY (cod_tiempo);


--
-- TOC entry 2121 (class 2606 OID 17804)
-- Name: uni_proc_grpo_sbgrpo_fun_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY uni_proc_grpo_sbgrpo_fun
    ADD CONSTRAINT uni_proc_grpo_sbgrpo_fun_pkey PRIMARY KEY (cod_uni, cod_proc, cod_grpo, cod_sbgrpo, cod_fun);


--
-- TOC entry 2123 (class 2606 OID 17809)
-- Name: unidades_dependencias_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY unidades_dependencias
    ADD CONSTRAINT unidades_dependencias_pkey PRIMARY KEY (cod_uni, cod_dep);


--
-- TOC entry 2125 (class 2606 OID 17814)
-- Name: unidades_funcionales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY unidades_funcionales
    ADD CONSTRAINT unidades_funcionales_pkey PRIMARY KEY (cod_uni);


--
-- TOC entry 2127 (class 2606 OID 17819)
-- Name: unidades_proceso_clase_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY unidades_proceso_clase
    ADD CONSTRAINT unidades_proceso_clase_pkey PRIMARY KEY (cod_uni, cod_proc, clase_rep);


--
-- TOC entry 2129 (class 2606 OID 17824)
-- Name: unidades_usuarios_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY unidades_usuarios
    ADD CONSTRAINT unidades_usuarios_pkey PRIMARY KEY (cod_uni, cod_fun);


--
-- TOC entry 2131 (class 2606 OID 17829)
-- Name: vehiculos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vehiculos
    ADD CONSTRAINT vehiculos_pkey PRIMARY KEY (cod_veh);


--
-- TOC entry 2133 (class 2606 OID 17834)
-- Name: vehiculos_procesos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vehiculos_procesos
    ADD CONSTRAINT vehiculos_procesos_pkey PRIMARY KEY (cod_proc, cod_veh);


--
-- TOC entry 2135 (class 2606 OID 17844)
-- Name: vehiculos_programacion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vehiculos_programacion
    ADD CONSTRAINT vehiculos_programacion_pkey PRIMARY KEY (cod_prog);


--
-- TOC entry 2137 (class 2606 OID 17852)
-- Name: vitacora_casos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres; Tablespace: 
--

ALTER TABLE ONLY vitacora_casos
    ADD CONSTRAINT vitacora_casos_pkey PRIMARY KEY (cod_reporte, cod_vitacora);


--
-- TOC entry 2251 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2013-09-09 12:13:50

--
-- PostgreSQL database dump complete
--


