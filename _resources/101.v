entity test_fsm is
end test_fsm;

architecture Behavioral of test_fsm is
    -- state type
    type state_type is (s0,s1,s2,s3);

    -- signals
    signal current_state, next_state : state_type;
    assert : std_logic;
    in : std_logic;

begin
    -- sequential part
    process(clk)
    begin
        if rising_edge(clk)
            current_state <= next_state;
        end if;
    end process;

    -- combinational part
    process(all_needed) begin
        -- initialize all signals here, as to prevent latching
        assert <= '0';

        case current_state is
            when s0 =>
                assert <= '0';
                if in = '1' then
                    next_state <= s1;
                elseif
                    next_state <= s0;
                end if;

            when s1 =>
                assert <= '0';
                if in = '1' then
                    next_state <= s1;
                elseif
                    next_state <= s2;
                end if;
            
            when s2 =>
                assert <= '0';
                if in = '1' then
                    next_state <= s3;
                elseif
                    next_state <= s0;
                end if;
            
            when s3 =>
                assert <= '1';
                if in = '1' then
                    next_state <= s1;
                elseif
                    next_state <= s0;
                end if;
    end process;
end Behavioral