import { ReactComponent as AuthLanding } from "../../assets/authLanding.svg";
import { Col, Row } from "reactstrap";

const AuthComponent = ({ children }) => {
  return (
    <div>
      <div
        style={{
          background: "#FFF9F4",
          minHeight: "100vh",
          display: "flex",
        }}
      >
        <Col
          lg={6}
          style={{
            display: "flex",
            justifyContent: "space-between",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          <h1 style={{ marginTop: "10vh" }}>DRAICXCanteen</h1>
          <AuthLanding style={{ marginBottom: "-40px" }} />
        </Col>
        <Col lg={6} style={{ background: "#FCE18F", width: "100%" }}>
          {children}
        </Col>
      </div>
    </div>
  );
};

export default AuthComponent;
